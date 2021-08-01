import os
import glob

basedir = '/home/ed716/Documents/NewSSD/lrs2/pretrain'
filenames = glob.glob(os.path.join(basedir, '*', '*.jpg'))
phonemepath = '/home/ed716/Documents/NewSSD/lrs2/phoneme/'

for filename in filenames:
    idx = filename.split('/')[-1][-7:-4]
    time = float(idx) * 0.04

    textfile = filename[:68] + '.txt'
    with open(textfile) as f:
        phoneme = f.read().replace(' ', '').splitlines()
    index = phoneme.index('name="phones"')
    
    phonelist = phoneme[index+4:]
    min = []
    max = []
    text = []
    for i in range(len(phonelist)):
        if phonelist[i][:4] == 'xmin':
            min.append(phonelist[i][5:])
        elif phonelist[i][:4] == 'xmax':
            max.append(phonelist[i][5:])
        elif phonelist[i][:4] == 'text':
            text.append(phonelist[i][6:-1])

    minidx = []
    maxidx = []
    for i in range(len(min)):
        if time >= float(min[i]):
            minidx.append(i)
        if time <= float(max[i]):
            maxidx.append(i)
    number = [l for l in minidx if l in maxidx]
    if len(number) == 0:
        continue

    phonemetext = text[int(number[0])]
    if len(number) == 2:
        number = number[-1]
        phonemetext = text[int(number)]
    
    if phonemetext == '':
        phonemetext = 'None'

    resultpath = phonemepath + phonemetext
    if not os.path.isdir('%s'%resultpath):
        os.mkdir('%s'%resultpath)
    name = filename.split('/')[-2] + '_' + filename.split('/')[-1][-13:]

    command = 'sudo mv %s %s/%s'%(filename, resultpath, name)
    os.system(command)

