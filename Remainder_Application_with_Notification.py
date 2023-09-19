from turtle import title
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
title = input("\nTitle of remainder:")
msg = input("Message:")
minutes = float(input("How Many Minutes:"))
seconds = minutes * 60
print("\nReminder Set successfully!\n")
time.sleep(seconds)
toaster.show_toast(title, msg, duration=10, threaded=True)
while toaster.notification_active:
    time.sleep(0.1)
