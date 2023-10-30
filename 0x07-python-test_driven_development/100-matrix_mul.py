#!/usr/bin/python3
"""
This module contains the function matrix_mul which multiplies two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Returns a matrix that is the result of multiplying m_a by m_b.
    
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    
    Returns:
        A new matrix that is the result of the multiplication.
    
    Raises:
        TypeError: For various conditions related to the type and format of the input matrices.
        ValueError: If matrices cannot be multiplied or are empty.
    """
    
    # Validate matrix format and contents
    for matrix, name in [(m_a, "m_a"), (m_b, "m_b")]:
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))
        if not matrix or not matrix[0]:
            raise ValueError("{} can't be empty".format(name))
        row_len = len(matrix[0])
        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError("{} should contain only integers or floats".format(name))
        if not all(len(row) == row_len for row in matrix):
            raise TypeError("each row of {} must be of the same size".format(name))
    
    # Check if multiplication is possible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Matrix multiplication
    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
