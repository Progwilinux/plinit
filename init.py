import os
import time
from utils.term import info, banner, ascii_logo
from utils.exec import run

os_release = {}
try:
    with open("/etc/os-release", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                value = value.strip().strip('"')
                os_release[key] = value
except FileNotFoundError:
    pass

EDITION = os_release.get("EDITION", "DEFAULT")

run("mount -t proc proc /proc")
info("Mounting proc.")
run("mount -t sysfs sysfs /sys")
info("Mounting sysfs.")
run("mount -t devtmpfs devtmpfs /dev")
info("Mounting devtmpfs.")

banner(EDITION)

run("hostname -F /etc/hostname")

run("clear")

ascii_logo()

run("chmod 777 /tmp")
run("chmod 777 /programs")

run("clear")

os.execv("/programs/cucumber", ["/programs/cucumber"])
