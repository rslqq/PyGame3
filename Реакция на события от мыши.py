import pygame


class Board(object):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.board = [[0] * heigth for _ in range(width)]
        self.set_view(10, 10, 50)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_pixel_size(self):
        return (self.cell_size * self.width, self.cell_size * self.heigth)

    def do(self, border=True):
        border_color = pygame.Color("white")
        for x in range(self.width):
            for y in range(self.heigth):
                fill_color = pygame.Color(
                    {0: "black", 1: "red", 2: "blue"}[self.board[x][y]])
                rect = pygame.Rect((x * self.cell_size + self.left, y *
                                    self.cell_size + self.top), (self.cell_size, ) * 2)
                pygame.draw.rect(screen, fill_color, rect, 0)
                if border:
                    pygame.draw.rect(screen, border_color, rect, 1)

    def pppos(self, pos):
        return (pos[0] - self.left, pos[1] - self.top)


    def click_get(self, pos):
        a = self.get_cell(pos)
        self.click(a)

    def click(self, cell):
        if cell is None:
            return
        self.board[cell[0]][cell[1]] = {0: 1, 1: 2, 2: 0}[
            self.board[cell[0]][cell[1]]]

    def get_cell(self, pos):
        if all(map(lambda pos, maximum: 0 < pos < maximum, self.pppos(pos), self.get_pixel_size())):
            return tuple(coord // self.cell_size for coord in self.pppos(pos))
        else:
            return None


running = True

heigth, width = 400, 350

board = Board(5, 7)

pygame.init()
screen = pygame.display.set_mode((width, heigth))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.click_get(event.pos)
    screen.fill(pygame.Color("black"))
    board.do()
    pygame.display.flip()

pygame.quit()
