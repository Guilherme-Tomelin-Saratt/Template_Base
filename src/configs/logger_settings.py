import logging
import os

class LoggerConfig:
    def __init__(self, log_level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.logger.handlers = []  
        self.formatter = logging.Formatter(
            '[%(asctime)s] - %(levelname)s - %(message)s', 
            datefmt='%d/%m/%Y - %H:%M:%S'
        )

    def _create_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

    def _create_file_handler(self, filepath, level=logging.ERROR):
        file_handler = logging.FileHandler(filepath, encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def setup_console_logging(self):
        self._create_console_handler()
    
    def get_logger(self):
        return self.logger

    def setup_file_logging(self):
        filename='important_logs.txt'
        directory = 'src/core/db/logs'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        self._create_file_handler(filepath)
        self._create_file_handler(filepath, level=logging.ERROR)

