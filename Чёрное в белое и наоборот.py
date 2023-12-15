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

    def render(self):
        color = pygame.Color("white")
        for x in range(self.width):
            for y in range(self.heigth):
                width = {0: 1, 1: 0}[self.board[x][y]]
                rect = pygame.Rect((x * self.cell_size + self.left, y *
                                    self.cell_size + self.top), (self.cell_size, ) * 2)
                pygame.draw.rect(screen, color, rect, width)

    def pppos(self, pos):
        return (pos[0] - self.left, pos[1] - self.top)\


    def get_click(self, pos):
        cell = self.get_cell(pos)
        print(cell)
        self.on_click(cell)

    def on_click(self, cell):
        if cell is None:
            return
        self.board[cell[0]][cell[1]] = {0: 1, 1: 0}[
            self.board[cell[0]][cell[1]]]
        for x in range(self.width):
            self.board[x][cell[1]] = {0: 1, 1: 0}[self.board[x][cell[1]]]
        for y in range(self.heigth):
            self.board[cell[0]][y] = {0: 1, 1: 0}[self.board[cell[0]][y]]

    def get_cell(self, pos):
        if all(map(lambda pos, maximum: 0 < pos < maximum, self.pppos(pos), self.get_pixel_size())):
            return tuple(coord // self.cell_size for coord in self.pppos(pos))
        else:
            return None


running = True
screen_heigth, screen_width = 400, 300

board = Board(5, 7)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill(pygame.Color("black"))
    board.render()
    pygame.display.flip()

pygame.quit()
