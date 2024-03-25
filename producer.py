import threading
import queue
import time

def producer(q):
    for i in range(10):
        print('Produced', i)
        q.put(i)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('Consumed', item)
        q.task_done()

q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))

t1.start()
t2.start()

t1.join()
q.put(None)  # Signal the consumer to exit
t2.join()