def console_log(msg):
    """
    Logs a message to the console.

    :param msg: message to log
    :type msg: str
    :return: None
    """
    print("KPotify - " + msg)


def warning(msg):
    """
    Logs a warning to the console.

    :param msg: warning message
    :return: None
    """
    console_log("Warning: " + msg)


def error(msg):
    """
    Logs an error to the console.

    :param msg: error message
    :return: None
    """
    console_log("Error: " + msg)


def debug(msg):
    """
    Logs a debug message to the console.

    :param msg: debug message
    :return: None
    """
    console_log("Debug: " + msg)