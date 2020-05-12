import logging
import logging.handlers
import os
from django.conf import settings


class Logger:

    def __init__(self, logger_name):
        logging.captureWarnings(True)
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        self.logPath = settings.LOG_PATH

        if not os.path.exists(self.logPath):
            self.logPath = os.path.dirname(os.path.abspath(__file__))

        LOG_FILENAME = os.path.normpath('{}/{}.log'.format(self.logPath, logger_name))

        fh = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5242880, backupCount=10)
        fh.setLevel(logging.INFO)
        fh.setFormatter(logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s'))
        self.logger.addHandler(fh)

    def debug(self, msg):
        self.log(logging.DEBUG, msg)

    def info(self, msg):
        self.log(logging.INFO, msg)

    def warning(self, msg):
        self.log(logging.WARNING, msg)

    def error(self, msg):
        self.log(logging.ERROR,msg)

    def critical(self, msg):
        self.log(logging.CRITICAL, msg)

    def log(self, level, msg):
        msg = str(msg).replace('%', '')
        self.logger.log(level, str(msg) +' %s', '')
