# Pseudo-codice visto a lezione

# CountingSort(A, B, k) {
#   C ⭠ new_array(k+1) \\ C[0 ... k]
#	for (j⭠0 to k) {
#		C[j] ⭠ 0
#	}
#	for (i⭠1 to A.length) {
#		C[A[i]] ⭠ C[A[i]] + 1
#	}
#	for (j⭠1 to k) {
#		C[j] ⭠ C[j] + C[j-1]
#	}
#	for (i⭠A.length down to 1) {
#		B[C[A[i]]] ⭠ A[i]
#		C[A[i]] ⭠ C[A[i]] - 1
#	}
# }

# Implementazione counting_sort

def counting_sort(arr):
    
    arr_ordinato = [0] * len(arr) # Output: array ordinato con stessa lunghezza di quello in input

    # Trovo i valori minimo e massimo dell'array
    val_min = min(arr)
    val_max = max(arr)

    # Inizializza l'array dei conteggi
    arr_conteggi = [0 for i in range(val_min, val_max + 1)]
    
    # Conta le occorrenze di ogni elemento
    for i in arr:
        arr_conteggi[i - val_min] += 1

    # Calcola le posizioni finali cumulative
    for j in range(1, len(arr_conteggi)):
        arr_conteggi[j] += arr_conteggi[j - 1]

    # Costruisce l'array ordinato (in ordine stabile crescente)
    for k in reversed(arr):
        arr_ordinato[arr_conteggi[k - val_min] - 1] = k 
        arr_conteggi[k - val_min] -= 1                
    
    return arr_ordinato 

# Main

def main():
    arr = list(map(int, input().split()))
    print(counting_sort(arr))

if __name__ == "__main__":
    main()
