# Simulación de sistemas: generación y validación de números pseudoaleatorios

Este proyecto genera una muestra de números pseudoaleatorios con el método
congruencial lineal y la analiza mediante pruebas estadísticas de uniformidad e
independencia.

## Flujo de trabajo

```text
Parámetros del generador
(semilla, a, c, m, n=120)
          |
          v
generar_congruencial_lineal.py
          |
          v
Muestra R1 ... R120, con valores en [0, 1)
          |
          +--> pruebaMedias.py ----------------------> media muestral
          +--> pruebaVarianza.py --------------------> varianza muestral
          +--> pruebaUniformidadChiCuadrado.py ------> frecuencias por intervalo
          +--> PruebaUniformidadKolmogorovSmirnov.py -> distancia D
          +--> pruebaUniformidadAndersonDarling.py --> estadístico A² ajustado
          +--> PruebaIndependenciaCorridas.py -------> cantidad de corridas
                                                       |
                                                       v
                                      Estadístico, valor crítico y decisión
```

La muestra es la entrada común de las pruebas: cada una calcula un estadístico,
lo compara con su valor crítico para `alpha = 0.05` y presenta una decisión.
Las pruebas son independientes; ninguna toma como entrada el resultado de otra.
Por ejemplo, el inicio de la muestra usado por las pruebas es
`[0.020403, 0.016548, 0.543156, 0.634904, 0.910030, ...]`; los puntos suspensivos
representan los valores restantes hasta completar los 120.

### Cómo está implementado actualmente

`generar_congruencial_lineal.py` genera 120 valores con estos parámetros:

| Parámetro | Valor |
|---|---:|
| Semilla (`X0`) | 12345 |
| Multiplicador (`a`) | 1664525 |
| Constante aditiva (`c`) | 1013904223 |
| Módulo (`m`) | 4294967296 |
| Cantidad (`n`) | 120 |

La recurrencia es `X(i+1) = (a * Xi + c) mod m`; cada salida se normaliza como
`Ri = Xi / m`, por lo que queda en `[0, 1)`.

**Nota sobre el flujo de datos:** aunque ese es el flujo conceptual, hoy las seis
pruebas tienen una copia fija de la muestra dentro de cada archivo. No importan
ni reciben automáticamente la salida del generador. Para probar otra semilla,
otros parámetros o una cantidad distinta de números, hay que actualizar la
muestra en cada prueba. Por eso, los resultados de abajo corresponden a la
muestra fija incluida en los scripts (120 valores redondeados a seis decimales),
no a una ejecución automatizada de extremo a extremo.

## Ejecución

Se requiere Python y las bibliotecas NumPy y SciPy:

```powershell
python -m pip install numpy scipy
```

Ejecuta el generador:

```powershell
python generar_congruencial_lineal.py
```

Ejecuta cada prueba por separado:

```powershell
python pruebaMedias.py
python pruebaVarianza.py
python pruebaUniformidadChiCuadrado.py
python PruebaUniformidadKolmogorovSmirnov.py
python pruebaUniformidadAndersonDarling.py
python PruebaIndependenciaCorridas.py
```

## Resultados obtenidos con la muestra incluida

Las salidas se calcularon ejecutando los scripts actuales. La hipótesis nula
(`H0`) de cada prueba representa la propiedad estadística que se evalúa; “no
rechazar” significa que la muestra no aportó evidencia suficiente para
rechazarla con el nivel de significancia usado, no que se haya demostrado que
sea verdadera.

| Prueba | Resultado observado | Valor crítico | Decisión del script |
|---|---:|---:|---|
| Media | Media = 0.535186; `Z0` = 1.3352 | ±1.9600 | No rechazar `H0` |
| Varianza | Varianza = 0.081222; `χ²` = 115.9848 | Límites: 90.6996 y 151.0844 | No rechazar `H0` |
| Chi-cuadrado de uniformidad | Frecuencias = `[18, 14, 21, 19, 28, 20]`; `χ²` = 5.3000 | 11.0705 | No rechazar `H0` |
| Kolmogorov-Smirnov | `D` = 0.0885 | 0.1242 | No rechazar `H0` |
| Anderson-Darling | `A²` ajustado = 1.2518 | 0.752 | **Rechazar `H0`** |
| Corridas (independencia) | 67 valores `>= 0.5`, 53 valores `< 0.5`; 63 corridas; `Z0` = 0.6166 | ±1.9600 | No rechazar `H0` |

## Interpretación

Con `alpha = 0.05`, cinco pruebas no rechazan sus hipótesis nulas y
Anderson-Darling sí rechaza la uniformidad. Por tanto, los resultados no son
unánimes: no se debe afirmar que la muestra pasó todas las pruebas ni que el
generador quedó validado de manera concluyente. Conviene revisar la discrepancia
y ejecutar las pruebas sobre una misma muestra transferida automáticamente,
preferiblemente con un tamaño mayor si el objetivo es estudiar el
comportamiento a gran escala.

La ejecución actual usa 120 valores; por sí sola no demuestra comportamiento a
gran escala. Además, las decisiones dependen de los métodos y valores críticos
implementados en cada script; este README reporta esas salidas y no sustituye
una revisión de sus supuestos estadísticos.
