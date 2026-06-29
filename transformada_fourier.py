myCompiler
myCompiler
Python
Transformada de Fourier
un usuario anónimo
·
hace 1 segundo

Español

Recientes
Iniciar sesión
Regístrate
Archivos
main.py
Sponsored: Guardsquare
Do you know if your mobile apps are under attack? Detect and analyze mobile threats in real-time.
hubs.la
Ads by EthicalAds
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
# ============================================
# Análisis de señales utilizando Python
# Transformada de Fourier
# ============================================

import numpy as np
import matplotlib.pyplot as plt

#---------------------------------
# Definición del tiempo
#---------------------------------

fs = 1000          # Frecuencia de muestreo
t = np.arange(-1,1,1/fs)

#---------------------------------
# Señal 1: Pulso rectangular
#---------------------------------

pulso = np.where(np.abs(t)<=0.2,1,0)

#---------------------------------
# Señal 2: Escalón
#---------------------------------

escalon = np.where(t>=0,1,0)

#---------------------------------
# Señal 3: Senoidal
#---------------------------------

f = 10
seno = np.sin(2*np.pi*f*t)

#---------------------------------
# Función para calcular FFT
#---------------------------------

def calcular_fft(signal):

    N=len(signal)

    fft=np.fft.fft(signal)

    frecuencia=np.fft.fftfreq(N,d=1/fs)

    magnitud=np.abs(fft)

    fase=np.angle(fft)

    return frecuencia,magnitud,fase

#---------------------------------
# FFT de cada señal
#---------------------------------


Ejecutar
Crear una copia

Salida
Entrada
Primer código del proyecto
