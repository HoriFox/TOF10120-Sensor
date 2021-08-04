import serial
import time

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
#start_time = time.time()
while True:
#for i in range(9):
    received_data = ser.read()              #read serial port
    time.sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    received_data = received_data.decode("utf-8").replace('mm\r\r\n', '')
    #print (received_data)                   #print received data
    dist = int(received_data)
    print('*'*round(dist/100))   
#ser.write(received_data)                #transmit data serially 
#print("--- %s seconds ---" % (time.time() - start_time))