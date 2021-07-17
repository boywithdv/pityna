import random

class Responder(object):
# スーパークラス
    def __init__(self,name):
        self.name = name
    def response(self,input):
        return ''



class RepeatResponder(Responder):
# サブクラス
    def response(self,input):
        return "{}って何だい?".format(input)


class RandomResponder(Responder):
# サブクラス
    def __init__(self,name):
        super().__init__(name)
        self.responses = ["いい天気だね","君はパリピ？","10円拾った"]
    def response(self,input):
        return (random.choice(self.responses))