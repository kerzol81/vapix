import requests

class Axis:

    def __init__(self, ID, ip, username, password):
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
