import time
import math
def BubbleSort(v):
    for i in range(0, len(v) - 1):
        for j in range(len(v) - 1 - i):
            if (v[j] > v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]
    return (v)
def RadixSort(v, radix=10):
  if len(v) == 0:
    return v
  minVal= v[0];
  maxVal = v[0];
  for i in range(1, len(v)):
    if v[i] < minVal:
      minVal = v[i]
    elif v[i] > maxVal:
      maxVal = v[i]
  exp = 1
  while (maxVal - minVal) / exp >= 1:
    v = CountSortDigit(v, radix, exp, minVal)
    exp *= radix
  return v
def CountSortDigit(v, radix, exp, minVal):
  bucketIndex = -1
  buckets = [0] * radix
  output = [None] * len(v)
  for i in range(0, len(v)):
    bucketIndex = math.floor(((v[i] - minVal) / exp) % radix)
    buckets[bucketIndex] += 1
  for i in range(1, radix):
    buckets[i] += buckets[i - 1]
  for i in range(len(v) - 1, -1, -1):
    bucketIndex = math.floor(((v[i] - minVal) / exp) % radix)
    buckets[bucketIndex] -= 1
    output[buckets[bucketIndex]] = v[i]
  return output
def QuickSort(v):
    n=len(v)
    if n < 2:
        return v
    p = 0
    for i in range(1,n):
        if v[i] <= v[0]:
            p=p+1
            aux = v[i]
            v[i] = v[p]
            v[p] = aux
    aux = v[0]
    v[0] = v[p]
    v[p] = aux
    left = QuickSort(v[0:p])
    right = QuickSort(v[p+1:n])
    v = left + [v[p]] + right
    return v
def mergeSort(v):
    if len(v) > 1:
        mid = len(v) // 2
        L = v[:mid]
        R = v[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i]
                i += 1
            else:
                v[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            v[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            v[k] = R[j]
            j += 1
            k += 1
def CountingSort(v):
    max_val=max(v)
    m = max_val + 1
    count = [0] * m

    for a in v:
        count[a] =count[a] + 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            v[i] = a
            i =i+ 1
    return v
def Verificare(w):
    a=w.copy()
    a.sort()
    if a == w :
        g.write("sortat" + '\n')
    else :
        g.write("nu e sortat" + '\n')
f = open("sortare.txt", "r")
g = open("sortareout.txt", "w")
v = []
from random import randint
from random import seed
seed(1)
nrteste = int(f.readline())  # se va introduce nr de teste din fisier
indextest = 1  # indextest-ul numara cate teste au fost introduse si while-ul se va incheia dupa ce a fost introdus un nr de "a" teste
while (indextest <= nrteste):

    y=f.readline()
    y=y.split()
    n=y[0]
    maxx=y[1]

    from random import randint
    from random import seed
    seed(1)
    v=[]
    for i in range(int(n)):  # se genereaza un vector random
        value = randint(0,int(maxx))
        v.append(value)


    v1 = v.copy()
    g.write("Testul nr.:")
    g.write(str(indextest) + '\n')  # incep testele pentru fiecare tip de sortare
    g.write("Sortare BubbleSort:" + '\n')
    start = time.time()
    g.write(str(BubbleSort(v1))+ '\n')
    g.write("Timp Sortare BubbleSort:" + '\n')  # se afiseaza timpul fiecarei sortari
    g.write(str(time.time() - start) + '\n')
    Verificare(v1)  # verific fiecare sortare sa fie corecta
    g.write('\n')


    v2 = v.copy()  # copie pentru sortarea mea
    g.write("Sortare QuickSort:" + '\n')
    start = time.time()
    v2=QuickSort(v2)
    g.write(str(v2) + '\n')
    g.write("Timp sortare QuickSort:" + '\n')
    g.write(str(time.time() - start))
    g.write('\n')
    Verificare(v2)
    g.write('\n')


    v3 = v.copy()
    g.write("Sortare MergeSort:" + '\n')
    start = time.time()
    mergeSort(v3)
    g.write(str(v3) + '\n')
    g.write("Timp sortare MergeSort:" + '\n')
    g.write(str(time.time() - start))
    g.write('\n')
    Verificare(v3)
    g.write('\n')


    v4 = v.copy()
    g.write("Sortare RadixSort:" + '\n')
    start = time.time()
    v4=RadixSort(v4)
    g.write(str(v4) + '\n')
    g.write("Timp sortare RadixSort:"+'\n')
    g.write(str(time.time() - start))
    g.write('\n')
    Verificare(v4)
    g.write('\n')


    v5 = v.copy()
    g.write("Sortare CountingSort:")
    g.write('\n')
    start = time.time()
    g.write(str(CountingSort(v5))+'\n')
    g.write('\n')
    g.write("Timp sortare CountingSort:")
    g.write('\n')
    g.write(str(time.time() - start))
    g.write('\n')
    Verificare(v5)
    g.write('\n')


    indextest = indextest + 1  # se numara inca un test facut
