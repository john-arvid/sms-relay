from usim800 import sim800

phonenumber = 12345678
times = 3

gsm = sim800(baudrate=9600,path="/dev/ttyUSB0")

for x in range(1,times+1):
    gsm.sms.send("+47{0}".format(phonenumber),"Sms spam test, {0} av 1000".format(x))

gsm.sms.send("+47{0}".format(phonenumber),"Tulla bare, ble bare {0} sms sendt :p".format(times))



