
def rocket_launcher():
    n = int(input ("Enter the starting number: "))
    while (n>=0):
        if (n== 0):
            print("Blast off! 🚀 !!", end= "")
        else :
            print(n," ", end= "")
        
        n-=1

def pahada():
    mul = int(input ("Enter the number: "))
    
    for i in range(1, 11):
        print(f" {mul} x {i} = {mul*i}")
    
def fact ():
    fact_num = int(input ("Enter the number: "))
    factorial =1
    for i in range (fact_num,0, -1):
        factorial *=i
        
        i-=1
    print(f"factorial : {factorial}")

def main ():
    rocket_launcher()
    pahada()
    fact ()
    
    

if __name__ == "__main__":
    main()
        


