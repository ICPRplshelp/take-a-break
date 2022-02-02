"""This is a literal python timer. What else did you expect?
"""

import time
from win10toast import ToastNotifier
# from playsound import playsound

# BREAKSOUND = 'Hamburger.mp3'
# RESUMESOUND = 'smallmedkit1.wav'

# literally half minutes
PRIMARY_TIME = 40
SECONDARY_TIME = 1

SECS_PER_INTERVAL = 30

if __name__ == '__main__':
    # playsound(RESUMESOUND)
    # exit()
    half_minutes_left = PRIMARY_TIME
    countdown = True
    toaster = ToastNotifier()
    print('Starting timer.')
    while True:
        mins, secs = divmod(half_minutes_left, 2)
        sec_str = '30s' if secs == 1 else '00s'
        print(f"You have {mins}m{sec_str} left")
        time.sleep(SECS_PER_INTERVAL)
        half_minutes_left -= 1
        if half_minutes_left == 0:
            if countdown:  # THIS HAPPENS IF BREAK TIME STARTS
                half_minutes_left = SECONDARY_TIME
                # playsound(BREAKSOUND)
                # tell me to take a break
                toaster.show_toast('TIMER', '20 MINUTES HAVE PASSED. LOOK AWAY.')
            else:  # THIS HAPPENS IF BREAK TIME ENDS
                # playsound(RESUMESOUND)
                half_minutes_left = PRIMARY_TIME
                toaster.show_toast('TIMER', '30 SECONDS HAVE PASSED. YOU MAY LOOK BACK.')
                # tell me to STOP MY BREAK

            countdown = not countdown
    # keyboard interrupt to stop this thing.
