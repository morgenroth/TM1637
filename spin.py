import tm1637
import time

disp = tm1637.TM1637(23, 24)

disp.set_brightness(0)
disp.set_doublepoint(False)
spin = 0

try:
    for i in range(0, 4):
        for j in range(0, 10):
            for s in ['S7', 'S3', 'S4', 'S5']:
                values = [' ', ' ', ' ', ' ']
                for k in range(0, i):
                    values[k] = 'o'
                values[i] = s
                disp.set_values(values)
                time.sleep(0.1)
    disp.set_values(['o', 'o', 'o', 'o'])
except KeyboardInterrupt:
    pass

disp.cleanup()
