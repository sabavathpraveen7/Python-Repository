import time

def start_countdown(seconds):
    print(f"Timer started for {seconds} seconds...")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        # The :02d format ensures numbers always take up 2 digits (e.g., 05 instead of 5)
        timer_format = f"{mins:02d}:{secs:02d}"
        
        # \r pushes the cursor back to the start of the line to overwrite it
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1
        
    print("⏰ Time's up! Project complete.")

# start_countdown(90) # Counts down from 1 minute and 30 seconds