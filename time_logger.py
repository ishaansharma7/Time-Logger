from functools import wraps
import os
import logging
from datetime import datetime

def time_logger(location='generic-logs'):
    
    def my_timer(orig_func):
        
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            
            final_location = os.path.join('logs', location)
            if os.path.exists(final_location) != True:
                print('Directory does not exist, creating directory')
                os.makedirs(final_location)
            
            logging.basicConfig(filename=f'{final_location}/{orig_func.__name__}.log', level=logging.INFO, force=True)
            starting_time = datetime.now()
            t1 = datetime.today().timestamp()
            result = orig_func(*args, **kwargs)
            ended_time = datetime.now()
            t2 = datetime.today().timestamp() - t1
            logging.info(f'{orig_func.__name__} ran in {round(t2, 3)} seconds on {starting_time}, ended at {ended_time}')
            
            return result  
        return wrapper
    return my_timer