
def area_T():
    b = float(input("Enter the value of base : "))
    h = float(input("Enter the value of height : "))
    return b*h/2;

def area_R():
    l = float(input("Enter the value of length : "))
    w = float(input("Enter the value of width : "))
    return l * w;

def star():
    q= int(input("Enter your input integer"));
    for x in range(q+1):
        for z in range(x):
            print("*", end=" ")
        print(" ")
    return 
