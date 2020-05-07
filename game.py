import board
import time



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


def main():
    b = board.Board((10, 20))

    for i in range(30):
        b2 = b.copy(with_data=True)

        for coord in to_coords(square):
            x, y = coord
            new_coord = x, y + i

            if b[new_coord]:
                # piece stops here
            b2[new_coord] = '■ '

        print('\n' * 10)
        b2.draw(use_borders=False)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
