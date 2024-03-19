import os
os.system('cls')
Odontologia = 0
Ginecologia = 0
consulta_gnr = 0
Maternidad = 0
Infancia = 0

sw = True

def fnt_selector  (opcionInt):
    if  opcionInt <= 0 or opcionInt >= 8:
        print('Seleccione una opción valida')
    if(opcionInt==1):
        global Odontologia
        Odontologia += 1
        
    if opcionInt ==2:
        global Ginecologia
        Ginecologia += 1

    if  opcionInt ==3 :
        global consulta_gnr
        consulta_gnr += 1

    if opcionInt ==4:
        global Maternidad 
        Maternidad+= 1
    
    if opcionInt==5:    
        global Infancia 
        Infancia += 1
    if opcionInt == 6:
        fnt_reporte()

def fnt_reporte():
        print()
        print('            <<< REPORTE >>>')
        print('La cantidad de registros en odontologia fue:          ',Odontologia)
        print('La cantidad de registros en Ginecologia fue:          ',Ginecologia)
        print('La cantidad de registros en Consulta general fue:     ',   consulta_gnr)
        print('La cantidad de registros en Maternidad fue:           ',Maternidad)
        print('La cantidad de registros en Infancia fue:             ',Infancia)



while sw == True:
    import os
    opcionInt = int(input('\n<<< SELECCIONE SU TIPO DE CITA >>>\n\n1. Odontologia\n2. Ginecologia\n3. Consulta general\n4. Maternidad\n5. Infancia\n6. Generar Reporte\n7. FINALIZAR\n--> '))
    os.system('cls')
    fnt_selector(opcionInt)
    if  opcionInt <= 0 or opcionInt >= 8:
        print('Seleccione una opción valida')
        
    if opcionInt == 6:
        sw == False
    if opcionInt == 7:
        print('            <<< REPORTE FINAL >>>')
        print('La cantidad de registros en odontologia fue:          ',Odontologia)
        print('La cantidad de registros en Ginecologia fue:          ',Ginecologia)
        print('La cantidad de registros en Consulta general fue:     ',   consulta_gnr)
        print('La cantidad de registros en Maternidad fue:           ',Maternidad)
        print('La cantidad de registros en Infancia fue:             ',Infancia)
        print('PROGRAMA FINALIZADO')
         
        break



