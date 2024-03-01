import vlc
import time
musica = vlc.MediaPlayer(r"C:\Users\mathe\Downloads\Cruel_Summer.mp3")
musica.play()
time.sleep(2)
musica.stop()

#podemos usar o modulo do pygame
