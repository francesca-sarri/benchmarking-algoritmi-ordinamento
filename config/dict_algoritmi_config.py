# Importazione classe di configurazione ALGORITMI
from config.alg_config import AlgConfig

# Importazione ALGORITMI del progetto
from algoritmi.quicksort import quicksort
from algoritmi.quicksort_3way import quicksort_3way
from algoritmi.countingsort import counting_sort
from algoritmi.introsort import intro_sort

"""
    DIZIONARIO DI ALGORITMI
    Questa è una struttura dati fondamentale per avere un'unica funzione in grado di calcolare il benchmark per un 
    numero indefinito di algoritmi, purché opportunamente inseriti in questo dizionario. Essa è strettamente legata alla
    classe AlgConfig, infatti ciascuna chiave è un oggetto di questa classe.
    Vengono considerati dinamici i seguenti parametri:
        - func = la funzione che implementa l'algoritmo vero e proprio, ovviamente varia a seconda dell'algoritmo.
        - nome = il nome dell'algoritmo serve per la creazione di un grafico personalizzato, avente il nome 
                 dell'algoritmo analizzato.
        - color = il colore dell'algoritmo analizzato varia, per distinguere le linee nel caso di un grafico comparativo
        - arg = gli argomenti da inserire all'interno della funzione (func) sono dinamici, nel nostro caso in QuickSort
                e QuickSort 3-Way.
                Quando viene chiamato oggetto.get_args(arr) verrà restituita la tupla corrispondente all'algoritmo. 
                
"""

# Funzioni per la preparazione degli argomenti in base all'algoritmo
# Valore ritornato: Tuple

def set_quicksort_args(arr):                                        # Vale anche per QuickSort 3-Way
    return (0, len(arr) - 1)                                        # Tuple[0, len(arr) - 1]

def set_no_args(arr):
    return ()                                                       # Tuple[] (vuota)

### Dizionario con scopo globale del progetto ###

ALGORITMI_CONFIG = {
    "CountingSort": AlgConfig(func=counting_sort, nome="CountingSort", color="xkcd:sky blue",
                              arg=set_no_args),
    "QuickSort": AlgConfig(func=quicksort, nome="QuickSort", color="xkcd:orange", arg=set_quicksort_args),
    "QuickSort 3-Way": AlgConfig(func=quicksort_3way, nome="QuickSort 3-Way", color="xkcd:light green",
                                 arg=set_quicksort_args),
    "IntroSort": AlgConfig(func=intro_sort, nome="IntroSort", color="xkcd:purple", arg=set_no_args),
}


