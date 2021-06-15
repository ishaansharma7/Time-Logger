from functools import wraps

'''In your python script write the following line to import this decorator (assuming both files are in same directory)

from time_logger import time_logger

'''


def time_logger(location='generic-logs'):
    
    def my_timer(orig_func):
        import time
        from datetime import datetime
        import logging
        import os
        final_location = os.path.join('logs', location)
        if os.path.exists(final_location) != True:
            print('Directory does not exist, creating directory')
            os.makedirs(final_location)
        
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            logging.basicConfig(filename=f'{final_location}/{orig_func.__name__}.log', level=logging.INFO)
            t1 = time.time()
            starting_time = datetime.now()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            ended_time = datetime.now()
            logging.info(f'{orig_func.__name__} ran in {round(t2, 2)} seconds on {starting_time}, ended at {ended_time}')
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)
            return result  
        return wrapper
    return my_timer