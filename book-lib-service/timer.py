import time
from functools import wraps
def timer(fn):
    """
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"function '{fn.__name__!r}' took {elapsed_time: 4f} seconds")
        return result
    
    return wrapper

@timer
def myfn(a, b):
    for i in range(1000000):
        pass
    return a+b

result = myfn(5, 3)
print(f"Result: {result}")