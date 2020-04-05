import random
arithmoi = [i for i in range(1, 45)]
tzoker = [i for i in range(1, 20)]

def epilogiArithmon(plithos):
    plithosArithmon = list(arithmoi)
    epilogi = []
    for i in range(plithos):
        epilegmeno = random.randint(0, len(plithosArithmon))
        epilogi.append(plithosArithmon[epilegmeno])
        plithosArithmon.pop(epilegmeno)

    for i in range(1, len(epilogi), 1):
        for j in range(len(epilogi)-1, i-1, -1):
            if epilogi[j] < epilogi[j-1]:
                epilogi[j], epilogi[j-1] = epilogi[j-1], epilogi[j]

    return epilogi

def epilogiTzoker(plithos):
    plithosTzoker = list(tzoker)
    epilogi = []
    for i in range(plithos):
        epilegmeno = random.randint(0, len(tzoker))
        epilogi.append(plithosTzoker[epilegmeno])
        plithosTzoker.pop(epilegmeno)

    for i in range(1, len(epilogi), 1):
        for j in range(len(epilogi)-1, i-1, -1):
            if epilogi[j] < epilogi[j-1]:
                epilogi[j], epilogi[j-1] = epilogi[j-1], epilogi[j]

    return epilogi

def deltia(arithmosdeltion):
    for i in range(arithmosdeltion):
        plithosepilogon = int(input('Posous arithmous epilegeis: '))
        plithostzoker = int(input('Posous arithmous tzoker epilegeis: '))
        arithmoi = epilogiArithmon(plithosepilogon)
        tzoker = epilogiTzoker(plithostzoker)
        print(str(i+1) + 'o deltio: Arithmoi: ' + str(arithmoi) + ' tzoker: '+ str(tzoker))

plithosdeltion = int(input('Posa deltia theleis na valeis: '))
deltia(plithosdeltion)
