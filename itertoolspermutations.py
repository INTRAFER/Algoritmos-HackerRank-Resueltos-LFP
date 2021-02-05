from itertools import permutations
if __name__ == '__main__':
    N = input()
    simon=N.split(" ")
    owo=list(permutations(simon[0],int(simon[1])))
    for i in sorted(owo):
        print ("".join(i))