from poke_env.utils.fundamental import meta_dict_to_str
from poke_env.utils.parameter_handling import load_parameters


def log_error(message: str, parameters: dict = None):
    """
    Log an error message and raise a ValueError.
    Args:
        message (str): The error message to log.
        parameters (dict, optional): Parameters dictionary containing the logger. See load_parameters for details.
        If parameters is None, the default parameters will be loaded from the config files
        If the log_file or log_dir is overwritten in the command line parameters, then calling this function with parameters=None
        will *not* log to the command line file. In general, use None only if you are confident that the parameters have not been changed.
    """
    parameters = load_parameters(parameters)
    logger = parameters["logger"]
    logger.error(message, stacklevel=2)
    raise ValueError(message)

def log_warn(message: str, parameters: dict = None):
    """
    Log a warning message.
    Args:
        message (str): The warning message to log.
        parameters (dict, optional): Parameters dictionary containing the logger. See load_parameters for details.
        If parameters is None, the default parameters will be loaded from the config files
        If the log_file or log_dir is overwritten in the command line parameters, then calling this function with parameters=None
        will *not* log to the command line file. In general, use None only if you are confident that the parameters have not been changed.
    """
    parameters = load_parameters(parameters)
    logger = parameters["logger"]
    logger.warn(message, stacklevel=2)

def log_info(message: str, parameters: dict = None):
    """
    Log an info message.
    Args:
        message (str): The info message to log.
        parameters (dict, optional): Parameters dictionary containing the logger. See load_parameters for details.
        If parameters is None, the default parameters will be loaded from the config files
        If the log_file or log_dir is overwritten in the command line parameters, then calling this function with parameters=None
        will *not* log to the command line file. In general, use None only if you are confident that the parameters have not been changed.
    """
    parameters = load_parameters(parameters)
    logger = parameters["logger"]
    logger.info(message, stacklevel=2)

def log_dict(meta_dict: dict, n_indents: int = 1, parameters: dict =None):
    """
    Print a dictionary in a readable format
    Args:
        meta_dict (dict): The dictionary to log.
        n_indents (int, optional): Number of indentation levels for formatting. Defaults to 1.
        parameters (dict, optional): Parameters dictionary containing the logger. See load_parameters for details.
        If parameters is None, the default parameters will be loaded from the config files
        If the log_file or log_dir is overwritten in the command line parameters, then calling this function with parameters=None
        will *not* log to the command line file. In general, use None only if you are confident that the parameters have not been changed.
    """
    parameters = load_parameters(parameters)
    logger = parameters["logger"]
    meta_dict_str = meta_dict_to_str(meta_dict, print_mode=True, n_indents=n_indents, skip_write_timestamp=False)
    logger.info(meta_dict_str, stacklevel=2)
