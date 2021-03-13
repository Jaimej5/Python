a=5
b=2

def suma(n1, n2):
    c=n1+n2
    return "La suma es "+str(c)

def resta(n1, n2):
    c=n1-n2
    return "La resta es "+str(c)

def mul(n1, n2):
    c=n1*n2
    return "La multiplicación es "+str(c)

def div(n1, n2):
    c=n1/n2
    return "La división es "+str(c)

#main innecesario
if __name__=="__main__":
    print(suma(a,b))
    print(resta(a,b))
    print(mul(a,b))
    print(div(a,b))
