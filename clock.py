import tm1637
import time

def updateTime(display):
    t = []
    for c in time.strftime("%H%M"):
        t.append(int(c))
    display.set_values(t)


disp = tm1637.TM1637(23, 24)

disp.set_brightness(0)

dot = False

try:
    while True:
        disp.set_doublepoint(dot)
        updateTime(disp)
        time.sleep(0.5)
        dot = not dot
except KeyboardInterrupt:
    pass

disp.cleanup()
