import time

ESC = "\x1b"

RESET = ESC + "[0m"
GREEN = ESC + "[32m"
RED = ESC + "[31m"
WHITE = ESC + "[1;37m"

def printf(text):
    print(text)

def info(msg):
    print(GREEN + msg + RESET)

def error(msg):
    print(RED + msg + RESET)

def banner(edition):
    if edition == "DEFAULT":
        print(RESET + "Welcome to " + GREEN + "Progwilinux" + RESET + "!")
    elif edition == "PRO":
        print(RESET + "Welcome to " + GREEN + "Progwilinux Pro" + RESET + "!")

def ascii_logo():
    print(ESC + "[1;31m██████╗ ██████╗  ██████╗ ██╗    ██╗██╗██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗")
    time.sleep(1)
    print(ESC + "[1;33m██╔══██╗██╔══██╗██╔═══██╗██║    ██║██║██║     ██║████╗  ██║██║   ██║╚██╗██╔╝")
    time.sleep(1)
    print(ESC + "[1;32m██████╔╝██████╔╝██║   ██║██║ █╗ ██║██║██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ ")
    time.sleep(1)
    print(ESC + "[1;36m██╔═══╝ ██╔══██╗██║   ██║██║███╗██║██║██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ ")
    time.sleep(1)
    print(ESC + "[1;34m██║     ██║  ██║╚██████╔╝╚███╔███╔╝██║███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗")
    time.sleep(1)
    print(ESC + "[1;35m╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝")
    time.sleep(5)