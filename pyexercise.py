import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate ((((sy.sin(sy.sqrt(x))))*(sy.cos(sy.sqrt(x)))), (x,0,(sy.pi**2)/4))
    return ans

def my_solution():
    A = np.array( [[1,3,5,9,10,15,16,14,12,4], [10,9,8,7,6,5,4,3,2,1],[1,8,6,2,3,20,5,4,8,5],[6,4,60,70,40,80,70,9,11,10],[1,2,3,7,8,9,4,5,6,1],[2,15,13,11,74,50,65,66,60,40],[2,3,2,1,2,6,2,8,2,7],[8,5,6,5,4,3,2,1,5,2],[5,6,4,3,2,1,1,2,3,4],[2,3,4,5,6,6,6,7,8,10]] )
    b = np.array([5,6,7,8,10,12,15,17,9,8])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1202348
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())