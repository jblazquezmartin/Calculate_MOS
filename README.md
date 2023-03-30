# Calculate_MOS

Se usa versión simplificada de la fórmula del modelo ITU-T G.107 para calcular el MOS a partir de la latencia, el jitter y la pérdida de paquetes.

https://www.itu.int/rec/T-REC-G.107-201506-I/es

La fórmula se basa en el modelo E-Model, que es un modelo de regresión matemática utilizado para estimar la calidad de la transmisión de voz en redes IP. La fórmula es menos compleja que la fórmula completa del modelo ITU-T G.107, pero puede ser útil para estimar el MOS de manera rápida y sencilla.

https://www.itu.int/rec/T-REC-G.107/es

La fórmula utiliza la latencia, el jitter y el retardo del códec para calcular una "latencia efectiva", que se utiliza para calcular el factor R. A partir del factor R, se calcula el MOS utilizando la fórmula estándar para el cálculo del MOS:

MOS = 1 + 0.035*R + 0.000007*R*(R-60)*(100-R)
