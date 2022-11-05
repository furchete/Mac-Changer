import subprocess
import optparse
import re

print("")
print(" __       __                             _____     _                                 ")
print("/  \     /  |                           /      \ /  |          ")
print("$$  \   /$$ |  ______    _______       /$$$$$$  |$$ |____    ______   _______    ______    ______    ______  ")
print("$$$  \ /$$$ | /      \  /       |      $$ |  $$/ $$      \  /      \ /       \  /      \  /      \  /      \ ")
print("$$$$  /$$$$ | $$$$$$  |/$$$$$$$/       $$ |      $$$$$$$  | $$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  | ")
print("$$ $$ $$/$$ | /    $$ |$$ |            $$ |   __ $$ |  $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/  ")
print("$$ |$$$/ $$ |/$$$$$$$ |$$ \_____       $$ \__/  |$$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |$$$$$$$$/ $$ |       ")
print("$$ | $/  $$ |$$    $$ |$$       |      $$    $$/ $$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$       |$$ |       ")
print("$$/      $$/  $$$$$$$/  $$$$$$$/        $$$$$$/  $$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$ | $$$$$$$/ $$/       ")
print("                                                                               /  \__$$ |                     ")
print("                                                                               $$    $$/                      ")
print("                                                                                $$$$$$/                       ")



print(" |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(" |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(" ||| [Info] This script makes it possible to change your mac address |||||||||||||||||||||||||||")
print(" ||| Written in Python  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(" ||| Not created by me rights reserved to Solo Python. created for cybersecurity practice. |||||")
print(" |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(" |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
 
 
 #HELP
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="Interface to change MAC Address")
    parser.add_option("-m", "--mac", dest = "new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Specify an interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] Specify a MAC address, use --help for more information")
    return options
#script
def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

ron = re.compile(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w")
def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode()
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else: 
            print("[-] Cannot read MAC address")
    except Exception as e:
        print(e)

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC successfully switched to " + current_mac)
else:
    print("[-] MAC address was not changed")
