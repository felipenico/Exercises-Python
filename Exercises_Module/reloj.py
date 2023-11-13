import pytz
import datetime
import time
import os

while True:#ctrl +  c para interrumpir la secuencia
    ha = datetime.datetime.now(pytz.timezone("America/Bogota"))
    print(ha.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system("cls")