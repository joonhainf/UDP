# UDPPingerClient.py
from socket import *
import time

# Set up socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout to 1 second
clientSocket.settimeout(1)

# Server address and port
serverAddress = ('192.168.1.77', 12000)

# Number of pings to send
numPings = 10

# Initialize sequence number
sequenceNumber = 1

# Initialize variables for RTT statistics
totalRTT = 0
minRTT = float('inf')
maxRTT = float('-inf')
lostPackets = 0

# Send pings
for i in range(numPings):
    # Record the time the message is sent
    sendTime = time.time()
    
    # Format the message
    message = f'Ping {sequenceNumber} {sendTime}'
    
    # Send the message to the server
    clientSocket.sendto(message.encode(), serverAddress)
    
    try:
        # Receive the response from the server
        response, serverAddress = clientSocket.recvfrom(1024)
        
        # Record the time the response is received
        receiveTime = time.time()
        
        # Calculate RTT
        rtt = receiveTime - sendTime
        
        # Update RTT statistics
        totalRTT += rtt
        if rtt < minRTT:
            minRTT = rtt
        if rtt > maxRTT:
            maxRTT = rtt
        
        # Print response and RTT
        print(f'Response from server: {response.decode()}, RTT: {rtt:.6f} seconds')
    except timeout:
        # If timeout occurs, print "Request timed out"
        print("Request timed out")
        lostPackets += 1
    
    # Increment sequence number
    sequenceNumber += 1

# Print RTT statistics
print(f'\nMinimum RTT: {minRTT:.6f} seconds')
print(f'Maximum RTT: {maxRTT:.6f} seconds')
print(f'Average RTT: {totalRTT / (numPings - lostPackets):.6f} seconds')
print(f'Packet loss rate: {(lostPackets / numPings) * 100:.2f}%')

# Close the socket
clientSocket.close()
