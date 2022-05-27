def SGmain():
    import pygame
    pygame.init()
    from GamePlay import GPmain
    ScrWgtOrig = 800
    ScrHgtOrig = 600
    ScrWgt = 1200
    ScrHgt = 900
    window = pygame.display.set_mode((ScrWgt, ScrHgt))
    pygame.display.set_caption("Pancreas-survivor/game")

    window.fill((150, 200, 0))

    LS = pygame.image.load('assets/LaunchStart.png')
    LSscale = pygame.transform.scale(LS, (LS.get_width() // 2 * (ScrWgt / ScrWgtOrig), LS.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    BP = pygame.image.load('assets/BegPerc.png')
    BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    R1 = pygame.image.load('assets/Cons1.png')
    R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    R2 = pygame.image.load('assets/Cons2.png')
    R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    R3 = pygame.image.load('assets/Cons3.png')
    R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

    EntMess = "ВВЕДИТЕ ДАННЫЕ"
    OrigState = ""
    R1Num = ""
    R2Num = ""
    R3Num = ""
    ErrorAll=""

    FS=(int)(R1.get_height() // 2 * (ScrHgt / ScrHgtOrig) *0.9)

    fontInput = pygame.font.Font('calibri.ttf', FS)
    fontEnter = pygame.font.Font('calibri.ttf', FS*2)
    fontError = pygame.font.Font('calibri.ttf', FS//2)

    StF=False
    R1F=False
    R2F=False
    R3F=False

    done = True
    while done:
        window.fill((150, 200, 0))

        textMess = fontEnter.render(EntMess, True, (50, 40, 50))
        textST = fontInput.render(OrigState, True, (50, 40, 50))
        textR1 = fontInput.render(R1Num, True, (50, 40, 50))
        textR2 = fontInput.render(R2Num, True, (50, 40, 50))
        textR3 = fontInput.render(R3Num, True, (50, 40, 50))
        textErrALL = fontError.render(ErrorAll, True, (50, 100, 0))

        window.blit(textMess, ((ScrWgt - BPscale.get_width()) // 2 * 0.2, (ScrHgt - BPscale.get_height()) // 2 * 0.1))

        window.blit(BPscale, ((ScrWgt - BPscale.get_width()) // 2, (ScrHgt - BPscale.get_height()) // 2 * 0.6))
        window.blit(R1scale, ((ScrWgt - R1scale.get_width()) // 2, (ScrHgt - R1scale.get_height()) // 2 * 0.8))
        window.blit(R2scale, ((ScrWgt - R2scale.get_width()) // 2, (ScrHgt - R2scale.get_height()) // 2))
        window.blit(R3scale, ((ScrWgt - R3scale.get_width()) // 2, (ScrHgt - R3scale.get_height()) // 2 * 1.2))
        window.blit(LSscale, ((ScrWgt - LSscale.get_width()) // 2, (ScrHgt - LSscale.get_height()) // 2 * 1.8))

        window.blit(textST, ((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()*0.62, (ScrHgt - BPscale.get_height()) // 2*0.62))
        window.blit(textR1, ((ScrWgt - R1scale.get_width()) // 2 + R1scale.get_width()*0.74, (ScrHgt - R1scale.get_height()) // 2*0.82))
        window.blit(textR2, ((ScrWgt - R2scale.get_width()) // 2 + R2scale.get_width()*0.74, (ScrHgt - R2scale.get_height()) // 2*1.02))
        window.blit(textR3, ((ScrWgt - R3scale.get_width()) // 2 + R3scale.get_width()*0.74, (ScrHgt - R3scale.get_height()) // 2*1.22))

        window.blit(textErrALL, ((ScrWgt - LSscale.get_width()) // 2 + LSscale.get_width() * 0.15, (ScrHgt - LSscale.get_height()) // 2 *2))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                return done
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if ((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()*0.6)<=pos[0]<=((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()) and ((ScrHgt - BPscale.get_height()) // 2 * 0.6)<=pos[1]<=((ScrHgt - BPscale.get_height()) // 2 * 0.75):
                        ErrorAll = ""
                        StF = True
                        R1F = False
                        R2F = False
                        R3F = False
                        BP = pygame.image.load('assets/ProcClicked.png')
                        BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R1 = pygame.image.load('assets/Cons1.png')
                        R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R2 = pygame.image.load('assets/Cons2.png')
                        R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R3 = pygame.image.load('assets/Cons3.png')
                        R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
                    elif ((ScrWgt - R1scale.get_width()) // 2 + R1scale.get_width()*0.7)<=pos[0]<=((ScrWgt - R1scale.get_width()) // 2 + R1scale.get_width()) and ((ScrHgt - R1scale.get_height()) // 2 * 0.8)<=pos[1]<=((ScrHgt - R1scale.get_height()) // 2 * 0.95):
                        ErrorAll = ""
                        StF = False
                        R1F = True
                        R2F = False
                        R3F = False
                        BP = pygame.image.load('assets/BegPerc.png')
                        BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R1 = pygame.image.load('assets/C1Clicked.png')
                        R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R2 = pygame.image.load('assets/Cons2.png')
                        R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R3 = pygame.image.load('assets/Cons3.png')
                        R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
                    elif ((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()*0.6)<=pos[0]<=((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()) and ((ScrHgt - BPscale.get_height()) // 2 * 1.0)<=pos[1]<=((ScrHgt - BPscale.get_height()) // 2 * 1.15):
                        ErrorAll = ""
                        StF = False
                        R1F = False
                        R2F = True
                        R3F = False
                        BP = pygame.image.load('assets/BegPerc.png')
                        BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R1 = pygame.image.load('assets/Cons1.png')
                        R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R2 = pygame.image.load('assets/C2Clicked.png')
                        R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R3 = pygame.image.load('assets/Cons3.png')
                        R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
                    elif ((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()*0.6)<=pos[0]<=((ScrWgt - BPscale.get_width()) // 2 + BPscale.get_width()) and ((ScrHgt - BPscale.get_height()) // 2 * 1.2)<=pos[1]<=((ScrHgt - BPscale.get_height()) // 2 * 1.35):
                        ErrorAll = ""
                        StF = False
                        R1F = False
                        R2F = False
                        R3F = True
                        BP = pygame.image.load('assets/BegPerc.png')
                        BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R1 = pygame.image.load('assets/Cons1.png')
                        R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R2 = pygame.image.load('assets/Cons2.png')
                        R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R3 = pygame.image.load('assets/C3Clicked.png')
                        R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
                    else:
                        StF = False
                        R1F = False
                        R2F = False
                        R3F = False
                        BP = pygame.image.load('assets/BegPerc.png')
                        BPscale = pygame.transform.scale(BP, (BP.get_width() // 2 * (ScrWgt / ScrWgtOrig), BP.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R1 = pygame.image.load('assets/Cons1.png')
                        R1scale = pygame.transform.scale(R1, (R1.get_width() // 2 * (ScrWgt / ScrWgtOrig), R1.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R2 = pygame.image.load('assets/Cons2.png')
                        R2scale = pygame.transform.scale(R2, (R2.get_width() // 2 * (ScrWgt / ScrWgtOrig), R2.get_height() // 2 * (ScrHgt / ScrHgtOrig)))

                        R3 = pygame.image.load('assets/Cons3.png')
                        R3scale = pygame.transform.scale(R3, (R3.get_width() // 2 * (ScrWgt / ScrWgtOrig), R3.get_height() // 2 * (ScrHgt / ScrHgtOrig)))
                    if ((ScrWgt - LSscale.get_width()) // 2) <= pos[0] <= ((ScrWgt - LSscale.get_width()) // 2 + LSscale.get_width()) and ((ScrHgt - LSscale.get_height()) // 2 * 1.8) <= pos[1] <= ((ScrHgt - LSscale.get_height()) // 2 * 1.8 + LSscale.get_height()):
                        if OrigState!="" and R1Num!="" and R2Num!="" and R3Num!="":
                            pygame.display.flip()
                            done = False
                            GPmain((int)(OrigState), (int)(R1Num),(int)(R2Num),(int)(R3Num))
                        else:
                            ErrorAll = "НЕ ВСЕ ПОЛЯ ЗАПОЛНЕНЫ"
            if e.type == pygame.KEYDOWN: #Ввод данных
                if e.key == pygame.K_BACKSPACE:
                    if StF==True:
                        OrigState = OrigState[:-1]
                        ErrorAll=""
                    elif R1F==True:
                        R1Num = R1Num[:-1]
                        ErrorAll=""
                    elif R2F==True:
                        R2Num = R2Num[:-1]
                        ErrorAll = ""
                    elif R3F==True:
                        R3Num = R3Num[:-1]
                        ErrorAll = ""
                elif e.key==pygame.K_1 or e.key==pygame.K_2 or e.key==pygame.K_3 or e.key==pygame.K_4 or e.key==pygame.K_5 or e.key==pygame.K_6 or e.key==pygame.K_7 or e.key==pygame.K_8 or e.key==pygame.K_9 or e.key==pygame.K_0:
                    if StF==True:
                        if len(OrigState)==0 and e.key==pygame.K_0:
                            ErrorAll = "Значение не может начинаться с 0"
                        elif len(OrigState)<6:
                            OrigState += e.unicode
                            ErrorAll=""
                        else:
                            ErrorAll="Значение состояния слишком длинное"
                    elif R1F==True:
                        if len(R1Num)==0 and e.key==pygame.K_0:
                            ErrorAll = "Значение не может начинаться с 0"
                        elif len(R1Num)<4:
                            R1Num+=e.unicode
                            ErrorAll=""
                        else:
                            ErrorAll="Значение первого расходника слишком длинное"
                    elif R2F==True:
                        if len(R2Num)==0 and e.key==pygame.K_0:
                            ErrorAll = "Значение не может начинаться с 0"
                        elif len(R2Num)<4:
                            R2Num+=e.unicode
                            ErrorAll=""
                        else:
                            ErrorAll="Значение второго расходника слишком длинное"
                    elif R3F==True:
                        if len(R3Num)==0 and e.key==pygame.K_0:
                            ErrorAll = "Значение не может начинаться с 0"
                        elif len(R3Num)<4:
                            R3Num+=e.unicode
                            ErrorAll=""
                        else:
                            ErrorAll="Значение первого расходника слишком длинное"
                else:
                    ErrorAll = "Можно вводить только цифры"
        pygame.display.flip()