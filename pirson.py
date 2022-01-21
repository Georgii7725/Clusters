def getAverages(mass: list):
    aver = 0
    for el in mass:
        aver += el
    aver = round(aver / len(mass), 2) 
    return aver

def getMassElements(mass: list, aver: float):
    for i in range(len(mass)):
        mass[i] = mass[i] - aver
    return mass

def getNumerator(mass1: list, mass2: list):
    numerator = 0
    for i in range(len(mass1)):
        numerator += mass1[i] * mass2[i]  
    return numerator

def getDenominator(mass1: list, mass2: list):
    denominator = 1
    sum1 = 0
    sum2 = 0
    for i in range(len(mass1)):
        sum1 += mass1[i]**2
        sum2 += mass2[i]**2
    denominator = round((sum1*sum2)**0.5, 3)
    return denominator

def get_KKP(mass1: list, mass2: list):
    first_one = mass1.copy()
    second_one = mass2.copy()
    faver = getAverages(first_one)
    saver = getAverages(second_one)
    first_one = getMassElements(first_one, faver)
    second_one = getMassElements(second_one, saver)
    KKP = getNumerator(first_one, second_one) / getDenominator(first_one, second_one)
    return KKP

mass1 = [1, 2, 10]
mass2 = [10, 9, 3]
print(get_KKP(mass1, mass2))