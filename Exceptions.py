if __name__ == '__main__':
    N = int(input())
    
    
    for N in range (0,N):
        x = input()
        
        simon = x.split(" ")
        
        try:
            owo=int (simon[0])
            uwu=int (simon[1])
            print (int(owo/uwu))
            
        except ZeroDivisionError as e:
            print ("Error Code: integer division or modulo by zero")
            
        except ValueError as e:
            print ("Error Code:",e)