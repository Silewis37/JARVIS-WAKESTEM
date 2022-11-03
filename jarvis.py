import os
import sys
import time
import socket
from colorama import Fore
import platform
import multiprocessing
import psutil
from datetime import datetime
from os import listdir
from os.path import isfile, join
import html
import giftoa

## All Variables Used and Needed in the Functions
uptime = None
hostname = socket.gethostname()
temps = psutil.sensors_temperatures()

## All Defined Functions

def clear():
    os.system('clear')

def internet_check():
    try:
        socket.create_connection(("www.google.com", 80))
        type(Fore.GREEN + "[JARVIS][*-*] Internet Connection is Online!")
        return None
    except OSError:
        type(Fore.RED + "[JARVIS][*-*] Warning! Internet Connection is Offline!")
        return None

def type(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.09)

def kira(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.19)

def yoshikage_kira():
    clear()
    type("A Man Aproaches you while you are Walking down the street...\n")
    time.sleep(2.5)
    type("Yoshikage Kira:\n")
    kira("My name is Yoshikage Kira.\n")
    kira("I'm 33 years old.\nMy house is in the northeast section of Morioh, where all the villas are, and I am not married.\nI work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest.\nI don't smoke, but I occasionally drink.\nI'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what.\nAfter having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning.\nJust like a baby, I wake up without any fatigue or stress in the morning.\nI was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life.\nI take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night.\nThat is how I deal with society, and I know that is what brings me happiness.\nAlthough, if I were to fight I wouldn't lose to anyone.\n")

def uptime_eval():
    with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()
    uptime = int(float(uptime))
    uptime_hours = uptime // 3600
    uptime_minutes = (uptime % 3600) // 60
    type("Uptime >>> " + str(uptime_hours) + " Hrs and " + str(uptime_minutes) + " Mins \n")
    


def system_info():
    clear()
    internet_check()
    type(Fore.BLACK + "\n\n-//--//--//--//--//--//--" + Fore.LIGHTRED_EX + "[JARVIS]" + Fore.BLACK + "--//--//--//--//--//--//-\n\n")
    type("Current User >>> " + os.getlogin() + "\n")
    type("Current IP >>> " + socket.gethostbyname(hostname) + "\n")
    type("Cpu Cores >>> " + str(multiprocessing.cpu_count()) + "\n")
    uptime_eval()
    type("Architecture >>> " + platform.architecture()[0] + "\n")
    type("Machine >>> " + platform.machine() + "\n")
    type("Node >>> " + platform.node() + "\n")
    type("System OS >>> " + platform.system() + "\n")

system_info()

#onlyfiles = [f for f in listdir('/home/silewis/Desktop/[JARVIS]Update_Files') if isfile(join('/home/silewis/Desktop/[JARVIS]Update_Files', f))]
#print(onlyfiles)

