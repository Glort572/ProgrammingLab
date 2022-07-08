# Inizializzo una lista sulla quale salvare i valori
floats = []

# Chiedo all'utente il file da aprire
print("Scegliere un file")
fileName = input()

# Apro e leggo il file, linea per linea
try:
    file = open(fileName, 'r')

except FileNotFoundError:
    # Se il file è inesistente, scrivo un messaggio d'errore
    print('FILE NON ESISTENTE: e stato digitato un nome inesistente, quindi non resta che finire il programma.')
    import sys
    from time import sleep
    sleep(3)
    sys.exit()

somma = 0
count = 0

# Iterazione fino all'ultimo valore
for line in file:

    # Separo i dati di ogni riga sulla virgola
    list_els = line.split(',')
    
    # Se NON sto processando l'intestazione...
    if list_els[0] != 'Date':

        #Imposto data e valore
        date = list_els[0]
        val = list_els[1]
        
        # Sommo ogni valore che trovo con il precedente (cambiandolo in float poiché è un carattere)
        try:
            floats.append(float(val))
        except ValueError as ve:
            # Il dato nella posizione attuale non è un numero
            count = count + 1
            print('ERRORE: Un dato non e un numero\t\tdati non chiari =',count)
        except Exception as argh:
            # Tutti gli altri tipi di errori possibili
            print('Ho avuto un problema mentre cercavo di inserire uno dei dati nella lista: "{}"'.format(argh))
        
# Iterazione dei valori nell'insieme "floats"
for item in floats:
    # Sommo i valori
    somma += item

# Restituisco la somma
print(somma)
