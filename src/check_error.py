from math import sqrt


def check_error(av: list[str]) -> int:
    if len(av) < 3:
        return 84
    sqrt_arg = sqrt(len(av) - 2)
    if sqrt_arg not in [1, 2, 3, 4, 5]:
        return 84
    for i in range(2, len(av)):
        try:
            int(av[i])
        except:
            return 84
    if av[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        return 84
    return 0
