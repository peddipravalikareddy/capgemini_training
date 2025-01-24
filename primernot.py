import math

def search_prime(n):

    if(n==2):

        return True

    if(n%2==0):

        return False

    i=3

    while(i<=math.sqrt(n)):

        if(n%i==0):

            return False

        i+=2

    return True

def main():

    n=int(input("Enter a number: "))

    val=search_prime(n)

    print(val)



main()
