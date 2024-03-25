# UDPPingerClient.py
from socket import *
import time

#AF_INET and SOCK_DGRAM setup
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 1 second timeout as the instructions say
clientSocket.settimeout(1)

#MY IP IS HERE
serverAddress = ('192.168.1.77', 12000)

#Sequence num here
seq = 1


# Send 10 pings
for i in range(10):
    # When was the message sent
    start = time.time()
    
    # State the time
    message = 'Ping number' + str(seq) + " " + time.ctime(start)
    
    # Send msg to server
    clientSocket.sendto(message.encode(), serverAddress)
    
    try:
        # Receive the response from the server
        response, serverAddress = clientSocket.recvfrom(1024)
        
        # Time 2 receive
        end = time.time()
        
        # RTT formula t2 -t1 = RTT
        rtt = end - start
        
        # Print the response/ RTT
        print(f'Response from server: {response.decode()}, RTT: {rtt:.4f} seconds')
    except timeout:
        # print "Request timed out" if timeout
        print("Request timed out")
    
    # Record sequence
    seq += 1



#Close
clientSocket.close()
