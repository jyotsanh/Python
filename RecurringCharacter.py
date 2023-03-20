str='DBCAA'

def recurring(str):
    i=0
    count=0
    while True:
        for j in range(len(str)):
            if i==j:
                j+=1
            elif str[i]==str[j]:
                count+=1
        if count>0:
            index = i
            break
        i+=1

    return str[index]
def main():
    print(recurring(str))


main()
