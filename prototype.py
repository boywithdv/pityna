import pityna

'''実行ブロック'''

def prompt(obj):
    '''pitynaプロンプトを作る関数'''
    return obj.get_name() + ":" + obj.get_responder_name() + " > "

#ここからプログラム開始
print("Pityna System prototype : pityna")
pityna = pityna.Pityna("Pityna")

while True:
    inputs = input(" > ")
    if not inputs:
        print("bye!")
        break
    else:
        response = pityna.dialogue(inputs)
        print(prompt(pityna), response)