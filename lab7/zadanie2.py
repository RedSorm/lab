import numpy as np
mac = np.random.randit(low =0 , high= 50 , size = (5, 5))
print(f"Najwieksza liczba: {mac.max())}")
print(f"Najmniejsza liczba: {mac.min()}")
print(f"Największe liczby w wierszach: {mac.max(axis=1)}")
print(f"Najmniejsze liczby w kolumnach: {mac.min(axis=0)}")
print(f"Suma liczby w wierszach: {mac.sum(axis=1}")
