from src.matrice_operand import (
    get_matrice_identite,
    divide_matrix,
    multiplication_matrix,
    adding_matrix,
    mul_matrix,
    get_matrice,
)
from src.exponatial import all_dif
from math import factorial


def cossinus(argv: list[str]) -> list[list[float]]:
    precision: float = 0.001
    matrice: list[list[float]] = get_matrice(argv)
    index: int = 2
    continu: bool = True
    matrice_pow: list[list[float]] = matrice
    facto: int = factorial(2)
    matrice_square = multiplication_matrix(matrice_pow, matrice)
    result: list[list[float]] = adding_matrix(
        get_matrice_identite(matrice),
        mul_matrix(divide_matrix(matrice_square, facto), -1),
    )
    temp: list[list[float]] = []
    old_matrice: list[list[float]] = matrice

    while continu:
        facto = factorial(index * 2)
        matrice_pow = multiplication_matrix(matrice_pow, matrice_square)
        temp = mul_matrix(
            divide_matrix(multiplication_matrix(matrice_pow, matrice), facto),
            pow(-1, index),
        )
        result = adding_matrix(result, temp)
        if all_dif(result, old_matrice) < precision:
            continu = False
        old_matrice = result
        index += 1
    return result


def cossinush(argv: list[str]) -> list[list[float]]:
    precision: float = 0.001
    matrice: list[list[float]] = get_matrice(argv)
    index: int = 2
    continu: bool = True
    matrice_pow: list[list[float]] = matrice
    facto: int = factorial(2)
    matrice_square = multiplication_matrix(matrice_pow, matrice)
    result: list[list[float]] = adding_matrix(
        get_matrice_identite(matrice), divide_matrix(matrice_square, facto)
    )
    temp: list[list[float]] = []
    old_matrice: list[list[float]] = matrice

    while continu:
        facto = factorial(index * 2)
        matrice_pow = multiplication_matrix(matrice_pow, matrice_square)
        temp = divide_matrix(multiplication_matrix(matrice_pow, matrice), facto)
        result = adding_matrix(result, temp)
        if all_dif(result, old_matrice) < precision:
            continu = False
        old_matrice = result
        index += 1
    return result
