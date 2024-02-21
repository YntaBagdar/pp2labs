
#Write a Python program to subtract five days from current date.

import datetime
x = datetime.datetime.now().date()
y = datetime.timedelta(5)

print(x-y)



#Write a Python program to print yesterday, today, tomorrow.
import datetime
x = datetime.datetime.now().date()
y = datetime.timedelta(1)

print("Today is: ", x)
print("Yesterday was: ", x-y)
print("Tomorrow will be: ", x+y)




#Write a Python program to drop microseconds from datetime.
import datetime
x = datetime.datetime.now()
print("Microseconds from datetime: ", x.strftime("%f"))


#Write a Python program to calculate two date difference in seconds.
"""import datetime
x = datetime.datetime.now()
y = datetime.timedelta(1)
z = x-y
print(z.strftime("%f"))"""

from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

import datetime
x = datetime.datetime.now()
y = datetime.timedelta(1)
z = x-y
print(z.strftime("%f"))






