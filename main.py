import time
from GamePlay import *
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

counter = GamePlay()
counter.run()
