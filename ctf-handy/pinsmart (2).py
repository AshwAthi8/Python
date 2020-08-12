#!/usr/bin/env python

import subprocess
import string
from time import sleep

charset = string.ascii_letters + string.digits + "_}"
flag = "flag{"

while True:
    arr = {}
    for i in charset:
        payload = flag + i + (72-(len(flag)+1))*'?'
        print(flag+i)
        subprocess.call('/home/student/Desktop/pincopy/pin -t /home/student/Desktop/pincopy/source/tools/ManualExamples/obj-intel64  -- /home/student/Desktop/ctf/redpwn ' + payload +' ;',shell=True)
        val = int(open("inscount.out").read().split()[1])
        print(val)
        arr[i] = val
    flag+=(max(arr, key=arr.get))
