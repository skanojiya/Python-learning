#! /usr/bin/python

from uiautomater import device as me

#import sys
import os

cmd1 ="adb root"
cmd2 = "adb shell getprop ro.serialno"

device_id = os.system(cmd2)
print(device_id)

m(text="Clock").click()


