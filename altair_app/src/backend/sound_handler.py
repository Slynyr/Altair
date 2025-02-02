from playsound import playsound
import threading
import os

class SoundHandler:
    def ding():
        try:
            base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
            sound_path = os.path.join(base_path, "ding.wav")
            playsound(sound_path)
        except Exception as ignore:
            pass

    def play_ding():
        thread = threading.Thread(target=ding)
        thread.start()