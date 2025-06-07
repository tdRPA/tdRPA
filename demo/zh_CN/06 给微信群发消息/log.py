"""
特别声明：
本代码仅供演示tdRPA功能使用，不得用于任何非法、违规或未经授权的操作。
使用者须自行承担因使用本代码引发的一切法律责任，tdRPA开发方不承担任何直接或间接责任。
请严格遵守相关法律法规，谨慎合法使用。
"""

import os
import warnings
from typing import Dict

import logging
from logging import handlers


loggers:Dict[str,logging.Logger] = {}

def getLogger(name:str) -> logging.Logger:
    logger=loggers.get(name)
    if logger==None:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        logPath  = r'.\log'
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        logFile  = os.path.join(logPath,'%s.log' % name)

        #formatter = logging.Formatter('%(asctime)s - %(levelname)s[%(processName)s %(filename)s %(funcName)s %(lineno)d] %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(name)s[%(levelname)s] %(message)s')
        file_handler = handlers.TimedRotatingFileHandler(filename=logFile, when='D',backupCount=365,encoding='utf8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
        loggers[name]=logger
    else:
        warnings.warn('logger name "%s" already in use' % name,Warning)
    return logger
