#!/usr/bin/python3
import signal, sys, time
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
     ______| |       |       |_____      |_____| |______ |  \_| by H4RRIZN"""
    print(font)

# Main

if __name__ == '__main__':
    while True:
        banner()
        eval = input("\n¿ Incluir eval() ? (y/n)\n")
        if eval == "y":
            payload = input("\nIngresa tu payload: \n")
            unicode_conv = [ord(char) for char in payload]
            unicode_string = ",".join([str(code) for code in unicode_conv])
            eval_string = f"eval(String.fromCharCode({unicode_string}));"
            print("\nCharcode Generado:\n")
            print(eval_string)
            break
        if eval == "n":
            payload = input("\nIngresa tu payload: \n")
            unicode_conv = [ord(char) for char in payload]
            unicode_string = ",".join([str(code) for code in unicode_conv])
            eval_string = f"String.fromCharCode({unicode_string});"
            print("\nCharcode Generado:\n")
            print(eval_string)
        else:
            print("[!] Opcion invalida [!]")
            time.sleep(2)
            system('clear')

