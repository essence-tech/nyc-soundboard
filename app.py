# sample.py
import falcon
import json
from wsgiref import simple_server


class Player(object):

    def play_sound(self, path):
        return 'Not implemented'


class Drumroll(Player):
    self.path = '/sound_files/drumroll.wav'

    def on_post(self, req, resp):
        res = self.play_sound(self.path)
        resp.body = json.dumps(res)

api = falcon.API()
api.add_route('/drumroll', Drumroll())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
