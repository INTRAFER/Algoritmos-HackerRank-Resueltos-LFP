if __name__ == '__main__':
    n = int(input())
    estudiantes = {}
    for i in range(0,n):
        nombre=input()
        div=nombre.split(" ")
        estudiantes[div[0]]=[float(div[1]),float(div[2]),float(div[3])]
    Npromedio=input()
    pro=(estudiantes[Npromedio][0]+estudiantes[Npromedio][1]+estudiantes[Npromedio][2])/3
    print ("{0:.2f}".format(pro))
        