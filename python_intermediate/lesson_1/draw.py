class AreaDrawer:
    def __init__(self, width: int, height: int, char: str):
        self.width = width
        self.height = height
        self.char = char

    def draw(self):
        for y in range(self.height):
            print(self.char * self.width)


class HollowArea(AreaDrawer):
    def draw(self):
        print(self.char * self.width)
        for y in range(1, self.height - 1):
            print(self.char, ' ' * (self.width - 2), self.char)
        print(self.char * self.width)


class CustomCornerHollowArea(HollowArea):
    corner_char = "@"

    def draw(self):
        print(self.corner_char, self.char * (self.width - 2), self.corner_char, sep='')
        for y in range(1, self.height - 1):
            print(self.char, ' ' * (self.width - 2), self.char, sep='')
        print(self.corner_char, self.char * (self.width - 2), self.corner_char, sep='')


# drawer = HollowArea(10, 10, "?")
# drawer.draw()
ch = CustomCornerHollowArea(10, 10, "#")
ch.corner_char = "A"
ch.draw()
