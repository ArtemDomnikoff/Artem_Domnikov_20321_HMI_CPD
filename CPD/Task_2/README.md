## Морской бой

## Листинг 1_1

```Py
from random import randint, choice


# Возвращает координаты всей зоны вокруг корабля
def get_zone(x: int, y: int, tp: int, length: int, size: int) -> list:
    zone = []
    if tp == 1:
        zone = [[i, j] for i in range(x - 1, x + 1 + length) for j in range(y - 1, y + 2) if
                0 <= i < size and 0 <= j < size]
    elif tp == 2:
        zone = [[i, j] for i in range(x - 1, x + 2) for j in range(y - 1, y + length + 1) if
                0 <= i < size and 0 <= j < size]
    return zone


# Возвращает координаты всех ячеек корабля
def get_self_zone(x, y, tp, length):
    if tp == 1:
        return [[i, y] for i in range(x, x + length)]
    else:
        return [[x, i] for i in range(y, y + length)]


class Ship:
    def __init__(self, length: int, tp: int = 1, x: int = None, y: int = None) -> None:
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    # Меняет начальные координаты корабля
    def set_start_cords(self, x, y) -> None:
        self._x = x
        self._y = y

    # Возвращает начальные координаты корабля
    def get_start_cords(self) -> tuple:
        return self._x, self._y

    # Метод для движения корабля
    def move(self, go) -> None:
        if self._is_move:
            x, y = self.get_start_cords()
            # Горизонтально
            if self._tp == 1:
                x += go
            # Вертикально
            elif self._tp == 2:
                y += go
            self.set_start_cords(x, y)

    # Проверка на столкновение с другим кораблём
    def is_collide(self, ship) -> bool:
        x, y = ship.get_start_cords()
        ship_zone = get_zone(x, y, ship.tp, ship.length, 10)
        self_zone = get_self_zone(self._x, self._y, self._tp, self._length)
        for cords in self_zone:
            if cords in ship_zone:
                return True
        return False

    # Проверка на выход из поля
    def is_out_pole(self, size) -> bool:
        x, y = self.get_start_cords()
        if self._tp == 1:
            if 0 > x or x > size - self._length:
                return True
        if self._tp == 2:
            if 0 > y or y > size - self._length:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells.insert(key, value)

    @property
    def tp(self):
        return self._tp

    @property
    def length(self):
        return self._length


class GameField:
    def __init__(self, size):
        self._size = size
        self._ships = []

    # Метод для инициализации 10 кораблей
    def init(self):
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2))
        ]
        self.update_board()

    # Метод для проверки на столкновение и выход из поля
    def move_check(self, ship, go) -> bool:
        x, y = ship.get_start_cords()
        if ship.tp == 1:
            # Провека на столкновение
            zone = get_zone(x + go, y, ship.tp, ship.length, self._size)
            if go == 1:
                check_length = x + go + ship.length
            else:
                check_length = x + go - 1
            for x_z, y_z in zone:
                if self.field[y_z][x_z] == 1 and x_z == check_length:
                    return False

            # Проверка на выход из поля
            if x + go < 0 or x + go + ship.length > self._size:
                return False

        elif ship.tp == 2:
            # Проверка на столкновение
            zone = get_zone(x, y + go, ship.tp, ship.length, self._size)
            if go == 1:
                check_lenght = y + go + ship.length
            else:
                check_lenght = y + go - 1
            for x_z, y_z in zone:
                if self.field[y_z][x_z] == 1 and y_z == check_lenght:
                    return False

            # Проверка на выход из поля
            if y + go < 0 or y + go + ship.length > self._size:
                return False
        return True

    # Метод для движения всех кораблей по полю
    def move_ships(self) -> None:
        for ship in self._ships:
            go = choice([-1, 1])
            flag = self.move_check(ship, go)
            if flag:
                ship.move(go)
                self.update_board()
            else:
                flag = self.move_check(ship, -go)
                if flag:
                    ship.move(-go)
                    self.update_board()

    # Метод для обновления доски
    def update_board(self) -> None:
        self.field = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = self.get_random_cords(ship) if ship._x == ship._y is None else ship.get_start_cords()
            if ship.tp == 1:
                for index, i in enumerate(range(x, x + ship.length)):
                    self.field[y][i] = ship._cells[index]
            elif ship.tp == 2:
                for index, i in enumerate(range(y, y + ship.length)):
                    self.field[i][x] = ship._cells[index]
            ship.set_start_cords(x, y)

    # Метод для определения случайных кординат корабля
    def get_random_cords(self, ship) -> tuple:
        x_rand = 0
        y_rand = 0
        check = False
        while not check:
            check = True
            if ship.tp == 1:
                x_rand, y_rand = (randint(0, self._size - ship.length), randint(0, self._size - 1))
            elif ship.tp == 2:
                x_rand, y_rand = (randint(0, self._size - 1), randint(0, self._size - ship.length))
            zone = get_zone(x_rand, y_rand, ship.tp, ship.length, self._size)
            for x, y in zone:
                if self.field[y][x] == 1:
                    check = False
                    break
        return x_rand, y_rand

    # Возвращает список всех кораблей
    def get_ships(self):
        return self._ships

    # Выводит доску в консоль
    def show(self):
        for row in self.field:
            print(' '.join(map(str, row)))
        print('===============')

    # Возвращает доску как двойной кортеж
    def get_field(self):
        return tuple(tuple(sublist) for sublist in self.field)


if __name__ == '__main__':
    # Tests
    ship = Ship(2)
    ship = Ship(2, 1)
    ship = Ship(3, 2, 0, 0)
    assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
    assert ship._cells == [1, 1, 1], "неверный список _cells"
    assert ship._is_move, "неверное значение атрибута _is_move"
    ship.set_start_cords(1, 2)
    assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
    assert ship.get_start_cords() == (1, 2), "неверно отработал метод get_start_coords()"
    ship.move(1)
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
    assert s1.is_collide(
        s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
    s2 = Ship(3, 2, 1, 5)
    assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"
    p = GameField(10)
    p.init()
    for nn in range(5):
        for s in p._ships:
            assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
            for ship in p.get_ships():
                if s != ship:
                    assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
        p.move_ships()

    gp = p.get_field()
    assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
    assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
    pole_size_8 = GameField(8)
    pole_size_8.init()
    print("\n Passed")
```

### Результат выполнения программы
Программа ничего не выводит. После прохождения всех тестов просто завершает работу.

### Пояснение
В программе объявлены два класса.
**Ship** - для представления кораблей;

**GamePole** - для описания игрового поля.

# Класс Ship
Класс Ship описывает корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);

length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);

tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).

# Класс GamePole

Следующий класс GamePole обеспечивает работу с игровым полем. Объекты этого класса создаются командой:
```Py
pole = GamePole(size)
```
где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса формируются локальные атрибуты:

_size - размер игрового поля (целое положительное число);

_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В классе GamePole реализованы следующие методы :

init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей случайная).

get_ships() - возвращает коллекцию _ships;

move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то пытается переместить в противоположную сторону, иначе (если перемещения невозможны), оставаётся на месте;

show() - отображение игрового поля в консоли (корабли отображаются значениями из коллекции _cells каждого корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов;

move_check() - проверка на возможность движения корабля в заданном направлении;

update_board() - обновляет доску после перемещения корабля;

get_random_cords() - возвращает случайные координаты для расстановки кораблей на поле.