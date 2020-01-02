import absl.logging
import datetime
import json
import logging
import logging.handlers
import os
import time

# Disable absl logging as it interferes with the default logger
logging.root.removeHandler(absl.logging._absl_handler)
absl.logging._warn_preinit_stderr = False

class Logger():
    """Creates the logging object"""

    def __init__(self, name, create=False):

        # Setup logging parameters
        level = logging.DEBUG
        _format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
        formatter = logging.Formatter(_format)

        # Create logger
        logging.basicConfig(level=level, format=_format)
        self.logger = logging.getLogger(name)

        # Log location
        username = os.getlogin()
        logLocation = f"C:\\Users\\{username}\\AppData\\Local\\Temp\\tf-easy-install"

        timestamp = ""
        if create:
            # Perform first-time setup
            try:
                os.makedirs(logLocation, exist_ok=True)
            except PermissionError:
                # Replace with UI error message
                raise PermissionError(f"Unable to access log location: {logLocation}")
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H%M%S")
        else:
            logFiles = os.listdir(logLocation)
            if logFiles == []:
                Logger(name, create=True)
            timestamp = logFiles[-1].strip(".log")

        logFile = os.path.join(logLocation, (timestamp + ".log"))

        # Setup file handler
        fileHandler = logging.handlers.TimedRotatingFileHandler(logFile, when="D", backupCount=7)
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)
        self.logger.debug("Initialized logging for {}".format(name))
