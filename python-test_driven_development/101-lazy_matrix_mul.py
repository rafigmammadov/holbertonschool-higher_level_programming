#!/usr/bin/python3
"""
    Module to multiply two matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix with numpy
    """
    return np.dot(m_a, m_b)
