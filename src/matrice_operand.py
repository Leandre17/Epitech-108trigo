from math import sqrt


def get_matrice_identite(m_a: list[list[float]]) -> list[list[float]]:
    m_r: list[list[float]] = []
    for i in range(len(m_a)):
        now: list[float] = []
        for j in range(len(m_a[i])):
            if i == j:
                now.append(1)
            else:
                now.append(0)
        m_r.append(now)
    return m_r


def divide_matrix(m_a: list[list[float]], nb: int) -> list[list[float]]:
    m_r: list[list[float]] = []
    for i in range(len(m_a)):
        now: list[float] = []
        for j in range(len(m_a[i])):
            element = m_a[i][j] / nb
            now.append(element)
        m_r.append(now)
    return m_r


def mul_matrix(m_a: list[list[float]], nb: int) -> list[list[float]]:
    m_r: list[list[float]] = []
    for i in range(len(m_a)):
        now: list[float] = []
        for j in range(len(m_a[i])):
            element = m_a[i][j] * nb
            now.append(element)
        m_r.append(now)
    return m_r


def multiplication_matrix(
    m_a: list[list[float]], m_b: list[list[float]]
) -> list[list[float]]:
    m_r: list[list[float]] = []
    for i in range(len(m_a)):
        now: list[float] = []
        for j in range(len(m_b[0])):
            element: float = 0.0
            for k in range(len(m_a[0])):
                element = element + m_a[i][k] * m_b[k][j]
            now.append(element)
        m_r.append(now)
    return m_r


def adding_matrix(m_a: list[list[float]], m_b: list[list[float]]) -> list[list[float]]:
    m_r: list[list[float]] = []
    for i in range(len(m_a)):
        now: list[float] = []
        for j in range(len(m_a[i])):
            element = m_a[i][j] + m_b[i][j]
            now.append(element)
        m_r.append(now)
    return m_r


def get_matrice(av: list[str]) -> list[list[float]]:
    len_arg_sqrt: int = int(sqrt(len(av) - 2))
    matrice: list[list[float]] = []

    for i in range(len_arg_sqrt):
        new: list[float] = []
        for j in range(len_arg_sqrt):
            new.append(int(av[2 + (i * len_arg_sqrt) + j]))
        matrice.append(new)
    return matrice
