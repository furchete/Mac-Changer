

![image](https://user-images.githubusercontent.com/98003412/200144326-df293e86-97ec-4f53-8897-90ff83b51167.png)


# Mac-Changer
Cybersecurity training

A brief summary of the MAC address:
In computer networks, the MAC address is a 48-bit identifier that corresponds uniquely to a network card or device. It is also known as a physical address, and is unique for each device.

This script makes it possible to change your mac address from the terminal has feedback to see the change without having to do ifconfig.

How to apply the command?

sudo python (namefile) + -i eth0 -m (new mac address)

Help

sudo python (namefile) --h 

  -h, --help            show this help message and exit
  
  -i INTERFACE, --interface = INTERFACE
                        Interface to change MAC Address
                        
  -m NEW_MAC, --mac = NEW_MAC
                        New MAC Address
                        

you must enter the mac in lower case 
