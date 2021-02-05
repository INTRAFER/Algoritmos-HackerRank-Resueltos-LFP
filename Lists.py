if __name__ == '__main__':
    N = int(input())
    arr=[]
    
    for N in range (0,N):
        x = input()
        
        simon = x.split(" ")
        
        if simon[0]=="insert":
              arr.insert(int(simon[1]),int(simon[2]))
              
        elif simon[0]=="append":
            arr.append(int(simon[1]))
            
        elif simon[0]=="remove":
            arr.remove(int(simon[1]))
            
        elif simon[0]=="pop":
            arr.pop()
            
        elif simon[0]=="reverse":
            arr.reverse()
            
        elif simon[0]=="print":
            print(arr)
            
        elif simon[0]=="sort":
            arr.sort()
            
        else:
            print ("sepalachcuca")