# Questo è un programma inutile creato per witz che manda in output il nome di un artista in <my_list> e un suo brano in <our_tracks>. Ovviamente dev'esserci un ordine numerico con le colonne.


my_list = ['Glort', 'LeSlovak', 'Mesney6']
our_tracks = ['Night At The Reactor', 'Underground', 'Owl']

n=0;                                                        # Questa variabile va a finire nelle istruzioni di output riportate qua sotto e comincia dal primo artista e dalla prima traccia.

print('{} - {}'.format(my_list[n],our_tracks[n]))           # automazione (primo artista e prima traccia)
print('{} - {}'.format(my_list[n+1],our_tracks[n+1]))       # automazione (secondo artista e seconda traccia)
print('{} - {}'.format(my_list[n+2],our_tracks[n+2]))          # automazione (terzo artista e terza traccia)


print('\n\n')

if 'Glort' in my_list:
    print('I found the best producer ever!\n')

if 'Mesney6' in my_list:
    print(our_tracks[n+3-1])