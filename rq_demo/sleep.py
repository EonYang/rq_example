from time import sleep
import signal
import os


warm_shut_down_received = False


def handle_warm_shut_down(signal_number, _):
    global warm_shut_down_received
    print(f'receive signal {signal_number}')
    warm_shut_down_received = True


def register_signals():
    print('Horse PID is:', os.getpid())
    signal.signal(signal.SIGINT, handle_warm_shut_down)
    signal.signal(signal.SIGTERM, handle_warm_shut_down)


def sleep_util_warm_shut_down(seconds: int):
    global warm_shut_down_received
    register_signals()
    while True:
        print(f'Sleeping for {seconds} seconds...')
        sleep(seconds)
        if warm_shut_down_received:
            print('Shutting down horse gracefully.')
            break
