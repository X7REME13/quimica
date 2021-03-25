
def main():
    orbitalS = [0, 0]
    orbitalP = [0, 0, 0, 0, 0, 0]
    orbitalD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    orbitalF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    orbitalesLlenosS = [0]
    orbitalesLlenosP = [1]
    orbitalesLlenosD = [2]
    orbitalesLlenosF = [3]
    cant_Electrones = int(input("Ingrese la cantidad de electrones del átomo: "))
    tanda = 0
    nomore = True
    electronesRestantes = cant_Electrones


    while electronesRestantes > 0:
        if tanda == 0:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)
        elif tanda == 1:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)
        elif tanda == 2:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)

        elif tanda == 3:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)
        elif tanda == 4:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalD, orbitalesLlenosD)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)
        elif tanda == 5:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalD, orbitalesLlenosD)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)
        elif tanda == 6:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalF, orbitalesLlenosF)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalD, orbitalesLlenosD)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalS, orbitalesLlenosS)

        elif tanda == 7:
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalF, orbitalesLlenosF)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalD, orbitalesLlenosD)
            electronesRestantes = aumentarOrbi(electronesRestantes, orbitalP, orbitalesLlenosP)

        elif tanda > 7:
            electronesRestantes = -1

        tanda += 1

    
    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 0, "S")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 1, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 1, "P")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 2, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 2, "P")
    imprimirOrbital(orbitalD, orbitalesLlenosD, 2, "D")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 3, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 3, "P")
    imprimirOrbital(orbitalD, orbitalesLlenosD, 3, "D")
    imprimirOrbital(orbitalF, orbitalesLlenosF, 3, "F")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 4, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 4, "P")
    imprimirOrbital(orbitalD, orbitalesLlenosD, 4, "D")
    imprimirOrbital(orbitalF, orbitalesLlenosF, 4, "F")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 5, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 5, "P")
    imprimirOrbital(orbitalD, orbitalesLlenosD, 5, "D")

    print(end="\n")
    imprimirOrbital(orbitalS, orbitalesLlenosS, 6, "S")
    imprimirOrbital(orbitalP, orbitalesLlenosP, 6, "P")

def imprimirOrbital(orbital, orbitalesLlenos, tanda, letra):
    if tanda < orbitalesLlenos[0]:
        print(tanda + 1, letra.lower(), "^", len(orbital), end=" | ")
    elif orbital[0] != 0:
        print(tanda + 1, letra.lower(),"^", sumalista(orbital), end=" | ")
        orbital[0]=0

def aumentarOrbi(electronesRestantes, orbital, orbitalesLlenos):
    for i in range(len(orbital)):
        if electronesRestantes > 0:
            orbital[i] = 1
            electronesRestantes -= 1
        else:
            orbital[i] = 0
    if orbital[-1] == 1:
        orbital[0] = 0
        orbitalesLlenos[0] += 1

    return electronesRestantes

def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

if __name__ == '__main__':
    main()
    input()