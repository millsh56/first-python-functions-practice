def hello():
    print('hi!')
hello()

def pack(x, y, z):
    print(x, y, z)
pack('shirt', 'pants', 'jacket')

def eat_lunch(myLunch):
        if len(myLunch) == 0:
            print('I forgot to pack anything')
        else:
             for x in range(len(myLunch)):
                if x == 0:
                       print(f'first i eat {myLunch[0]}')
                else:
                       print(f'next i eat {myLunch[x]}')
packingLunch = ['sandwich', 'chips', 'apple', 'celery', 'cookie']
eat_lunch(packingLunch)