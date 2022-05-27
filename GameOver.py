def GOmain(Final):
    import pygame
    pygame.init()
    RECORDSCORE=99999999
    from StartGame import SGmain
    from PancGameMain import mainmain
    ScrWgtOrig = 800
    ScrHgtOrig = 600
    ScrWgt = 1200
    ScrHgt = 900
    window = pygame.display.set_mode((ScrWgt, ScrHgt))
    pygame.display.set_caption("Pancreas-survivor/watching_model")

    CSC = pygame.image.load('assets/CurrScore.png')
    CSCscale = pygame.transform.scale(CSC, (CSC.get_width() // 2 * (ScrWgt / ScrWgtOrig), CSC.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
    RSC = pygame.image.load('assets/RecordScore.png')
    RSCscale = pygame.transform.scale(RSC, (RSC.get_width() // 2 * (ScrWgt / ScrWgtOrig), RSC.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
    OMT= pygame.image.load('assets/OneMoreTime.png')
    OMTscale = pygame.transform.scale(OMT, (OMT.get_width() // 2 * (ScrWgt / ScrWgtOrig), OMT.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
    TMM = pygame.image.load('assets/ToMainMenu.png')
    TMMscale = pygame.transform.scale(TMM, (TMM.get_width() // 2 * (ScrWgt / ScrWgtOrig), TMM.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    window.fill((150, 200, 0))

    window.blit(CSCscale, ((ScrWgt - CSCscale.get_width()) // 2, (ScrHgt - CSCscale.get_height()) // 2 * 0.8))
    window.blit(RSCscale, ((ScrWgt - RSCscale.get_width()) // 2, (ScrHgt - RSCscale.get_height()) // 2 * 1.0))
    window.blit(OMTscale, ((ScrWgt - OMTscale.get_width()) // 2, (ScrHgt - OMTscale.get_height()) // 2 * 1.6))
    window.blit(TMMscale, ((ScrWgt - TMMscale.get_width()) // 2, (ScrHgt - TMMscale.get_height()) // 2 * 1.8))

    EndMess = "ИГРА ОКОНЧЕНА"

    FS = (int)(TMM.get_height() // 2 * (ScrHgt / ScrHgtOrig) * 0.9)
    fontInput = pygame.font.Font('calibri.ttf', FS)
    fontEnter = pygame.font.Font('calibri.ttf', FS * 2)
    textMess = fontEnter.render(EndMess, True, (50, 40, 50))
    CurrScore = fontInput.render((str)(Final), True, (50, 40, 50))
    RecScore = fontInput.render((str)(RECORDSCORE), True, (50, 40, 50))
    window.blit(textMess, ((ScrWgt - TMMscale.get_width()) // 2 * 0.3, (ScrHgt - TMMscale.get_height()) // 2 * 0.1))
    window.blit(CurrScore, ((ScrWgt - CSCscale.get_width()) // 2 + CSCscale.get_width()*0.5, (ScrHgt - CSCscale.get_height()) // 2 * 0.82))
    window.blit(RecScore, ((ScrWgt - RSCscale.get_width()) // 2 + RSCscale.get_width() * 0.5, (ScrHgt - RSCscale.get_height()) // 2 * 1.02))
    done = True
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                return done
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if ((ScrWgt - OMTscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - OMTscale.get_width()) // 2 + OMTscale.get_width()) and ((ScrHgt - OMTscale.get_height()) // 2 * 1.6) <= pos[1] <= ((ScrHgt - OMTscale.get_height()) // 2 * 1.6 + OMTscale.get_height()):
                        pygame.display.flip()
                        done = False
                        SGmain()
                    elif ((ScrWgt - TMMscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - TMMscale.get_width()) // 2 + TMMscale.get_width()) and ((ScrHgt - TMMscale.get_height()) // 2 * 1.8) <= pos[1] <= ((ScrHgt - TMMscale.get_height()) // 2 * 1.8 + TMMscale.get_height()):
                        pygame.display.flip()
                        done = False
                        mainmain()
        pygame.display.flip()