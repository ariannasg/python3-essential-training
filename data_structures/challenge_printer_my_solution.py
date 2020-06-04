#!usr/bin/env python3
import random

from data_structures.customqueue import CustomQueue


# create three classes that, together, model how a printer could take print
# jobs out of a print queue. There are a few requirements.
# 1. The first is a class called "PrintQueue" that follows the queue data
# structure implementation.
# 2. The second requirement would be a class called "Job", that has a "pages"
# attribute and each job can have one to 10 pages. You can assign this number
# randomly in your program. The Job class should also have a "print_page"
# method that decrements "pages" and a "check_complete" method, which will
# check whether or not all the pages have been printed.
# 3. The third requirement is a "Printer" class. The "Printer" class should
# have a "get_job" method that makes use of the queues built-in dequeue
# method to take the first job in the PrintQueue off of the queue.

class PrintQueue(CustomQueue):
    def __init__(self):
        super().__init__()


class Job:
    def __init__(self, job_name):
        self._name = job_name
        self._pages = random.randint(1, 10)

    def print_page(self):
        if self._pages > 0:
            print('.', end=' ')
            self._pages -= 1

    def check_complete(self):
        return self._pages == 0

    def __repr__(self):
        return f'Job <name: {self._name} pages:{self._pages}>'


class Printer:
    def __init__(self):
        self._queue = PrintQueue()

    def add_job(self, job):
        if not isinstance(job, Job):
            raise TypeError('the job should be of type Job')
        self._queue.enqueue(job)

    def get_job(self):
        while not self._queue.is_empty():
            job: Job = self._queue.dequeue()
            print(f'Printing pages of: {str(job)}')
            while job.check_complete() is False:
                job.print_page()
            print('\n')
        return None


printer = Printer()

printer.add_job(Job('job1'))
printer.add_job(Job('job2'))
printer.add_job(Job('job3'))

printer.get_job()

# CONSOLE OUTPUT (it will vary!):
# Printing pages of: Job <name: job1 pages:3>
# . . .
#
# Printing pages of: Job <name: job2 pages:2>
# . .
#
# Printing pages of: Job <name: job3 pages:5>
# . . . . .
