#Episode-01 (Opening lock)

def open_lock(key, combs = 100, color = 'red'):

    i = 1
    while True:
        i = i+1
        if i == key:
            color = 'green'
        if (color != 'red'):
            print("Door opened at : " + str(i))
            break
        if (i > 100):
            print("Operation failed")
            break

open_lock(int(input("Set the key : ")))
