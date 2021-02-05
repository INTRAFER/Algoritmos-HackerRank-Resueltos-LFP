from itertools import combinations
if __name__ == '__main__':
    N = input()
    simon=N.split(" ")
    arreglito=[]
    ari=[]
    for i in range (0,len(simon[0])):
        arreglito.append(simon[0][i])
    arreglito.sort() 
    for i in sorted(arreglito):
        print ("".join(i))
    for n in range (2,int(simon[1])+1):
        ari=(list(combinations(arreglito,n)))
        for u in sorted(ari):
            print ("".join(u))