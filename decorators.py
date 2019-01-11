def kuchje(func):
    def wrapper():
        print('*kuchje*')
        func()
        print('*kuchje*')

    return wrapper


@kuchje
def vraagje():
    print('kan ik wat korting krijgen?')


@kuchje
def antwoord():
    print('tuurlijk kan dat, krent')


vraagje()
antwoord()