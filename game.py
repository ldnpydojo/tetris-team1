import board

b = board.Board((10, 20))

square = '''\
XX
XX
'''

def to_coords(shape: str):
    return set(
        (x,y)
        for y, line in enumerate(shape.splitlines())
        for x, char in enumerate(line)
    )


shapes = {square,}

if __name__ == '__main__':
    print(b.draw())
