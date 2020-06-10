#!usr/bin/env python3
from contextlib import contextmanager

HEADER = "this is the header\n"
FOOTER = "this is the footer\n"


@contextmanager
def new_log_file(name):
    try:
        log_name = name
        file = open(log_name, 'w')
        file.write(HEADER)
        yield file
    finally:
        file.write(FOOTER)
        print('logfile created')
        file.close()


def main():
    with new_log_file('logfile') as file:
        file.write('this is the body\n')


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT (to logfile):
# this is the header
# this is the body
# this is the footer
