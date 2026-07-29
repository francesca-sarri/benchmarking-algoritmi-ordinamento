"""
    La funzione Partition permette di 'trasformare' un array che abbia:
         - Tutti gli elementi <= A[q] a SINISTRA del PIVOT.
         - Tutti gli elementi > A[q] a DESTRA del PIVOT.

     Viene suddiviso in diversi sottoarray, essendo un algoritmo "Divide et Impera", grazie
     alle chiamate ricorsive.
"""

def partition(arr, p, q):
    # (alla fine) Il puntatore i punta sull'ultimo elemento <= al pivot
    i = p - 1
    x = arr[q]                                                  # Pivot: l'ultimo elemento dell'array

    # Il puntatore j punta alla cella da analizzare
    for j in range(p, q + 1):

        # Se risulta che l'elemento attuale sia più piccolo del pivot -> si effettua uno scambio
        # Ovvero si aggiunge un elemento in più nella partizione a sinistra (gli elementi più piccoli del pivot)
        if arr[j] <= x:
            i += 1                                              # Viene spostato solamente se viene trovato un elemento
                                                                # più piccolo del pivot
            arr[i], arr[j] = arr[j], arr[i]                     # Swap A[i] e A[j]
    return i

"""
    La funzione principale Quicksort ha come parametri:
        - r: il perno, viene trovato dalla funzione Partition.
        - p: puntatore al primo elemento dell'array.
        - q: puntatore all'ultimo elemento dell'array.
        
        Dopo aver spostato gli elementi in modo tale da avere gli elementi 
        minori o uguali a sinistra di A[r], mentre a destra gli elementi maggiori (non ordinati).
        
        Dividiamo il problema principale in due sottoarray, ovvero chiamando due sottochiamate, prendendo 
        il perno (r) come 'confine' (non compreso).
"""

def quicksort(arr, p, q):
    if p < q:
        r = partition(arr, p, q)
        quicksort(arr, p, r - 1)
        quicksort(arr, r + 1, q)

def main():
    arr = list(map(int, input().split()))                   # Input

    quicksort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == "__main__":
    main()