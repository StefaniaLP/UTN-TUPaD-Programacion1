# 10)Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# •Mostrar el total vendido por cada producto.
# •Mostrar el día con mayores ventas totales.
# •Indicar cuál fue el producto más vendido en la semana

tienda = [   # [NombreProducto , ventaDia1, ventaDia2 ....etc ]
    ["Remeras", 10, 12, 19, 18, 33, 45, 14], #151
    ["Pantalones", 17, 24, 38, 16, 22, 15, 25], #157
    ["Camperas", 8, 30, 1, 12, 17, 23, 33], #124
    ["Camisas", 9, 11, 13, 17, 2, 21, 100] #74 
]

prod_masVendido = ""
mayor=0
suma_ventas_Dia1=0
suma_ventas_Dia2=0
suma_ventas_Dia3=0
suma_ventas_Dia4=0
suma_ventas_Dia5=0
suma_ventas_Dia6=0
suma_ventas_Dia7=0


for prod in tienda:
    sumaVenta = 0
    lista_maximoPorDia = []
    #sumo las ventas por dia
    suma_ventas_Dia1 = suma_ventas_Dia1 + prod[1]
    suma_ventas_Dia2 = suma_ventas_Dia2 + prod[2]
    suma_ventas_Dia3 = suma_ventas_Dia3 + prod[3]
    suma_ventas_Dia4 = suma_ventas_Dia4 + prod[4]
    suma_ventas_Dia5 = suma_ventas_Dia5 + prod[5]
    suma_ventas_Dia6 = suma_ventas_Dia6 + prod[6]
    suma_ventas_Dia7 = suma_ventas_Dia7 + prod[7]
    
    #sumo ventas de cada producto
    for ventas in prod[1:]:
        sumaVenta= sumaVenta + ventas
                
    print (f"El total vendido de ", prod[0], " es:", sumaVenta)
    print()
        
    #identifico el mas vendido en la semana
    if(sumaVenta > mayor):
        mayor=sumaVenta
        prod_masVendido= prod[0]


lista_maximoPorDia.append(suma_ventas_Dia1)
lista_maximoPorDia.append(suma_ventas_Dia2)
lista_maximoPorDia.append(suma_ventas_Dia3)
lista_maximoPorDia.append(suma_ventas_Dia4)
lista_maximoPorDia.append(suma_ventas_Dia5)
lista_maximoPorDia.append(suma_ventas_Dia6)
lista_maximoPorDia.append(suma_ventas_Dia7)

dia_max= max(lista_maximoPorDia)
indice_diaMax= lista_maximoPorDia.index(dia_max)+1
print(f"El dia ", indice_diaMax , " es que realizo mas ventas = ", dia_max)
print()
print(f"El producto mas vendido es: ", prod_masVendido)