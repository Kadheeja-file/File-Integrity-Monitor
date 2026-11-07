import os
import hashlib
import time

folder = input("Enter folder path: ")

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def scan():
    files = {}
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            files[name] = get_hash(path)
    return files

old = scan()
print("Monitoring started!")

while True:
    time.sleep(5)
    new = scan()

    for name in new:
        if name not in old:
            print("NEW FILE:", name)
        elif new[name] != old[name]:
            print("FILE MODIFIED:", name)

    for name in old:
        if name not in new:
            print("FILE DELETED:", name)

    old = new