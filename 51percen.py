"""
The basic idea behind this stocks trading algorithm is that if enough people start using this indicator the market begins to move according to this indicator, and thus completing a self-fulfilling cycle
"""

import datetime

li = ["BUY","SELL"]
weekend = [6,7]

todayDay = datetime.datetime.today().weekday()

if todayDay not in weekend:
    if todayDay %2 == 0:
        print("BUY")
    else:
        print("SELL")
else:
    raise ValueError ("Cannot calculate signal for weekends")
