import logging
import os

env_log_level = os.getenv('LOG_LEVEL')

def getLogger(_name):
    logger = logging.getLogger(_name)
    log_level = logging.INFO
    
    if env_log_level == 'DEBUG':
        log_level = logging.DEBUG
    elif env_log_level == 'INFO':
        log_level = logging.INFO
    elif env_log_level == 'ERROR':
        log_level = logging.ERROR
    elif env_log_level == 'CRITICAL':
        log_level = logging.CRITICAL
    elif env_log_level == 'WARNING':
        log_level = logging.WARNING
    logger.setLevel(log_level)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s][%(levelname)s] : %(message)s')
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    return logger