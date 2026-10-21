import scipy.stats as stats

# Muestra exacta de 120 números pseudoaleatorios
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

# Parámetros básicos
N = len(muestra)
alpha = 0.05

# Cálculo de la media muestral requerida para la varianza
media_muestral = sum(muestra) / N

# Cálculo de la varianza muestral (S^2)
varianza_muestral = sum((x - media_muestral)**2 for x in muestra) / (N - 1)

# Grados de libertad y Estadístico Chi^2
gl = N - 1
chi_calc = 12 * gl * varianza_muestral

# Valores críticos
chi_inf = stats.chi2.ppf(alpha / 2, gl)
chi_sup = stats.chi2.ppf(1 - alpha / 2, gl)

# Regla de decisión
decision = "No rechazar H0" if chi_inf <= chi_calc <= chi_sup else "Rechazar H0"

# Impresión de resultados
print("=== PRUEBA DE LA VARIANZA ===")
print(f"Tamaño de muestra (N): {N}")
print(f"Media muestral (R_bar): {media_muestral:.6f}")
print(f"Varianza muestral (S^2): {varianza_muestral:.6f}")
print(f"Grados de libertad (N - 1): {gl}")
print(f"Estadístico Chi-cuadrado calculado: {chi_calc:.4f}")
print(f"Valor crítico inferior Chi^2 (0.975, {gl}): {chi_inf:.4f}")
print(f"Valor crítico superior Chi^2 (0.025, {gl}): {chi_sup:.4f}")
print(f"Decisión: {decision}")