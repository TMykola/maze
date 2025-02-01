from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()

game = True

while game:
    events = pygame.event.get()
    window.fill(BLACK)

    #x,y = 0, 0
    #for i in range(85):
    #    pygame.draw.line(window,WHITE, (0,y), (size_window[0], y))
    #    pygame.draw.line(window,WHITE, (x,0), (x, size_window[1]))
    #    x += 15
    #    y += 15
    for wall in wall_list:
        pygame.draw.rect(window, wall.color, wall)


    for event in events:
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
    pygame.display.flip()