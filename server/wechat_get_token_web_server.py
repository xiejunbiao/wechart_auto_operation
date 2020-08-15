# -*- coding: utf-8 -*-
"""
"""

"""
多线程
增加  @run_on_executor
"""

import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.httpclient
import tornado.web
import tornado.gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from get_token import get_token

import logging
logging.basicConfig()


def getLogger():
    logger = logging.getLogger("GetAccessToken-log")
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


class GetAccessTokenHandler(tornado.web.RequestHandler):
    
    executor = ThreadPoolExecutor(20)
    
    def initialize(self, logger):
        self.__logger = logger

    @tornado.gen.coroutine
    def get(self):
        
        """get请求"""
        # query = self.get_argument('inputTxt')
        # areaCode = self.get_argument('areaCode', default='')
        # ownerCode = self.get_argument('ownerCode', default='')
        page_json = yield self.get_query_answer()
        self.write(page_json)

    @run_on_executor
    def get_query_answer(self):
        
        """把异常写进日志"""
        try:
            self.__logger.info("获取token")  # #用query-作为分隔符
            access_token = get_token(self.__logger)
            self.__logger.info("access_token-"+access_token)

        except Exception as e:
            self.__logger.info("error:")
            self.__logger.info(e)
            self.__logger.info("traceback My:")
            self.__logger.info(traceback.format_exc())  # #返回异常信息的字符串，可以用来把信息记录到log里
            access_token = {}

        return access_token


def start():
    port = 6603
    logger = getLogger()
    app = tornado.web.Application(handlers=[
        (r"/wechat-operation/officialAccount-01/gettoken", GetAccessTokenHandler,  dict(logger=logger)), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(port)
    http_server.start(10)
    tornado.ioloop.IOLoop.instance().start()
  
    """
    请求url:
    http://10.18.222.105:6603/cloudbrain-assistant/assistant/intentionparse?inputTxt=我要报修&ownerCode=a
    http://10.18.222.105:6603/cloudbrain-assistant/assistant/intentionparse?inputTxt=报修
    http://10.18.222.105:6603/bigdata-assistant/assistant/answerOfquery_test1?query=报修
    /bigdata-assistant/assistant/intentionparse
    http://39.107.69.132:6603/wechat-operation/officialAccount-01/gettoken
    """


if __name__ == "__main__":

    print('the main is not this path')




    
    
    
    
    
    
    
    
    
    
    
    
