#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from os import sep
from sys import stderr

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
        print("Download {} started".format(uri))
        await f.write(content)
        print("Download {} ended".format(uri))
        return uri


async def get_images_src_from_html(html_doc):
    """Récupère tous les contenus des attributs src des balises img"""
    soup = BeautifulSoup(html_doc, "html.parser")
    for img in soup.find_all('img'):
        print("src extracting {} started".format(img.get('src')))
        await img.get('src')
        print("src extracting {} ended".format(img.get('src')))


async def get_uri_from_images_src(base_uri, images_src):
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
            print("Absolute uri compiling {} started".format(path))
            await parsed_base.scheme + '://' + parsed_base.netloc + path
            print("Absolute uri compiling {} ended".format(path))
        else:
            print("Absolute uri compiling {} started".format(path))
            await parsed.geturl()
            print("Absolute uri compiling {} ended".format(path))


async def get_images_uri(page_uri):
    #
    # Récupération des URI de toutes les images d'une page
    #
    html = wget(page_uri)
    if not html:
        print("Erreur: La page web n'a pas été trouvée ou analysée", sys.stderr)
        return None
    print("Get Images uri from {} started".format(page_uri))
    await get_uri_from_images_src(page_uri, get_images_src_from_html(html))
    print("Get Images uri from {} ended".format(page_uri))


def parse_html_page_and_get_all_images(page_uri):
    images_uri = get_images_uri('http://www.formation-python.com/')
    #
    # Récupération des images
    #
    for image_uri in images_uri:
        print('Téléchargement de %s' % image_uri)
        download(image_uri)


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('parse_html_page_and_get_all_images(web_page_uri)',
                 number=10,
                 setup="from __main__ import parse_html_page_and_get_all_images, web_page_uri"))

# Temps évalue: 4.75s

