from threading import Thread

class WorkerThread(Thread):
    def __init__(self, fn, *args, **kwargs):
        super(WorkerThread, self).__init__()
        
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

def createThread(fn, *args, **kwargs):
    worker = WorkerThread(fn, *args, **kwargs)
    
    return worker
    
    