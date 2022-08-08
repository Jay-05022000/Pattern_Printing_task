'''pattern printing
you have to ask user a number for printing pattern.
you havee to ask user second number for selecting type of pattern.
2 types are available : normal,inverted'''

def normal(n):
    for i in range(n):
        print((i+1)*'*')

def inverted(n):
    i=n
    while(i>0):
        print(i*'*')
        i=i-1
        continue
try:
    row=int(input("how many rows you want in your pattern: "))
    choice=bool(int(input("select number a 0 or 1 for choice of pattern: ")))    # 0 for normal,1 for inverted
    if(choice==True):
        normal(row)
    else:
        inverted(row)
except:
    print("An error occured \nplease enter integer")


