from queue import Queue
from typing import Optional

from Data.Post import Post


class SharedList:
    def __init__(self):
        self._queue = Queue()

    def add(self, post: Post):
        self._queue.put(post)

    def take(self) -> Optional[Post]:
        return self._queue.get()  # Blocks until an item is available

    # print method for testing
    def print_all(self):
        items = list(self._queue.queue)
        for item in items:
            print(item.platform)
