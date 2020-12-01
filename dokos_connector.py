import requests


class DokosConnector:

    def __init__(self, api_url, dokos_client, dokos_token):
        """
        Init the dokos connector with the required parameters

        :param api_url: The Dokos url that ends with api/
        :param dokos_client: The Dokos API Client
        :param dokos_token: The Dokos API Client Token
        """
        self.api_url = api_url
        self.api_login = dokos_client
        self.api_password = dokos_token

        # Init the headers used in the authenticated request
        self.headers = {
            'Authorization': "token " + dokos_client + ":" + dokos_token,
            'Accept': 'application/json'
        }

    def insert_resource(self, resource, data):
        """
        Insert a resource

        :param resource:  The DocType name
        :param data: Data to be inserted, should be a json formatted String
        :return: True if inserted, false if not
        """
        return requests.post(self.api_url + "resource/" + resource, data=data, headers=self.headers).status_code == 200

    def get_resources(self, resource):
        """
        Get a list of resources for the required DocType

        :param resource: The DocType name
        :return: Return a JSON that contain the resources's name
        """
        r = requests.get(self.api_url + "resource/" + resource, headers=self.headers)
        return r

    def get_resource(self, resource, name):
        """
        Get a unique resource by name

        :param resource: The DocType name
        :param name: The resource's name
        :return: : Return a JSON that contain the resource
        """
        r = requests.get(self.api_url + "resource/" + resource + "/" + name, headers=self.headers)
        return r

    def get_resources_by_filter(self, resource, filters):
        """
        Get a list of filtered resources

        :param resource: The Doctype name
        :param filters: Should be an array that contains filters
        :return: Return a JSON that contain the resources's names
        """
        request = self.api_url + 'resource/' + resource + '?filters=' + str(filters)
        request = request.replace("'", '"')
        r = requests.get(request, headers=self.headers)
        return r

    def update_resource_by_name(self, resource, name, data):
        """
        Update a resource by his name

        :param resource: The Doctype name
        :param name: The resource name
        :param data: The data, should in dict format
        :return: Return the updated content in json and request the status code
        """
        data = str(data)
        data = data.replace("'", '"')
        r = requests.put(self.api_url + "resource/" + resource + "/" + name, data=data, headers=self.headers)
        return r.content, r.status_code

    def delete_resource_by_name(self, resource, name):
        """
        Delete a specified resource by name

        :param resource: The Doctype name
        :param name: The resource name
        :return: The request status codee
        """
        r = requests.delete(self.api_url + "resource/" + resource + "/" + name, headers=self.headers)
        return r.status_code
