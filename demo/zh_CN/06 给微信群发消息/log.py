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
