#!/usr/bin/env python3

import datetime
import time

print("Welcome to Yuki's Poland time calculator.\n")
print("Press CTRL+C to exit.\n")

try:
  while True:
    dt_now_pl= datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    print(dt_now_pl)
    time.sleep(1)
except KeyboardInterrupt:
  print("\nThank you for using this tool!")
