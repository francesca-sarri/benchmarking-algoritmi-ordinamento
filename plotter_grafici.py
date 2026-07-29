# Importazione librerie per la creazione dei GRAFICI
import matplotlib.pyplot as plt

# Importazione FUNZIONI principali calcolo_benchmark
from calcolo_benchmark import esegui_benchmark, salva_tempi_csv, carica_tempi_csv

# Importazione del DIZIONARIO
from config.dict_algoritmi_config import ALGORITMI_CONFIG

# Importazione della classe configurazione parametri principali
from config.alg_config import BenchmarkConfig

"""
    FUNZIONE PRINCIPALE di plotting dei dati: compare_plot_algoritmi(...)
        - (val_min, val_max) = sono la coppia di range minimo e massimo in base al dato FISSATO (n o m), dato 
                               dallo riempimento della variabile m_fixed o n_fixed.
                               Ad esempio, se si ha m_fixed = 100'000 come valore FISSO di m, si avrà la seguente coppia 
                               di val_min e val_max: (100, 100'000) di n.
        
        - algoritmi_arr = è l'array che conterrà i nomi degli o dell'algoritmo scelto per l'analisi del grafico. I 
                          nomi, specificati come stringhe, corrispondono alle keys che si trovano all'interno del 
                          dizionario ALGORITMI_CONFIG.
                          
        - is_log = è una variabile booleana che indica se il grafico che si vuole ottenere sia in scala doppiamente
                   logaritmica.
                   
    La seguente funzione è dinamica, poiché permette di creare grafici sia singoli che comparativi, grazie alle 
    strutture dati utilizzate: la classe AlgConfig e il dizionario ALGORITMI_CONFIG.
"""

def compare_plot_algoritmi(val_min, val_max, algoritmi_arr, m_fixed=None, n_fixed=None, is_log=False):

    # Stile globale del GRAFICO
    plt.style.use("seaborn-v0_8-whitegrid")

    # Setting della DIMENSIONE del grafico
    if is_log:
        plt.figure(figsize=(12, 6))
    else:
        plt.figure(figsize=(10, 6))

    # Suddivisione dei casi in base a m fissato o n fissato
    if m_fixed is not None and n_fixed is not None:                                             # Impossibile!
        print("Errore: bisogna specificare solamente UNO dei due parametri.")
        return

    # benchmark_tipo = serve per tracciare se il grafico è in funzione della variabile specificata.
    # fixed_val = per rendere dinamica la funzione, viene impiegata questa variabile per tracciare il valore fissato

    elif m_fixed is not None and n_fixed is None:
        benchmark_tipo = 'n'
        fixed_val = m_fixed
        asse_x_label = "n (dimensione input)"                                                   # Label dinamica

    elif n_fixed is not None and m_fixed is None:
        benchmark_tipo = 'm'
        fixed_val = n_fixed
        asse_x_label = "m (dimensione input)"                                                   # Label dinamica

    else:                                                                                       # Errore!
        print("Errore: Specificare O m_fixed OPPURE n_fixed per il benchmark.")
        return

    # Si itera il vettore con i nomi degli algoritmi specificati al suo interno
    for nome_alg in algoritmi_arr:
        alg_obj = ALGORITMI_CONFIG[nome_alg]                            # Ricerco l'algoritmo nel dizionario
                                                                        # Valore ritornato: oggetto di tipo AlgConfig

        print(f"\n=== Benchmarking {nome_alg} ===")

        # FLAG ATTIVO: calcolo benchmark + salvataggio su file CSV
        if BenchmarkConfig.AVVIO_BENCHMARK:

            # Esegui benchmark
            alg_obj.tempi_medi_finali = esegui_benchmark(
                val_min, val_max, fixed_val, alg_obj, benchmark_tipo
            )

            # Salvataggio
            salva_tempi_csv(alg_obj.nome, benchmark_tipo, alg_obj.tempi_medi_finali)

        # FLAG NON ATTIVO: caricamento da file CSV
        else:
            print("Caricamento dati da file...")

            # Caricamento
            alg_obj.tempi_medi_finali = carica_tempi_csv(alg_obj.nome, benchmark_tipo)

        # Plotting
        plt.plot(alg_obj.get_asse_x(),
                 alg_obj.get_asse_y(),
                 marker='o', linestyle='-', markersize=3,
                 color=alg_obj.color,
                 label=alg_obj.nome)

    # Setting scala doppiamente logaritmica se is_log = True
    if is_log:
        plt.xscale('log')
        plt.yscale('log')

    # Riempimento etichetta dinamica
    if len(algoritmi_arr) == 1:
        title = f"Tempo medio di esecuzione: {algoritmi_arr[0]}"
    else:
        title = f"Grafico comparativo: {' vs '.join(algoritmi_arr)}"

    plt.title(f"{title}", fontsize=14)
    plt.xlabel(asse_x_label, fontsize=12)
    plt.ylabel("Tempo medio (secondi)", fontsize=12)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()