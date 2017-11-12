import requests

class Axis:
    """ Describes an Axis camera object
    initialize it with the default arguments
    after resetting the camera """
    def __init__(self, ip='192.168.0.90', username='root', password='root'):
        self.ip = ip
        self.username = username
        self.password = password
        self.base_url = 'http://{}:{}@{}/axis-cgi/'.format(username, password, ip)

    def get_VAPIX_version(self):
        """Returns the version of Axis VAPIX API supported by the camera"""
        try:
            r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.API.HTTP.Version')
            if r.status_code == 200:
                r = str(r.content.decode('utf-8'))
                print(r)
            else:
                print(r.status_code)

        except:
            print('Error')
            pass


    def restart(self):
        """ Restarts the Axis camera """
        try:
            r = requests.get(self.base_url + '/admin/restart.cgi')
            print('Restaring ' + self.ip)
            print('Return status: ' + str(r.status_code))
            if r.status_code == 200:
                print('Axis camera has been restarted succesfully')
                return r.status_code
            else:
                return r.status_code
        except:
            pass
