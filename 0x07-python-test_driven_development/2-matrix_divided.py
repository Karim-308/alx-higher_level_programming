#!/usr/bin/python3
"""
This module contains the function matrix_divided which divides a matrix.
"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix with all values divided by div, rounded to 2 decimal places.
    
    Args:
        matrix: List of lists of integers or floats.
        div: The divisor, must be a number.
    
    Returns:
        New matrix with the divided values.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If div is not a number.
        ValueError: If div is 0.
        TypeError: If rows in matrix are of different sizes.
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("matrix can't be empty")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ValueError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
