from time import sleep
from threading import Timer
 
def sleepsort(values):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepsort.result
 
if __name__ == '__main__':
    x = [3,2,4,1,3,2,1,1]
    sortedx = sleepsort(x)
    if sortedx == sorted(x):
        print(sortedx)
        print('sleep sort worked for:',x)
    else:
        print('sleep sort FAILED for:',x)
