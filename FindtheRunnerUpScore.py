if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    owo=set(arr)
    
    uwu=list(owo)
    
    uwu.sort()
    
    print(uwu[len(owo)-2])