# Stima e analisi dei tempi medi di esecuzione di QuickSort, QuickSort 3-Way e CountingSort e IntroSort

Il seguente progetto è stato realizzato in gruppo, per l'esame di laboratorio di Algoritmi e Strutture Dati presso l'Università degli Studi di Udine.

## Descrizione

Il progetto analizza il comportamento pratico di quattro algoritmi di ordinamento, confrontando i tempi medi di esecuzione misurati sperimentalmente con la complessità teorica attesa. Oltre a QuickSort, QuickSort 3-Way e CountingSort, è stato incluso IntroSort come algoritmo di approfondimento, in quanto ibrido tra QuickSort, InsertionSort e HeapSort e algoritmo di ordinamento predefinito in diverse librerie standard.

- `n`: la lunghezza dell'array, compresa tra 100 e 100.000;
- `m`: la dimensione dell'intervallo di interi da cui vengono estratti gli elementi dell'array, compresa tra 10 e 1.000.000.

Per ciascun algoritmo vengono generati grafici in funzione di `n` (con `m` fissato a 100.000) e in funzione di `m` (con `n` fissato a 10.000), sia in scala lineare sia in scala doppiamente logaritmica.

## Struttura del progetto

```
quicksort.py                implementazione di QuickSort
quicksort_3way.py           implementazione di QuickSort 3-Way
countingsort.py             implementazione di CountingSort
introsort.py                implementazione di IntroSort
calcolo_benchmark.py        funzioni per la misurazione dei tempi di esecuzione
plotter_grafici.py          gestione della creazione dei grafici
main_grafici.py             punto di ingresso del programma
```

La funzione principale `compare_plot_algoritmi(...)`, richiamata dal `main()`, consente di generare grafici sia singoli sia comparativi, indicando in un vettore di stringhe i nomi degli algoritmi da confrontare. Ogni nome fa riferimento al relativo algoritmo tramite il dizionario `ALGORITMI_CONFIG`, le cui voci sono oggetti della classe `AlgConfig`. Questo approccio evita la duplicazione del codice e rende la generazione dei grafici flessibile rispetto al parametro scelto come variabile (`n` o `m`).

La classe `BenchmarkConfig` permette invece di configurare i parametri del benchmark, in particolare il numero di ripetizioni e il numero di campioni. Al suo interno è definito il flag `AVVIO_BENCHMARK`:

- `TRUE`: esegue la misurazione dei tempi medi dell'algoritmo scelto e salva i risultati in un file CSV;
- `FALSE`: carica i risultati già calcolati dal file CSV corrispondente, senza rieseguire il benchmark.

## Esecuzione

Il punto di ingresso del programma è `main_grafici.py`. All'avvio, lo script imposta automaticamente il limite di ricorsione a 100.000 (necessario per QuickSort) e fissa il seed casuale a `2`, per garantire la riproducibilità dei dati generati.

Per eseguire il programma e riprodurre tutti i grafici presenti nella relazione (singoli e comparativi, in funzione di `n` e di `m`, in scala lineare e doppiamente logaritmica), è sufficiente lanciare:

```
python main_grafici.py
```

La funzione `main()` contiene già tutte le chiamate necessarie a `compare_plot_algoritmi(...)` per generare l'intero set di grafici, quindi non è necessario modificarla per riprodurre i risultati.
Per generare grafici diversi da quelli già presenti, è possibile aggiungere o modificare le chiamate a `compare_plot_algoritmi(...)` nella funzione `main()`, secondo il seguente schema:

```
compare_plot_algoritmi(val_min, val_max, lista_algoritmi, m_fisso=None, n_fisso=None, log_log=False)
```

- `val_min`, `val_max`: estremi dell'intervallo del parametro scelto come variabile (`n` oppure `m`);
- `lista_algoritmi`: lista di stringhe con i nomi degli algoritmi da includere nel grafico, es. `["QuickSort", "CountingSort"]`;
- `m_fisso`: valore di `m` da mantenere costante, da specificare quando si genera un grafico in funzione di `n` (per questo progetto è fissato a 100.000);
- `n_fisso`: valore di `n` da mantenere costante, da specificare quando si genera un grafico in funzione di `m` (per questo progetto è fissato a 10.000);
- `log_log`: `True` per generare il grafico in scala doppiamente logaritmica, `False` (default) per la scala lineare.

Ad esempio, per generare il grafico comparativo di QuickSort e CountingSort in funzione di `n`, in scala lineare:

```python
compare_plot_algoritmi(100, 100000, ["QuickSort", "CountingSort"], 100000)
```

Il flag `AVVIO_BENCHMARK`, definito nella classe `BenchmarkConfig` (in `calcolo_benchmark.py`), stabilisce se i tempi medi vengono ricalcolati da zero (`TRUE`, salvandoli poi su file CSV) oppure se vengono caricati dai CSV già generati in precedenza (`FALSE`), evitando di rieseguire il benchmark ogni volta che si vuole solo rigenerare un grafico.

## Generazione dei campioni

Per ciascun algoritmo vengono generati 250 campioni, ciascuno costituito dalla coppia (valore di `n` o `m`, tempo medio misurato). I valori da testare non sono distribuiti in modo lineare ma seguono una progressione geometrica, così da concentrare più punti nella parte bassa dell'intervallo, dove le variazioni sono generalmente più significative, e meno punti nella parte alta.

La formula utilizzata per generare l'i-esimo valore (con `i` compreso tra 0 e 249) è:

```
x_i = val_min * (val_max / val_min) ^ (i / (num_campioni - 1))
```

dove `val_min` e `val_max` sono gli estremi dell'intervallo del parametro scelto come variabile.

---

Per visualizzare i risultati completi, con i relativi grafici e commenti, è possibile visionare la relazione `relazione_benchmarking_algoritmi.pdf`.
