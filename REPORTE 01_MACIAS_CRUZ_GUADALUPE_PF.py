#!/usr/bin/env python
# coding: utf-8

# In[5]:


from lifestore_file import lifestore_products #IMPORTANDO LA LISTA DE PRODUCTOS
from lifestore_file import lifestore_sales #IMPORTANDO LA LISTA DE VENTAS
from lifestore_file import lifestore_searches #IMPORTANDO LA LISTA DE BUSQUEDAS
 

#........................CREACION DE LOGIN: CREDENCIALES DE ADMINISTRADOR Y ACCESO A URUARIOS......................

#CREACION DE LA CUENTA DEL ADMINISTRADOR
Administrador=input("Ingrese su nombre:") #con input se permite al usuario ingresar su nombre
password = input("Introduzca su password:") #Se le permite al Admi ingresar su contraseña
Guadalupem='Administrador'#Este es el administrador
Flower='password' #La contraseña con la cual podra acceder el administrador


#..................AUTENTIFICACION DE ADMINISTRADOR-ACCESOS

if Administrador=="Guadalupem" and password=="Flower": #Resaldando que el administrado solo tiene un nombre y contraseña establecida
    print('BIENVENIDO ADMINISTRADOR A LIFESTORE:AHORA ODRA CONSULTAR LOS REPORTES') #Mensaje de bienvenida al admin
    print('\nReporte 1-MAYORES VENTAS\n:')  #EN ESTE REPORTE EL ADMIPODRA VER LOS REPORTE DE PROD CON MAS VENTAS
    print(big_sales)  
    print('\nReporte 2-MAYORES BUSQUEDAS\n:') #EN ESTE REPORTE SE ENCUENTRAN LOS PRODUCTOS CON MAYORES BUSQUEDAS
    print(Searches_m)
    print('\nReporte 3-MENORES VENTAS POR CATEGORIA\n:') #EN ESTE REPORTE ESTAN LOS PROD CON MENOR VENTAS POR CATEGORIA
    print(short_sales) 
    print('\nReporte 4-BUSQUEDAS REZAGADAS POR CATEGORIA \n:') #EN ESTE REPORTE SE ENCUENTRAN LOS PRODUCTOS MENOS BUSCADOS
    print(Search_rezag)
    print('\nReporte 5-VALUACION DE PRODUCTOS_RESEÑAS\n:') #EN ESTE REPORTE SE ENCUENTRAN LOS PRODUCTOS POR CALIFICACIONES, EN ESTE CASO LAS MAS ALTAS
    print(serv_sales)
    print('\nReporte 6-VALUACION DE PRODUCTOS_PEORES RESEÑAS_CONTANDO PROD DEVUELTOS\n:') #EN ESTE REPORTE ESTAN LOS PRODUCTOS DEVUELTOS Y CON MALA CALIF
    print(total_serv) 
    print('\nReporte 7-TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES:\n') #ESTE REPORTE INCLUYE EL TOTAL DE INGRESOS Y LOS PROMEDIOS DE VENTAS
    print('\n Ingresos por ventas:\n') #Se encuentra el total de los ingresos multiplicados por las ventas
    print(Total_ingresos)
    print('\n INGRESOS GENERALES TOTALES:\n') #Aqui se encuentran los totales de los productos 
    print(1035278)#Resultado de la multiplicacion de la matriz de precio x venta
    print('\nReporte 8-"VENTAS PROMEDIO MENSUALES Y TOTAL ANUAL DE INGRESOS":\n')
    print('\nVentas promedio\n:') #aqui se encuentra el reporte de ventas promedio mensual 
    print(Promedio_mensual)
    print('\n Total anual\n:') #aqui se encuentra el total anual 
    print(Ventas_anutotales)
    print('\nMESES CON MAS VENTAS:\n') #los meses con mayores ventas 
    print('Enero, Febrero, Marzo, Abril, Mayo')
#...................................COMANDO PARA QUE EL ADMINISTRADOR CIERRE SESION........................................
comando = input("Escriba un comando para cerrar sesion:") #El administrador puede salir con cualquier comando 
if comando =="Salir" or "bye": #No necesariamente tiene que usar esos comandos
    print ("Ahora ha cerrado la sesión: vuelva pronto",Administrador) #Mensaje de despedida al adminstrador

#.................................PERMITIENDO EL ACCESO A UN USUARIO.................................
else: 
    print('Lo sentimos, no eres el administrador,solo se te permitira ver un reporte mensual como usuario') #mensaje de error para 
    #el usuario que intente entrar con la cuenta del administrador
    print('Entrara con una cuenta de usuario al reporte mensual de mayores ventas en lifestore, introduzca sus datos') #Mensaje para que el usuario tome en cuenta los que solo padra ver

    # ...................................INGRESO CON CUENTA DE USUARIO.............................
Usuario_visualizador= input("Ingrese un nombre: ") #Usuario 
print('Asegurese de que sus datos sean correctos') 
password= input("Ingrese una contraseña: ") #PARA QUE INGRESE LA CONTRASEÑA SE USA INPUT
print ("Tu id de usuario es",Usuario_visualizador,'Asegurate de recordarlo') #Aqui le recuerdo al usuario cual seria su id, para la proxima vez que entre
print('BIENVENIDO USUARIO A LIFESTORE:') #MENSAJE DE BIENVENIDA A LA TIENDA VIRTUAL 
print('Saludos Usuario!: A continuacion se le mostrara el reporte de mayores ventas y la lista de ingresos totales') 
#Saludando al usuario
print('\n Lista con los productos de mayores ventas: nombre, cantidad total vendida\n') #Describiendo lo que visualizara de las ventas
#PERMITIENDO AL USUARIO VISUALILZAR LA LISTA DE LOS ID_PROD CON MAYORES VENTAS...........

#...........................................REPORTE DE MAYORES VENTAS .............


contador= 0   #CONTADOR 
ventas_generales =[] #id1_producto, nombre,contador [id2_producto,contador2]
for product in lifestore_products:#FOR 1
    for bsales in lifestore_sales: #FOR 2
        if product[0]==bsales[1]:  #aqui se indica con el if que se hra referencia tanto a los productos de lifestore como a las ventas
            contador+=1
    
    Sales_tot=[product[0], product [1], contador] #aqui se encuentran los productos mostrados con el indice
    ventas_generales.append(Sales_tot)  #agregando la lista anterior
    contador=0
    
    # for general in ventas_generales:
        #print('\nEste producto:\n', general[1], '\nfueron vendidos\n', general[2]) #Con este print modificamos los elementos
        #a los cuales me interesan de la lista de ventas de lifestore
    
#ORDENACION DE MI LISTA CON VENTAS GENERALES 

sales_orden=[ventas_generales]  #nombre como sales_orden a mi lista que pretendo ordenar
sales_orden.sort() #SORT PARA ORDENAR DE MENOR A MAYOR SOLO QUE SE ORDENARON POR ID_PRODUCTO
"print(sales_orden)#print(sales_orden) #IMPRIMIMOS"
    
# DE LA LISTA ANTERIOR YA ORDENADA CREARE UNA LISTA CON LOS PRODUCTOS MAS VENDIDOS POR MEDIO DE LOS INDICE:

# MI LISTA CON LOS PORDUCTO CON MAYORES VENTAS LO QUE HICE FUE UNIR LAS LISTA ORDENADA Y MEDIANTE EL INDICE DE LOS 
#PRODUCTOS CON MAS VENTAS SE GENERO LA LISTA

"print('\n Lista con los productos de mayores ventas: nombre, cantidad total vendida\n')"
big_sales=[[big_sales[53] for big_sales in sales_orden],[big_sales[2] for big_sales in sales_orden],
          [big_sales[4] for big_sales in sales_orden], [big_sales[41] for big_sales in sales_orden], 
          [big_sales[56] for big_sales in sales_orden], [big_sales[28]for big_sales in sales_orden], 
           [big_sales[1] for big_sales in sales_orden], [big_sales[3] for big_sales in sales_orden], 
           [big_sales[46] for big_sales in sales_orden], [big_sales[47] for big_sales in sales_orden]]

if Administrador=="Guadalupem" and password=="Flower": #Con un if indico que en este caso esta lista la puede ver tanto el
    print(big_sales)                                #Admi como el usuario pero en caso de que este ultimo no pudiera se restringe con un else
else:
    print('Usuario:Solo se le mostrara la lista con mayores ventas:')  #else es para mostrar sino ocurre if ocurre else
# La lista anterior esta acomodada de acuerdo al producto con mas ventas
print(big_sales)

#.........................................REPORTE DE MAYORES BUSQUEDAS.............

#BIG_SEARCH=('Reporte de los Id_productos con mayores busquedas)

#VOLVERE HACER EL MISMO PORCESO QUE CON LA DE LAS VENTAS: FILTRAR LA LISTA, CONCATENAR Y ORDENAR
contador= 0   #CONTADOR 
Busquedas_totales=[] #id1_producto, nombre,busqueda
for product in lifestore_products:#FOR 1   #en este for incluyo la lista de los productos para mostrar el nombre de estos
    for busquedas in lifestore_searches:#FOR 2  en este for incluyo la lista que me interesa contar ](n_busquedas)
        if product[0]== busquedas[1]:
            contador += 1
            
    Busq_search=[ product[3], product [1],contador] #Definiendo los indices de la lista de los productos
    Busquedas_totales.append(Busq_search)
    contador=0
    
    #for total in Busquedas_totales:
      #print('\nEste producto:\n', total [0],'\nSe busco:\n', total[1],'veces') #En el caso de las busquedas 
    #al igual que en el de las ventas en este caso selecciono los inidices que me interesa hacer referencia

#...................LISTA_ID_PRODUCTOS CON MAYORES BUSQUEDAS...........
# ORDENARE LA LISTA ANTERIOR PARA GENERAR UNA NUEVA Y DE AHI SACAR LA DE MAYORES BUSQUEDAS


busq_ordenadas = [Busquedas_totales] #haciendo referencia a la lista que me interesa ordenar 
busq_ordenadas.sort() #SORT UTILIZADO PARA ORDENAR LA LISTA ANTERIOR 
"print(busquedas_totales)" #Al imprimir se ordena una lista que incluye el id_producto, nombre y numero de busquedas

#GENERO MI LISTA DE MAYORES BUSQUEDAS:

"print('\n  Informe de los productos de mayores busquedas:nombre, cantidad total de busquedas \n')"

#Este lista esta ordenada por el producto con mayores busquedas y la cree a partir de los indices de la lista de busquedas_totales
#Asimismo con ayuda del for la use para dar referencia a la anterior lista ordenada
Searches_m= [[Searches_m[53] for Searches_m in busq_ordenadas],[Searches_m [56] for Searches_m in busq_ordenadas],
[Searches_m [28]for Searches_m in busq_ordenadas], [Searches_m [2] for Searches_m in busq_ordenadas], 
[Searches_m [84] for Searches_m in busq_ordenadas], [Searches_m [66] for Searches_m in busq_ordenadas],
[Searches_m [6] for Searches_m in busq_ordenadas], [Searches_m [4] for Searches_m in busq_ordenadas], 
[Searches_m [46] for Searches_m in busq_ordenadas], [Searches_m [47] for Searches_m in busq_ordenadas],
[Searches_m [43] for Searches_m in busq_ordenadas], [Searches_m [1] for Searches_m in busq_ordenadas],
[Searches_m [41] for Searches_m in busq_ordenadas], [Searches_m [7] for Searches_m in busq_ordenadas],
[Searches_m [20] for Searches_m in busq_ordenadas], [Searches_m [50]for Searches_m in busq_ordenadas],
[Searches_m [0] for Searches_m in busq_ordenadas], [Searches_m [3] for Searches_m in busq_ordenadas],
[Searches_m [5] for Searches_m in busq_ordenadas], [Searches_m [24]for Searches_m in busq_ordenadas],
[Searches_m [30] for Searches_m in busq_ordenadas], [Searches_m [39] for Searches_m in busq_ordenadas],
[Searches_m [48] for Searches_m in busq_ordenadas], [Searches_m [83] for Searches_m in busq_ordenadas],
[Searches_m [49] for Searches_m in busq_ordenadas], [Searches_m [88]for Searches_m in busq_ordenadas]]


#print(Searches_m)  #Se imprime la lista de los productos con mayores busquedas, partiendo de los productos con mayores busquedas


#...................................PRODUCTOS MAS REZAGADOS POR CATEGORIAS.......

#VENTAS REZAGADAS 

#Esta lista la cree apartir de la lista de sales_orden donde vienen los productos mas vendidos y los rezagados, 
#En este caso solo me enfoque en los indices de los productos de menores ventas
# Dichos indices los ordene de los productos mas rezagados, es decir, que tienen ventas nulas==0

"print('\nInforme mensual de los productos con ventas rezagadas:categoria, nombre y num_de ventas\n')"

short_sales=[[short_sales[13:15]for short_sales in sales_orden], [short_sales[18:19]for short_sales in sales_orden],
[short_sales[22:23]for short_sales in sales_orden], [short_sales[25:26]for short_sales in sales_orden],
[short_sales [29]for short_sales in sales_orden], [short_sales[31]for short_sales in sales_orden], 
[short_sales[33:38]for short_sales in sales_orden],[short_sales[40]for short_sales in sales_orden],
[short_sales[42]for short_sales in sales_orden], [short_sales[52]for short_sales in sales_orden], 
[short_sales[54:55]for short_sales in sales_orden], [short_sales[57:58]for short_sales in sales_orden],
[short_sales[60:64]for short_sales in sales_orden], [short_sales[67:72]for short_sales in sales_orden],
[short_sales[74:82]for short_sales in sales_orden], [short_sales[85:87]for short_sales in sales_orden],
[short_sales[89:92]for short_sales in sales_orden], [short_sales[94:95]for short_sales in sales_orden],
[short_sales[0]for short_sales in sales_orden], [short_sales[9]for short_sales in sales_orden], 
[short_sales[12]for short_sales in sales_orden], [short_sales[16]for short_sales in sales_orden], 
[short_sales[16:17]for short_sales in sales_orden], [short_sales[21]for short_sales in sales_orden],
[short_sales[27]for short_sales in sales_orden], [short_sales[39]for short_sales in sales_orden], 
[short_sales[44:45]for short_sales in sales_orden], [short_sales[49]for short_sales in sales_orden], 
[short_sales[59]for short_sales in sales_orden], [short_sales[65:66]for short_sales in sales_orden], 
[short_sales[88]for short_sales in sales_orden], [short_sales[93]for short_sales in sales_orden], 
[short_sales[7]for short_sales in sales_orden], [short_sales[10]for short_sales in sales_orden], 
[short_sales[12]for short_sales in sales_orden], [short_sales[17]for short_sales in sales_orden], 
[short_sales[20]for short_sales in sales_orden], [short_sales[89:92]for short_sales in sales_orden], 
[short_sales[24]for short_sales in sales_orden], [short_sales[32]for short_sales in sales_orden], 
[short_sales[50:51]for short_sales in sales_orden], [short_sales[73]for short_sales in sales_orden],
[short_sales[6]for short_sales in sales_orden]]

        
#elem= len(short_sales) #Use len para saber los elementos de la lista anterior 
#print(elem) 
#print(short_sales)   #Se imprime la lista de los productos con menores ventas partiendo de los que tiene ventas nulas=0


#...................................MENORES BUSQUEDAS POR CATEGORIA..................
"print('\nInforme mensual de los productos de busquedas rezagadas:categoria, nombre y total de busquedas\n')"

#Esta lista la cree tomando como referencia los indices con menores busquedas o en si partiendo de las nulas=0
#De ahi fui haciendo mi lista y con un for 
Search_rezag=[[Search_rezag[13] for Search_rezag in busq_ordenadas],[Search_rezag[15] for Search_rezag in busq_ordenadas], 
            [Search_rezag[18] for Search_rezag in busq_ordenadas], [Search_rezag[22:23] for Search_rezag in busq_ordenadas],
            [Search_rezag[29] for Search_rezag in busq_ordenadas], [Search_rezag[31:33] for Search_rezag in busq_ordenadas],
            [Search_rezag[35:37] for Search_rezag in busq_ordenadas],[Search_rezag[40] for Search_rezag in busq_ordenadas],
            [Search_rezag[42] for Search_rezag in busq_ordenadas], [Search_rezag[52] for Search_rezag in busq_ordenadas],
            [Search_rezag[54] for Search_rezag in busq_ordenadas], [Search_rezag[58] for Search_rezag in busq_ordenadas],
            [Search_rezag[59:61] for Search_rezag in busq_ordenadas], [Search_rezag[67:68] for Search_rezag in busq_ordenadas],
            [Search_rezag[70:71] for Search_rezag in busq_ordenadas], [Search_rezag[76:78] for Search_rezag in busq_ordenadas],
            [Search_rezag[80:82] for Search_rezag in busq_ordenadas], [Search_rezag[85:87] for Search_rezag in busq_ordenadas], 
            [Search_rezag[89] for Search_rezag in busq_ordenadas], [Search_rezag[91] for Search_rezag in busq_ordenadas],
            [Search_rezag[95]for Search_rezag in busq_ordenadas], [Search_rezag [8:9]for Search_rezag in busq_ordenadas],
            [Search_rezag[44:45] for Search_rezag in busq_ordenadas], [Search_rezag[51]for Search_rezag in busq_ordenadas],
            [Search_rezag[62] for Search_rezag in busq_ordenadas], [Search_rezag[75]for Search_rezag in busq_ordenadas],
            [Search_rezag[26] for Search_rezag in busq_ordenadas], [Search_rezag[58]for Search_rezag in busq_ordenadas],
            [Search_rezag[34] for Search_rezag in busq_ordenadas], [Search_rezag[38]for Search_rezag in busq_ordenadas],
            [Search_rezag[69] for Search_rezag in busq_ordenadas], [Search_rezag[79]for Search_rezag in busq_ordenadas],
            [Search_rezag[92] for Search_rezag in busq_ordenadas], [Search_rezag[55] for Search_rezag in busq_ordenadas],
            [Search_rezag[90]for Search_rezag in busq_ordenadas],[Search_rezag[12] for Search_rezag in busq_ordenadas], 
           [Search_rezag[14]for Search_rezag in busq_ordenadas],[Search_rezag[94] for Search_rezag in busq_ordenadas], 
            [Search_rezag[10]for Search_rezag in busq_ordenadas],[Search_rezag[16] for Search_rezag in busq_ordenadas], 
            [Search_rezag[21]for Search_rezag in busq_ordenadas],[Search_rezag[25:27] for Search_rezag in busq_ordenadas], 
            [Search_rezag[51]for Search_rezag in busq_ordenadas],[Search_rezag[72:73] for Search_rezag in busq_ordenadas],
            [Search_rezag[49] for Search_rezag in busq_ordenadas],[Search_rezag[88] for Search_rezag in busq_ordenadas], 
            [Search_rezag[93] for Search_rezag in busq_ordenadas]]


#print(Search_rezag)  #EN ESTE CASO SE IMPRIME LA LISTA DE BUSQUEDAS REZAGADAS PARTIENDO DE LAS NULAS = 0 MEDIANTE SUS INDICES

#...........................PRODUCTOS POR RESEÑA EN EL SERVICIO

#List=[list [2] for list in lifestore_sales]
#print(List)

"print('\nLISTA DE LOS PRODUCTOS CON MEJORES RESEÑAS:id-producto, nombre, precio, categoria\n')"
#PRODUCTOS POR RESEÑA EN EL SERVICIO
p_serv=lifestore_products[0:1]
p_serv2=lifestore_products[3:7]
p_serv3=lifestore_products[10:11]
p_serv4=lifestore_products[17]
p_serv5=lifestore_products[20]
p_serv6=lifestore_products[24]
p_serv7=lifestore_products[32]
p_serv8=lifestore_products[39]
p_serv9=lifestore_products[41]
p_serv10=lifestore_products[43]
p_serv11=lifestore_products[46]
p_serv12=lifestore_products[47:48]
p_serv13=lifestore_products[50]
p_serv14=lifestore_products[54]
p_serv15=lifestore_products[56]
p_serv16=lifestore_products[59]
p_serv17=lifestore_products[65:66]
p_serv18=lifestore_products[73]
p_serv19=lifestore_products[83]
p_serv20=lifestore_products[84]
p_serv21=lifestore_products[93]


serv_sales=[p_serv+p_serv2+p_serv3+p_serv4+p_serv5+p_serv6+p_serv7+p_serv8+p_serv9+p_serv10+p_serv11+p_serv12+p_serv13+
           p_serv14+p_serv15+p_serv16+p_serv17+p_serv18+p_serv19+p_serv20+p_serv21] #SUME TODAS LAS LISTAS ANT PARA GENERAR UNA SOLA
#QUE CONTIENE TODOS LOS PRODUCTOS CON MAYORES RESEÑAS
"print(serv_sales)" #IMPRIMIENDO LA LISTA DE LOS PRODUCTOS CON MEJORES RESEÑAS


#..................PEORES RESEÑAS........................
#CREE MI LISTA DE LAS PEORES RESEÑAS TOMANDO EN CUENTA LAS CALIFICACIONES Y DEVOLUCIONES
#print('\nLISTA DE LOS PRODUCTOS CON PEORES RESEÑAS:id-producto, nombre, precio, categoria\n')
list_serv=lifestore_products[2]
list_serv2=lifestore_products[16]
list_serv3=lifestore_products[28]
list_serv4=lifestore_products[30]
list_serv5=lifestore_products[44]
list_serv6=lifestore_products[45]
list_serv7=lifestore_products[53]
list_serv8=lifestore_products[88]
list_serv9=lifestore_products[46]
list_serv10=lifestore_products[3]
list_serv11=lifestore_products[1]

total_serv=[list_serv+list_serv2+list_serv3+list_serv4+list_serv5+list_serv6+list_serv7+list_serv8+list_serv9+list_serv10+
           list_serv11] #AL IGUAL QUE LA LISTA ANTERIOR ESTA LISTA LA CREE A PARTIR DE INDICES Y TOMANDO EN CUENTA LAS DEVOLUCIONES Y VALUACIONES
#print(total_serv) #IMPRIMIENDO UNA SOLA LISTA

#.....................TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES
#TOTAL ANUAL Y MESES CON MAS VENTAS
list_precios=[list_precios[2] for list_precios in lifestore_products] #CON ESTA FORMULA OBTUVE LOS PRECIOS DE C/PROD EN UNA MATRIZ
#print(list_precios) #AL IMPRIMIR LA LISTA, LA COPIE PARA MULTIPLICAR EL PRECIO POR EL N_VENTAS TOTAL DE C/PRODUCTO

#voy a sumar todo lo que se obtuvo de las ventas multiplicando los precios por num de ventas de c/producto
#print('\n LISTA: INGRESOS POR VENTA\n:') #PRECIO DEL PRODUCTO * VENTAS 
Total_ingresos=[[3019*2,4209*13,3089*42,2209*13, 1779*20, 11809*3, 8559*7, 5399*4, 2549, 889*1,7399*3,6619*9, 3989*1,1439, 8439,
                 9799, 4199*1,2199*5, 4509,11509,5159*2,3429*1,909, 30449, 5529*2,1249, 2109, 9579*1, 2499*29, 4029, 2229*6,
                4309, 4269*2, 5289, 3419, 4159, 4289, 1369, 2169, 17439*1,3329, 1779*18, 6369, 2759*6,2869*1, 1539*1,1209*11, 
                2559*9, 3139*3, 2949*1,2399*3, 5659*2, 2039, 259*50,4399, 3269, 889*15, 3679,5539, 2519*1,5209, 2899,3369, 12029, 
            21079, 8049*1, 3229*1, 4229, 5359, 7679, 4829, 9759, 10559,4239*2, 441, 589, 178, 769, 709, 1359,1169, 549, 499, 1089*1, 
            2159*2, 8359, 1719, 909, 859*1, 539, 137, 149, 160,2869*1, 999, 769]]
# print(Total_ingresos)

#print('\nTOTAL INGRESOS\n')
for i in Total_ingresos:
    print(i) #  imprime la sumatoria de la lista anterior
    print(sum(i))  #CON ESTO SE IMPRIME LA SUMA DE LOS INGRESOS DANDO ASI SU TOTAL
        
#................VENTAS PROMEDIO MENSUALES
#print('\nPROMEDIO MENSUAL VENTAS\n:')
Promedio_mensual=[1035278/30] #CALCULANDO EL PROMEDIO DE LAS VENTAS este nnumero es del total de la sumatoria anterior,
                                #lo dividi entre 30 PARA OBTENER LAS VENTAS PROMEDIO MENSUALES 
#print(Promedio_mensual) #Imprimiendo la lista del promedio de ventas


#............TOTAL ANUAL
#print('\nTOTAL ANUAL DE INGRESOS:\n')  
    
Ventas_anutotales=[1035278*12]  #DE LA SUMATORIA DE INGRESOS TOTALES LA MULTIPLIQUE POR 12 PARA OBTENER LOS INGRESOS ANUALES
#print(Ventas_anutotales) #imprimiendo la lista de ls ventas totales anuales

#.............MESES CON MAS VENTAS AL AÑO..........

Fechas=[list_fechas[3] for list_fechas in lifestore_sales] #FILTRACION DE LISTA VENTAS PARA OBTENER SOLO LAS FECHAS
sorted_Fechas=sorted(Fechas) #ORDENANDO LA LISTA DE FECHAS

#print(sorted_Fechas)#IMPRESION DE LAS LISTAS_ORDENADAS #
#DE LA LISTA GENERADA ANTERIORMENTE GENERE MI PROPIA LISTA DE FECHAS SOLO POR MESES DONDE: 1=ENE, 2=FEB, 3=MZO, 4=ABRIL, 5=MAY,,ETC

fechas_mes=[1, 1, 2, 3, 3, 4, 4, 5, 7, 1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 7, 8, 8, 1, 1, 2, 2, 3, 4, 4, 4, 
             5, 6, 6, 7, 8, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 1, 3, 4, 5, 5, 5, 5, 5, 7, 
            9, 1, 1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 1, 2, 2, 3, 3, 3, 4, 4, 1, 1, 3, 4, 5, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 
            4, 4, 1, 2, 2, 2, 3, 3, 3, 4, 6, 11, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 2, 2, 2, 1, 1, 3, 4, 4, 4, 4, 4, 4, 1, 2, 
            3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 2, 4, 4, 5, 5, 2, 3, 4, 4, 4, 4, 1, 1, 2, 3, 4, 4, 4, 4, 6, 6, 1, 2, 4,
            1, 3, 3, 4, 4, 4, 6, 1, 2, 3, 3, 3, 3, 4, 4, 5, 3, 3, 7, 7, 1, 1, 2, 2, 3, 3, 4, 4, 5, 1, 1, 1, 2, 3, 3,
            4, 4, 4, 5, 5, 5, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 7, 1, 1, 1, 2, 2, 2, 2, 3, 4, 7, 1, 2, 3, 4,
            4, 4, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 7, 7 , 1, 1, 3, 3, 4, 1, 1, 1, 1, 1,3, 3, 3, 4, 4, 6, 6, 1, 1, 1, 3]

#Utilice la funcion de count para saber el numero de veces en que se repetia un mes y como resultados obtuve los sig:
#fechas_mes.count(1)...RESULTADOS = 53

#fechas_mes.count(2)...RESULTADOS = 42
#fechas_mes.count(3)...RESULTADOS = 51
#fechas_mes.count(4)...RESULTADOS = 75
#fechas_mes.count(5)...RESULTADOS = 36

#fechas_mes.count(6)...RESULTADOS = 11
#fechas_mes.count(7)...RESULTADOS = 11
#fechas_mes.count(8)...RESULTADOS = 3

#print(sorted_fechas_mes)

#print('\nMESES CON MAS VENTAS:\n') #DADO LO ANTERIOR LOS MESES CON MAS VENTAS SON
#print('Enero, Febrero,Marzo, Abril, Mayo') #los meses de mayores ventas que se identificaron dado el conteo los integre en una cadena

#...................................COMANDO PARA QUE EL USUARIO CIERRE SESION........................................
comando = input("Escriba un comando para cerrar sesion:") # Comando para que el usuario pueda cerrar sesion 
if comando =="Salir u otro": #Puede usar el comando salir o numeros u otros
    print ("Ahora ha cerrado la sesión: Gracias por consultarnos!, vuelva pronto",Usuario_visualizador) #Mensaje de despedida al usuario


# In[ ]:





# In[ ]:




