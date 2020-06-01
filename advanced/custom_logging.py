#!usr/bin/env python3
import logging

data = {'user': 'ari@example.com'}


def main():
    # set the output file and debug level and use a custom
    # formatting specification
    fmt_str = '[%(asctime)s] %(levelname)s %(message)s ' \
              'STACKTRACE: %(funcName)s:%(lineno)d USER:%(user)s'
    date_str = '%m/%d/%Y %I:%M:%S %p'

    logging.basicConfig(filename='custom_output.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format=fmt_str,
                        datefmt=date_str)

    logging.info('This is an info-level log message', extra=data)
    logging.warning('This is a warning-level message', extra=data)
    another_function()


def another_function():
    logging.debug('This is a debug-level log message', extra=data)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT (in the file):
# [06/01/2020 02:18:55 PM] INFO This is an info-level log message STACKTRACE: main:20 USER:ari@example.com
# [06/01/2020 02:18:55 PM] WARNING This is a warning-level message STACKTRACE: main:21 USER:ari@example.com
# [06/01/2020 02:18:55 PM] DEBUG This is a debug-level log message STACKTRACE: another_function:26 USER:ari@example.com
