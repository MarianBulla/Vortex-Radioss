import logging
import platform

from vortex_radioss.lasso.utils.console_coloring import ConsoleColoring

# settings
MARKER_INFO = "[/]"
MARKER_RUNNING = "[~]"
MARKER_WARNING = "[!]"
MARKER_SUCCESS = "[Y]" if platform.system() == "Windows" else "[✔]"
MARKER_ERROR = "[X]" if platform.system() == "Windows" else "[✘]"

LOGGER_NAME = "lasso"


def str_info(msg: str):
    """Format a message as stuff is running

    Parameters
    ----------
    msg: str
        message to format

    Returns
    -------
    msg_ret: str
        formatted message
    """
    # return ConsoleColoring.blue("[/] {0}".format(msg), light=True)
    return f"{MARKER_INFO} {msg}"


def str_running(msg: str):
    """Format a message as stuff is running

    Parameters
    ----------
    msg: str
        message to format

    Returns
    -------
    msg_ret: str
        formatted message
    """
    return f"{MARKER_RUNNING} {msg}"


def str_success(msg: str):
    """Format a message as successful

    Parameters
    ----------
    msg: str
        message to format

    Returns
    -------
    msg_ret: str
        formatted message
    """
    return ConsoleColoring.green(f"{MARKER_SUCCESS} {msg}")


def str_warn(msg: str):
    """Format a string as a warning

    Parameters
    ----------
    msg: str
        message to format

    Returns
    -------
    msg_ret: str
        formatted message
    """
    return ConsoleColoring.yellow(f"{MARKER_WARNING} {msg}")


def str_error(msg: str):
    """Format a string as an error

    Parameters
    ----------
    msg: str
        message to format

    Returns
    -------
    msg_ret: str
        formatted message
    """
    return ConsoleColoring.red(f"{MARKER_ERROR} {msg}")


def get_logger(file_flag: str) -> logging.Logger:
    """Get the logger for the lasso module

    Returns
    -------
    logger: logging.Logger
        logger for the lasso module
    """
    logging.basicConfig(
        datefmt="[%(levelname)s] %(message)s [%(pathname)s %(funcName)s %(lineno)d]"
    )
    return logging.getLogger(file_flag)
