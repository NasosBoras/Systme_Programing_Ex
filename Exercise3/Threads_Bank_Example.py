import threading
import time
bacc_A, bacc_B = 100_000, 100_000

def transfer5():
  global bacc_A, bacc_B
  #time.sleep(0.1)
  lock.acquire()
  AtoB(5)
  lock.release()


def transfer15():
  global bacc_A, bacc_B
  #time.sleep(0.2)
  lock.acquire()
  BtoA(15)
  lock.release()


    
def transfer20():
  global bacc_A, bacc_B
  #time.sleep(0.15)
  lock.acquire()
  AtoB(20)
  lock.release()



def transfer40():
  global bacc_A, bacc_B
  #time.sleep(0.05)
  lock.acquire()
  BtoA(40)
  lock.release()

def runExperiment():
  global bacc_A, bacc_B
  bacc_A, bacc_B = 100_000, 100_000

  for i in range(10):
      threading.Thread(target = transfer5()).start()
      threading.Thread(target = transfer20()).start()
      if (i % 2) != 0: 
          threading.Thread(target = transfer15()).start()
          threading.Thread(target = transfer40()).start()

  
def AtoB(x):
    global bacc_A, bacc_B
    bacc_A-=x
    bacc_B+=x

def BtoA(x):
    global bacc_A, bacc_B
    bacc_A+=x
    bacc_B-=x
      
      
lock = threading.Lock() 
for i in range(5): 
  runExperiment()  
  print(bacc_A, bacc_B)
