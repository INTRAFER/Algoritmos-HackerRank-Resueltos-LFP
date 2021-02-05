import textwrap

def wrap(string, max_width):
    
    aka=textwrap.fill(string, max_width)
    
    return aka

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)