import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="Water Reminder",
            message="It's time to drink water! Stay hydrated.",
            timeout=10
        )
        time.sleep(3600)  # Remind every hour

if __name__ == "__main__":
    water_reminder()