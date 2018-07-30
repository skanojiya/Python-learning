#! /usr/bin/python

import subprocess

#cmd1 = "adb shell am start com.android.settings/.accounts.AddAccountSettings"
cmd1 = "adb shell am start com.android.chrome"
#cmd1 = "adb shell am start com.google.android.apps.nexuslauncher/.NexusLauncherActivity"
#p1= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

p1= subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
p2= subprocess.Popen("driver.navigate().back()", shell=True,stdout=subprocess.PIPE)
#p1= subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
#for results in p1.stdout:
 #  ss = results
  # print ss
def Test():
 Mobile.SetCurrent("MyDevice")
 p = Mobile.Device().Process("com.android.chrome")
 Toggle = p.RootLayout("").Layout("layoutTop").Layout("layout1").ToggleButton("toggle1")
 Toggle.Touch()
 Log.Message(Toggle.wState)
 print ("State:" + Toggle.wState)

 
