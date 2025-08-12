
password = input("Enter your password: ")

def check_password(password):
    
    print("length:", len(password))
    print("lowercase:", password.islower())
    print("uppercase:", password.isupper())
    
    for char in password:

        if char.isdigit():
            print("contains digit: True")      
            break 
        else:
            continue
    else:
            print("contains digit: False")       
    
            


print(check_password(password))