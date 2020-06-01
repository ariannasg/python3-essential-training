#!usr/bin/env python3
import logging


# use the built-in logging module
def main():
    # Use basicConfig to configure the min logging level for output.
    # this is only executed once, subsequent calls to basicConfig will have
    # no effect.
    # if the level is not specified then only the warning, error & critical
    # logs will be shown.
    # if we don't specify a filename then the logging will be printed to the
    # console.
    # if we don't specify the filemode then it opens the file in append mode
    # by default.
    logging.basicConfig(level=logging.DEBUG,
                        filemode='w',
                        filename='output.log')

    # Try out each of the log levels
    logging.debug('This is a debug-level log message')
    logging.info('This is an info-level log message')
    logging.warning('This is a warning-level message')
    logging.error('This is an error-level message')
    logging.critical('This is a critical-level message')

    # Output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format('string', 10))


if __name__ == "__main__":
    main()


# CONSOLE OUTPUT (in the file):
# DEBUG:root:This is a debug-level log message
# INFO:root:This is an info-level log message
# WARNING:root:This is a warning-level message
# ERROR:root:This is an error-level message
# CRITICAL:root:This is a critical-level message
# INFO:root:Here's a string variable and an int: 10
