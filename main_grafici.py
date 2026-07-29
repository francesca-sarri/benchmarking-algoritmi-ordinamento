import random

# Impostazione limite ricorsivo per gli algoritmi RICORSIVI (Quicksort / Quicksort 3-Way)
import sys
sys.setrecursionlimit(100000)

# Importazione funzione per il PLOTTING dei grafici
from plotter_grafici import compare_plot_algoritmi

"""

    PANNELLO DI AVVIO: main()
    Nel main sono presenti le linee di codice che permettono di creare i grafici:
        - in forma lineare
        - in forma doppiamente logaritmica
    degli algoritmi richiesti dalla consegna (QuickSort, QuickSort 3-Way e CountingSort) e l'algoritmo a scelta
    (IntroSort).
    
    (*) Si hanno sia i grafici singoli (in funzione di n/m) che quelli di confronto; verranno descritti con precisione
        nella relazione.
        
    Nel seguente pannello è possibile creare sia grafici singoli che comparativi, mediante la funzione principale 
    compare_plot_algoritmi(...) (presente nel file plotter_grafici.py), gestendo tramite un vettore il tipo di algoritmi
    es. ["QuickSort", "QuickSort 3-Way", "CountingSort"] che si vogliono inserire nel grafico.
    
          
    NOTA:
    - IN FUNZIONE DI N: n = 100 a n = 100'000   | m = 100'000 (fisso)
    - IN FUNZIONE DI M: m = 10 a  m = 1'000'000 | n = 10'000 (fisso)

"""


### MAIN: AVVIO PRINCIPALE DEL PROGRAMMA ###

def main():
    # Grafici SINGOLI: in funzione di n (lineare)
    compare_plot_algoritmi(100, 100000, ["QuickSort"], 100000)  #
    compare_plot_algoritmi(100, 100000, ["CountingSort"], 100000)  #
    compare_plot_algoritmi(100, 100000, ["QuickSort 3-Way"], 100000)  #
    compare_plot_algoritmi(100, 100000, ["IntroSort"], 100000)  #

    # Grafici SINGOLI: in funzione di m (lineare)
    compare_plot_algoritmi(10, 1000000, ["QuickSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["CountingSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["QuickSort 3-Way"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["IntroSort"], None, 10000)  #

    # Grafici SINGOLI: in funzione di n (log-log)
    compare_plot_algoritmi(100, 100000, ["QuickSort"], 100000, None, True)  #
    compare_plot_algoritmi(100, 100000, ["CountingSort"], 100000, None, True)  #
    compare_plot_algoritmi(100, 100000, ["QuickSort 3-Way"], 100000, None, True)  #
    compare_plot_algoritmi(100, 100000, ["IntroSort"], 100000, None, True)  #

    # Grafici SINGOLI: in funzione di m (log-log)
    compare_plot_algoritmi(10, 1000000, ["QuickSort"], None, 10000, True)  #
    compare_plot_algoritmi(10, 1000000, ["CountingSort"], None, 10000, True)  #
    compare_plot_algoritmi(10, 1000000, ["QuickSort 3-Way"], None, 10000, True)  #
    compare_plot_algoritmi(10, 1000000, ["IntroSort"], None, 10000, True)  #

    # Grafici COMPARATIVI: ... (in funzione di n)
    compare_plot_algoritmi(100, 100000, ["QuickSort", "CountingSort"], 100000)  #
    compare_plot_algoritmi(100, 100000, ["QuickSort", "CountingSort", "QuickSort 3-Way", "IntroSort"], 100000)  #
    compare_plot_algoritmi(100, 100000, ["QuickSort", "CountingSort", "QuickSort 3-Way", "IntroSort"], 100000, None,
                           True)  #

    # Grafici COMPARATIVI: ... (in funzione di m)
    compare_plot_algoritmi(10, 1000000, ["QuickSort 3-Way", "QuickSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["IntroSort", "CountingSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["QuickSort", "CountingSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["QuickSort", "CountingSort", "QuickSort 3-Way", "IntroSort"], None, 10000)  #
    compare_plot_algoritmi(10, 1000000, ["QuickSort", "CountingSort", "QuickSort 3-Way", "IntroSort"], None, 10000,
                           True)  #




### BLOCCO ESECUZIONE PRINCIPALE ###

if __name__ == "__main__":
    random.seed(2)
    main()