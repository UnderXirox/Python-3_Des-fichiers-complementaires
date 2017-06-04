#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from os import sep
from sys import stderr

import asyncio

from http.client import HTTPConnection
from contextlib import closing
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from timeit import timeit


def wget(uri):
    """
    Renvoi le contenu désigné par une URI

    Paramètre :
    > uri (str, par exemple 'http://inspyration.org')

    Retour :
    > contenu d'un fichier (bytes, fichier textuel ou binaire)
    """
    # Analyse de l'URI
    parsed = urlparse(uri)
    # ouverture de la connexion
    with closing(HTTPConnection(parsed.netloc)) as conn:
        # Chemin sur le serveur
        path = parsed.path
        if parsed.query:
            path += '?' + parsed.query
        # Envoi de la requête vers le serveur
        conn.request('GET', path)
        # Récupération de la réponse
        response = conn.getresponse()
        # Analyse de la réponse
        if response.status != 200:
            # 200 = Ok, 3xx = redirection, 4xx = erreur client, 5xx = erreur serveur
            return
        # Renvoi de la réponse si tout est OK.
        return response.read()


async def download(uri):
    """
    Enregistre sur le disque dur un fichier désigné par une URI

    Paramètre :
    > uri (str, par exemple 'http://www.inspyration.org/logo.png')

    Retour :
    > contenu d'un fichier (bytes, fichier textuel ou binaire)
    """
    content = wget(uri)
    if content is None:
        return None
    async with open(uri.split(sep)[-1], 'wb') as f:
        await f.write(content)
        return uri


class ImageFinderAwaitable:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    async def __await__(self):
        self.soup = BeautifulSoup(self.html_doc, "html.parser")
        return self.soup.find_all('img')


class ImageFinder:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    async def __aiter__(self):
        return self

    async def __anext__(self):
        for img in ImageFinderAwaitable(self.html_doc):
            await img.get('src')


class URIRetreiver:
    def __init__(self, base_uri, image_finder):
        self.parsed_base = urlparse(base_uri)
        self.image_finder = image_finder

    async def __aiter__(self):
        return self

    async def __anext__(self):
        async for src in self.image_finder:
            parsed = urlparse(src)
            if parsed.netloc == '':
                path = parsed.path
                if parsed.query:
                    path += '?' + parsed.query
                if path[0] != '/':
                    if self.parsed_base.path == '/':
                        path = '/' + path
                    else:
                        path = '/' + '/'.join(self.parsed_base.path.split('/')[:-1]) + '/' + path
                await self.parsed_base.scheme + '://' + self.parsed_base.netloc + path
            else:
                await parsed.geturl()


def get_images_uri(page_uri):
    #
    # Récupération des URI de toutes les images d'une page
    #
    html = wget(page_uri)
    if not html:
        print("Erreur: La page web n'a pas été trouvée ou analysée", sys.stderr)
        return None
    images_src_coroutine = ImageFinder(html)
    images_uri_coroutine = URIRetreiver(page_uri, images_src_coroutine)


    return images_uri_coroutine


async def parse_html_page_and_get_all_images(page_uri):
    images_uri = get_images_uri('http://www.formation-python.com/')
    #
    # Récupération des images
    #
    async for image_uri in images_uri:
        print('Téléchargement de %s' % image_uri)
        await download(image_uri)


def do(page_uri):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parse_html_page_and_get_all_images(page_uri))
    loop.close()


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('do(web_page_uri)',
                 number=10,
                 setup="from __main__ import do, web_page_uri"))

# Temps évalue: 4.63s

