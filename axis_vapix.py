import requests
import io
from PIL import Image


class Axis:
    """ Describes an Axis camera object
    initialize it with the default arguments
    after resetting the camera """
    def __init__(self, ip='192.168.0.90', username='root', password='root'):
        self.ip = ip
        self.username = username
        self.password = password
        self.base_url = 'http://{}:{}@{}/axis-cgi/'.format(username, password, ip)

    def user_or_password_error(self):
        print('[-] Username or password error')

    def error_with_status_code(self):
        print('[-] Error: ' + str(r.status_code))

    def get_VAPIX_version(self):
        """ displays the version of Axis VAPIX API supported by the camera """
        try:
            print('[*] Requestion VAPIX version...')
            r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.API.HTTP.Version')
            if r.status_code == 200:
                r = str(r.content.decode('utf-8'))
                vapix_version = r.split("=")[1]
                print('[+] VAPIX version: ' + vapix_version)

            elif r.status_code == 401:
                self.user_or_password_error()

            else:
                self.error_with_status_code()

        except:
            print('[-] Error: getting VAPIX verision')
            pass


    def restart(self):
        """ Restarts the Axis camera """
        try:
            r = requests.get(self.base_url + '/admin/restart.cgi')
            print('[*] Restaring ' + self.ip)
            if r.status_code == 200:
                print('[+] Axis camera has been restarted successfully')
            elif r.status_code == 401:
                self.user_or_password_error()
            else:
                self.error_with_status_code()
        except:
            self.error_with_status_code()
            pass

    def display_live_image(self):
        """ Gets the latest image from the camera and displays it using PIL package """
        r = requests.get(self.base_url + 'jpg/image.cgi')
        if r.status_code == 200:
            f = io.BytesIO(r.content)
            img = Image.open(f)
            img.show()

    def set_overlay_text(self, text='test'):
        requests.get(self.base_url + 'param.cgi?action=update%20&Image.I0.Text.TextEnabled=yes&Image.I0.Text.String=' + text)
