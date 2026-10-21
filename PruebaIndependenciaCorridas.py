# Muestra de 120 números pseudoaleatorios
muestra = [
    0.020403, 0.016548, 0.543156, 0.634904, 0.910030, 0.112462, 0.495889, 0.548349, 0.596100, 0.783450,
    0.039854, 0.743801, 0.965809, 0.073668, 0.699607, 0.460294, 0.396484, 0.959521, 0.406125, 0.952764,
    0.993678, 0.663701, 0.422896, 0.499925, 0.287285, 0.423302, 0.675319, 0.155304, 0.088769, 0.852686,
    0.311563, 0.007071, 0.462667, 0.291678, 0.572984, 0.962277, 0.015465, 0.779755, 0.302248, 0.321135,
    0.954988, 0.546828, 0.667262, 0.656965, 0.623416, 0.161249, 0.929064, 0.767423, 0.457067, 0.725680,
    0.331773, 0.712652, 0.576053, 0.761422, 0.442738, 0.205966, 0.456951, 0.671864, 0.521010, 0.872701,
    0.391604, 0.925643, 0.742251, 0.142855, 0.685179, 0.350165, 0.358227, 0.793137, 0.796611, 0.176099,
    0.118979, 0.404065, 0.874549, 0.723475, 0.535832, 0.247719, 0.391944, 0.870002, 0.813334, 0.371786,
    0.832383, 0.692248, 0.528277, 0.895521, 0.631317, 0.920287, 0.383904, 0.783247, 0.825291, 0.096452,
    0.617445, 0.611012, 0.112306, 0.578816, 0.889093, 0.092048, 0.276440, 0.780021, 0.730548, 0.376631,
    0.179858, 0.282085, 0.881265, 0.391987, 0.775317, 0.717811, 0.090511, 0.737865, 0.842316, 0.559423,
    0.213379, 0.903388, 0.399995, 0.205052, 0.678864, 0.820831, 0.999926, 0.003697, 0.658135, 0.021928
]

N = len(muestra)
alpha = 0.05

# 1. Calcular la mediana o valor de referencia (típicamente 0.5 para U(0,1))
# O se puede usar la mediana exacta de la muestra. Usaremos 0.5 por convención de la prueba.
mediana = 0.5

# 2. Clasificar cada valor respecto a 0.5 (+ si >= 0.5, - si < 0.5)
# Tratamiento de empates (= 0.5): se asumen como '+' según convención estándar o se descartan si caen exactos.
signos = []
for x in muestra:
    if x >= mediana:
        signos.append('+')
    else:
        signos.append('-')

# 3. Contar el número de corridas (b)
b = 1
for i in range(1, N):
    if signos[i] != signos[i-1]:
        b += 1

# 4. Calcular parámetros estadísticos teóricos (Media y Varianza de b)
# n1: cantidad de '+', n2: cantidad de '-'
n1 = signos.count('+')
n2 = signos.count('-')

mu_b = ((2 * n1 * n2) / N) + 0.5
sigma_b_sq = (2 * n1 * n2 * (2 * n1 * n2 - N)) / ((N ** 2) * (N - 1))
sigma_b = sigma_b_sq ** 0.5

# 5. Estadístico Z0
z_0 = (b - mu_b) / sigma_b

# 6. Valor crítico Z_alpha/2
import scipy.stats as stats
z_critico = stats.norm.ppf(1 - alpha / 2)

# 7. Regla de decisión
decision = "No rechazar H0" if abs(z_0) <= z_critico else "Rechazar H0"

# Impresión de resultados
print("=== PRUEBA DE CORRIDAS (INDEPENDENCIA) ===")
print(f"Tamaño de muestra (N): {N}")
print(f"Cantidad de valores >= 0.5 (n1): {n1}")
print(f"Cantidad de valores < 0.5 (n2): {n2}")
print(f"Número de corridas observadas (b): {b}")
print(f"Media teórica (mu_b): {mu_b:.4f}")
print(f"Desviación estándar (sigma_b): {sigma_b:.4f}")
print(f"Estadístico Z0 calculado: {z_0:.4f}")
print(f"Valor crítico Z_alpha/2: +/-{z_critico:.4f}")
print(f"Decisión: {decision}")