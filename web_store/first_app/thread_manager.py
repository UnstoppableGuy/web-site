import threading

'''
    Just adds a function to a pool of threads and starts it.
'''
class ThreadManager(): # pragma: no cover
    all_threads = []

    def add(self, our_function, *args, **kwargs):
        new_thread = threading.Thread(target=our_function, args=args, kwargs=kwargs)
        new_thread.start()
        self.all_threads.append(new_thread)

    def stop_all(self):
        threading._shutdown()