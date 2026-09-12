import subprocess, threading



def abrir_notepad():
    print("Thread 1: Abrindo Bloco de Notas ")
    subprocess.Popen("notepad.exe")

def abrir_calculadora():
    print("Thread 2: Abrindo Calculadora ")
    subprocess.Popen("calc.exe")

def abrir_paint():
    print("Thread 3: Abrindo Paint ")
    subprocess.Popen("mspaint.exe")

                       #Criação de Threads
t1 = threading.Thread(target=abrir_calculadora)
t2 = threading.Thread(target=abrir_paint)
t3 = threading.Thread(target=abrir_notepad)

                       #Iniciar Threads
t1.start()
t2.start()
t3.start()

                       #Aguardando Todas Terminarem
t1.join()
t2.join()
t3>join()


print("PID:", processo.pid)
