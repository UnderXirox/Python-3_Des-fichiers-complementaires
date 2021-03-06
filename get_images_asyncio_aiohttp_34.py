import atexit
import sys
from os import sep

import asyncio
import aiohttp

from bs4 import BeautifulSoup
from urllib.parse import urlparse

from timeit import timeit


@asyncio.coroutine
def wget(url):  
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read()
    return body


@asyncio.coroutine
def download(uri):
    """
    Enregistre sur le disque dur un fichier désigné par une URI

    Paramètre :
    > uri (str, par exemple 'http://www.inspyration.org/logo.png')

    Retour :
    > contenu d'un fichier (bytes, fichier textuel ou binaire)
    """
    print("Write {} started".format(uri))
    content = yield from wget(uri)
    if content is None:
        return None
    with open(uri.split(sep)[-1], "wb") as f:
        f.write(content)
        print("Write {} ended".format(uri))
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
    print("### GET_IMAGES")
#    import pdb; pdb.set_trace()
    loop = asyncio.get_event_loop()
    print("### GET IMAGES: HTML")
    html = loop.run_until_complete(wget(page_uri))
    print("### GET IMAGES: HTML Done")

    if not html:
        print("Erreur: La page web n'a pas été trouvée ou analysée", sys.stderr)
        return None
    images_src_gen = get_images_src_from_html(html)
    images_uri_gen = get_uri_from_images_src(page_uri, images_src_gen)

    print("### GET IMAGES")
    loop.run_until_complete(
        asyncio.wait([download(image_uri) for image_uri in images_uri_gen]))
    #loop.close()
    print("### GET IMAGES Done")

#    import pdb; pdb.set_trace()
    #
    # Récupération des images
    #
#    for image_uri in images_uri_gen:
#        print('Téléchargement de %s' % image_uri)
#        await download(image_uri)

def close_loop():
    loop = asyncio.get_event_loop()
    loop.close()
atexit.register(close_loop)


if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('get_images(web_page_uri)',
                 number=10,
                 setup="from __main__ import get_images, web_page_uri"))

