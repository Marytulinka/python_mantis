from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def mc_projects(self, username, password):
        client: Client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_projects_get_user_accessible(username, password)
