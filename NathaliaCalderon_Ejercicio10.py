import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal

datos1 = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt", sep=";", header=None, decimal=",")

datos1[0] = pd.to_datetime(datos1[0], format='%d/%m/%Y %H:%M:%S')
datos1[1] = pd.to_datetime(datos1[1], format='%d/%m/%Y %H:%M:%S')
#datos.set_index([0],inplace=True)

datos1[1]=str(datos1[1])
datos1[1]=datos1[1].str[1:20]

datos2 = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt", sep=";", header=None, decimal=",")
datos2[0] = pd.to_datetime(datos2[0], format='%d/%m/%Y %H:%M:%S')
datos2[1] = pd.to_datetime(datos2[1], format='%d/%m/%Y %H:%M:%S')

datos2[1]=str(datos2[1])
datos2[1]=datos2[1].str[1:20]

datos3 = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt", sep=";", header=None, decimal=",")
datos3[0] = pd.to_datetime(datos3[0], format='%d/%m/%Y %H:%M:%S')
datos3[1] = pd.to_datetime(datos3[1], format='%d/%m/%Y %H:%M:%S')

datos3[1]=str(datos3[1])
datos3[1]=datos3[1].str[1:20]


N  = 2
Wn = 0.01 
B, A = signal.butter(N, Wn)

costo = pd.concat([datos1[2],datos2[2],datos3[2]])
costo = np.array(costo)
costo = costo.astype(np.float)
costoF = signal.filtfilt(B,A,costo)
fecha = pd.concat([datos1[0],datos2[0],datos3[0]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,costo, 'b-')
plt.plot(fecha,costoF, 'r-',linewidth=2)
plt.ylabel(r"Costo")
plt.legend(['Original','Filtrado'])
plt.title("Costos en la bolsa")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(fecha,costo-costoF, 'b-')
plt.ylabel(r"Costos")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.show()
plt.savefig("Figura.png")



plt.figure(figsize=(20,7))
ruido=costo-costoF
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.show()
plt.savefig("Figura2.png")