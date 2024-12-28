# _*_ coding:utf-8 _*_

from concurrent.futures import ThreadPoolExecutor


"""
线程池使用说明：
1. 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
2. 向线程池提交一个task, 20会作为action()函数的参数
future1 = pool.submit(action, 20)
3. 向线程池再提交一个task, 30会作为action()函数的参数
future2 = pool.submit(action, 30)
4. 判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
5. 判断future2代表的任务是否结束
print(future2.done())
6. 查看future1代表的任务返回的结果
print(future1.result())
7. 查看future2代表的任务返回的结果
print(future2.result())
8. 关闭线程池
pool.shutdown()
"""


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=10)

class ThreadPool:
    def __init__(self) -> None:
        pass
    def thread_start_get_docker_server_info(self,f,params):
        pool.submit(f, params)