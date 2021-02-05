if __name__ == '__main__':
    n = int(input())
    v = input()
    xd=v.split()
    arr=[]
    for i in range (0,n):
        arr.append(int(xd[i]))
    owo=tuple(arr)
    print(hash(owo))