import signal
import os
import time

def receive_signal(signum, stack):
    print('Received:', signum)

signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGINT, receive_signal)

print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)