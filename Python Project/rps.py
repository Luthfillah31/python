import random
# permainan kertas gunting batu
def play():
    #input dari pemain
    player = input("'k' untuk kertas, 'g' untuk gunting, dan 'b' untuk batu : ")
    
    #input dari komputer secara acak
    computer = random.choice(['k','g','b'])
    
    # menentukan hasilg
    
    if player == computer:
        return "seimbang"
    else:
        return who_win(player, computer)
    
# fungsi untuk menentukan hasil selain seimbang
def who_win(player, computer):
    if (player == 'k' and computer == 'g') or (player == 'g' and computer == 'b') or (player == 'b' and computer == 'k'):
        return "you win"
    else:
        return "you lose"

print(play())