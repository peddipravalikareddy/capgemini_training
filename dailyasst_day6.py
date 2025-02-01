class Email:
    # def __init__(self):
    #     self.email=" "
    def send(self):
        print(f'Email sent to receiver')
class SMS:
    def send(self):
        print(f'SMS sent to receiver')
class Push():
    def send(self):
        print(f'Pushed message to receiver')
def callSend(obj):
    if hasattr(obj,"send"):
        obj.send()
    else:
        print("send() method not found")

e=Email()
callSend(e)
s=SMS()
callSend(s)
p=Push()
callSend(p)            
