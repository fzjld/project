from multiprocessing import Pool
import os


def get_pid(name):
    print(f"pid_name: {name}", os.getpid())


if __name__ == '__main__':
    n = os.cpu_count()
    pool = Pool(n)
    for i in range(n):
        pool.apply_async(get_pid, args=(f"子进程-{n}",))

    pool.close()
    pool.join()
