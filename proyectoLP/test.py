import serial, time, json

hw_sensor = serial.Serial(port='COM3', baudrate=9600, timeout=1, write_timeout=1)
raw_string_j = json.loads('{"x":"0","y":"0"}')
while True:
        raw_string_b = hw_sensor.readline()
        raw_string_s = raw_string_b.decode('utf-8')
        if(len(raw_string_s)>0):
                raw_string_j = json.loads(raw_string_s)
                print(raw_string_j["x"])