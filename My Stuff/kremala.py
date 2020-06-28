# _*_ coding: utf-8 -*-

#ΔΕΝ ΛΕΙΤΟΥΡΓΕΙ ΜΕ ΤΑ ΕΛΛΗΝΙΚΑ ΠΡΟΣ ΤΟ ΠΑΡΟΝ

pavles = []
grammataPouPaixtikan = []
lathos_lekseis = []
clear = '\n' * 100
arithmosLathon = 0
kerdises = False
settingLathi = 8

def display():
    print(clear)
    if arithmosLathon == 8:
        print('_______ ')
        print('|     | ')
        print('|    _O_')
        print('|     | ')
        print('|    | |')
        print('|       ')
    elif arithmosLathon == 7:
        print('_______ ')
        print('|     | ')
        print('|    _O_')
        print('|     | ')
        print('|    |  ')
        print('|       ')
    elif arithmosLathon == 6:
        print('______  ')
        print('|     | ')
        print('|    _O_')
        print('|     | ')
        print('|       ')
        print('|       ')
    elif arithmosLathon == 5:
        print('_______ ')
        print('|     | ')
        print('|    _O_')
        print('|       ')
        print('|       ')
        print('|       ')
    elif arithmosLathon == 4:
        print('_______ ')
        print('|     | ')
        print('|    _O ')
        print('|       ')
        print('|       ')
        print('|       ')
    elif arithmosLathon == 3:
        print('_______  ')
        print('|     | ')
        print('|     O ')
        print('|       ')
        print('|       ')
        print('|       ')
    elif arithmosLathon == 2:
        print('_______ ')
        print('|     | ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|      ')
    elif arithmosLathon == 1:
        print('        ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|       ')
    elif arithmosLathon == 0:
        print('        ')
        print('        ')
        print('        ')
        print('        ')
        print('        ')
        print('|       ')
    print('')
    print(pavles)
    print('')
    print('Λάθος γράμματα: ' + str(grammataPouPaixtikan))
    print('')
    print('Λάθος λέξεις: ' + str(lathos_lekseis))

print(clear)
leksi = input('Δώσε λέξη: ')
leksiCaps = leksi.upper()
grammataLeksis = list(leksiCaps)

for i in range(len(grammataLeksis)):
    pavles.append('_')

display()

while arithmosLathon < settingLathi and kerdises != True:
    print('')
    mantepsia = input('Δώσε γράμμα ή λέξη: ')
    mantepsiaCaps = mantepsia.upper()

    #elegxos an dothike gramma h leksh
    if len(mantepsiaCaps) > 1:
        if mantepsiaCaps == leksiCaps:
            for i in range(0, len(grammataLeksis)):
                pavles[i] = grammataLeksis[i]
                kerdises = True
            display()
        else:
            arithmosLathon += 1
            lathos_lekseis.append(mantepsiaCaps)
            display()
            print('')
            print('--------> Η λέξη που έδωσες είναι λάθος <--------')
    else:
        #an mantepsei swsta ena gramma
        if mantepsiaCaps in grammataLeksis:
            for i in range(0, len(grammataLeksis)):
                if mantepsiaCaps == grammataLeksis[i]:
                    pavles[i] = grammataLeksis[i]
            display()
        #an exeis ksanapaiksei to idio lathos gramma
        elif mantepsiaCaps in grammataPouPaixtikan:
            display()
            print("Έχεις δώσει ήδη το ίδιο γράμμα " + mantepsiaCaps)
        #an paikseis kainourgio lathos gramma
        else:
            arithmosLathon += 1
            grammataPouPaixtikan.append(mantepsiaCaps)
            display()
            print('')
            print('--------> Δεν υπάρχει το γράμμα στη λέξη <--------')
        #elexos an nikises
        if pavles == grammataLeksis:
            kerdises = 1

if kerdises == True:
    display()
    print('')
    print('')
    print('         ΜΠΡΑΒΟ ΚΕΡΔΙΣΕΣ!!!!!        ')
    print('')
    print('')
else:
    display()
    print('ΕΧΑΣΕΣ ΧΑΧΑΧΑΑΧΑΧ')
    print('')
    print('Η λέξη είναι: ')
    print(grammataLeksis)
