import board

b = board.Board((10, 20))

square = '''\
XX
XX
'''

def to_coords(shape: str):
    return (
        'foo'
        for line in shape.splitlines()
    )


shapes = {square,}

if __name__ == '__main__':
    print(b.draw())
