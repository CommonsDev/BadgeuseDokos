import config
import time
from dokos_connector import DokosConnector as DokosConnector

class User:

    def __init__(self, rfid):
        self.dokos = DokosConnector(config.api_url, config.dokos_client, config.dokos_token)
        # Get the name of the document associated to a rfid
        user_document_name = self.dokos.get_resources_by_filter(resource="Members", filters=[["rfid", "=", rfid]]).json()["data"]
        # Get the userdata associated to a rfid
        user_data = self.dokos.get_resource("Members", user_document_name[0]['name']).json()["data"]
        print(user_data)
        self.document_name = user_data["name"]
        self.client_name = user_data["client_name"]
        self.nb_ticket = int(user_data["nb_ticket"])
        self.timestamp_activated = int(user_data["timestamp_activated"])
        self.timestamp_valid = int(user_data["timestamp_valid"])
        self.rfid = user_data["rfid"]

    def can_enter(self):
        """
        Determine if a user can enter
        :return: Return true if a user can enter else if not
        """

        # TODO d'abord check la validité du ticket actuel sinon on vérifie s'il a un ticket et on utilise, sinon on refuse
        current_time_in_milliseconds = int(round(time.time() * 1000))

        if current_time_in_milliseconds < self.timestamp_valid:
            print("Un ticket est encore en cours de validité")
            return True
        else:
            if self.nb_ticket > 0:
                # 300000 is 5 minutes in milliseconds
                updated_content, status_code = self.dokos.update_resource_by_name("Members", self.document_name, {"nb_ticket" : (self.nb_ticket - 1), "timestamp_activated": current_time_in_milliseconds, "timestamp_valid": current_time_in_milliseconds + 300000})
                if status_code == 200:
                    print("Le ticket a été consommé")
                    return True
                else:
                    print("Le ticket ne peut être consommé")
                    return False
        return False