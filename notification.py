import time 
from plyer import notification 

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "***Drink Water***",
            message = "An average male requires 3.7L and female requires 2.5L of water per day.",
            timeout = 10
        )
        time.sleep(60*60)
