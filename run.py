import json
import time 
import os
import threading
from libs import color
from libs.__ghs__ import Facebook

def __logo__(logo):
    os.system("clear")
    print("\n")
    os.system(f'figlet -f small " {logo}"')
    print("\n")
    

if not os.path.exists('config/cookies.json'):
    email_id = input(color.BOLD+color.YELLOW+color.BOLD+"\n[+] Enter Email/ID/Phone : "+color.LIGHT_CYAN)
    u_pass = input(color.BOLD+color.YELLOW+color.BOLD+"\n[+] Enter Facebook Password : "+color.LIGHT_CYAN)
    fb = Facebook(email_id,u_pass)


fb = Facebook("","")
print(color.BOLD+color.YELLOW+color.BOLD+"\n  [1] Default Friend Request"+color.LIGHT_CYAN)
print(color.BOLD+color.YELLOW+color.BOLD+"\n  [2] Request From Group/Friend List"+color.LIGHT_CYAN)
print(color.BOLD+color.YELLOW+color.BOLD+"\n  [3] Cancel All Friend Request"+color.LIGHT_CYAN)
print(color.BOLD+color.YELLOW+color.BOLD+"\n  [4] Unfriend All Friends"+color.LIGHT_CYAN)

cmd = int(input(color.BOLD+color.GREEN+color.BOLD+"\n  [+] Select An Option : "+color.LIGHT_CYAN))
os.system("clear")
if cmd == 1:
    os.system("clear")
    __logo__("Requesting")
    while True:
        fb.friend_request()
elif cmd ==2:
    request = input(color.BOLD+color.CYAN+color.BOLD+"\n  [+] Enter Friend List URL : "+color.LIGHT_CYAN)
    os.system("clear")
    __logo__("Requesting")
    while True:
        fb.friend_request(request)
elif cmd ==3:
    os.system("clear")
    __logo__("Canceling")
    while True:
        fb.__Cancel_Request__()
elif cmd ==3:
    os.system("clear")
    __logo__("Canceling")
    while True:
        fb.unfriend()
else:
    os.system("clear")
    print(color.BOLD+color.RED+color.BOLD+"\n  [!] Please Select 1 Or Two "+color.LIGHT_CYAN)
    



