import traceback
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
sys.path.append(rootPath)
from util.get_conf import conf
import requests


class GetDataByUrl(object):
    def __init__(self, logger):
        self._title = ''
        self.__conf = conf['toutiao']
        self.__logger = logger

    def get_data(self, title: str = 'news_history-url'):
        self._title = title
        url = self._get_url()
        return self._request_url(url)

    def _request_url(self, url):
        self.__logger.info('url-{}'.format(url))
        requ = requests.get(url)
        return requ.text

    def _get_url(self):
        return self.__conf[self._title]


if __name__ == '__main__':
    from util.get_logging import get_logger
    gdbu = GetDataByUrl(get_logger('FIRST_LOG'), 'news_history-url')
    txt = gdbu.get_data()
    print(txt)
