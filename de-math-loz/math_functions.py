def square(n: int) -> int:
    """
    Calcula el cuadrado de un numero.
    
    Args:
        n (int): El numero a elevar al cuadrado.

    Returns:
        int: El cuadrado del numero.
    """
    return n * n

def factorial(n: int) -> int:
    """
    Calcula el factorial de un numero.
    
    Args:
        n (int): El numero a calcular el factorial.

    Returns:
        int: El factorial del numero.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """
    Verifica si un numero es primo.
    
    Args:
        n (int): El numero a verificar.

    Returns:
        bool: True si el numero es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """
    Calcula el maximo comun divisor de dos numeros.
    
    Args:
        a (int): El primer numero.
        b (int): El segundo numero.

    Returns:
        int: El maximo comun divisor de los dos numeros.
    """
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """
    Calcula el minimo comun multiplo de dos numeros.
    
    Args:
        a (int): El primer numero.
        b (int): El segundo numero.

    Returns:
        int: El minimo comun multiplo de los dos numeros.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
