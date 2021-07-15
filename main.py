EMPTY = '.'
CELL = 'o'
WIDTH = 20
HEIGHT = 20

one = {
    'energy': 40,
    'satiety': 0,
    'genome': {
        'eat': 1,
        'light_absorb': 1
    }
}


def get_empty_buffer(width, height):
    return [[EMPTY for i in range(width)] for j in range(height)]


def place(buffer, cell, x, y) -> bool:
    if is_empty(buffer[x][y]):
        buffer[x][y] = cell
        stay_on_place(cell, x, y)
        return True
    return False


def out_of_range(to_x, to_y) -> bool:
    return 0 > to_x >= WIDTH or 0 > to_y >= HEIGHT


def stay_on_place(cell, x, y):
    cell['energy'] += cell['genome']['light_absorb'] * (1 if y == 0 else -1)
    cell['satiety'] += cell['genome']['eat'] if y == HEIGHT - 1 else 0


def is_empty(cell) -> bool:
    return cell == EMPTY


def is_want_light(cell) -> bool:
    return not is_empty(cell) and cell['energy'] <= 20


def is_want_eat(cell) -> bool:
    return not is_empty(cell) and cell['satiety'] < 100 and cell['energy'] > 20


def is_dead(cell) -> bool:
    return is_empty(cell) or cell['energy'] <= 0


def show(field):
    log = []
    for y in range(20):
        row = []
        for x in range(20):
            if is_empty(field[x][y]):
                row.append(EMPTY)
            else:
                row.append(CELL)
                log.append(f"energy:{field[x][y]['energy']}")
                log.append(f"satiety:{field[x][y]['satiety']}")
        print(''.join(row))
    print(' '.join(log))


def main(field):
    place(field, one, 0, 0)
    while True:
        input('press any key for next move:')
        show(field)
        buffer = get_empty_buffer(WIDTH, HEIGHT)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cell = field[x][y]
                if is_empty(cell):
                    break
                if is_want_light(cell) and not y == 0:
                    place(buffer, cell, x, y - 1)
                elif is_want_eat(cell) and not y == 19:
                    place(buffer, cell, x, y + 1)
                else:
                    place(buffer, cell, x, y)
                if is_dead(cell):
                    print('is dead')
                    exit()

        field = buffer.copy()


if __name__ == '__main__':
    main(get_empty_buffer(WIDTH, HEIGHT))
