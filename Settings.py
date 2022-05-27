def SETTmain():
    import pygame
    pygame.init()
    from PancGameMain import mainmain
    ScrWgtOrig = 800
    ScrHgtOrig = 600
    ScrWgt = 1200
    ScrHgt = 900
    window = pygame.display.set_mode((ScrWgt, ScrHgt))
    pygame.display.set_caption("Pancreas-survivor/settings")

    BW = pygame.image.load('assets/BackWards.png')
    BWscale = pygame.transform.scale(BW, (BW.get_width() // 2 * (ScrWgt / ScrWgtOrig), BW.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    window.fill((150, 200, 0))

    window.blit(BWscale, ((ScrWgt - BWscale.get_width()) // 2, (ScrHgt - BWscale.get_height()) // 2 *1.8))

    done = True
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                return done
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if ((ScrWgt - BWscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - BWscale.get_width()) // 2 + BWscale.get_width()) and ((ScrHgt - BWscale.get_height()) // 2*1.8 ) <= pos[1] <= ((ScrHgt - BWscale.get_height()) // 2*1.8 + BWscale.get_height()):
                        pygame.display.flip()
                        done = False
                        mainmain()
        pygame.display.flip()