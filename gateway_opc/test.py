import time
import threading
import random

box = []


def box_input():
    temp = []
    for i in range(100000):
        temp.append(random.randint(0, 10000))
    return temp


if __name__ == '__main__':
    while True:
        box = box_input()
        # print(f'количество потоков {threading.active_count()}')
        print(box[5])
        time.sleep(1)
