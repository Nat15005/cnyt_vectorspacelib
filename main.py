import numpy as np

#FUNCIONES NECESARIAS PARA HACER LA NUEVA LIBRERÍA

# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)

#Conjuga números complejos
def concplx (n):
    real = (n[0])
    img = ((n[1])*(-1))
    return (real, img)


#SEGUNDA LIBRERÍA


#Adición vectores complejos

def adicionVectrs(v1,v2):
    sumavector = []
    c = 0
    while c < len(v1):
        sumav = sumacplx((v1[c]), (v2[c]))
        sumavector.append(sumav)
        c += 1
    print (sumavector)

#Inverso aditivo Vector

def inversoAditivoVec(v1):
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            v1[i][j] = (v1[i][j][0] * (-1),  v1[i][j][1] * (-1))
    print(v1)

#Multiplicación Escalar

def multiplicacionEscalar(v1, c):
    v = []
    for i in range(len(v1)):
        multi = multcplx(v1[i], c)
        v.append(multi)
    print(v)

#Adición de matrices

def adicionMatrices (m1,m2):
    sumamtrx = []
    c = 0
    while c < len(m1):
        sumaM = sumacplx((m1[c]), (m2[c]))
        sumamtrx.append(sumaM)
        c += 1
    print(sumamtrx)

#Inverso aditivo matrices

def inversoaditivoMtx (m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = ((-1) * m1[i][j][0], (-1) * m1[i][j][1])
    print (m1)

#multiplicación escalar de matrices

def multiplicacionEscalarMtrx(m1, v1):
    for i in range(len(m1)):
        for j in range(2):
            mltplxmat = multcplx(m1[i][j], v1)
            m1[i][j] = mltplxmat

    print(m1)

#Traspuesta de una matriz/vector

def Traspuesta(m1):
    result = [[0 for i in range(len(m1))] for j in range(len(m1[0]))]

    for i in range(len(m1[0])):
        for j in range(len(m1)):
            result[i][j] = m1[j][i]

    return(result)

#conjugada de una Matriz o un vector

def conjugarMtrx (m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = (m1[i][j][0], (-1) * m1[i][j][1])
    return (m1)

#Daga de una Matriz o un vector

def dagaMtrz (m1):
    m = Traspuesta(m1)
    n = conjugarMtrx(m)
    return (n)

#Producto de 2 matrices nxn
def productoMtrx (m1, m2):
    mtplx = [[None for j in range(len(m1))] for i in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            aux = (0, 0)
            for k in range(len(m2)):
                component1, component2 = m2[k][j], m1[i][k]

                aux = sumacplx(aux, multcplx(component1, component2))
            mtplx[i][j] = aux
    print(mtplx)

#Acción de una matriz sobre un vector

def accion_matriz(m1,v1):
    accion = [[None for j in range(len(m1))] for i in range(len(v1[0]))]
    for i in range(len(m1)):
        for j in range(len(v1[0])):
            aux = (0, 0)
            for k in range(len(v1)):
                component1  = v1[k][j]
                component2 = m1[i][k]
                aux = sumacplx(aux, multcplx(component1, component2))
            accion[i][j] = aux
    return(accion)

#Producto Interno de vectores

def producto_Int(v1, v2):
    Inner_productVec = 0
    for i in range(len(v1)):
        Inner_productVec += (v1[i] * v2[i])
    print(Inner_productVec)

#Norma de un vector

def Norma_v(v1):
    norma = np.linalg.norm(v1)
    print (norma)

#Distancia entre dos vectores

def distance_v(v1, v2):
    real = v1[0] - v2[0]
    img = v1[1] - v2[1]
    v = (real, img)
    distance = np.linalg.norm(v)

    print (distance)


#Revisar si una matriz unitaria

def unitaria(m1):
    Trx = Traspuesta(m1[:])
    result = Trx == m1
    if result == False:
        return ('No es unitaria')
    else:
        return ('Es unitaria')

#Revisar si una matriz es hermitiana
def hermitiana(m1):
    daga = dagaMtrz(m1[:])
    result = daga == m1
    if result == False:
        return ('No es hermitiana')
    else:
        return ('Es hermitiana')

#Producto Tensor
def productoTrsx(m1,m2):
    s = len(m1[0])*len(m2[0])
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=multiplicacionEscalarMtrx(m1[i][j],m2)
    for i in m1:
        return(i)

'''-------------------------------------------------------------------------'''


#PRUEBAS

adicionVectrs([(1,2),(1,1)],[(3,1),(1,3)])
inversoAditivoVec([[(4, 5), (7, 2), (3, 2)]])
multiplicacionEscalar([(6, 3), (0, 0), (5, 1), (4, 0)], (3, 2))
adicionMatrices ([(1,5),(1,1)],[(6,1),(1,4)])
inversoaditivoMtx ([[(2, 3), (4, 4), (1, 2)], [(1, 1), (1, -8), (5, 4)]])
multiplicacionEscalarMtrx ([[(8, 4), (5, 3)],[(8, 4), (5, 3)]], (2, 3))
print(Traspuesta([[(8, 4), (5, 3)], [(6, 7), (9, 2)]]))
print(conjugarMtrx([[(1,5),(1,1)],[(6,1),(1,4)]]))
print(dagaMtrz ([[(1,5),(1,1)],[(6,1),(1,4)]]))
productoMtrx([[(5, 3), (7, 1), (9, -2)], [(0, 5), (3, 6), (1, 1)], [(-4, 6), (3, 9), (3, 6)]], [[(3, 4), (6, 2), (-76, -5)], [(5, 0), (3, 6), (2, 7)], [(7, -3), (5, 2), (6, 0)]])
print(accion_matriz([[(7, 2), (1, 1), (2, -2)], [(2, 5), (5, 6), (1, 7)], [(-4, 7), (2, 11), (9, 11)]], [[(12, 4), (8, 2), (-1, -4)], [(5, 5), (6, 2), (1, 7)], [(2, 4), (6, 1), (6, 0)]]))
producto_Int([6, 2, 11],[-5, -7, 1])
Norma_v((1,2))
distance_v((1,2), (3,4))
print (unitaria([[(3,4), (1,2)]]))
print (hermitiana([[(1,2), (3,4)]]))
adicionVectrs([(-2,3),(5,-6)],[(4,-8),(9,2)])
inversoAditivoVec([[(4, 3), (2, 1), (6, 3)]])
multiplicacionEscalar([(4, 1), (1, 1), (-7, -4), (3, 5)], (6, -1))
adicionMatrices ([(4,3),(-2,5)],[(10,2),(3,5)])
inversoaditivoMtx ([[(1, 6), (3, 2), (4, 1)], [(-1, -3), (5, -6), (3, 7)]])
multiplicacionEscalarMtrx ([[(5, 3), (7, 1)],[(2, 6), (3, 3)]], (-2, 1))
print(Traspuesta([[(6, 3), (4, 1)], [(5, 2), (1, 1)]]))
print(conjugarMtrx([[(8,4),(3,1)],[(4,2),(2,3)]]))
print(dagaMtrz ([[(5,5),(2,2)],[(1,4),(11,3)]]))
productoMtrx([[(15,33), (5, 2), (5, -5)], [(1, 0), (39, 8), (14, 0)], [(-3, -5), (2, 4), (1, 3)]], [[(3, 5), (9, 2), (-6, -15)], [(3, 4), (3, 4), (4, 2)], [(5, 3), (6, 1), (6, 2)]])
print(accion_matriz([[(4, 2), (3, 11), (2, -2)], [(4, 6), (5, 3), (3, 7)], [(-4, 6), (2, 1), (9, 3)]], [[(1, 6), (5, 2), (-1, -4)], [(4, 6), (6, 2), (1, 6)], [(2, 4), (6, 1), (6, 2)]]))
producto_Int([5, 6, 1],[-4, -6, 12])
Norma_v((13,4))
distance_v((3,4), (1,1))
print (unitaria([[(-3,3), (5,7)]]))
print (hermitiana([[(1,6), (4,4)]]))
productoMtrx([[(5, 6), (10, 2), (4, -4)], [(3, 8), (3, 1), (6, 8)], [(-5, 11), (8, 3), (4, 7)]], [[(4, 1), (8, 1), (-6, -15)], [(25, 4), (13, 5), (2, 17)], [(57, -3), (15, 12), (6, 1)]])