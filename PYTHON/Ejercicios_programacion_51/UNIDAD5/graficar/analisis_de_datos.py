import os
os.system('cls')


import matplotlib as plt


x1=[2,5,6,14]
y1= [11,22,33,44]

x2=[2,5,6,15]
y2=[4,12,18,45]

#Graficar 2 lineas en la misma grid
plt.plot(x1,y1, color="blue", linewidth = 3, label = 'Linea 1')
plt.plot(x2,y2, color="green", linewidth = 3, label = 'Linea 2')

plt.title('Dos Graficas juntas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid()
plt.show()



#Grafico de barras. Cuando coinciden la misma X, las apila
plt.bar(x1,y1, color="blue", linewidth = 3, label = 'Barra 1')
plt.bar(x2,y2, color="green", linewidth = 3, label = 'Barra 2')

plt.title('Dos Barras juntas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid()
plt.show()

#Histogramas
Datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30,]
Rangobin=[0,10,20,20,30,40]

plt.hist(Datos, Rangobin, histtype='bar',rwidth=0.8, color='lightgreen')

plt.title('Histograma')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
#plt.grid()  #la grid no es necesaria (lineas horizontales y verticales)
plt.show()


