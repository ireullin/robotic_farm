import serial
import time
import json
import sys
import requests
from pprint import pprint
from threading import Thread


def readLine(ser):
    cmd = ''
    while True:
        c = ser.read()
        if c == "\n":
            break
        cmd += c

    return cmd


def wait(ser, keyword):
    while True:
        line = readLine(ser).rstrip()
        #print line
        if line == keyword:
            break

        time.sleep(0.1)


def main():

    groupId = sys.argv[1]
    seq = sys.argv[2]

    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1)
    wait(ser, 'READY')
    time.sleep(1)
    ser.write('INFO\n')
    data = json.loads(readLine(ser))
    data['gotAt'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data['groupId'] = sys.argv[1]
    data['seq'] = sys.argv[2]
    print json.dumps(data)
    rsp = requests.post("http://192.168.1.221/kaoru/robotic_farm/import.json", data=data)
    #pprint(data)
    print rsp.text

    telegram_url = "https://api.telegram.org/bot349444036:AAHeHPdTxbF-HPCTVxaRD8FH-PkTVAXZtRE"
    chat_id = "@RoboticFarm"
    photo_file =  "http://ireullin.asuscomm.com/kaoru/robotic_farm/{0}_{1}.jpg".format(groupId,seq)
    rsp = requests.post(telegram_url+"/sendPhoto", data={"chat_id":chat_id, 'photo': photo_file} )
    #print rsp.text


    telgram_msg = telegram_url+"/sendMessage?chat_id="+chat_id+"&text="+json.dumps(data)
    rsp = requests.get(telgram_msg)
    #print rsp.text




if __name__ == '__main__':
    main()

