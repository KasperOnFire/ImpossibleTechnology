from time import sleep
from functools import partial
from multiprocessing import cpu_count, Pool


def long_running_function(word_to_find):
    sleep(1)


pool = Pool(processes=cpu_count())
r = pool.map(partial(long_running_function, "love"), range(40))