def angka():
    for i in range (1,2000):
        angka = int(input(f'masukkan angka ke {i}: '))
        oper = input('''masukkan operator
    1. + 
    2. -
    3. *
    4. /
    pilih nomor berepe : ''')
    if '+' in oper:
        print()

while True:
    angka()