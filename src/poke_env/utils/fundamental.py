# This file contains all the fundamental utilities that do not rely on any other file. 
import os
import logging

def get_logger(level: int = logging.INFO, filename: str = None, add_console: bool = True):
    """
    Sets up and returns a logger with specified configurations.
    Args:
        level (int, optional): Logging level. Defaults to logging.INFO.
        filename (str, optional): If provided, logs will be written to this file. Defaults to None.
        add_console (bool, optional): If True, logs will also be printed to the console. Defaults to True.
    Returns:
        logging.Logger: Configured logger instance.
    """
    fmt_str = "%(asctime)s, [%(levelname)s, %(filename)s:%(lineno)d] %(message)s"
    logging.basicConfig(format=fmt_str)
    logger = logging.getLogger("PROJECT_NAME")
    if add_console:
        logger.handlers.clear()
        console_handler = logging.StreamHandler()
        log_formatter = logging.Formatter(fmt_str)
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)
    if filename is not None:
        file_handler = logging.FileHandler(filename, mode="a")
        log_formatter = logging.Formatter(fmt_str)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
    if level is not None:
        logger.setLevel(level)
        logger.propagate = False
    return logger

def meta_dict_to_str(meta_dict: dict, print_mode: bool = False, n_indents: int = 1, skip_write_timestamp: bool = True):
    """
    Converts a metadata dictionary to a string representation.
    Args:
        meta_dict (dict): The metadata dictionary to convert.
        print_mode (bool, optional): If True, formats the string for printing with indentation. Defaults to False.
        n_indents (int, optional): Number of indentation levels for print mode. Defaults to 1.
        skip_write_timestamp (bool, optional): If True, skips the 'write_timestamp' key in non-print mode. Defaults to True.
    Returns:
        str: String representation of the metadata dictionary.
    """
    keys = list(meta_dict.keys())
    keys.sort()
    meta_str = ""
    for key in keys:
        if print_mode:
            indent = '\t' * n_indents
            meta_str += f"{indent}{key}: {meta_dict[key]}\n"
        else:
            if skip_write_timestamp and key == "write_timestamp":
                continue
            meta_str += f"{key.lower().strip()}_{str(meta_dict[key]).lower().strip()}"
    return meta_str


def logger_print_dict(logger: logging.Logger, meta_dict: dict, n_indents: int = 1):
    """
    Logs the string representation of a metadata dictionary using the provided logger.
    Args:
        logger (logging.Logger): The logger to use for logging.
        meta_dict (dict): The metadata dictionary to log.
        n_indents (int, optional): Number of indentation levels for formatting. Defaults to 1.
    """
    meta_dict_str = meta_dict_to_str(meta_dict, print_mode=True, n_indents=n_indents, skip_write_timestamp=False)
    logger.info(meta_dict_str)


def file_makedir(file_path: str):
    """
    Ensures that the directory for the given file path exists. If not, it creates the necessary directories.
    Args:
        file_path (str): The file path for which to ensure the directory exists.
    """
    dirname = os.path.dirname(file_path)
    if dirname != "" and not os.path.exists(dirname):
        os.makedirs(dirname)
    return
