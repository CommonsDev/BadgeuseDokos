import config
import urllib3
import json
from authentication import Authentication

# Without certificat :
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Authentication
auth = Authentication(rfid="10:10:60")
print(auth.add_passage_to_log(type=config.badging_type))