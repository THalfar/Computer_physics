import numpy as np
"""
Calculates first derivate 

Param:
function  -  Function that shall be derivated
x         -  Where derivate
dx        -  Difference step in derivate calculation  

Return:
Value of first derivate
"""
def first_derivate(function, x, dx):
    
    jakaja = 2*dx
    jaettava = function(x+dx) - function(x-dx)
    
    return jaettava / jakaja

"""
Calculates second derivate 

Param:
function  -  Function that shall be derivated
x         -  Where derivate
dx        -  Difference step in derivate calculation  

Return: 
Value of second derivate    
"""
def second_derivate(function, x, dx):
    
    jakaja = dx**2
    jaettava = function(x+dx) + function(x-dx) - 2*function(x)
    
    return jaettava / jakaja

"""
Calculates a numerical integral of the trapezoid integral

Param:
x       -  a uniformly spaced x-values 
function -  function thats going to be integrated

Return:
Trapezoid integral of function
"""
def trapezoid_int(x, function):
    
    # calculate point interval, assuming that x has at least 2 points    
    h = x[1] - x[0]
        
    summa = 0
    
    # Loops through points x and add to the summa the block values
    for i in range(0, len(x)-1):
        
        summa += (function(x[i]) + function(x[i+1]))*h
        
    return summa * 0.5

"""   
Calculates numerical integral using rieman sum

Param:    
x       -  a uniformly spaced x-values 
function -  function thats going to be integrated

Return:
Rieman sum integral of function
    
"""    
def riemann_sum(x, function):
    
    # calculate point interval, assuming that x has at least 2 points    
    h = x[1] - x[0]
        
    summa = 0
    
    # Loops through points x and add to the summa the block values
    for i in range(0, len(x)-1):
        
        summa += (function(x[i+1]))*h
        
    return summa

"""
Calculates numerical integral using rieman sum

Param:    
x       -  a uniformly spaced x-values 
function -  function thats going to be integrated

Return:
Rieman sum integral of function
"""    
def simpson_int(x, function):
    
    # calculate point interval, assuming that x has at least 2 points    
    h = x[1] - x[0]

    summa = 0
    
        
    # Number of intervals is one shorter than len(x)
    if (len(x)-1) % 2 == 0:   # if even intervals                  
        askelia = int( (len(x) -1) / 2 - 1 )
            
        for i in range(askelia+1):
            summa += function(x[2*i]) + 4*function(x[2*i+1]) + function(x[2*i+2])
        
        summa *= h/3
            
    else: 
        
        askelia = int( (len(x)-2) / 2 -1 ) # sum odd intervals
            
        for i in range(askelia+1):
            summa += function(x[2*i]) + 4*function(x[2*i+1]) + function(x[2*i+2])
            
        summa *= h/3
        # Add the odd tail            
        summa += h/12 * ( -1*function(x[-3]) + 8*function(x[-2]) + 5*function(x[-1]) )
                    
    return summa 

"""
Monte carlo integral

Param:
fun    -   Function that shall be integrated
xmin   -   Minimum value of x
xmax   -   Maximum value of x
blocks -   How many blocks in monte carlo integration
iters  -   Number of iterations per block

Return:
Monte carlo intergral of function
"""     
def monte_carlo_integration(fun,xmin,xmax,blocks,iters):
    # Set blocks and Lenght of each
    block_values=np.zeros((blocks,)) 
    L=xmax-xmin
    
    # Iterate through blocks and calculate function values at random points in block
    for block in range(blocks):
        for i in range(iters):
            
            x = xmin+np.random.rand()*L
            block_values[block]+=fun(x) # sum in block the values at interval random points
            
        block_values[block]/=iters 
            
    I = L*np.mean(block_values) # use mean of block value to calculate integral
    dI = L*np.std(block_values)/np.sqrt(blocks) # take std. to measure statistical error
            
    return I,dI


"""
These are example functions for testing
"""
# f(x) = x^2 + 3x
def testifun1(x): return x**2 + 3*x

# f(x) = 2x^3+xˆ2+42
def testifun2(x): return 2* x**3 + x**2 + 42

# f(x) = exp(2x) + sin(x)
def testifun3(x): return np.exp(2*x) + np.sin(x)
    
    
"""
Testing first derivate with three functions

Param:
x   -  point where derivate
dx  -  difference step in derivate

Return:
None
"""
def test_first_derivate(x, dx):
    
    # f1(x) = x^2 + 3x -> 2x + 3
   oikea =  2*x+3
   testi = first_derivate(testifun1, x, dx)
   erotus = np.abs(oikea-testi)
   print("f1'({}) dx: {} virhe abs.: {}".format(x,dx,erotus))
   
   # f2(x) = 2x^3+xˆ2+42 -> 6xˆ2 + 2x   
   oikea =  6*x**2 + 2*x
   testi = first_derivate(testifun2, x, dx)
   erotus = np.abs(oikea-testi)
   print("f2'({}) dx: {} virhe abs.: {}".format(x, dx, erotus))
   
    # f3(x) = exp(2x) + sin(x) -> 2*exp(2x) - cos(x)
   oikea = 2* np.exp(2*x) + np.cos(x)
   testi = first_derivate(testifun3, x, dx)
   erotus = np.abs(oikea-testi)
   print("f3'({}) dx: {} virhe abs.: {}".format(x, dx, erotus))

"""
Testing second derivate with three function

Param:
x   -  point where derivate
dx  -  difference step in derivate

Return:
None
"""
def test_second_derivate(x, dx):
    
    # f1(x) = x^2 + 3x -> 2
    oikea = 2
    testi = second_derivate(testifun1, x, dx)
    erotus = np.abs(oikea-testi)
    print("f1''({}) dx: {} virha abs: {}".format(x,dx,erotus))
    
    # f2(x) = 2x^3+xˆ2+42 -> 12x + 2  
    oikea = 12*x+2
    testi = second_derivate(testifun2, x, dx)
    erotus = np.abs(oikea-testi)
    print("f2''({}) dx: {} virhe abs: {}".format(x,dx,erotus))
    
    # f3(x) = exp(2x) + sin(x) -> 2*exp(2x) - sin(x)
    oikea = 4*np.exp(2*x) - np.sin(x)
    testi = second_derivate(testifun3, x, dx)
    erotus = np.abs(oikea-testi)
    print("f3''({}) dx: {} virhe abs: {}".format(x,dx,erotus))
   
"""
Testing of numerical integrals

Param:
jako   -   how many points if integral method use these
xmin   -   minimum x of test integrals
xmax   -   maximum x of test integrals
blocks -   number of blocks in monte carlo integral
iterations - number of iterations per block in monte carlo   
"""
def test_integral(jako, xmin, xmax, blocks = 10, iterations = 100):
                    
    x = np.linspace(xmin,xmax, jako)
    jako = jako -1 # montako väliä
    
    # Right anwers analytically 
    
    # f1(x) = x^2 + 3x -> 1/3 * x^3 + 3/2 * x^2
    oikeaF1 = ( 1/3 * xmax**3 + 3/2 * xmax**2 ) -  ( 1/3 * xmin**3 + 3/2 * xmin**2 ) 
    
    # f2(x) = 2x^3+xˆ2+42 -> 1/2 * x^4 + 1/3 x^3 + 42x 
    oikeaF2 = (1/2 * xmax**4 + 1/3 * xmax**3 + 42*xmax ) - ( 1/2 * xmin**4 + 1/3 * xmin**3 + 42*xmin )
    
    # f3(x) = exp(2x) + sin(x) -> 1/2 exp(2x) - cos(x)
    oikeaF3 = ( 1/2 * np.exp(2*xmax) - np.cos(xmax) ) - ( 1/2 * np.exp(2*xmin) - np.cos(xmin) )
        
    testi = riemann_sum(x, testifun1)
    erotus = np.abs(oikeaF1-testi)
    print("Rieman: F1({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
                
    testi = riemann_sum(x, testifun2)
    erotus = np.abs(oikeaF2-testi)
    print("Rieman: F2({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
    
    testi = riemann_sum(x, testifun3)
    erotus = np.abs(oikeaF3-testi)
    print("Rieman: F3({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
    
    testi = trapezoid_int(x, testifun1)
    erotus = np.abs(oikeaF1-testi)
    print("Trapezoid: F1({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
            
    testi = trapezoid_int(x, testifun2)
    erotus = np.abs(oikeaF2-testi)
    print("Trapezoid: F2({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
            
    testi = trapezoid_int(x, testifun3)
    erotus = np.abs(oikeaF3-testi)
    print("Trapezoid: F3({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax, jako , erotus))
            
    testi = simpson_int(x, testifun1)
    erotus = np.abs(oikeaF1-testi)
    print("Simpson: F1({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax,jako, erotus))
        
    testi = simpson_int(x, testifun2)
    erotus = np.abs(oikeaF2-testi)
    print("Simpson: F2({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax,jako, erotus))
               
    testi = simpson_int(x, testifun3)
    erotus = np.abs(oikeaF3-testi)
    print("Simpson: F3({} , {}) jako: {} virhe abs.: {}".format(xmin, xmax,jako, erotus))
        
    testi = monte_carlo_integration(testifun1, xmin, xmax, blocks, iterations)
    erotus = np.abs(oikeaF1- testi[0])
    print("Monte carlo: F1({} , {}) blocks: {} iter : {} virhe abs.: {}".format(xmin, xmax,blocks, iterations, erotus))
    
    testi = monte_carlo_integration(testifun2, xmin, xmax, blocks, iterations)
    erotus = np.abs(oikeaF2- testi[0])
    print("Monte carlo: F2({} , {}) blocks: {} iter : {} virhe abs.: {}".format(xmin, xmax,blocks, iterations, erotus))
    
    testi = monte_carlo_integration(testifun3, xmin, xmax, blocks, iterations)
    erotus = np.abs(oikeaF3- testi[0])
    print("Monte carlo: F3({} , {}) blocks: {} iter : {} virhe abs.: {}".format(xmin, xmax,blocks, iterations, erotus))
    
        
def main():
    
    test_first_derivate(1.42, 0.0001)
    test_second_derivate(1.42, 0.0001)
    
    test_first_derivate(-1.42, 0.001)
    test_second_derivate(-1.42, 0.001)
    
    test_integral(11, 0, 2)
    
if __name__ == "__main__":
    main()
   
   