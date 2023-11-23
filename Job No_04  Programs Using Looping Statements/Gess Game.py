secret_gess = 7
gess_count: int = 0
gess_limit = 3

while gess_count < gess_limit:
    gess = int(input('Gess:'))
    gess_count += 1
    if gess == secret_gess:
        print('You won')
        break
else:
    print('Sorry! You,failed')
