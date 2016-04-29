# sample.py
import falcon
import json
import subprocess
from wsgiref import simple_server


class Player(object):

    def on_get(self, req, resp):
        resp.body = json.dumps({
            'file': self.path
        })

    def on_post(self, req, resp):
        res = self.play_sound(self.path)
        resp.body = json.dumps(res)

    def play_sound(self, path):
        subprocess.Popen(['mplayer', path])
        return 'Not implemented'


class Drumroll(Player):
    path = './sound_files/drumroll.wav'


api = falcon.API()
api.add_route('/drumroll', Drumroll())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
