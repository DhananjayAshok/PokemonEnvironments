# These are all the utils functions or classes that you may want to import in your project
from poke_env.utils.parameter_handling import load_parameters
from poke_env.utils.log_handling import log_error, log_info, log_warn, log_dict
from poke_env.utils.fundamental import file_makedir
from pandas import isna

def is_none_str(s):
    """
    Checks if a string is None or represents a null value.

    Args:
        s (str or None): The string to check.

    Returns:
        bool: True if the string is None or represents a null value, False otherwise.
    """
    if s is None:
        return True
    if isinstance(s, str):
        options = ["none", "null", "nan", ""]
        for option in options:
            if s.lower() == option:
                return True
    return isna(s)


def nested_dict_to_str(nested_dict, indent=0, indent_char="  "):
    """
    Converts a nested dictionary to a formatted string representation.
    Example Usage: 
    ```python
    nested_dict={2: 4, 3: {4: 5, 6: {7: 8}}}
    print(nested_dict_to_str(nested_dict))
    2: 4
    3: Dict: 
      4: 5
      6: Dict: 
        7: 8
    ```

    Args:
        nested_dict (dict): The nested dictionary to convert.
        indent (int): The current indentation level.
        indent_char (str): The character(s) used for indentation.
    Returns:
        str: A formatted string representation of the nested dictionary.

    """
    result = ""
    for key, value in nested_dict.items():
        result += indent_char * indent + str(key) + ": "
        if isinstance(value, dict):
            result += "Dict: \n" + nested_dict_to_str(value, indent + 1, indent_char=indent_char)
        else:
            result += str(value) + "\n"
    return result