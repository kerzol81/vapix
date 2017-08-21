import requests

class Axis:

    def __init__(self, id='default', ip='192.168.0.90', username='root', password='root'):
        self.id = ID
        self.ip = ip
        self.username = username
        self.password = password

    def restart(self):
        # API: http://<servername>/axis-cgi/admin/restart.cgi
        try:
            requests.get("http://" + self.username + ":" + self.password + "@" + self.ip + "/axis-cgi/admin/restart.cgi")
        except:
            pass
