import os
import glob

basedir = '/home/ed716/Documents/NewSSD/lrs2/pretrain'
filepath = glob.glob(os.path.join(basedir, '*'))
lexicon_path = '/home/ed716/Documents/NewSSD/lrs2/lexicon.txt'

for filename in filepath:

    savepath = filename.replace('pretrain', 'phoneme')
    mfapath = filename.replace('NewSSD/lrs2/pretrain','MFA')
    if not os.path.isdir('%s'%savepath):
        os.mkdir('%s'%savepath)

    command = 'mfa align %s %s english %s;' %(filename, lexicon_path, savepath)
    os.system(command)
    command2 = 'sudo rm -r %s;' %(mfapath)
    os.system(command2)
