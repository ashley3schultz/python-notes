import random
ai = ['r', 'p', 's']
s1 = 0
s2 = 0

while (s1 < 3) and (s2 < 3):
    print('Please enter: r, p or s')
    p1 = input("player 1, make your move:").lower()
    print("---------------------------")
    p2 = ai[random.randint(0,2)]
    if p1 == p2:
        print(f"it's a draw, you both tired with {p1}")
        print("---------------------------")
        print(s1)
        print(s2)
    elif (p1 == "r" and p2 == "s") or (p1 == "p" and p2 == "r") or (p1 == "s" and p2 == "p"):
        print(f"player 1 wins {p1} over {p2}")
        s1+=1
        print("---------------------------")
        print(s1)
        print(s2)
    else:
        print(f"player 2 wins {p2} over {p1}")
        s2+=1
        print("---------------------------")
        print(s1)
        print(s2)
        
if s1 > s2:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")
