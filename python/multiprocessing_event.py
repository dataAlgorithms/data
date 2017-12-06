from multiprocessing import Event, Process 
import time

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print("wait_for_event: starting")
    e.wait()
    print("wait_for_event: e.is_set()->" + str(e.is_set()))

def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print("Wait_for_event_timeout: starting")
    e.wait(t)
    print("Wait_for_event_timeout: e.is_set()->" + str(e.is_set()))

'''
Wait_for_event_timeout: starting
wait_for_event: starting
Wait_for_event_timeout: e.is_set()->False
main: event is set
wait_for_event: e.is_set()->True
'''
if __name__ == "__main__":
    e = Event()
    w1 = Process(name='block',
                 target=wait_for_event,
                 args=(e, ))
    w1.start()

    w2 = Process(name='non-block',
                 target=wait_for_event_timeout,
                 args=(e, 2))
    w2.start()
    time.sleep(3)
    e.set()
    print("main: event is set")