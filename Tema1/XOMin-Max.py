turn = 'X'
values = {'X': 'O', 'O': 'X'}


# This represents a table of game
class Table:
    hash_table_values = {}

    # initialisation table is the current table
    # side is the current side to move
    def __init__(self, table, side):
        self.table = table
        self.side = side
        self.children = []
        self.value_position = 0

    # hash function to index the tables that have been created
    def make_hash(self):
        score = 0
        for i, var in enumerate(self.table):
            if var == 'X':
                score += i * 40
            elif var == 'O':
                score += i * 50
        return score

    # calculates the score for the current table
    # turn_aux means the turn it has to be calculated
    # Min or Max depending on the depth
    def calculate_values(self, turn_aux):
        maximum = -100
        minimum = 100

        if self.verify_end_final():
            return

        for i in self.children:
            i.calculate_values(turn_aux + 1)

        if turn_aux % 2 == 0:
            for i in self.children:
                if maximum < i.value_position:
                    maximum = i.value_position
            self.value_position = maximum
            return
        else:
            for i in self.children:
                if minimum > i.value_position:
                    minimum = i.value_position
            self.value_position = minimum
            return

    # Calculates the number of moves left
    def has_moves_left(self):
        nr = 0
        for i in self.table:
            if i == '_':
                return True
        return False

    # returns true if the game is finished or false if it is not true
    def verify_end_final(self):
        # horizontal
        if self.table[0] == self.table[1] == self.table[2] != '_':
            return True

        if self.table[3] == self.table[4] == self.table[5] != '_':
            return True

        if self.table[6] == self.table[7] == self.table[8] != '_':
            return True

        # vertical

        if self.table[0] == self.table[3] == self.table[6] != '_':
            return True

        if self.table[1] == self.table[4] == self.table[7] != '_':
            return True

        if self.table[2] == self.table[5] == self.table[8] != '_':
            return True

        # diagonal
        if self.table[0] == self.table[4] == self.table[8] != '_':
            return True

        if self.table[2] == self.table[4] == self.table[6] != '_':
            return True

        return False

    def show_table(self):
        print("{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(*self.table))


# Calculates the best move for the engine
def get_best_solution(table):
    maximum = -100
    index = 0
    create_children(table, 1)
    table.calculate_values(0)

    for i, val in enumerate(table.children):
        print(val.value_position)
        val.show_table()
        if val.value_position > maximum:
            index = i
            maximum = val.value_position

    return table.children[index]


# creates all possible moves for the current table
def create_children(table, depth):
    table.value_position = verify_end(table, color_bot) + 10 - depth

    if not table.verify_end_final():
        for i, var in enumerate(table.table):
            if var == '_':
                andrei = table.table.copy()
                andrei[i] = table.side
                new_table = Table(andrei, values[table.side])
                create_children(new_table, depth + 1)
                table.children.append(new_table)


# this actually calculates the value of the position for a certain side
# it's made to prioritise the center and the diagonal
def verify_end(table, side):
    # Horizontal verification
    if table.table[0] != '_' and table.table[1] != '_' and table.table[2] != '_':
        if table.table[0] == table.table[1] == table.table[2]:
            if table.table[0] == side:
                return 20
            else:
                return -20

    if table.table[3] != '_' and table.table[4] != '_' and table.table[5] != '_':
        if table.table[3] == table.table[4] == table.table[5]:
            if table.table[3] == side:
                return 20
            else:
                return -20

    if table.table[6] != '_' and table.table[7] != '_' and table.table[8] != '_':
        if table.table[6] == table.table[7] == table.table[8]:
            if table.table[6] == side:
                return 20
            else:
                return -20

    # Vertical verification
    if table.table[0] != '_' and table.table[3] != '_' and table.table[6] != '_':
        if table.table[0] == table.table[3] == table.table[6]:
            if table.table[0] == side:
                return 20
            else:
                return -20

    if table.table[1] != '_' and table.table[4] != '_' and table.table[7] != '_':
        if table.table[1] == table.table[4] == table.table[7]:
            if table.table[1] == side:
                return 20
            else:
                return -20

    if table.table[2] != '_' and table.table[5] != '_' and table.table[8] != '_':
        if table.table[2] == table.table[5] == table.table[8]:
            if table.table[2] == side:
                return 20
            else:
                return -20

    # Diagonal verification
    if table.table[0] != '_' and table.table[4] != '_' and table.table[8] != '_':
        if table.table[0] == table.table[4] == table.table[8]:
            if table.table[0] == side:
                return 20
            else:
                return -20

    if table.table[2] != '_' and table.table[4] != '_' and table.table[6] != '_':
        if table.table[2] == table.table[4] == table.table[6]:
            if table.table[2] == side:
                return 20
            else:
                return -20

    return 0


# table initialization
table_current = Table(['_', '_', '_', '_', '_', '_', '_', '_', '_'], 'X')

while 1:
    side_human = int(input("Choose your side\n 1 = X, 2 = O\n"))
    if side_human == 1:
        side_human = 'X'
        color_bot = 'O'
    else:
        side_human = 'O'
        color_bot = 'X'
    turn = 'X'
    # keeps the game going as long as it has
    while not table_current.has_moves_left() == 0 and not table_current.verify_end_final():
        # if it's the turn of the human or tha ai's
        if turn == side_human:
            position = int(input('Choose your square\n'))
            # keep input till you find an empty square
            while not (9 > position > -1) or (table_current.table[position] == 'X' or
                                              table_current.table[position] == 'O'):
                position = int(input('Choose your square\n'))
            table_current.table[position] = side_human
            table_current.side = values[side_human]
            turn = values[turn]
        else:
            table_current = get_best_solution(table_current)
            table_current.children = []
            table_current.show_table()
            table_current.side = values[turn]
            turn = values[turn]

    table_current.show_table()

    # the final verdict
    if 2 >= verify_end(table_current, color_bot) >= -2:
        print("Draw")
    elif verify_end(table_current, color_bot) < -2:
        print("You won!!")
    else:
        print("You lost")

    # choose if you want to continue or not
    replay = input("Do you want to try again?\n 1 = YES 2 = NO\n")
    if replay == "1":
        table_current = Table(['_', '_', '_', '_', '_', '_', '_', '_', '_'], 'X')
        continue
    else:
        print("Have a nice day!\n")
        break

