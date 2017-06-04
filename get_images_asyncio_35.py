#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from os import sep

import asyncio

from http.client import HTTPConnection
from contextlib import closing
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from timeit import timeit


class FileSystemWriter:

    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.file = open(self.filename, 'wb')
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.file.close()

    async def write(self, content):
        await asyncio.coroutine(self.file.write)(content)
#        loop = asyncio.get_event_loop()
#        await loop.run_in_executor(None, self.file.write, content)


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
    async with FileSystemWriter(uri.split(sep)[-1]) as f:
        await f.write(content)
        return uri


def get_images_src_from_html(html_doc):
    """Récupère tous les contenus des attributs src des balises img"""
    soup = BeautifulSoup(html_doc, "html.parser")
    return (img.get('src') for img in soup.find_all('img'))


def get_uri_from_images_src(base_uri, images_src):
    """Renvoi un à un chaque URI d'image à télécharger"""
    parsed_base = urlparse(base_uri)
    for src in images_src:
        parsed = urlparse(src)
        if parsed.netloc == '':
            path = parsed.path
            if parsed.query:
                path += '?' + parsed.query
            if path[0] != '/':
                if parsed_base.path == '/':
                    path = '/' + path
                else:
                    path = '/' + '/'.join(parsed_base.path.split('/')[:-1]) + '/' + path
            yield parsed_base.scheme + '://' + parsed_base.netloc + path
        else:
            yield parsed.geturl()


def get_images(page_uri):
    #
    # Récupération des URI de toutes les images d'une page
    #
    html = wget(page_uri)
    if not html:
        print("Erreur: La page web n'a pas été trouvée ou analysée", sys.stderr)
        return None
    images_src_gen = get_images_src_from_html(html)
    images_uri_gen = get_uri_from_images_src(page_uri, images_src_gen)

    return asyncio.wait([download(image_uri) for image_uri in images_uri_gen])
    #
    # Récupération des images
    #
#    for image_uri in images_uri_gen:
#        print('Téléchargement de %s' % image_uri)
#        await download(image_uri)


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    loop = asyncio.get_event_loop()
    print(timeit('loop.run_until_complete(get_images(web_page_uri))',
                 number=10,
                 setup="from __main__ import get_images, web_page_uri, loop"))
    loop.close()

# Temps évalue: 4.75s

