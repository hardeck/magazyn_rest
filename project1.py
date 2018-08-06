import RPi.GPIO as GPIO   # import pakietu ustawiającego porty GPIO jako wyjścia/wejścia
import serial
import os
import time
class Shelf(object):
    status='waiting'
    ser=serial.Serial('/dev/ttyACM0',115200) #inicjalizacja portu com
    def __init__(self,number):
        self.led_number=number
        self.sensor=Sensor(self.led_number)  
    def turn_on(self):
        Shelf.status='running'
        self.ser.write(('r%d'% self.led_number).encode('utf-8'))
        os.system("mpg321 %s.mp3" % self.led_number)
        while not GPIO.input(self.sensor.number):
            pass
        self.ser.write(('w%d'% self.led_number).encode('utf-8'))
        self.send_response()
        Shelf.status='waiting'
    @staticmethod
    def test():
        Shelf.status='running'
        os.system('mpg321 hi.mp3')
        for i in range(1,25):
            time.sleep(0.1)
            Shelf.ser.write(('r%d'% i).encode('utf-8'))
            os.system('mpg321 {}.mp3'.format(i))
            time.sleep(0.1)
            Shelf.ser.write(('w%d'% i).encode('utf-8'))
        os.system('mpg321 bye.mp3')
        Shelf.status='waiting'
    def send_response(self):
        pass
    def __repr__(self):
        return 'Numer półki: {}, numer portu GPIO czujnika: {}\n'.format(self.led_number, self.sensor.number)
    def __str__(self):
        return ('Numer półki to: %d, numer portu GPIO czujnika : %d\n' 
                % (self.led_number, self.sensor.number))
class Sensor(object):
    porty_gpio={1 : 20, 2 : 16, 3 : 12, 4 : 24, 5 : 23}
    def __init__(self, number):
        self.number=self.porty_gpio.get(number)
        self.prepare_sensor()
    def prepare_sensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.number, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        
'''shelf=[]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)
for i in range(5):
    k=Shelf(i+1)
    print(k.host)
    shelf.append(k)
print(shelf)
Shelf.sock.bind(('172.26.40.131',Shelf.port))                   
Shelf.sock.listen(1)                           #ustawienie nasłuchiwania
conn,addr = Shelf.sock.accept()
while True:
    data = conn.recv(1024)
    if not data: break
    try:
        shelf[int(data)-1].turn_on()
        conn.send(b'ok')
    except IndexError:
        continue
        
    #shelf[int(input('Którą półkę chcesz zaświecić?' ))-1].turn_on()'''
    
