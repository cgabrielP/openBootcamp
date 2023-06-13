import _thread as th
import time

def horaActual(n_thread, tiempo_espera):
    count=0
    while count<5:
        time.sleep(tiempo_espera)
        print(f'{n_thread} - {time.ctime(time.time())}')
        count+=1

th.start_new_thread(horaActual,('hilo 1',1))
th.start_new_thread(horaActual,('hilo 2', 2))

while True:
    pass
