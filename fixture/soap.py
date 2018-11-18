from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_list_project(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            list_projects = client.service.mc_projects_get_user_accessible(username, password)
            l = map(self.list_convert, list_projects)
            return list(l)
        except WebFault:
            return False

    def list_convert(self, list):
        l = Project(id=list.id, name=list.name)
        return l