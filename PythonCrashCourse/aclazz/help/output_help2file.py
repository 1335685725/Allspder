import os
import sys
import turtle
import datetime
out = sys.stdout
sys.stdout = open("helpOfDatetime.txt","w")

help(datetime)
sys.stdout.close()
sys.stdout = out