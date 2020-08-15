# -*- coding:utf-8 -*-
import logging


def get_logger(log_name):
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(log_name)
    return logger
