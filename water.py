import Adafruit_DHT
import RPi.GPIO as GPIO
import datetime
import time

sensor = Adafruit_DHT.DHT11
pin_sensor = 25

init = False

GPIO.setmode(GPIO.BOARD)

def get_status(pin = pin_sensor):
    umid, temp = Adafruit_DHT.read_retry(sensor, pin);
    umid = '{0:0.1f}' .format(umid)
    temp = '{0:0.1f}' .format(temp)
    temp_umid = 'Temperatura: ' + temp + ' Umidade: ' + umid
    return temp_umid

def get_ultima_irrigacao():
    try:
        f = open("ultimas_irrigacoes.txt", "r")
        return f.readline()
    except:
        return "Ainda não foi feita nenhuma irrigação"
      

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pin_irrigador = 7, sensor_umidade = pin_sensor):
    consecutive_water_count = 0
    init_output(pin_irrigador)
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            umid, temp = Adafruit_DHT.read_retry(sensor, sensor_umidade);
            wet = umid
            print("umid: " + str(umid))
            if umid < 50:
                print(1)
                if consecutive_water_count < 5:
                    irrigador_on(pin_irrigador, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

def irrigador_on(pin_irrigador = 7, delay = 1):
    init_output(pin_irrigador)
    horario = datetime.datetime.now()
    dia = horario.strftime("%d")
    mes = horario.strftime("%m")
    ano = horario.strftime("%Y")
    hora = horario.strftime("%H")
    minuto = horario.strftime("%M")
    
    f = open("ultimas_irrigacoes.txt", "w")
    f.write("Ultima irrigação: " + dia + "-" + mes + "-" + ano + "  " + hora + ":" + minuto)
    f.close()
    GPIO.output(pin_irrigador, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(pin_irrigador, GPIO.LOW)
