import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_c = time.perf_counter()

        result = func(*args, **kwargs)

        time_d = time.perf_counter()
        print(f"Time to completion: {time_d - time_c}")
        return result

    return wrapper
