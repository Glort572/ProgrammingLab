# Inizializzo una lista sulla quale salvare i valori
floats = []

# Apro e leggo il file, linea per linea
file = open("shampoo_sales.csv", 'r')

sum = 0

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
        floats.append(float(val))
        
# Iterazione dei valori nell'insieme "floats"
for item in floats:
    # Sommo i valori
    sum += item

# Restituisco la somma
print(sum)
