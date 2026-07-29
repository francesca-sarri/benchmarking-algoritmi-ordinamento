from typing import Callable, Tuple, List, Optional
import numpy as np

class AlgConfig:

    # Costruttore di default
    def __init__(self, func: Callable, nome: str, color: str,

                 # Può essere una funzione (Callable) oppure None (valore predefinito)
                 arg: Optional[Callable] = None,

                 # Può essere una lista di Tuple[param_variabile, tempo_medio] oppure None (valore predefinito)
                 tempi_medi_finali: Optional[List[Tuple[int, int]]] = None):

        self.func = func
        self.nome = nome
        self.color = color

        # Se arg non è None -> funzione_algoritmo, altrimenti funzione lambda che restituisce una tupla vuota.
        self.arg = arg if arg is not None else lambda a: ()

        # Se tempi_medi_finali -> [.. tempi_medi ..], altrimenti viene inizializzata come una lista vuota.
        self.tempi_medi_finali = tempi_medi_finali if tempi_medi_finali is not None else []

    # Ritorna N o M, in base a cosa si sceglie
    def get_asse_x(self):
        return np.array([cella[0] for cella in self.tempi_medi_finali])

    # Ritorna i TEMPI MEDI in base al parametro variabile scelto
    def get_asse_y(self):
        return np.array([cella[1] for cella in self.tempi_medi_finali])

    # Prepara gli ARGOMENTI per l'esecuzione dell'algoritmo
    # Valore ritornato: Tuple[] oppure Tuple[0, len(array) - 1]
    def get_args(self, array):
        return self.arg(array)

# Classe CONFIGURAZIONE PARAMETRI principali
class BenchmarkConfig:
    N_RIPETIZIONI = 75
    NUM_CAMPIONI = 250
    ERRORE_RELATIVO = 0.001
    AVVIO_BENCHMARK = True


