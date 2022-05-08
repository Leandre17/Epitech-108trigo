from math import sqrt, factorial
from src.matrice_operand import (
    get_matrice_identite,
    divide_matrix,
    multiplication_matrix,
    adding_matrix,
    mul_matrix,
    get_matrice,
)


def all_dif(m_a: list[list[float]], m_b: list[list[float]]) -> float:
    diff: float = 0.0

    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            diff += pow(m_a[i][j] - m_b[i][j], 2)
    return sqrt(abs(diff))


def print_matrice(m_a: list[list[float]]) -> int:
    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            print(f"{m_a[i][j]:.2f}", end="")
            if j != len(m_a[i]) - 1:
                print("\t", end="")
        print()
    return 0


def exponantiel(argv: list[str]) -> list[list[float]]:
    precision: float = 0.00001
    matrice: list[list[float]] = get_matrice(argv)
    index: int = 2
    continu: bool = True
    matrice_pow: list[list[float]] = matrice
    result: list[list[float]] = adding_matrix(matrice, get_matrice_identite(matrice))
    old_matrice: list[list[float]] = matrice
    facto: int = 0

    while continu:
        facto = factorial(index)
        matrice_pow = multiplication_matrix(matrice_pow, matrice)
        result = adding_matrix(result, divide_matrix(matrice_pow, facto))
        if all_dif(result, old_matrice) < precision:
            continu = False
        old_matrice = result
        index += 1
    return result
