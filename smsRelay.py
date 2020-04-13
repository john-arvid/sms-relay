#tes

import serial

try:
  ser = serial.Serial( # set parameters, in fact use your own :-)
    port="COM4",
    baudrate=9600
  )
  ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
  print ("port is opened!")

except IOError: # if port is already opened, close it and open it again and print message
  ser.close()
  ser.open()
  print ("port was already open, was closed and opened again!")


