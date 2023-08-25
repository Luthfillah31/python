import random

cap = int(input("capacity : "))

def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f"Tebak nomor dari 1 - {x}: "))
        count += 1
        if guess > random_number:
            print("nomor kelebihan")
        elif guess < random_number:
            print("nomor kurang")
        else:
            print("jackpot")
            print("anda menebak sebanyak " + str(count) + " kali") 
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low,high)
        feedback = input(f"apakah {guess} kelebihan (>), kekurangan(<), atau benar (c) : ").lower()
        if feedback == ">":
            high = guess - 1
        elif feedback == "<":
            low = guess + 1
            
    print(f"computer berhasil menebak angka anda {guess}")
    
user_guess(cap)
            
        
            