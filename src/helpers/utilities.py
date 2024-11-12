from src.configs.logger_settings import LoggerConfig


def instantitate_logs():
    log_config = LoggerConfig()
    log_config.setup_console_logging()  
    log_config.setup_file_logging()
    logger = log_config.get_logger()
    return logger
