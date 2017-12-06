from multiprocessing import Process, Lock

def worker_with(lock, f):
    with lock:
        fs = open(f, "a+")
        fs.write("Lock acquired via with\n")
        fs.close()

def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, "a+")
        fs.write("Lock acquired directly\n")
        fs.close()
    finally:
        lock.release()

if __name__ == "__main__":
    f = "file.txt"
    lock = Lock()
    w = Process(target=worker_with, args=(lock, f))
    nw = Process(target=worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    w.join()
    nw.join()