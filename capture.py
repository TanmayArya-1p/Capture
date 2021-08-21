import cv2
import numpy as np
import time
import math
import threading
from win10toast import ToastNotifier
import os
from PIL import ImageGrab
import subprocess


class InvalidMode(Exception):
    pass

class Recorder:

    def __init__(self,fps:float,res:tuple,codec:str,otpt_file:str , mode:str="STANDARD"):
        valid_modes = ["STANDARD","GRAYSCALE" , "FASTPACE" , "SLOWPACE"]
        if(not mode in valid_modes):
            raise InvalidMode(f"'{mode}' is an invalid mode. Valid modes are {valid_modes}")
        self.SCREEN_SIZE = res
        self.fps = fps
        self.codec = cv2.VideoWriter_fourcc(*codec)
        self.otpt_file = otpt_file
        if(mode == "STANDARD" ):
            self.out = cv2.VideoWriter(otpt_file, self.codec, 15.5, self.SCREEN_SIZE) #15.5
        elif(mode == "GRAYSCALE"):
            self.out = cv2.VideoWriter(otpt_file, self.codec, 15.5, self.SCREEN_SIZE , False) 
        elif(mode == "FASTPACE"):
            self.out = cv2.VideoWriter(otpt_file, self.codec, 60, self.SCREEN_SIZE)
        elif(mode=="SLOWPACE"):
            self.out = cv2.VideoWriter(otpt_file, self.codec, 5, self.SCREEN_SIZE)
        self.fps =fps
        self.running = False
        self.toaster = ToastNotifier()
        self.mode = mode
    
    def start(self):
        self.running = True

        self.recorder_thread = threading.Thread(target=self.__recorder)
        self.recorder_thread.start()
        threading.Thread(target=self.toaster.show_toast , args=("Capture","Capture is Recording Your Screen",) , daemon=True).start()
        
    def __recorder(self):    
        iteration = 0             
        prev = 0
        sdt = 0
        while True:
            
            dt = time.time() - prev
            sdt += dt
            if(sdt>=1.0):
                print(iteration)
                iteration = 0
                sdt = 0
            img = ImageGrab.grab()

            if(dt > (1.0/self.fps)):
                prev = time.time()
                frame = np.array(img)
                if(self.mode == "GRAYSCALE"):
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                else:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                iteration+=1
                cv2.imshow("Capture - Preview", frame)
                self.out.write(frame)

            if cv2.waitKey(1) == ord('q') or not self.running:

                self.out.release()
                cv2.destroyAllWindows()

                os.system("ffmpeg -i video.mkv write.mp4")
                self.running = False
                break

    def stop(self):
        self.running = False
        subprocess.call("ffmpeg -i video.mkv write.mp4" , shell=True)


    def content(self):
        if(self.otpt_file in os.listdir()):
            with open(self.otpt_file , "rb") as f:
                return f.read()
        else:
            return None


        


        

# r = Recorder(200.0 , (1366, 768),"mp4v","output.mp4" , mode="GRAYSCALE")              
# r.start()   
# time.sleep(5)        
# r.stop()

