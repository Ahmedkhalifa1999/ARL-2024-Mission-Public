#!/usr/bin/env python3
import matplotlib.pyplot as plt  
from typing import List
      
def numOfYears(a:int , b:int) ->int:
    """
    Implement your Logic here

    Input:
    a (int): first number
    b (int): second number

    Output:
    n (int): number of years for a to become larger than b
    """
    pass

def visualizer(A_List:List[int], B_List:List[int], n:int) ->None:
    """
    Implement your matplot lib visualizer here
    
    Inputs:
    -------
    A (List[int]): All Height values of bar A
    B (List[int]): All Height values of bar B
    n (int): Number of years
    """
    pass


def main() ->None:

    input_string = input("Please Enter The 2 Numbers: ")

    a, b = map(int, input_string.split())
    print("Number of years: " , numOfYears(a,b))
    plt.show()

if __name__ == "__main__":
    main()
