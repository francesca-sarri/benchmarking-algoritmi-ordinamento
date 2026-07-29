import math

def intro_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return # Un array con 0 o 1 elemento è già ordinato
        
    # Calcola il limite di profondità della ricorsione per quick_sort (partition)
    profondità_max = 2 * (math.floor(math.log2(n))) # log(n) è standard (usare n-1 oppure n non cambia)
    
    introsort_rec(arr, 0, n - 1, profondità_max)    # La chiamata iniziale DEVE usare gli indici 0 e n-1

def introsort_rec(arr, inizio, fine, limite_profondità):
    # Esco dalla ricorsione se: partizione vuota o con un elemento
    if inizio >= fine:
        return

    # Se la partizione è piccola, insertion_Sort è la scelta più efficiente
    if fine - inizio + 1 <= 16:
        insertion_sort(arr, inizio, fine)
        return

    # Se il limite di ricorsione è raggiunto, scelgo heap_sort che garantisce O(n log n)
    if limite_profondità == 0:
        heap_sort(arr, inizio, fine)
        return

    # Altrimenti, continua con il partizionamento di quick_sort (partition)
    else:
        pivot= partition(arr, inizio, fine)
        introsort_rec(arr, inizio, pivot - 1, limite_profondità - 1)
        introsort_rec(arr, pivot + 1, fine, limite_profondità - 1)

def insertion_sort(arr, inizio, fine):
    for i in range(inizio + 1, fine + 1):
        key = arr[i]
        j = i-1
        while j >= inizio and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

def heapify(arr, n, i, inizio):
    largest = i
    l = 2 * (i+1)
    r = 2 * (i+2)
  
    if l < n and arr[inizio + l] > arr[inizio + largest]:
        largest = l
  
    if r < n and arr[inizio + r] > arr[inizio + largest]:
        largest = r
  
    if largest != i:
        arr[inizio + i], arr[inizio + largest] = arr[inizio + largest], arr[inizio + i] #swap
        heapify(arr, n, largest, inizio)
  
def heap_sort(arr, inizio, fine):
    n = fine - inizio + 1
    # Costruisce un max-heap, riorganizzando l'array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, inizio)
    
    # Estrae gli elementi uno ad uno
    for i in range(n - 1, 0, -1):
        arr[inizio + i], arr[inizio] = arr[inizio], arr[inizio + i]  # Sposta la radice alla fine
        heapify(arr, i, 0, inizio) # Chiama heapify sulla heap ridotta

def partition(arr, inizio, fine):
    pivot = arr[fine]
    i = inizio - 1
    for j in range(inizio, fine):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[fine] = arr[fine], arr[i+1]
    return i + 1

def main():
    arr = list(map(int, input().split()))
    intro_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()