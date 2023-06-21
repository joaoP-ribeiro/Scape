import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QApplication
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets, uic
import img_rc
from threading import Timer
import pygame


import sys



app = QApplication(sys.argv)

class Tela():
    def __init__(self):

        pygame.init()
        self.ultima_janela = ""
        self.tempo = 0
        self.ativo = False
        self.energia = True
        self.contador = 0
        self.bt_sair = ""
        
        
        self.tela_saida =  uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/saida_tela.ui")
        self.tela_lab =  uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/lab_tela.ui")
        self.tela_cima =  uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/cima_tela.ui")
        self.tela_robo =  uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/robo_tela.ui")
        self.tela_escuro = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/escuro.ui")
        self.tela_ataque_freddy = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/ataque_freddy.ui")
        self.tela_ataque_springtrap = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/ataque_springtrap.ui")
        
        self.tela_inicio = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/inicio_tela.ui")
        self.tela_final_f = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/final_f.ui")
        self.tela_final_v = uic.loadUi("C:/Users/52211545874/Desktop/Scape_room-main/telas/final_v.ui")

        self.tela_saida.bt_cima.clicked.connect(lambda: self.abrir_janela_monstro(self.tela_saida, self.tela_cima))
        self.tela_saida.bt_dir.clicked.connect(lambda: self.abrir_janela(self.tela_saida, self.tela_lab))
        self.tela_saida.bt_esq.clicked.connect(lambda: self.abrir_janela(self.tela_saida, self.tela_robo))
        self.tela_saida.bt_papel1.clicked.connect(lambda: self.abrir_frame(self.tela_saida.frame_1, self.tela_saida.bt_frames_saida))
        self.tela_saida.bt_papel2.clicked.connect(lambda: self.abrir_frame(self.tela_saida.frame_3, self.tela_saida.bt_frames_saida))
        self.tela_saida.bt_senha.clicked.connect(lambda: self.abrir_frame(self.tela_saida.frame_2, self.tela_saida.bt_frames_saida))

        self.tela_cima.bt_baixo_cima.clicked.connect(lambda: self.abrir_janela_monstro(self.tela_cima, self.ultima_janela))

        self.tela_lab.bt_cima.clicked.connect(lambda: self.abrir_janela_monstro(self.tela_lab, self.tela_cima))
        self.tela_lab.bt_dir.clicked.connect(lambda: self.abrir_janela(self.tela_lab, self.tela_robo))
        self.tela_lab.bt_esq.clicked.connect(lambda: self.abrir_janela(self.tela_lab, self.tela_saida))
        self.tela_lab.bt_papel1.clicked.connect(lambda: self.abrir_frame(self.tela_lab.frame1, self.tela_lab.bt_frames_lab))
        self.tela_lab.bt_papel2.clicked.connect(lambda: self.abrir_frame(self.tela_lab.frame2, self.tela_lab.bt_frames_lab))
        self.tela_lab.bt_papel3.clicked.connect(lambda: self.abrir_frame(self.tela_lab.frame3, self.tela_lab.bt_frames_lab))


        self.tela_robo.bt_cima.clicked.connect(lambda: self.abrir_janela_monstro(self.tela_robo, self.tela_cima))
        self.tela_robo.bt_dir.clicked.connect(lambda: self.abrir_janela(self.tela_robo, self.tela_saida))
        self.tela_robo.bt_esq.clicked.connect(lambda: self.abrir_janela(self.tela_robo, self.tela_lab))
        self.tela_robo.bt_papel1.clicked.connect(lambda: self.abrir_frame(self.tela_robo.frame1, self.tela_robo.bt_frames_robo))
        self.tela_robo.bt_papel2.clicked.connect(lambda: self.abrir_frame(self.tela_robo.frame2, self.tela_robo.bt_frames_robo))
        
        
        self.tela_inicio.bt_inicio.clicked.connect(lambda: self.abrir_janela(self.tela_inicio, self.tela_saida))
        self.tela_final_f.bt_finalizar_f.clicked.connect(lambda: self.abrir_tela_morte(self.tela_final_f))
        #self.tela_final_v.bt_finalizar_v.connect(lambda: self.abrir_janela(self.tela_inicio, self.tela_saida))

        self.tela_ataque_freddy.bt_finalizar.clicked.connect(lambda: self.fechar_tela())
        self.tela_ataque_springtrap.bt_finalizar.clicked.connect(lambda: self.fechar_tela())

        self.tela_saida.bt_frames_saida.clicked.connect(lambda: self.fechar_frames())
        self.tela_saida.bt_enter.clicked.connect(lambda: self.confirmar_senha())
        
        self.tela_lab.bt_frames_lab.clicked.connect(lambda: self.fechar_frames())

        self.tela_robo.bt_frames_robo.clicked.connect(lambda: self.fechar_frames())

        self.tela_inicio.show()
        self.fechar_frames()
        

        app.exec()
        

    def abrir_janela(self, janela_anterior, proxima_janela):
        """
        faz a troca de telas, fecha a tela anterior e abre a tela desejada
        """
        if not self.ativo and self.energia:
            self.ultima_janela = janela_anterior
            if self.ultima_janela == self.tela_inicio:
                self.tempo_morte(5)
                janela_anterior.close()
                proxima_janela.show()
                self.som("choque")
                self.contador += 1
                self.queda_energia(self.contador)
            else:
                janela_anterior.close()
                proxima_janela.show()
                self.som("choque")
                self.contador += 1
                self.queda_energia(self.contador)
        else:
            if not self.energia:
                self.abrir_tela_sem_energia(janela_anterior)
            else:

                 self.abrir_tela_morte(janela_anterior)
    
    def abrir_janela_monstro(self, janela_anterior, proxima_janela):
        """
        faz a troca de telas, fecha a tela anterior e abre a tela do monstro, além de voltar o tempo do ataque do monstro
        """
        if not self.ativo and self.energia:   
            self.ultima_janela = janela_anterior
            self.tempo_morte(10)
            janela_anterior.close()
            proxima_janela.show()
        else:
            if not self.energia:
                self.abrir_tela_sem_energia(janela_anterior)
            else:
                self.abrir_tela_morte(janela_anterior)

    


    def som(self, som):
        pygame.mixer.music.stop()  
        pygame.mixer.music.load("C:/Users/52211545874/Desktop/Scape_room-main/som/$som$.mp3".replace("$som$", som))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(100)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()




    def abrir_frame(self, frame, bt_sair):
        self.fechar_frames()
        frame.show()
        self.som("papel")
        self.bt_sair = bt_sair
        self.bt_sair.show()

    def fechar_frames(self):
         self.tela_saida.frame_1.close()
         self.tela_saida.frame_2.close()
         self.tela_saida.frame_3.close()
         self.tela_saida.bt_frames_saida.close()
         self.tela_lab.frame1.close()
         self.tela_lab.frame2.close()
         self.tela_lab.frame3.close()
         self.tela_lab.bt_frames_lab.close()
         self.tela_robo.frame1.close()
         self.tela_robo.frame2.close()
         self.tela_robo.bt_frames_robo.close()
         self.tela_saida.inp_senha.clear()




    def queda_energia(self, contador):
        if contador >= 5:
            self.energia = False

    def abrir_tela_sem_energia(self, fechar):
        fechar.close()
        self.tela_escuro.show()
        self.som("choque")
        self.tela_escuro.close()


        gif_freddy = QMovie("C:/Users/52211545874/Desktop/Scape_room-main/gifs/ataque_freddy.gif")
        self.tela_ataque_freddy.lb_fundo.setMovie(gif_freddy)
        gif_freddy.start()
        self.tela_ataque_freddy.show()
        self.som("grito")
        


    
    def tempo_morte(self, seg):
        """
        tempo que o bot tem para ficar parado até ativar
        """
        self.tempo_ativar = Timer(seg, self.ativo_bot)
        self.tempo_ativar.start()

    def ativo_bot(self):
        self.ativo = True
        self.som("respiração")
        self.tempo_desativar = Timer(20, self.desativo_bot)
        self.tempo_desativar.start()

    def desativo_bot(self):
        self.ativo = False
        self.som("respiração")

    def abrir_tela_morte(self, fechar):
        fechar.close()
        self.tela_escuro.show()
        self.som("respiração")
        self.tela_escuro.close()

        gif_spring = QMovie("C:/Users/52211545874/Desktop/Scape_room-main/gifs/ataque_springtrap.gif")
        self.tela_ataque_springtrap.lb_fundo.setMovie(gif_spring)
        gif_spring.start()

        self.tela_ataque_springtrap.show()
        self.som("grito")



    def fechar_tela(self):
        QApplication.closeAllWindows()

    
    def confirmar_senha(self):
        senha = self.tela_saida.inp_senha.text()
        if senha == "12345":
            self.tela_saida.inp_senha.clear()
            self.tela_saida.close()
            self.tela_final_f.show()

        else:
            self.tela_saida.close()
            self.abrir_tela_sem_energia()
            self.tela_saida.inp_senha.clear()
            
