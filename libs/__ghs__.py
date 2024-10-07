import mechanize
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import re
from libs import color
from libs import file 
import time
from libs import agent 
import json 
import os
import urllib.parse
from threading import Thread, Lock

class Facebook:
    """ Create A Object Of This Class And Send Two Parameters.
    As Arguments First One Is User Name/Email/Phone/ID Number
    And Second One Is Password. """
    def __init__(self, username, password):
        self.browser = mechanize.Browser()
        self.cj = mechanize.CookieJar()
        self.print_lock = Lock()
        self.browser.set_cookiejar(self.cj)
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_gzip(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        self.browser.addheaders = [('User-agent',agent.ghs_agent)]
        if os.path.exists('config/cookies.json'):
            self.set_cookie("datr",self.get_cookies("datr"))
            self.set_cookie("sb",self.get_cookies("sb"))
            self.set_cookie("noscript",self.get_cookies("noscript"))
            self.set_cookie("c_user",self.get_cookies("c_user"))
            self.set_cookie("xs",self.get_cookies("xs"))
            self.set_cookie("fr",self.get_cookies("fr"))
            self.set_cookie("m_page_voice",self.get_cookies("m_page_voice"))
        self.username = username
        self.password = password
        if self.check_login():
            self.welcom()
        else:
            self.sign_in()
    def sign_in(self):
        self.browser.open('https://m.facebook.com/login.php')
        self.browser.select_form(nr=0)
        self.browser.form['email'] = self.username
        self.browser.form['pass'] = self.password
        self.browser.submit()
        time.sleep(0.5)
        response_data = self.browser.response()
        res_data = response_data.read()
        res = res_data.decode()
        file.save_data(str(res))
        if "Enter login code to continue" in res:
            print("\n Waiting For Approve...")
            time.sleep(5)
            self.checkpoint()
        else:
            self.save_cookie()
    def welcom(self):
        self.browser.open('https://free.facebook.com/profile')
        time.sleep(0.5)
        response_data = self.browser.response()
        res_data = response_data.read()
        res = res_data.decode()
        soup = BeautifulSoup(res, 'html.parser')
        name = soup.find("title")
        os.system("clear")
        print("\n")
        os.system('figlet -f small "  Facebook "')
        print("\n")
        print(color.YELLOW+color.BOLD+"  [+] Account Owner : "+color.BOLD+color.LIGHT_CYAN+name.get_text())
        print("\n"+color.YELLOW+color.BOLD+"  [+] Login Status : "+color.BOLD+color.GREEN+"Successful")
        print("\n"+color.YELLOW+color.BOLD+"  [+] Profile ID : "+color.BOLD+color.RED+self.get_cookies("c_user"))
        
    def save_cookie(self):
        cookies = self.cj
        cookie_info = {}
        for cookie in cookies:
            cookie_info[cookie.name] = cookie.value
        f = open("config/cookies.json", "w")
        f.write(json.dumps(cookie_info))
        f.close()
    def checkpoint(self):
        self.sign_in()
    def check_login(self):
        if 'c_user' in [cookie.name for cookie in self.browser.cookiejar]:
            return True
        else:
            return False
    def set_cookie(self,c_name,c_value):
        c = cookielib.Cookie(version=0, name=c_name, value=c_value, port=None, port_specified=False, domain='.facebook.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)
        self.cj.set_cookie(c)
    def get_cookies(self,name):
        f = open("config/cookies.json", "r")
        f_data = f.read()
        json_data = json.loads(f_data)
        return json_data[name]
    def friend_request(self,url="https://free.facebook.com/friends/"):
        self.browser.open(url)
        user = ""
        count = 0
        all_links = self.browser.links()
        for link in all_links:
            if link.attrs[0][1] =="ck": #or link.attrs[0][1] == "ca" or link.attrs[0][1] == "cn":
                user = link.text
            if link.text == "Add friend":
                self.browser.follow_link(link)
                count+=1
                print(" ["+color.RED+str(count)+"]"+color.BOLD+color.YELLOW+" Sending Friend Request To --> "+color.BOLD+color.LIGHT_WHITE+user,end="\r")
        #response = self.browser.response()
        #res_data = response.read()
        #res = res_data.decode()
        #file.save_data(res)
        print("\n\n [+]"+color.BOLD+color.LIGHT_CYAN+f" Total {count} Request Was Sent \n")
        
    def unfriend(self,url="https://free.facebook.com/friends/center/friends/"):
        frinend_link = "https://free.facebook.com/removefriend.php?friend_id=100095319515876&removed"
        self.browser.open(url)
        user = ""
        count = 0
        all_links = self.browser.links()
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        file.save_data(res)
        print("\n\n [+]"+color.BOLD+color.LIGHT_CYAN+f" Total {count} Unfriended Successfully \n")
        
    def __Cancel_Request__(self):
        url = "https://free.facebook.com/friends/center/requests/outgoing/"
        self.browser.open(url)
        users = ""
        count = 0
        for link in self.browser.links():
           if link.attrs[0][1] == "be bg ca cb bf" or link.attrs[0][1] == "bw":
               users = link.text
           if link.text == "Cancel request":
               self.browser.follow_link(link)
               count+=1
               print(" ["+color.RED+str(count)+"]"+color.BOLD+color.YELLOW+"  Canceling Request --> "+color.BOLD+color.LIGHT_WHITE+users,end="\r")
        print("\n\n [+]"+color.BOLD+color.LIGHT_CYAN+f" Total {count} Request Was Cancelled\n")
    def write_post(self):
        url ="https://free.facebook.com/"
        self.browser.open(url)
        self.browser.select_form(nr=1)
        self.browser["xc_message"] = "Something..."
        self.browser.submit()
        time.sleep(2)
        self.browser.select_form(nr=0)
        self.browser.form['update_default_privacy']=["on"]
        self.browser.submit()
        self.browser.select_form(nr=0)
        self.browser["xc_message"] = "Something..."
        self.browser.submit()
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        #file.save_data(res)
        soup = BeautifulSoup(res, 'html.parser')
    def make_friends(self,url="https://free.facebook.com/friends/center/mbasic/"):
        self.browser.open(url)
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        #file.save_data(res)
        users = ""
        count = 0
        for link in self.browser.links():
            if link.attrs[0][1] == "ck" or link.attrs[0][1] == "ca" or link.attrs[0][1] == "cn":
                users = link.text
            if link.text == "Add Friend":
                with open("config/friend_list.txt", 'r') as frnd_title:
                    names = [line.strip() for line in frnd_title]
                    for title in names:
                        if title in users.strip():
                            self.browser.follow_link(link)
                            print(color.BOLD+color.YELLOW+"  Sending Friend Request ===>> "+color.BOLD+color.LIGHT_WHITE+users+"\n")
                            response = self.browser.response()
                            res_data = response.read()
                            res = res_data.decode()
                            count+=1
                            #file.save_data(res)
        #print(color.BOLD+color.LIGHT_CYAN+f" \n  Total {count} Request Was Sent \n")
    def go_to(self,url):
        if self.check_login:
            print("Opening...")
            self.browser.open(url)
            
            form = self.browser.forms()[1]
            
            
            form.submit()
            response_data = self.browser.response()
            res_data = response_data.read()
            res = res_data.decode()
            file.save_data(res)
            print("Closed...!")




