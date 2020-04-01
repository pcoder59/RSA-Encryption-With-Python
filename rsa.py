import random

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def euclid(n, c):
    while c != 0:
        n, c = c, n%c
    return n

def gene(cop):
    number = random.randrange(1, cop)
    euc = euclid(number, cop)
    while euc != 1:
        number = random.randrange(1, cop)
        euc = euclid(number, cop)
    return number

def generateKeys(k1, k2):
    num = k1 * k2
    coprime = (k1-1) * (k2-1)
    e = gene(coprime)
    d = multiplicative_inverse(e, coprime)
    return ((e, num),(d, num))

def isprime(key):
    if key == 2:
        return True
    if key % 2 == 0:
        return False
    for i in range(3, int(key/2)):
        if key % i == 0:
            return False
    return True

def enterKeys():
    public_key_1 = int(input("Enter a Prime Number: "))
    if(not isprime(public_key_1)):
        print("Entered Number is Not Prime")
        return 0, 0
    public_key_2 = int(input("Enter Another Prime Number(Not the Previous): "))
    if(not isprime(public_key_2)):
        print("Entered Number is Not Prime")
        return 0, 0
    return public_key_1, public_key_2

def equals(check1, check2):
    if check1 == check2:
        return True
    else:
        return False

if __name__ == "__main__":
    print("RSA Public and Private Keys Generator By PRR! :)")
    matching = False
    while(matching == False):
        key1, key2 = enterKeys()
        if equals(key1, key2):
            print("You Entered Same Numbers!!!")
        else:
            matching = True
    print("Generating Your Public and Private Keys...")
    public, private = generateKeys(key1, key2)
    print("You Public Key is: ", public, " and your private key is ", private)