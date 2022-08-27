import numpy as np

# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

#Resta números complejos representados como una tupla (real, imaginaria)
def restacplx(a,b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real, img)

# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)

#Divide números complejos representados como una tupla
def divcplx(a,b,):
    denominador = ((a[1])**2 + (b[1])**2)
    numerador1 = ((a[0]*a[1])+(b[0]*b[1]))
    numerador2 = ((a[1]*b[0])-(a[0]*b[1]))
    real = numerador1/denominador
    img = numerador2/denominador
    return (real, img)

#Conjuga números complejos
def concplx (n):
    real = (n[0])
    img = ((n[1])*(-1))
    return (real, img)

#Saca el módulo de un número complejo
def modulcmplx(n):
    modulo = ((n[0])**2+(n[1])**2)**(0.5)
    return modulo

#Convierte de cartesiano a polar
def toPolar(c):
    theta = np.arctan2(c[1],c[0])
    rho = np.sqrt((c[0] * c[0]) + (c[1] * c[1]))
    return (rho, theta)

#Convierte de polar a cartesiano representados como una tupla (rho, theta)
def toCartesiano(n):
    real = ((n[0])*np.cos(n[1]))
    img = ((n[0])*np.sin(n[1]))
    return (real,img)

#Retorna la fase de un número complejo
def phase(n):
    theta = np.arctan2(n[1], n[0])
    return theta

def prettyprinting(c):
    #Para cartesianos
    print( str(c[0]) + " + " + str(c[1]) + "i")
def polprettyprinting(c):
    #Para polares
    print( str(c[0]) + " e^(i " + str(c[1]) + ")")
def prettyprentingmod(c):
    print (round(c,3))

#PRUEBAS SUMA
prettyprinting(sumacplx((5,4),(6,3)))
prettyprinting(sumacplx((-5,4),(6,-3)))
prettyprinting(sumacplx((-6,-3),(-8,-7)))
prettyprinting(sumacplx((2,-4),(9,-7)))

#PRUEBAS PRODUCTO
prettyprinting(multcplx((2,3),(4,7)))
prettyprinting(multcplx((-3,3),(-6,2)))
prettyprinting(multcplx((-8,-9),(-6,-1)))
prettyprinting(multcplx((-3,-3),(4,-5)))

#PRUBAS RESTA
prettyprinting(restacplx((4,3),(5,6)))
prettyprinting(restacplx((-5,-5),(-9,-2)))
prettyprinting(restacplx((0,1),(-4,2)))
prettyprinting(restacplx((-3,4),(5,-7)))

#PRUEBAS DIVISIÓN
prettyprinting(divcplx((-2,1),(1,2)))
prettyprinting(divcplx((2,1),(4,3)))
prettyprinting(divcplx((3,-2),(5,-6)))
prettyprinting(divcplx((-2,-1),(-1,-2)))

#PRUEBAS MODULO
prettyprentingmod(modulcmplx((1,-1)))
prettyprentingmod(modulcmplx((2,-3)))
prettyprentingmod(modulcmplx((4,-1)))
prettyprentingmod(modulcmplx((-4,-3)))

#PRUEBAS CONJUGADO
prettyprinting(concplx((-3,4)))
prettyprinting(concplx((5,-8)))
prettyprinting(concplx((6,-11)))
prettyprinting(concplx((-3,-5)))

#Prueba polares
polprettyprinting(toPolar((-3,-2)))
polprettyprinting(toPolar((5,-8)))
polprettyprinting(toPolar((2,2)))
polprettyprinting(toPolar((-3,-7)))

#PRUEBA A CARTESIANOS
prettyprinting(toCartesiano((3,(np.pi/3))))
prettyprinting(toCartesiano((4,(np.pi/6))))
prettyprinting(toCartesiano((2,(np.pi/5))))

#RETORNAR FASE
prettyprentingmod(phase((3,(np.pi))))
prettyprentingmod(phase((4,((np.pi)/2))))
prettyprentingmod(phase((2,(np.pi))))
