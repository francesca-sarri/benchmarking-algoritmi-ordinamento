"""
    La funzione three_partition permette di 'trasformare' un array in modo da avere:
         - arr[p ... lt-1] < pivot -> elementi MINORI del PIVOT
         - arr[lt ... gt] == pivot -> elementi UGUALI al PIVOT
         - arr[gt+1 ... q] > pivot -> elementi MAGGIORI del PIVOT

    Restituisce:
        - lt: indice iniziale della sezione di elementi uguali al pivot
        - gt: indice finale della sezione di elementi uguali al pivot
"""

def three_partition(arr, p, q):
    i = p                                  # i: elemento corrente
    x = arr[q]                             # x (Pivot): l'ultimo elemento dell'array

    lt = p                                 # lt (Lower Than): elementi minori del pivot
    gt = q                                 # gt (Greater Than): elementi maggiori del pivot

    # Il ciclo termina quando i supera gt: non ci sono più elementi da ispezionare tra i e gt
    while i <= gt:

        # Partition-1: elementi minori del pivot
        if arr[i] < x:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1

        # Partition-3: elementi maggiori del pivot
        elif arr[i] > x:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1

        # Partition-2: elementi uguali al pivot (si trova già nella sezione [= v])
        else:
            i += 1

    return lt, gt

def quicksort_3way(arr, p, q):
    if p < q:
        m1, m2 = three_partition(arr, p, q)
        quicksort_3way(arr, p, m1 - 1)                     # Sotto-array SX
        quicksort_3way(arr, m2 + 1, q)                     # Sotto-array DX

def main():
    arr = list(map(int, input().split()))                  # Input

    quicksort_3way(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == "__main__":
    main()

