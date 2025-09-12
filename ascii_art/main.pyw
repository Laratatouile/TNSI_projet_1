"""
n = int(input("n :"))

print("X " * n)
for i in range(n - 2):
    print("X " + "  "*(n-2) +"X ")
print("X "*n)
"""
"""
def carre_croix(n):
print("X " * n)
for i in range(n - 2):
    print("X " + "  "*(n-2) +"X ")
print("X "*n)
"""


def triangle(n):
    for i in range(1, n+1):
        if i == 1:  
            print("  " * (n-i) + "X ")
        elif i == n:  
            print("X " * (2*i-1))
        else:  
            print("  " * (n-i) + "X " + " " * (2*i-3) + "X ")

triangle(6)

