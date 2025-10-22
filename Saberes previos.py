#1.	Lea tres números y calcule el resultado de su suma.
# una=float(input("Ingresa un numero"))
# dos=float(input("igresa segundo numero"))
# tres=float(input("ingresa tecer nuemro"))
# resultado=una+dos+tres
# print(resultado)


#2.	Lea dos números y calcule el resultado de su suma, resta, multiplicación y división.
# num1=int(input("ingrese un numero"))
# num2=int(input("ingrese un numero"))
# print(f"la suma es: {num1+num2}.\nla resta es: {num1-num2}.\nla multiplicacion es: {num2*num1}.\nla division es:{num1/num2}.")

#3. Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura.
# notas=[5,3,1]
# promedio=0
# for i in notas:
#     promedio+=i    
# print(promedio/3)

#4.	Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura si la primera nota tiene un valor del 20%, la segunda del 30% y la última del 50%.
#Definitiva=(5×0.20)+(3×0.30)+(1×0.50)
# nota1=float(input("Ingresa nota 1: "))
# nota2=float(input("Ingresa nota 2: "))
# nota3=float(input("Ingresa nota 3: "))
# print(f"Definitiva es:{(nota1*0.20)+(nota2*0.30)+(nota3*0.50)}")

#5.	Lea la distancia (en kilómetros) recorrida por un auto, el tiempo (en horas) en que la recorrió y calcule la velocidad a la cual se desplazaba el auto (V=D/T).
# distancia=float(input("ingrese la distancia en KM"))
# tiempo=float(input("Ingrese el tiempo en HORAS"))
# print(f"En promedio el carro se movilizaba a: {distancia/tiempo}")

#6.	Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (antes de aplicarle el IVA).
# numproc=int(input("Valor total de la compra?3"))
# descuento=str(input("Es valido el descuento?\nSi es valido marque 1\nDe lo contrario 2."))
# descuento_por=0
# if descuento=="1":
#     descuento_por=numproc-(numproc*0.10)
# iba=numproc+(numproc*0.19)
# print(f"total:{(numproc-descuento)+iba}")

#7.	Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.
# horas=int(input("dame las horas"))
# min=int(input("dame los minutos"))
# seg=int(input("dame los segundos"))
# print(f"La cantidad de{seg+(min*60)+((horas*60)*60)} ")

# #8.	Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 2% mensual.
# inversion=float(input("Dr, de cuanto sera su inversion?"))
# print(f"Esto retornara el 2% mensual que serian: {inversion*0.02}")

# #9.	Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y 
# comisiones.
# sueldo_base=float(input("Ingresa el sueldo base"))
# comisiones=sueldo_base*0.10
# print(f"El total es {sueldo_base} las comisiones tienen un valode de {comisiones}, en TOTAL serian: {sueldo_base+comisiones}")

#10. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
# toal=float(input("Cuanto es el total a pagar?"))
# print(f"El total a pagar es {toal-(toal*0.15)}")

#11.	Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.  Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
# 	30% de la calificación del examen final. 
#	15% de la calificación de un trabajo final
# nota_parcial=[]
# promedio1=0
# for i in range(3):
#     nota=float(input(f"Cual es tu nota #{i+1}: "))
#     nota_parcial.append(nota)
# for j in nota_parcial:
#     promedio1=promedio1+j
# promedio1=promedio1/3
# print(promedio1)
# examen_f=float(input("Cuanto sacaste en el examen final"))
# trabajo_final=float(input("Cuanto sacaste en el trabajo final"))
# print(f"El promedio de la materia fue {(promedio1*0.55)+(examen_f*0.30)+(trabajo_final*0.15)}")

# 12. Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.
# hombres=int(input("Cuantos hombres hay?\n"))
# mujeres=int(input("Cuantas mujeres hay?\n"))
# print(f"El porcentaje de hombres es {(hombres/(hombres+mujeres))*100}%")
# print(f"El porcentaje de mujeres es {(mujeres/(hombres+mujeres))*100}%")

#13. Dada las horas trabajadas de una persona y el valor por hora. Calcular su salario e imprimirlo. 
# horas=float(input("Cuantas horas trabajaste? "))
# valorxH=float(input("Que valor tiene la hora de trabajo? "))
# print(f"El salario es {horas*valorxH}")

#14. Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una 
# compra de varios artículos (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.
# tomate=5000
# leche=6000
# arepa=1500
# huevo=400
# total=0
# total_unidades=0
# objeto=int(input("MARCA\n1. para toamte\n2. para leche\n3. para arepa\n4. para huevo\n"))

# while True:
#     objeto=int(input(" "))
#     if objeto==1:
#         print(f"Tomate : {tomate}")
#         total+=tomate
#         total_unidades+=1
#     elif objeto==2:
#         print(f"Leche : {leche}")
#         total+=leche
#         total_unidades+=1
#     elif objeto==3:
#         print(f"Arepa : {arepa}")
#         total+=arepa
#         total_unidades+=1
#     elif objeto==4:
#         print(f"Huevo : {huevo}")
#         total+=huevo
#         total_unidades+=1
#     else:
#         print("saliendo de la facturacion")
#         break
# print(f"El total a pagar con iva es: {total+(total*0.19)}\nTotal de unidades es: {total_unidades}")

#15. Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por 
# cada cliente: 
#●	El monto de la venta, calcule e imprima el IVA.
#●	calcule e imprima el total a pagar 
#●	lea la cantidad con la que paga el cliente (solo efectivo), calcule e imprima el cambio. 2
def registrar_venta():
    """Registra una venta individual con cálculo de IVA y cambio"""
    
    print("\n" + "="*50)
    print("         REGISTRO DE VENTA")
    print("="*50)
    
    #Leer el monto de la venta
    while True:
        try:
            monto_venta = float(input("\nIngrese el monto de la venta: $"))
            if monto_venta < 0:
                print("Error: El monto no puede ser negativo")
                continue
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
    
    # Calcular IVA (19% en Colombia, ajusta según tu país)
    IVA_PORCENTAJE = 0.19
    iva = monto_venta * IVA_PORCENTAJE
    
    # Calcular total a pagar
    total_pagar = monto_venta + iva
    
    # Imprimir detalles de la venta
    print("\n" + "-"*50)
    print("           DETALLE DE LA VENTA")
    print("-"*50)
    print(f"Subtotal:        ${monto_venta:,.2f}")
    print(f"IVA ({IVA_PORCENTAJE*100:.0f}%):         ${iva:,.2f}")
    print(f"TOTAL A PAGAR:   ${total_pagar:,.2f}")
    print("-"*50)
    
    # Leer cantidad con la que paga el cliente
    while True:
        try:
            pago_cliente = float(input("\nCantidad con la que paga (efectivo): $"))
            if pago_cliente < 0:
                print("Error: El monto no puede ser negativo")
                continue
            if pago_cliente < total_pagar:
                print(f"Error: El pago es insuficiente. Faltan ${total_pagar - pago_cliente:,.2f}")
                continue
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
    
    # Calcular cambio
    cambio = pago_cliente - total_pagar
    
    # Imprimir cambio
    print("\n" + "-"*50)
    print(f"Pago recibido:   ${pago_cliente:,.2f}")
    print(f"CAMBIO:          ${cambio:,.2f}")
    print("-"*50)
    print("\n¡Gracias por su compra!")
    print("="*50)


def main():
    """Función principal del sistema de ventas"""
    
    print("\n╔════════════════════════════════════════════════╗")
    print("║     SISTEMA DE REGISTRO DE VENTAS - TIENDA     ║")
    print("╚════════════════════════════════════════════════╝")
    
    while True:
        registrar_venta()
        
        # Preguntar si desea registrar otra venta
        print("\n")
        otra_venta = input("¿Desea registrar otra venta? (s/n): ").lower()
        
        if otra_venta != 's':
            print("\n" + "="*50)
            print("     Gracias por usar el sistema de ventas")
            print("="*50)
            break


# Ejecutar el programa
main()



#16. Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le corresponde en un día trabajado, teniendo 
# en cuenta que tiene derecho a el 19% del total recaudado.
# recaudado=float(input("Total recaudado...:"))
# print(f"lo que te corresponde es: {recaudado*0.19} en total")

#17. Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una empresa. La colilla debe mostrar:
# ●	El Salario del Empleado 
# ●	El Valor de Ahorro mensual programado.
# ●	La suma a deducir por aporte a la Salud (EPS) 12,5 %
# ●	La suma a deducir por aporte al Fondo de Pensiones  16%
# ●	Total a Recibir 
# ●	Toda la información que debe proveer el usuario del programa es el  Salario del Empleado y el Valor de Ahorro mensual programado.
#  El programa debe calcular y devolver el resto de los datos.4

# while True:
#     salario=float(input("Cual es tu salario?"))
#     ahorro=float(input("Que porcentaje deseas ahorrar"))
#     ahorrobb=ahorro/100
#     print(f"deberias ahorrar {salario*ahorrobb} mensual")
#     pago_salud=salario*0.125
#     print(f"Debes deducir en salud un {pago_salud}")
#     pago_pension=salario*0.16
#     print(f"Tu pago de la pension debe debe de ser {pago_pension}")
#     print(f"El total a recibir es: {salario-pago_salud-pago_pension-(salario*ahorrobb)}")
#     salir=int(input("Si desea salir marque .1"))
#     if salir==1:
#         break

#18.    En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de la siguiente forma 
#●    Primera cuota: 40% 
#●    Segunda cuota: 25%
#●     Tercera cuota: 20% 
#●    Cuarta cuota: 15% 
#Diga cuanto es el valor que tiene que pagar por cuota un estudiante.

# valor_matricula = float(input("Ingrese el valor total de la matrícula: "))

# primera_cuota = valor_matricula * 0.40
# segunda_cuota = valor_matricula * 0.25
# tercera_cuota = valor_matricula * 0.20
# cuarta_cuota = valor_matricula * 0.15

# print(f"Primera cuota 40%: {primera_cuota:,.2f}")
# print(f"Segunda cuota 25%: {segunda_cuota:,.2f}")
# print(f"Tercera cuota 20%: {tercera_cuota:,.2f}")
# print(f"Cuarta cuota 15%: {cuarta_cuota:,.2f}")
# print(f"Total a pagar: ${primera_cuota + segunda_cuota + tercera_cuota + cuarta_cuota:,.2f}")
# #19) Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.  Hacer un algoritmo que:
# #Muestre el nombre
# #Muestre el programa de formación
# #Se debe calcular y mostrar su promedio final.

# nombre = input("Ingrese el nombre del estudiante: ")
# programa = input("Ingrese el programa de formación: ")
# ficha = input("Ingrese el número de ficha: ")

# nota1 = float(input("Nota 1: "))
# # nota2 = float(input("Nota 2: "))
# # nota3 = float(input("Nota 3: "))
# # nota4 = float(input("Nota 4: "))
# # nota5 = float(input("Nota 5: "))

# # promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# # print(f"Nombre: {nombre}")
# # print(f"Programa de formación: {programa}")
# # print(f"Ficha: {ficha}")
# # print(f"Promedio final: {promedio:.2f}")

# #20  Ingresar el precio de compra unitario de un producto y la cantidad de compra de dicho producto y un descuento. Calcular y
# #  mostrar el subtotal, el monto del IVA que es el 19% del subtotal, y el precio neto (precio parcial con el Monto del IVA).
# import random
# numero=random.randint(3000,10000)
# producto=str(input("Que producto deseas comprar?\n"))
# precio=float(numero)
# cantidad=int(input("    Que cantidad deseas llevar? "))
# print(f"Vas a llevar {cantidad} {producto} que tiene un sub total de {cantidad*precio} y con iba te quedaria {(cantidad*precio)+((cantidad*precio)*0.19)} ")

# #21 Realice un algoritmo que permita realizar el cálculo del siguiente enunciado, se solicita el año de nacimiento del aprendiz,
# #  el nombre, la dirección, se requiere conocer la edad de la persona y la información completa ingresada. 
# año = int(input("que año naciste?\n"))
# nombre_com=str(input("que año naciste?\n"))
# direccion=str(input("Ingresa tu direccion...\n"))
# print(f"___INFORMACION APRENDIZ___\nTu edad es {año-2025}.\nTu nombre es {nombre_com}\nTu direccion es {direccion}")

#22. Se tienen tres baldes de agua, uno de cinco litros, otros de tres litros y otro de un litro; si el de un litro tarda una hora y media en
#  llenarse, resuelva cuanto tiempo pueden tardar en llenarse los otros baldes. Si tiene tres baldes, pero se desconoce su tamaño debe de 
# resolver igualmente el ejercicio. 
''' Cada litro de agua demora un total de 1:30 horas o 90 minutos. Entonces para saber cuales baldes son debemos de saber cuanto tiempo 
se demoraron en llenarse'''
# tiempoxlitro=1.5
# baldes=[5,3,1]
# tiempoDllenado=[]
# for i in baldes:
#     tiempoDllenado.append(i*tiempoxlitro)
# print(tiempoDllenado)


#23.Una persona tarda 5 horas en subir una montaña de 7 metros, si un escalador desea subir más o menos de la montaña,
#  cuanto tiempo tarda en subir. Debe de resolver el ejercicio. 
# metros=float(input("Cuantos metros vas a subir en la montaña?"))
# hxm=(5/7)*60
# print("Te demoras un estimado de ", ((hxm*metros)/60) , " horas en subir la montaña")

#24.Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y se desea calcular la siguiente información. 
# • Cuanto dinero se ha pagado de intereses en un año. 
# • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año. 
# • Cuanto dinero se ha pagado de intereses en el primer mes. 
# • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses. 
# # Solicitar el monto del préstamo
# monto = float(input("Ingrese el monto del préstamo: "))

# Datos del préstamo
# tasa_anual = 0.05   # 5%
# plazo_anios = 5

# # Cálculos
# interes_anual = monto * tasa_anual
# interes_trimestre = interes_anual / 4   # un año tiene 4 trimestres
# interes_mes = interes_anual / 12        # un año tiene 12 meses
# interes_total = interes_anual * plazo_anios
# total_pagar = monto + interes_total

# # Resultados
# print(f"\n--- RESULTADOS ---")
# print(f"Interés pagado en un año: ${interes_anual:,.2f}")
# print(f"Interés pagado en el tercer trimestre del año: ${interes_trimestre:,.2f}")
# print(f"Interés pagado en el primer mes: ${interes_mes:,.2f}")
# print(f"Total a pagar (monto + intereses): ${total_pagar:,.2f}")





