import pytest
import logging
import inspect
import os


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        #log_directory = r"D:\DevLibrary\python\Demoblaze Framework\reports"
        log_directory = r"C:\REPORTS"
        log_filepath = os.path.join(log_directory, 'logfile.log')
        fileHandler = logging.FileHandler(log_filepath)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        
        return logger