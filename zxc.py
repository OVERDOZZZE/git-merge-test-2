import time


while True:
    for i in range(40):
        print(' '*i, 'test')
        time.sleep(0.1)
    for i in range(40,0,-1):
        print(' '*i, 'test')
        time.sleep(0.1)

print('image added')