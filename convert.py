import os
import glob

basedir = '/home/ed716/Documents/NewSSD/lrs2/pretrain'
filenames = glob.glob(os.path.join(basedir, '*', '*.mp4'))

for filename in filenames:
    name = filename
    f_name = str(name[0:-4])
    command = 'ffmpeg -y -i %s.mp4 -ar 16000 %s.wav;' % (f_name, f_name)
    os.system(command)
