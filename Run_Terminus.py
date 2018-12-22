from colorama import Fore, Back, Style
from colorama import init
from colorama import init
import config
import time


init(autoreset=True)
init()
import os

logo= '''

 /$$$$$$$$                                /$$                                     /$$    /$$   /$$
|__  $$__/                               |__/                                    | $$   | $$ /$$$$
   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$  /$$   /$$  /$$$$$$$      | $$   | $$|_  $$
   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$| $$  | $$ /$$_____/      |  $$ / $$/  | $$
   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$| $$  | $$|  $$$$$$        \  $$ $$/   | $$
   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$| $$  | $$ \____  $$        \  $$$/    | $$
   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$/ /$$$$$$$/         \  $/    /$$$$$$
   |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \______/ |_______/           \_/    |______/

'''
x="Loaded"



def print_menu():
    os.system("clear")
    print(Style.BRIGHT+Fore.YELLOW+logo)      ## Your menu design here
    print (40 * "-" , "Quick" , 40 * "-")
    print (Style.BRIGHT+Back.BLACK+Fore.GREEN+"1.",Fore.WHITE+"Google Chrome ")

    print (Style.BRIGHT+Back.BLACK+Fore.BLUE+"2.",Fore.WHITE+config.qApp2)
    print (Style.BRIGHT+Back.BLACK+Fore.CYAN+"3.",Fore.WHITE+config.qApp3)
    print (Style.BRIGHT+Back.BLACK+Fore.MAGENTA+"4.",Fore.WHITE+config.qApp4)
    print (Style.BRIGHT+Back.BLACK+Fore.YELLOW+"5.",Fore.WHITE+config.qApp5)
    print (Style.BRIGHT+Back.BLACK+Fore.RED+"6.",Fore.WHITE+config.qApp6)
    print (Style.BRIGHT+Back.BLACK+Fore.WHITE+"7.",Fore.WHITE+config.qApp7)
    print (40 * "-", "Menu" , 40 * "-")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"Quick Keys- Hit Enter To Select Option")


def chrome_menu():
    print (40 * "-" , "Chrome" , 40 * "-")
    print (Style.BRIGHT+Back.BLACK+Fore.GREEN+"0." "Launch Google Chrome ")
    print (Style.BRIGHT+Back.BLACK+Fore.BLUE+"1.",config.qName1)
    print (Style.BRIGHT+Back.BLACK+Fore.CYAN+"2.",config.qName2)
    print (Style.BRIGHT+Back.BLACK+Fore.MAGENTA+"3.",config.qName3)
    print (Style.BRIGHT+Back.BLACK+Fore.YELLOW+"4.",config.qName4)
    print (40 * "-", "Links" , 40 * "-")

def terminalmenu():
    print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"Enter Terminal Command:")
    osterminal=input()
    os.system(osterminal)
    print (Style.BRIGHT+Back.BLACK+Fore.YELLOW+"1.Enter Terminal Command, 2. Go Back To To Menu")
    osterminal=input()
    if osterminal=="1":
        terminalmenu()
    if osterminal=="2":
        start()





def start():
    print(Style.BRIGHT+Back.BLACK+Fore.RED+x)
    print_menu()
    option=input()



    if option=='1':
        chrome_menu()
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"Quick Keys- Select URL")
        cmenu=input()
        if cmenu=='1':
            os.system (config.url1)
            start()
        elif cmenu=="2":
            os.system("open",config.url2)
            start()
        elif cmenu=='3':
            os.system("open",config.url3)
            start()
        elif cmenu=="4":
            os.sytem("open",config.url4)
            start()
        elif cmenu=="0":
            os.system("open -a '/Applications/Google Chrome.app' ")
            start()






    elif option=='2':
        os.system(config.appId2)
        start()



    elif option=='3':
        os.system(config.appId3)
        start()
    elif option=='4':
        os.system(config.appId4)
        start()
    elif option=='5':
        os.system(config.appId5)
        start()
    elif option=='6':
        os.system(config.appId6)
        start()
    elif option=='7':
        os.system(config.appId7)
        start()

    elif option==".fquit":
        quit()
    elif option==".about":
        print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"Made by iZevo")
        print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"www.projectzevo.com")
        time.sleep(6)
        start()
    elif option==".sourcecode":
        os.system("open https://github.com/iozevo/iozevo.github.io")
    elif option==".oscommand":
        terminalmenu()
    elif option==".list":
        os.system("ls")
        time.sleep(10)
        start()
    elif option==".terminus":
        print(logo)
        print("pre alpha buld version 2")
        print ("Type (Open-Source)")
        print ("Script Ended")
    elif option==".systeminfo":
        os.system("system_profiler")
        time.sleep(10)
        start()
    elif option==".reportbug":
        os.system("open -a https://github.com/iozevo/iozevo.github.io/issues")







    else:
        start()


print ("Loading")
start()
