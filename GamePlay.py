def GPmain(A,B,C,D):
    import pygame
    from random import randrange
    from GameOver import GOmain
    pygame.init()
    SCORE=0
    ScrWgtOrig=800
    ScrHgtOrig = 600
    ScrWgt = 1200
    ScrHgt = 900
    window = pygame.display.set_mode((ScrWgt, ScrHgt))
    pygame.display.set_caption("Pancreas-survivor/Gameplay")

    window.fill((150, 200, 0))
    done = True
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                return done
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
        SCORE+=randrange(1,6)
        A-=1
        if (A==0):
            pygame.display.flip()
            done = False
            GOmain(SCORE)
        pygame.display.flip()
