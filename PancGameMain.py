def mainmain():
    import pygame
    pygame.init()
    from StartGame import SGmain
    from Settings import SETTmain
    from WatchModel import WMmain
    ScrWgtOrig=800
    ScrHgtOrig = 600
    ScrWgt = 1200
    ScrHgt = 900
    window = pygame.display.set_mode((ScrWgt, ScrHgt))
    pygame.display.set_caption("Pancreas-survivor")

    GN = pygame.image.load('assets/FinalName.png')
    GNscale = pygame.transform.scale(GN, (GN.get_width() // 2*(ScrWgt/ScrWgtOrig), GN.get_height() // 2*(ScrHgt/ScrHgtOrig)))

    ST = pygame.image.load('assets/Start.png')
    STscale = pygame.transform.scale(ST, (ST.get_width() // 2*(ScrWgt/ScrWgtOrig), ST.get_height() // 2*(ScrHgt/ScrHgtOrig)))

    SETT = pygame.image.load('assets/Settings.png')
    SETTscale = pygame.transform.scale(SETT, (SETT.get_width() // 2 * (ScrWgt / ScrWgtOrig), SETT.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    WM = pygame.image.load('assets/WatchModel.png')
    WMscale = pygame.transform.scale(WM, (WM.get_width() // 2 * (ScrWgt / ScrWgtOrig), WM.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    EX = pygame.image.load('assets/Exit.png')
    EXscale = pygame.transform.scale(EX, (EX.get_width() // 2 * (ScrWgt / ScrWgtOrig), EX.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    window.fill((150, 200, 0))

    window.blit(GNscale, ((ScrWgt - GNscale.get_width()) // 2, (ScrHgt - GNscale.get_height()) // 2 // 5))
    window.blit(STscale, ((ScrWgt - STscale.get_width()) // 2, (ScrHgt - STscale.get_height()) // 2 ))
    window.blit(SETTscale, ((ScrWgt - SETTscale.get_width()) // 2, (ScrHgt - SETTscale.get_height()) // 2*1.2))
    window.blit(WMscale, ((ScrWgt - WMscale.get_width()) // 2, (ScrHgt - WMscale.get_height()) // 2 * 1.4))
    window.blit(EXscale, ((ScrWgt - EXscale.get_width()) // 2, (ScrHgt - EXscale.get_height()) // 2 * 1.6))

    done = True
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                return done
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if ((ScrWgt - STscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - STscale.get_width()) // 2 + STscale.get_width()) and ((ScrHgt - STscale.get_height()) // 2 ) <= pos[1] <= ((ScrHgt - STscale.get_height()) // 2 + STscale.get_height()):
                        pygame.display.flip()
                        SGmain()
                    elif ((ScrWgt - SETTscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - SETTscale.get_width()) // 2 + SETTscale.get_width()) and ((ScrHgt - SETTscale.get_height()) // 2*1.2 ) <= pos[1] <= ((ScrHgt - SETTscale.get_height()) // 2*1.2 + SETTscale.get_height()):
                        pygame.display.flip()
                        SETTmain()
                    elif ((ScrWgt - WMscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - WMscale.get_width()) // 2 + WMscale.get_width()) and ((ScrHgt - WMscale.get_height()) // 2*1.4) <= pos[1] <= ((ScrHgt - WMscale.get_height()) // 2 *1.4+ WMscale.get_height()):
                        pygame.display.flip()
                        WMmain()
                    elif ((ScrWgt - EXscale.get_width()) // 2) <=pos[0]<= ((ScrWgt - EXscale.get_width()) // 2 + EXscale.get_width()) and ((ScrHgt - EXscale.get_height()) // 2 * 1.6) <=pos[1]<= ((ScrHgt - EXscale.get_height()) // 2 * 1.6 + EXscale.get_height()):
                        done = False
                        return done
        pygame.display.flip()