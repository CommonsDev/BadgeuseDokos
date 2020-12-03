import config
import json
from datetime import datetime as dt
from dokos_connector import DokosConnector


class Authentication:

    def __init__(self, rfid):
        self.rfid = rfid
        self.connector = DokosConnector(config.api_url, config.dokos_client, config.dokos_token)

    def get_user_and_customer_for_rfid(self):
        document = self.connector.get_resources_by_filter(resource=config.badge_allocation_resource_name,
                                                          filters=[["rfid", "=", self.rfid]]).json()['data']
        result = \
        self.connector.get_resource(resource=config.badge_allocation_resource_name, name=document[0]['name']).json()[
            'data']
        return result['user'], result['customer']

    def add_passage_to_log(self, date=None,type="None"):
        user, customer = self.get_user_and_customer_for_rfid()
        if date==None:
            date = str(dt.now())
        data = {
            'user': user,
            'customer': customer,
            'rfid': self.rfid,
            'date': date,
            'type': type
        }
        return self.connector.insert_resource(resource=config.passage_log_resource_name, data=json.dumps(data))
