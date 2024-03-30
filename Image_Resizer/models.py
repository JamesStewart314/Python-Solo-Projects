import itertools
import math
import multiprocessing.pool as mpp

class LoadingBar:

    def __init__(self, number_of_tasks) -> None:

        self._number_of_tasks = number_of_tasks
        self._tasks_done = 0
        self._progress_percent = 0
        self._progress = 0
        self._status = "\033[3m\033[1mLoading\033[0m"

        self._ellipsis_anim = itertools.cycle(("\033[31m.  \033[0m", "\033[33m.. \033[0m", "\033[34m...\033[0m"))
        self._bar_anim = itertools.cycle(("|", "/", "-", "\\"))
        self._reversed_bar_anim = itertools.cycle(("|", "\\", "-", "/"))

    def increase_progress(self) -> None:
        if self._number_of_tasks == self._tasks_done: return
        
        self._tasks_done += 1
        self._progress_percent = round(self._tasks_done * 100 / self._number_of_tasks, 1)
        self._progress = math.floor(self._progress_percent)

        if self._progress == 100: 
            self._status = "\033[3m\033[1mDone\033[0m"
            self._ellipsis_anim = itertools.repeat("!!!")
            self._bar_anim = itertools.repeat("-")
            self._reversed_bar_anim = self._bar_anim
    
    def __str__(self) -> str:
        return f"{self._status}{next(self._ellipsis_anim)} {next(self._reversed_bar_anim)} "\
        f"[\033[32m{"═" * (qtd := int(self._progress / 2))}\033[31m{"═" * (50 - qtd)}\033[0m] "\
        f"{next(self._bar_anim)}"


# istarmap.py for Python 3.8+
def istarmap(self, func, iterable, chunksize=1):
    
    """starmap-version of imap"""

    self._check_running()

    if chunksize < 1:
        raise ValueError("Chunksize must be 1+, not {0:n}".format(chunksize))

    task_batches = mpp.Pool._get_tasks(func, iterable, chunksize)
    result = mpp.IMapIterator(self)
    self._taskqueue.put(
        (
            self._guarded_task_generation(result._job, mpp.starmapstar, task_batches),
            result._set_length
        ))
    
    return (item for chunk in result for item in chunk)


mpp.Pool.istarmap = istarmap
