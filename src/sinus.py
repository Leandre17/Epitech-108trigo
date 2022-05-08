from src.matrice_operand import (
    divide_matrix,
    multiplication_matrix,
    adding_matrix,
    mul_matrix,
    get_matrice,
)
from src.exponatial import all_dif
from math import factorial, sinh


def sinuss(argv: list[str]) -> list[list[float]]:
    precision: float = 0.001
    matrice: list[list[float]] = get_matrice(argv)
    index: int = 2
    continu: bool = True
    facto: int = factorial(3)
    matrice_pow: list[list[float]] = multiplication_matrix(matrice, matrice)
    matrice_pow = multiplication_matrix(matrice_pow, matrice)
    result: list[list[float]] = adding_matrix(
        matrice, mul_matrix(divide_matrix(matrice_pow, facto), -1)
    )
    temp: list[list[float]] = []
    old_matrice: list[list[float]] = matrice

    while continu:
        facto = factorial(index * 2 + 1)
        matrice_pow = multiplication_matrix(matrice_pow, matrice)
        matrice_pow = multiplication_matrix(matrice_pow, matrice)
        temp = mul_matrix(divide_matrix(matrice_pow, facto), pow(-1, index))
        result = adding_matrix(result, temp)
        if all_dif(result, old_matrice) < precision:
            continu = False
        old_matrice = result
        index += 1
    return result


def sinush(argv: list[str]) -> list[list[float]]:
    index: int = 2
    continu: bool = True
    precision: float = 0.000001
    facto: int = factorial(3)
    matrice: list[list[float]] = get_matrice(argv)
    matrice_pow: list[list[float]] = multiplication_matrix(matrice, matrice)
    matrice_pow = multiplication_matrix(matrice_pow, matrice)

    result: list[list[float]] = adding_matrix(
        matrice, divide_matrix(matrice_pow, facto)
    )
    temp: list[list[float]] = []
    old_matrice: list[list[float]] = matrice

    while continu:
        facto = factorial(index * 2 + 1)
        matrice_pow = multiplication_matrix(matrice_pow, matrice)
        matrice_pow = multiplication_matrix(matrice_pow, matrice)
        temp = divide_matrix(matrice_pow, facto)
        result = adding_matrix(result, temp)
        if all_dif(result, old_matrice) < precision:
            continu = False
        old_matrice = result
        index += 1

    return result
