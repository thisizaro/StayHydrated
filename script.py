import time
from plyer import notification

def timer(n):
    print("Timer started!")
    while n > 0:
        n = n - 1
        time.sleep(1)
        s = str(n)
        for i in range(0, len(s)):
            print("\b", end="", flush=True)
        print(n, end = "", flush=True)
    

def remind_to_drink_water(interval_minutes):
    interval_seconds = interval_minutes * 60
    count = 0
    while True:
        print("Running...", count)
        count += 1
        timer(interval_seconds)
        notification.notify(
            title='Hydration Reminder',
            message='It\'s time to drink water!',
            timeout=10
        )

# Set the interval time in minutes
interval_minutes = 30  # for example, set to 60 minutes
remind_to_drink_water(interval_minutes)
