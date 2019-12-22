#Episode-04 (Train heist)

def train_heist(x):
   
    a = 10
    for i in range(len(x)):
        print(a)
        temp = x[i]
        if a != 0:
            if temp == 'r':
                a = a-1
                if a == 0:
                    return "Press the button"
            elif temp == 'l':
                a = a+1
                if a == 0:
                    return "Press the button"
            else :
                return "Sorry, I am not programmed to understand the variable", x[i]
      
    return "Sorry, the container that contains the power node never came under the crane"
    


#Testbench

x = input("Enter the string:(Enter l for '<-', r for '->')")    #Enter l for '<-', r for '->'
print(train_heist(x))
