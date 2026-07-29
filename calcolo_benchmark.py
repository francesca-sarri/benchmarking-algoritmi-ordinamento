import csv
import random
import time

from alg_config import BenchmarkConfig

### STIMA RISOLUZIONE CLOCK ###

"""

    Calcolo risoluzione del clock: resolution()
    Misura la più piccola differenza di tempo che il sistema operativo può misurare.
    Il valore che si ottiene può variare a seconda del sistema operativo e dell'hardware 
    su cui viene eseguito il codice.
    
"""

def resolution():
    start = time.perf_counter()                # Restituisce il valore di tempo attuale ad alta risoluzione (per brevi intervalli di tempo)
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()

    return stop - start


### CREAZIONE ARRAY CASUALE ###

"""
    Creazione dell'array CASUALE: inizializza_vettore(...)
    Questa funzione ha l'intento di inizializzare un vettore con n numeri pseudocasuali, dove 
    gli estremi sono inclusi. Mentre il valore m indica il valore massimo che ogni elemento può assumere, nello
    specifico il range di valori è compreso tra (1, m), estremi inclusi.

"""

def inizializza_vettore(n, m):
    return [random.randint(1, m) for _ in range(n)]

"""
    Calcolo del tempo medio di inizializzazione dell'array casuale: misura_tempo_init(...)
    Questa funzione permette di calcolare quanto mediamente ci impiega a creare il vettore casuale, eseguendo 
    l'operazione in un ciclo per un periodo di tempo minimo prestabilito. 
"""

### CALCOLO TEMPO MEDIO INIZIALIZZAZIONE ARRAY CASUALE ###

def misura_tempo_init(n, m, min_time):
    count = 0
    start_time = time.perf_counter()                                # Misura il tempo prima dell'esecuzione

    while True:
        a = inizializza_vettore(n, m)                               # Genera un nuovo array
        count += 1

        end_time = time.perf_counter()                              # Misura il tempo dopo l'esecuzione

        # Calcola il tempo trascorso totale dal momento in cui è partito start_time.
        current_time = end_time - start_time

        # Se il tempo trascorso complessivo è maggiore o uguale a min_time, interrompi.
        if current_time >= min_time:
            break

    return current_time / count


### TEMPO MEDIO DI ESECUZIONE ###

"""

    Calcolo del tempo medio di esecuzione: misura_tempo_medio(...)
    La seguente funzione serve a calcolare quanto tempo impiega mediamente un algoritmo a processare array di una 
    determinata dimensione, escludendo il tempo necessario per inizializzare i dati di test.
    
"""

def misura_tempo_medio(dim_array, range_val, min_time, alg_config):
    count = 0

    # Calcolo del tempo di inizializzazione del vettore pseudocasuale
    avg_init_time = misura_tempo_init(dim_array, range_val, min_time)

    start_time = time.perf_counter()                                        # Misura il tempo prima dell'esecuzione

    while True:
        a = inizializza_vettore(dim_array, range_val)                       # Genera array pseudocasuale

        args = alg_config.get_args(a)                               # Ricavo degli argomenti necessari per l'algoritmo
        alg_config.func(a, *args)                                   # Esecuzione dell'algoritmo scelto

        count += 1

        end_time = time.perf_counter()                      # Misura il tempo dopo l'esecuzione

        # Calcola il tempo trascorso totale dal momento in cui è partito start_time.
        current_time = end_time - start_time

        # Se il tempo trascorso complessivo è maggiore o uguale a min_time, interrompi.
        if current_time >= min_time:
            break

    return current_time / count - avg_init_time

"""

    FUNZIONE PRINCIPALE del calcolo benchmark: esegui_benchmark(...)
    Questa funzione permette di misurare il tempo di esecuzione medio dell'algoritmo scelto, o meglio passato come
    parametro alla funzione come oggetto alg_config. Il tempo di esecuzione varia a seconda di un parametro variabile 
    (ovvero n o m), dove vengono creati 250 CAMPIONI, nonché i punti che si possono vedere nei grafici finali. Quindi,
    un punto non è altro che (n/m, tempo medio).
    Inoltre, per catturare il comportamento dell'algoritmo sia per valori piccoli che grandi e in modo tale da avere
    una distribuzione uniforme quando viene visualizzata in scala logaritmica, viene utilizzata la progressione
    geometrica (molto più efficiente della progressione lineare).
    
"""

def esegui_benchmark(min_val, max_val, fixed_val, alg_config, param_variabile):
    # Calcola il tempo minimo misurabile T_min per garantire l'errore relativo E
    R = resolution()
    min_time = R * ((1 / BenchmarkConfig.ERRORE_RELATIVO) + 1)

    # Progressione GEOMETRICA
    A = min_val
    B = (max_val / min_val) ** (1 / (BenchmarkConfig.NUM_CAMPIONI - 1))

    # Generazione dei campioni n / m
    campioni_generati = [round(A * (B ** i)) for i in range(BenchmarkConfig.NUM_CAMPIONI)]

    # Misura il tempo medio per ogni dimensione
    tempi_medi_finali = []

    # Itero sull'elemento corrente (n / m) per misurare il corrispondente tempo medio.
    for curr_val in campioni_generati:
        somma_tempi = 0

        # Per ogni n / m svolgo N_RIPETIZIONI
        for _ in range(BenchmarkConfig.N_RIPETIZIONI):
            if param_variabile == 'n':
                tempo_singola_misurazione = misura_tempo_medio(curr_val, fixed_val, min_time, alg_config)

            else:  # param_variabile == 'm'
                tempo_singola_misurazione = misura_tempo_medio(fixed_val, curr_val, min_time,
                                                               alg_config)
            somma_tempi += tempo_singola_misurazione

        media = somma_tempi / BenchmarkConfig.N_RIPETIZIONI

        # Stampa della coppia (n / m, tempo medio)
        tempi_medi_finali.append((curr_val, media))
        print(f"{param_variabile} = {curr_val}, Tempo medio (su {BenchmarkConfig.N_RIPETIZIONI} runs) = {media:.6f} secondi")

    # Ritorno della List[Tuple[int, int]] con al suo interno la coppia (n / m, tempo medio)
    return tempi_medi_finali


"""

    La funzione 'salva_tempi_csv' salva i tempi medi finali in un file CSV con un nome di file dinamico.
    
    Per poter salvare i dati è necessario settare il flag AVVIO_BENCHMARK = TRUE.
    
"""

def salva_tempi_csv(nome_alg, benchmark_tipo, tempi_medi_finali):
    # Creazione del nome file dinamico
    nome_file = f"{nome_alg.lower().replace(' ', '_')}_{benchmark_tipo}_benchmark.csv"

    # Il file verrà creato all'interno della cartella del progetto
    # Apertura file in scrittura
    with open(nome_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['valore_input', 'tempo_medio'])                        # Intestazione che compare nel file
        writer.writerows(tempi_medi_finali)                                     # Scrittura dati

    print(f"Tempi medi finali salvati su {nome_file}")

"""

    La funzione carica_tempi_csv(...) carica i tempi medi finali da un file CSV già esistente, all'interno di una lista 
    di tuple (List[Tuple[int, int]]).
    
    Per poter caricare i dati è necessario settare il flag AVVIO_BENCHMARK = FALSE.

"""

def carica_tempi_csv(nome_alg, benchmark_tipo):
    # Creazione nome file dinamico
    nome_file = f"{nome_alg.lower().replace(' ', '_')}_{benchmark_tipo}_benchmark.csv"

    tempi_medi_finali = []

    # Apriamo in lettura il file da caricare (corrispondente all'algoritmo scelto)
    with open(nome_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)                                                    # Riga di intestazione saltata

        # Leggo riga per riga
        for riga in reader:
            param_variabile = int(riga[0])                              # Parametro variabile: n o m
            tempo_medio = float(riga[1])                                # Tempo medio di quel n o m
            tempi_medi_finali.append((param_variabile, tempo_medio))

    print(f"Tempi medi finali caricati da {nome_file}.")

    return tempi_medi_finali


