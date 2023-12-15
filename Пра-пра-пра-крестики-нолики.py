import pygame


class Board(object):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.board = [[0] * heigth for _ in range(width)]
        self.set_view(10, 10, 50)
        self.player = 1

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
                cell = self.board[x][y]
                x_pix, y_pix = x * self.cell_size + self.left, y * self.cell_size + self.top
                if cell == 1:
                    color = pygame.Color("blue")
                    pygame.draw.line(screen, color, (x_pix + 2, y_pix + 2),
                                     (x_pix + self.cell_size - 2, y_pix + self.cell_size - 2), 2)
                    pygame.draw.line(screen, color, (x_pix + 2, y_pix + self.cell_size - 2),
                                     (x_pix + self.cell_size - 4, y_pix + 2), 2)
                elif cell == 2:
                    color = pygame.Color("red")
                    rect = pygame.Rect((x_pix + 2, y_pix + 2),
                                       (self.cell_size - 4, ) * 2)
                    pygame.draw.ellipse(screen, color, rect, 2)
                if border:
                    rect = pygame.Rect((x_pix, y_pix), (self.cell_size, ) * 2)
                    pygame.draw.rect(screen, border_color, rect, 1)

    def pppos(self, pos):
        return (pos[0] - self.left, pos[1] - self.top)


    def click_get(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def on_click(self, cell) -> None:
        if cell is None:
            return
        x, y = cell
        if self.board[x][y] == 0:
            self.board[x][y] = self.player
        self.next_player()

    def next_player(self):
        self.player = {1: 2, 2: 1}[self.player]

    def get_cell(self, pos):
        if all(map(lambda pos, maximum: 0 < pos < maximum, self.pppos(pos), self.get_pixel_size())):
            return tuple(coord // self.cell_size for coord in self.pppos(pos))
        else:
            return None


running = True
screen_heigth, screen_width = 370, 520

board = Board(10, 7)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.click_get(event.pos)
    screen.fill(pygame.Color("black"))
    board.do()
    pygame.display.flip()

pygame.quit()
