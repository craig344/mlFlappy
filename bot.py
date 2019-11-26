import json


class Bot(object):
    def __init__(self):
        self.gameCNT = 0 
        self.DUMPING_N = 25 
        self.discount = 1.0
        self.r = {0: 1, 1: -1000}
        self.lr = 0 #0.7
        self.load_qvalues()
        self.last_state = "420_240_0"
        self.last_action = 0
        self.moves = []

    def load_qvalues(self):

        self.qvalues = {}
        try:
            fil = open("qvalues.json", "r")
        except IOError:
            return
        self.qvalues = json.load(fil)
        fil.close()

    def act(self, xdif, ydif, vel):

        state = self.map_state(xdif, ydif, vel)
        self.moves.append(
            (self.last_state, self.last_action, state)
        )
        self.last_state = state

        if self.qvalues[state][0] >= self.qvalues[state][1]:
            self.last_action = 0
            return 0
        else:
            self.last_action = 1
            return 1
