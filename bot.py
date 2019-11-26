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

    def update_scores(self, dump_qvalues = True):

        history = list(reversed(self.moves))
        high_death_flag = True if int(history[0][2].split("_")[1]) > 120 else False

        t = 1
        for exp in history:
            state = exp[0]
            act = exp[1]
            res_state = exp[2]
            if t == 1 or t == 2:
                cur_reward = self.r[1]
            elif high_death_flag and act:
                cur_reward = self.r[1]
                high_death_flag = False
            else:
                cur_reward = self.r[0]
