import config
from dokos_connector import DokosConnector
from authentication import Authentication
import json

connector = DokosConnector(config.api_url,config.dokos_client,config.dokos_token)
print("Connection reussi")

auth = Authentication("88:88:88:88")

print(auth.get_user_and_customer_for_rfid())


