import os, time, random
from multiprocessing import Process, Value

"""
multiprocess中join的作用

"""


def sub_process(name, v):
    print(f'子进程：{name}（{os.getpid()}）开始！')


if __name__ == '__main__':
    print(f'主进程（{os.getpid()}）开始...')
    v = Value("i", 0)  # i 指整数
    p1 = Process(target=sub_process, args=('进程-1', 2))
    # p2 = Process(target=sub_process, args=("进程-2", v,))
    p1.start()
    p1.join()
    print("主进程结束")
