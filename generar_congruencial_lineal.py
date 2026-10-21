def generar_congruencial_lineal(n, semilla, a, c, m):
    """
    Genera n números pseudoaleatorios usando el Algoritmo Congruencial Lineal.
    X_{i+1} = (a * X_i + c) % m
    """
    numeros_aleatorios = []
    x = semilla
    for _ in range(n):
        x = (a * x + c) % m
        # Normalizar en el intervalo [0, 1)
        r = x / m
        numeros_aleatorios.append(r)
    return numeros_aleatorios

# Parámetros del generador
SEMILLA = 12345
MULTIPLICADOR = 1664525
CONSTANTE_ADITIVA = 1013904223
MODULO = 2**32
CANTIDAD = 120  # Mayor a 100 números requeridos

# Generar la muestra
muestra = generar_congruencial_lineal(CANTIDAD, SEMILLA, MULTIPLICADOR, CONSTANTE_ADITIVA, MODULO)

print("Parámetros utilizados:")
print(f"Semilla (X0): {SEMILLA}")
print(f"Multiplicador (a): {MULTIPLICADOR}")
print(f"Constante aditiva (c): {CONSTANTE_ADITIVA}")
print(f"Módulo (m): {MODULO}\n")

print(f" números pseudoaleatorios generados (Total: {len(muestra)}):")
for i, val in enumerate(muestra[:120], 1):
    print(f"X_{i} = {val:.6f}")
