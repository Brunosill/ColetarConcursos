from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def extraiPagina(url, ReturnErro =None):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return ReturnErro
  try:
    page = BeautifulSoup(
        html.read().decode('utf8'), 'lxml')
  except AttributeError as e:
    return ReturnErro
  return page


