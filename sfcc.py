#!/usr/bin/python3
import signal, sys
from os import system

# Exit
def ctrl_c(sig, frame):
    system('clear')
    print("\n [!] Saliendo [!]")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

# Banner
def banner():
    font = """
     _______ _______ _______ _______      ______ _______ __   _
     |______ |______ |______ |       ___ |  ____ |______ | \  |
     ______| |       |       |_____      |_____| |______ |  \_| """
    print(font)

# Main

if __name__ == '__main__':
    banner()
    while True:
        eval = input("\n¿ Incluir eval() ? (y/n)\n")
        if eval == "y":
            payload = input("\nIngresa tu payload: \n")
            results = []
            for char in payload:
                unicode_value = ord(char)
                results.append(unicode_value)
            results.sort()
            formatted_results = ",".join(str(value) for value in results)
            print("\neval(String.fromCharCode("+formatted_results+"))")
            break
        if eval == "n":
            payload = input("\nIngresa tu payload: \n")
            results = []
            for char in payload:
                unicode_value = ord(char)
                results.append(unicode_value)
            results.sort()
            formatted_results = ",".join(str(value) for value in results)
            print("\nString.fromCharCode("+formatted_results+"))")
            break
