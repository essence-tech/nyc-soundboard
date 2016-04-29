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
        self.play_sound(self.path)
        resp.body = json.dumps(res)

    def play_sound(self, path):
        return subprocess.Popen(['mplayer', path]).pid


class Applause(Player):
    path = './sound_files/applause.wav'


class Drumroll(Player):
    path = './sound_files/drumroll.wav'


class Hercules(Player):
    path = './sound_files/hercules.mp3'


class HowYouDoin(Player):
    path = './sound_files/howyoudoin.mp3'


class Jerry(Player):
    path = './sound_files/Jerry-hello.mp3'


class Kramer(Player):
    path = './sound_files/Kramer-crazy.mp3'


class PhatBeat(Player):
    path = './sound_files/phat_beat.wav'


class SadTrombone(Player):
    path = './sound_files/sad_trombone.wav'


class ThatWasEasy(Player):
    path = './sound_files/that_was_easy.wav'


api = falcon.API()
api.add_route('/applause', Applause())
api.add_route('/drumroll', Drumroll())
api.add_route('/hercules', Hercules())
api.add_route('/howyoudoin', HowYouDoin())
api.add_route('/jerry', Jerry())
api.add_route('/kramer', Kramer())
api.add_route('/phatbeat', PhatBeat())
api.add_route('/sadtrombone', SadTrombone())
api.add_route('/thatwaseasy', ThatWasEasy())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
