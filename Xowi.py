#!/usr/bin/python3
#pip3 install python-nmap
#pip3 install colorama
#pip3 install os
import colorama
import nmap
import webbrowser
import os
from colorama import Fore
from colorama import Style

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #clear the console
url = 'https://github.com/UhhGorzz'
sc = nmap.PortScanner() #scan public port 
colorama.init() #initialise colorama

#MAIN

def main():
	clearConsole()
	print(Fore.RED + "____  ___            .__ ")
	print(Fore.RED+ "\   \/  /______  _  _|__|")
	print(Fore.RED + " \     //  _ \ \/ \/ /  |")
	print(Fore.RED + " /     (  <_> )     /|  |")
	print(Fore.RED + "/___/\  \____/ \/\_/ |__|")
	print(Fore.RED + "      \_/                ")
	print(Fore.RED + "                  By Xowi\n" + Style.RESET_ALL)

	n = input(Fore.YELLOW + "1 - Network Scanner\n2 - Vulnerabilities Check\n3 - Exploit\n4 - Github\n\n>" + Style.RESET_ALL)



	if n == '1':
		clearConsole()
		nmap()

	if n == '2':
		clearConsole()
		vuln()

	if n == '3':
		clearConsole()
		print("[*] Launching...")
		os.system('msfconsole')

	if n == '4':
		webbrowser.open_new_tab(url)
		clearConsole()
		return main()



#Number 1

def nmap():
	print(Fore.MAGENTA + " ███▄    █   ██████ ")
	print(Fore.MAGENTA + " ██ ▀█   █ ▒██    ▒ ")
	print(Fore.MAGENTA + "▓██  ▀█ ██▒░ ▓██▄   ")
	print(Fore.MAGENTA + "▓██▒  ▐▌██▒  ▒   ██▒")
	print(Fore.MAGENTA + "▒██░   ▓██░▒██████▒▒")
	print(Fore.MAGENTA + "░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░")
	print(Fore.MAGENTA + "░ ░░   ░ ▒░░ ░▒  ░ ░")
	print(Fore.MAGENTA + "   ░   ░ ░ ░  ░  ░  ")
	print(Fore.MAGENTA + "         ░       ░  ")
	print(Fore.MAGENTA + "                    " + Style.RESET_ALL)
	ip = input(Fore.YELLOW + "IP adress : " + Style.RESET_ALL)
	sc.scan(ip , '1-1024')
	print(sc.scaninfo())
	print(sc[ip]['tcp'].keys())
	input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
	return main()



#Number 2

def vuln():
	print(Fore.CYAN + " ___      ___ ________      ")
	print(Fore.CYAN + "|\  \    /  /|\   ____\     ")
	print(Fore.CYAN + "\ \  \  /  / | \  \___|_    ")
	print(Fore.CYAN + " \ \  \/  / / \ \_____  \   ")
	print(Fore.CYAN + "  \ \    / /   \|____|\  \  ")
	print(Fore.CYAN + "   \ \__/ /      ____\_\  \ ")
	print(Fore.CYAN + "    \|__|/      |\_________\ ")
	print(Fore.CYAN + "                 \|_________|")
	print(Fore.CYAN + "                            " + Style.RESET_ALL)
	ip = input(Fore.YELLOW + "IP adress : " + Style.RESET_ALL)
	print(os.system('nmap -sV --script=vulscan/vulscan.nse ' +ip))
	input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
	return main()




if __name__ == "__main__":
	main()