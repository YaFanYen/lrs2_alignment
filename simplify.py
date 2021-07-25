import os
import glob

basedir = '/home/ed716/Documents/NewSSD/lrs2/pretrain'
filenames = glob.glob(os.path.join(basedir, '*', '*.txt'))
savedir = '/home/ed716/Documents/NewSSD/lrs2/pretrain'

for filename in filenames:
    word = []
    with open(filename) as f:
        text = f.readline().rstrip().split()
        text = text[1:]
    f = open(filename, 'w')
    for i in range(len(text)):
        word = str(text[i] + '\n')
        f.write(word)
    f.close()


