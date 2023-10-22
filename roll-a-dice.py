import random

response = input("press y to roll  ")

def roll(response):
     num = random.randint(1,6)
     if (response == "y" and num == 1):
         print("[     ]")
         print("[  0  ]")
         print("[     ]")
         print("press y to roll again and n to exit ")
     elif (response == "y" and num == 2):
           print("[ 0    ]")
           print("[      ]")
           print("[    0 ]")
           print("press y to roll again and n to exit ")
     elif (response == "y" and num == 3):
           print("[     ]")
           print("[0 0 0]")
           print("[     ]")
           print("press y to roll again and n to exit ")
     elif (response == "y" and num == 4):
           print("[ 0  0 ]")
           print("[      ]")
           print("[ 0  0 ]")
           print("press y to roll again and n to exit ")
     elif (response == "y" and num == 5):
           print("[0   0]")
           print("[  0  ]")
           print("[0   0]")
           print("press y to roll again and n to exit ")
     elif (response == "y" and num == 6):
           print("[0 0 0]")
           print("[     ]")
           print("[0 0 0]")
           print("press y to roll again and n to exit ")
     elif (response == "n"):
           exit()
    
roll(response)