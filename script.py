import time
from plyer import notification

def remind_to_drink_water(interval_minutes):
    interval_seconds = interval_minutes * 60
    while True:
        print("Running...")
        time.sleep(interval_seconds)
        notification.notify(
            title='Hydration Reminder',
            message='It\'s time to drink water!',
            timeout=10
        )

# Set the interval time in minutes
interval_minutes = 30  # for example, set to 60 minutes
remind_to_drink_water(interval_minutes)
