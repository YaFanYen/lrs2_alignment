import os
import glob

basedir = '/home/ed716/Documents/NewSSD/lrs2/phoneme'
filenames = glob.glob(os.path.join(basedir, '*', '*.TextGrid'))

for filename in filenames:
    savedir = filename.replace('phoneme', 'pretrain')
    savename = savedir[:63] + savedir[-14:-8] + 'txt'
    command = 'sudo mv %s %s' %(filename, savename)
    os.system(command)
