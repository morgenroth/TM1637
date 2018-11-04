import tm1637
import time

disp = tm1637.TM1637(23, 24)

disp.set_brightness(0)
disp.set_doublepoint(False)
spin = 0

try:
    while True:
        for s in ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']:
            disp.set_values([' ', s, s, ' '])
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

disp.cleanup()
