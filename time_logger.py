from functools import wraps


def time_logger(location='generic-logs'):
    
    def my_timer(orig_func):

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
            starting_time = datetime.now()
            result = orig_func(*args, **kwargs)
            ended_time = datetime.now()
            t2 = ended_time - starting_time
            logging.info(f'{orig_func.__name__} ran in {t2} seconds on {starting_time}, ended at {ended_time}')
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)
            return result  
        return wrapper
    return my_timer
