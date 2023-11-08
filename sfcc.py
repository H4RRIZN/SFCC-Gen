

# Exit
def ctrl_c(sig, frame):
    system('clear')
    print(style.RED + "\n [!] Saliendo [!]")
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)