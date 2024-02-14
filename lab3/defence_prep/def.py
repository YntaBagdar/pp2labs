def get_min(a, b, c):
   if (a <= b) and (a <= c):
      return a
   elif (b<=a) and (b<=c):
      return b
   else:
      return c
    
print("the min is:", get_min(99, 100, 6))