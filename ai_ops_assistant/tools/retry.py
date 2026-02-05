import time

def retry(func, retries=3, delay=1):
    last_error = None

    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_error = e
            time.sleep(delay)

    raise last_error
