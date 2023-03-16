import random,sys
win = 0
loss = 0
tie = 0

while True:
    bot = random.randint(1, 3)
    if bot == 1:
        bot = 'stone'
    elif bot == 2:
        bot = 'paper'
    else:
        bot = 'scissor'
    print("| WIN = %s | LOSS = %s | TIE = %s |" % (win,loss,tie))
    while True:
        print(" Aejjja khelam")
        reply = input()
        if reply == 'quit':
            sys.exit()
        elif reply == 'stone' or reply == 'paper' or reply == 'scissor':
            break
    if reply == 'stone' and bot == 'stone':
        print("Stone ")
        print("bachis saleyy")
        tie = tie + 1
    elif reply == 'stone' and bot == 'paper':
        print("paper")
        print("allu khaa")
        loss = loss + 1
    elif reply == 'stone' and bot == 'scissor':
        print("scissor")
        print("talai vaii vanera jitna deko")
        win = win + 1
    elif reply == 'paper' and bot == 'stone':
        print("stone")
        print("jhukkera vako")
        win = win + 1
    elif reply == 'paper' and bot == 'paper':
        print("paper")
        print("alli kati ley bachiss")
        tie = tie + 1
    elif reply == 'paper' and bot == 'scissor':
        print("scissor")
        print("allu training ley vaii yarrr")
        loss = loss + 1
    elif reply == 'scissor' and bot == 'stone':
        print("stone")
        print("Mero vai snga khel bey tespaxi aess")
        loss = loss + 1
    elif reply == 'scissor' and bot == 'paper':
        print("paper")
        print("cheating kheleko herna ")
        win = win + 1
    elif reply == 'scissor' and bot == 'scissor':
        print("scissor")
        print("bachisssss.....")
        tie = tie + 1
