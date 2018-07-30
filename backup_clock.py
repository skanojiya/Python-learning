#! /usr/bin/python
#!/usr/bin/env python

from uiautomator import device as me  

import os
#import sys

cmd1 ="adb root"
cmd2 = "adb shell getprop ro.serialno"

device_id = os.system(cmd2)
print(device_id)

me(text="Clock").click()

me(descriptionMatches="Add alarm").click()

me(resourceIdMatches="android:id/hours").click()

me(descriptionMatches="6").click()

me(resourceIdMatches="android:id/minutes").click()

me(descriptionMatches="0").click()

me(textMatches="OK").click()
