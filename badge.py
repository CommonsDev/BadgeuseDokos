import config
import urllib3
import json
import os
import time
from user import User as User

# Without certificat :
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""
user = User(rfid="60:78:24")
print(user.can_enter())
"""
cmd = "nfc-poll|grep UID"
while True:
    t = os.popen(cmd).read().strip()
    if (t.startswith("UID")):
        UID_avec_space = t.split(":")[1]
        UID_sans_space = UID_avec_space.replace("  ",":").strip()
        print(UID_sans_space)
        user = User(rfid=UID_sans_space)
        if user.can_enter():
            print("C'est bon")
        else:
            print("Non")
    else:
        print("Rien")
    time.sleep(1)