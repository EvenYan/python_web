import threading


local_name = threading.local()


def save_name(name):
    local_name.name = name
    print("name:%s, thread name:%s" % (local_name.name,
                        threading.current_thread().name))


t1 = threading.Thread(target=save_name, args=("Alice",), name="Thread-1")
t2 = threading.Thread(target=save_name, args=("Even",), name="Thread-2")
t1.start()
t2.start()
t1.join()
t2.join()
