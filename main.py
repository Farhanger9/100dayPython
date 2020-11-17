import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rad = random.randint(0,1)

if rad == "1":
  print("this is Head")
else:
   print("This is Tail") 