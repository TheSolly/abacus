
# procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.



def rows(n):
    if n == 0:
        return '|00000*****   |'
    if n == 1:
        return '|00000****   *|'
    if n == 2:
        return '|00000***   **|'
    if n == 3:
        return '|00000**   ***|'
    if n == 4:
        return '|00000*   ****|'
    if n == 5:
        return '|00000   *****|'
    if n == 6:
        return '|0000   0*****|'
    if n == 7:
        return '|000   00*****|'
    if n == 8:
        return '|00   000*****|'
    if n == 9:
        return '|0   0000*****|'


def print_abacus(value):
    rows_factor = 1000000000
    while rows_factor >= 1:
        print rows(value / rows_factor)
        value = value % rows_factor
        rows_factor = rows_factor / 10

    # TEST CASES


print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
