from os import system
from time import sleep
from requests import post
from threading import Thread
from Terminalia import Color
from random import choices, choice

class checker:
    def __init__(self):
        self.t = 240
        self.min = 0
        self.name = []
        self.fails = 0
        self.checker = 0
        self.threadd = 10
        self.available = 0

    def count(self, t):
        while t:
            mins, secs = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            sleep(1)
            t -= 1

    def main(self):
        system("cls")

        while True:
            self.username = open('usernames.txt').read().splitlines()
            for user in self.username:
                system('title ^| Made By Sophi#9106.')
                if user not in self.name:
                    self.name.append(user)
                    headers = {
                        'Accept': '*/*',
                        'Sec-Fetch-Mode': 'cors',
                        'sec-ch-ua-mobile': '?0',
                        'Sec-Fetch-Dest': 'empty',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Site': 'cross-site',
                        'sec-ch-ua-platform': '"Windows"',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Origin': 'https://id.sonyentertainmentnetwork.com',
                        'Referer': 'https://id.sonyentertainmentnetwork.com/',
                        'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
                        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                    }
                    json_data = {
                        'onlineId': f'{user}',
                        'reserveIfAvailable': True,
                    }
                    try:
                        response = post('https://accounts.api.playstation.com/api/v1/accounts/onlineIds', headers=headers, json=json_data)
                        if response.status_code == 201:
                            print(f"{Color.BRIGHT_CYAN}[+] {Color.CYAN}Available {user}")
                            with open('Available.txt', 'a+') as f:
                                f.write(user + '\n')
                            self.available += 1

                        #if self.letters in self.username:
                        #    print(f"Found Name With one of these: {self.letters}")
                        #input("Press Space To Exit...")
                        #exit()
                        elif response.status_code == 400:
                            print(f"{Color.BRIGHT_CYAN}[-] {Color.RED}Taken {user}")
                            self.fails += 1
                        else:
                            print(f"{Color.BRIGHT_CYAN}[!] {Color.PURPLE}Error {user}")
                            self.count(self.t)
                            if self.t == 0:
                                self.main()
                    except Exception as e:
                        print(e)
                else:
                    print("Exiting")
                    sleep(10)
                    exit()
checker().main()
