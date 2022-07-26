# The task is to press "Play" and "Next" buttons automatically to play the whole chapter of Vasilenko's video course

# https://webfanat.com/article_id/?id=147
# https://tonais.ru/library/biblioteka-pyautogui-v-python

import time
import pyautogui as pag
import random


def mysleep():
    time.sleep(30 + random.uniform(0, 0.4))


def printtime(msg):
    print(msg, time.ctime(time.time()))


def removepointer():
    pag.moveTo(1 + random.uniform(1, 20), 1 + random.uniform(100, 200))

def digits4(num):
    d4 = ''
    n = num
    for i in range(4):
        d4 = str(n%10) + d4
        n = n // 10
    return d4

def findandclick(picname):
    mysleep()
    screen = pag.screenshot('screenshot.png')
    pos = pag.locateOnScreen(picname + '.png')
    if pos is None:
        print(picname + '.png not found!')
        exit(1)
    else:
        pag.moveTo(pos[0], pos[1])
        pag.click()
        removepointer()


printtime('Starting at')
times = [time.time()]
screenshotnumber = 0
time.sleep(3)

for i in range(3000):
    mysleep()
    screen = pag.screenshot('screenshot.png')
    pos = pag.locateOnScreen('arrow1.png')
    if pos is None:
        pos = pag.locateOnScreen('arrow2.png')
    if pos is not None:
        pag.moveTo(pos[0], pos[1])
        pag.click()
        removepointer()
        pos = None
        while pos is None:
            mysleep()
            screen = pag.screenshot('screenshot.png')
            pos = pag.locateOnScreen('finish.png')
        pag.moveTo(813, 1000)
        pag.click()
        while pos is not None:
            mysleep()
            screenshotnumber += 1
            screen = pag.screenshot(f'screenshot{digits4(screenshotnumber)}.png')
            im = pag.screenshot(region=(979, 1016, 1, 1))
            pag.moveTo(989, 1026)
            if list(im.getdata())[0][0] < 100:
                pag.click()
            else:
                pos = None
        findandclick('cross')
    pos = None
    while pos is None:
        pag.scroll(-1000)
        mysleep()
        screen = pag.screenshot('screenshot.png')
        pos = pag.locateOnScreen('next.png')
    pag.moveTo(pos[0], pos[1])
    pag.click()
    removepointer()
    times.append(time.time())

print(times)
