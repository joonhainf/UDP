# UDPPingerClient.py
from socket import *
import time
#AF_INET and SOCK_DGRAM setup
client_sock = socket(AF_INET, SOCK_DGRAM)
# 1 second timeout as the instructions say
client_sock.settimeout(1)
#MY IP IS HERE
server_addr = ('192.168.1.77', 12000)

# Send 10 pings
for i in range(1,11):
    # t1 in RTT, start time
    start = time.time()
    # State the time
    message = 'Ping number' + str(i) + " " + time.ctime(start)    
    # Send msg to server
    client_sock.sendto(message.encode(), server_addr)
    
    try:
        # Get response and server address
        response, server_addr = client_sock.recvfrom(1024)
        # Time 2 receive, t2 in RTT
        end = time.time()
        # RTT formula t2 -t1 = RTT
        rtt = end - start
        # Print the response/ RTT at 4 decimal points
        print(f'Server Response at {i}: {response.decode()}')
        print('RTT of ping ' + str(i) + ' ' + str(rtt))
    except timeout:
        # print "Request timed out" if timeout
        print("Request timed out at ping " + str(i))

#Close
client_sock.close()
