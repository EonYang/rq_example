import os
from rq.worker import Worker
from rq_demo.redis_client import redis_client


def main():
    worker = Worker(
        ['high', 'default', 'low'],
        connection=redis_client
    )
    worker.work()
    return


if __name__ == '__main__':
    print('Worker PID is:', os.getpid())
    main()
