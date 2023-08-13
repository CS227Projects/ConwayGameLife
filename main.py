import pygame
import Grid

board = Grid.Grid(20)
size = (550, 550)

pygame.init()
pygame.display.set_caption("Conway\'s Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
setUp = True

blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Press space to begin', True, blue)
textRect = text.get_rect()
textRect.center = (size[0] // 2, size[1] // 2)


# creates the cells in the nxn matrix, making them red or green depending on living state
# tiles are sized to fit the screen size
def update_cells():
    width = board.get_size()
    for i in range(0, width):
        for j in range(0, width):
            if board.is_alive(i, j):
                pygame.draw.rect(screen, (0, 100, 0),
                                 (i*(size[0]//width), j*(size[1]//width), 25, 25))
            else:
                pygame.draw.rect(screen, (100, 0, 0),
                                 (i*(size[0]//width), j*(size[1]//width), 25, 25))


# loop in which the game is played
def game_loop():
    while board.is_life():
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                board.clear()

        screen.fill("white")
        update_cells()
        pygame.display.update()

        board.grid_check()
        clock.tick(1)


# static loop allowing player to update the tiles to alive by clicking on them
# press space when read to start
while setUp:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setUp = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_loop()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            length = board.get_size()
            board.set_grid(mouse[0]//(size[0]//length), mouse[1]//(size[1]//length))

    screen.fill("white")
    update_cells()

    screen.blit(text, textRect)

    pygame.display.update()
