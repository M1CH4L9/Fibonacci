import time
import math

def fib_iter(n):
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        tmp =  a + b
        a = b
        b = tmp
    return b

def mnozenie_macierzy(A, B):
    c00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    c01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    c11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return [[c00, c01], [c10, c11]]

def potega_macierzy(M, n):
    if n == 1:
        return M
    elif n % 2 == 0:
        polowa = potega_macierzy(M, n // 2)
        return mnozenie_macierzy(polowa, polowa)
    else:
        reszta = potega_macierzy(M, n - 1)
        return mnozenie_macierzy(M, reszta)
    
def fib_matrix(n):
    if n == 0: return 0
    if n == 1: return 1

    Q = [[1, 1], [1, 0]]

    WynikMacierz = potega_macierzy(Q, n)

    return WynikMacierz[0][1]

def fib_binet(n):
    pierwiastek_z_5 = math.sqrt(5)
    phi = (1 + pierwiastek_z_5) / 2
    
    wynik = (phi**n - (1 - phi)**n) / pierwiastek_z_5
    return round(wynik)

if __name__ == "__main__":
    try:
        n_input = int(input("Podaj numer wyrazu ciągu Fibonacciego (n): "))
    except ValueError:
        print("Złe value. Podaj poprawną liczbę całkowitą")
        exit()

    print(f"\nObliczamy {n_input}-ty wyraz ciągu fibonaczjego\n")

    start = time.perf_counter()
    wynik_iter = fib_iter(n_input)
    end = time.perf_counter()
    czas_iter = end - start
    print(f"[Iteracyjnie] Wynik: {wynik_iter}")
    print(f"Czas wykonania: {czas_iter:.10f} sekund\n")
    print("-" * 40)

    start  = time.perf_counter()
    wynik_matrix = fib_matrix(n_input)
    end = time.perf_counter()
    czas_matrix = end - start
    print(f"[Macierzowo] Wynik: {wynik_matrix}")
    print(f"Czas wykonania: {czas_matrix:.10f} sekund\n")

    if(czas_matrix < czas_iter):
        print("Macierz była szybsza od itera")
    else:
        print("Iter był szybszy od macierzy")
    print("-" * 40)

    try:
        start = time.perf_counter()
        wynik_binet = fib_binet(n_input)
        end = time.perf_counter()
        czas_binet = end - start
        print(f"[Wzór Binet'a] Wynik: {wynik_binet}")
        print(f"Czas wykonania: {czas_binet:.10f} sekund\n")
    
        if(wynik_binet == wynik_matrix):
            print("Wzór Binet'a zgadza się z innymi wynikami")
        else:
            print("Błąd: Wzór Bineta dał zły wynik (problem precyzji float) (za duża luczba)")
    except OverflowError:
        print("[Wzór Bineta] Błąd: Liczba jest zbyt duża dla typu float")

