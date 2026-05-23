import time

def profile_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000
        print(f"⏱️ Function '{func.__name__}' took {execution_time:.4f} ms to run.")
        return result
    return wrapper

# Applying our custom tool to a heavy calculation loop
@profile_runtime
def process_heavy_loop():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

# process_heavy_loop()