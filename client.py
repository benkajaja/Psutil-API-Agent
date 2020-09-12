import requests
import time
import configparser
from requests.exceptions import ConnectionError

col = ['IP', 'CPU(%)', 'MEM(%)', 'RECV(MB)', 'SENT(MB)', 'ΔRECV(Mbps)', 'ΔSENT(Mbps)']
SAMPLETIME = 0.5

def show():
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    target = conf['target']['server'].split(',')

    packetCount = {}
    for i in target:
        packetCount.setdefault(i, [0,0])

    print('%-15s %7s %7s %15s %15s %15s %15s' % (col[0] ,col[1] ,col[2], col[3], col[4], col[5], col[6]))
    while True:
        for i in target:
            res = requests.get("http://%s:5000" % i).json()

            bytesR = int(res['Network']['bytes_recv'])
            bytesS = int(res['Network']['bytes_sent'])

            dRECV = (bytesR - packetCount[i][0])*8/(SAMPLETIME*1000000)
            dSENT = (bytesS - packetCount[i][1])*8/(SAMPLETIME*1000000)

            packetCount[i][0] = bytesR
            packetCount[i][1] = bytesS

            print('%-15s %7s %7s %15.2f %15.2f %15.2f %15.2f' % \
                  (i, \
                   res['CPU'], \
                   res['Memory'], \
                   bytesR/1000000, \
                   bytesS/1000000, \
                   dRECV, \
                   dSENT), \
                  flush = True)

        for _ in target:
            print('\033[A', end = "")

        time.sleep(SAMPLETIME)

try:
    show()
except KeyboardInterrupt:
    print('\033[B\033[B')
except ConnectionError:
    print('\033[B\033[B')
    print('ConnectionError')
