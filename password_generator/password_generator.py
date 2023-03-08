
import random


# password gen function =========================================
def passwordGenerator():
    name = input("Enter a word (has to have at least 5 letters): ")

    i = name[0] + name[1] + name[-1]

    n = str(random.randint(99, 1001))

    alpha = "abcdefghijklmonpqrstuvwxyz"
    alpha_list = list(alpha)
    
    a = random.choice(alpha_list)

    symbol = "!@#$%&*_-"
    symbol_list = list(symbol)
    symbol_list1 = list(symbol)

    s = random.choice(symbol_list)
    s1 = random.choice(symbol_list1)


    password = s + i + n + a + s1
    # return password 
    print(f"\nThe password is: {password} \n")

# end of function ======================================
# passwordGenerator()

