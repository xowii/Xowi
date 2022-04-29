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
url = 'https://github.com/xowii'
sc = nmap.PortScanner() #scan public port 
colorama.init() #initialise colorama

#MAIN

def main():
	clearConsole()
	print(Fore.RED + "____  ___            .__ ")
	print("\   \/  /______  _  _|__|")
	print(" \     //  _ \ \/ \/ /  |")
	print(" /     (  <_> )     /|  |")
	print("/___/\  \____/ \/\_/ |__|")
	print("      \_/                ")
	print(Fore.CYAN + "                  By xowii\n" + Style.RESET_ALL)

	n = input(Fore.YELLOW + "1 - Web Attack\n0 - Github\n\n>" + Style.RESET_ALL)


	if n == '0':
		webbrowser.open_new_tab(url)
		clearConsole()
		return main()


	if n == '1':
		clearConsole()
		wa()

	else:
		input(Fore.RED + "[!] Only number between 0 and 1" + Style.RESET_ALL)
		return main()


def wa():
	clearConsole()
	print(Fore.GREEN + " __          __     ")
	print(" \ \        / /\    ")
	print("  \ \  /\  / /  \   ")
	print("   \ \/  \/ / /\ \  ")
	print("    \  /\  / ____ \ ")
	print("     \/  \/_/    \_\ \n" + Style.RESET_ALL)

	print(Fore.CYAN + "┌════════════════════════════════┐")
	print("█         Web Attack Menu        █")
	print("└════════════════════════════════┘" + Style.RESET_ALL)

	n = input(Fore.YELLOW + "\n1 - Network Scanner\n2 - Vulnerabilities Check\n3 - Exploit\n4 - DDOS (use on lowend website)\n\n0 - Return to main menu\n\n>" + Style.RESET_ALL)


	if n == '0':
		clearConsole()
		return main()

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
		input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
		return main()

	if n == '4':
		clearConsole()
		ddos()

	if n == '5':
		webbrowser.open_new_tab(url)
		clearConsole()
		return main()

	else:
		input(Fore.RED + "[!] Only number between 0 and 4" + Style.RESET_ALL)
		return wa()



#Number 1

def nmap():
	print(Fore.MAGENTA + " ███▄    █   ██████ ")
	print(" ██ ▀█   █ ▒██    ▒ ")
	print("▓██  ▀█ ██▒░ ▓██▄   ")
	print("▓██▒  ▐▌██▒  ▒   ██▒")
	print("▒██░   ▓██░▒██████▒▒")
	print("░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░")
	print("░ ░░   ░ ▒░░ ░▒  ░ ░")
	print("   ░   ░ ░ ░  ░  ░  ")
	print("         ░       ░  ")
	print("                    \n" + Style.RESET_ALL)

	print(Fore.CYAN + "┌════════════════════════════════┐")
	print("█         Network Scanner        █")
	print("└════════════════════════════════┘" + Style.RESET_ALL)

	ip = input(Fore.YELLOW + "\nIP adress : " + Style.RESET_ALL)
	sc.scan(ip , '1-1024')
	print(sc.scaninfo())
	print(sc[ip]['tcp'].keys())
	input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
	return main()



#Number 2

def vuln():
	print(Fore.CYAN + " ___      ___ ________      ")
	print("|\  \    /  /|\   ____\     ")
	print("\ \  \  /  / | \  \___|_    ")
	print(" \ \  \/  / / \ \_____  \   ")
	print("  \ \    / /   \|____|\  \  ")
	print("   \ \__/ /      ____\_\  \ ")
	print("    \|__|/      |\_________\ ")
	print("                 \|_________|")
	print("                            \n" + Style.RESET_ALL)

	print(Fore.CYAN + "┌════════════════════════════════┐")
	print("█          Vuln Scanner          █")
	print("└════════════════════════════════┘" + Style.RESET_ALL)

	ip = input(Fore.YELLOW + "\nWebsite URL: " + Style.RESET_ALL)
	print(os.system('sqlmap -u ' +ip))
	input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
	return main()




	#Number 4

def ddos():
	print(Fore.RED + "      :::::::::  :::::::::   ::::::::   :::::::: ")
	print("     :+:    :+: :+:    :+: :+:    :+: :+:    :+: ")
	print("    +:+    +:+ +:+    +:+ +:+    +:+ +:+         ")
	print("   +#+    +:+ +#+    +:+ +#+    +:+ +#++:++#++   ")
	print("  +#+    +#+ +#+    +#+ +#+    +#+        +#+    ")
	print(" #+#    #+# #+#    #+# #+#    #+# #+#    #+#     ")
	print("#########  #########   ########   ########       \n" + Style.RESET_ALL)

	print(Fore.CYAN + "┌════════════════════════════════┐")
	print("█            Web DDOSer          █")
	print("└════════════════════════════════┘" + Style.RESET_ALL)

	site = input(Fore.YELLOW + "\nWebsite URL: " + Style.RESET_ALL)
	print(os.system('python3 goldeneye.py ' +site))
	input(Fore.GREEN + "\nPress ENTER to show the main menu." + Style.RESET_ALL)
	return main()




if __name__ == "__main__":
	main()
