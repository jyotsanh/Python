import random
ranNumber=random.randint(1,50)
print("oee mailey number sochey k holaa?")
print("katii xoti ko guess ma milauna sakxas??")
n=int(input())
print("guess gaar tah!!!")
for rime in range(n):
    k = int(input())
    if k>ranNumber:
        print("number  dheraii vayo")
    elif k<ranNumber:
        print("number  kaam vayo")
    else:
        break
if k == ranNumber:
    print("saii ho ka bata thapaes thaikaiii " + str(int(rime)+1) + " guess thapeas tah??")
    reply=input()
else:
    print("thukka tero zindagi tetro " + str(int(rime)+1) +  " guess ma pani sakinas hana ")
    print("mailey " + str(ranNumber) + " socheko theyy")
if reply=='tero dai ho':
    print("Cool bro timi tah")
else:
    print("Sai hoo")
