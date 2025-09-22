```python

```

```python
def carre_diagonale(n):
    for i in range(n):
        ligne = ""
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j :
                ligne += "X "
            else:
                ligne += "  "
        print(ligne)

carre_diagonale(7)
```