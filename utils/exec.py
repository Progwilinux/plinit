import os

def run(cmd):
    return os.system(cmd)

def must(cmd, msg):
    code = os.system(cmd)
    return code == 0