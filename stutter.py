import enum
from itertools import repeat
import re
import librosa
import numpy as np
import tensorflow as tf
from pydub import AudioSegment
from keras.models import load_model
import os
import shutil

def detect_prolongation(mfcc,model_pro): 
    s = 0
    pro_lst=[]
    for m in mfcc:
        y = model_pro.predict(m.reshape(1,2,44,1), batch_size=1)
        y = np.around(y,decimals=2)
        if y[0][0] > 0.5:
            s += y[0][0]
            pro_lst.append(1)
        else:
            pro_lst.append(0)
    p_sev = s/len(mfcc)*100
    # return p_sev
    return pro_lst,p_sev

def detect_repetition(mfcc,model_rep):
    rep_lst=[]
    s = 0
    for m in mfcc:
        y = model_rep.predict(m.reshape(1,13,44,1), batch_size=1)
        y = np.around(y,decimals=2)
        if y[0][0] > 0.5:
            rep_lst.append(1)
            s += y[0][0]
        else:
            rep_lst.append(0)
    r_sev = s/len(mfcc)*100
    # return r_sev
    return rep_lst,r_sev

def clean_result(predict_list):
    for x in range (1,len(predict_list)-1):
        if predict_list[x-1] != predict_list[x] and predict_list[x+1] != predict_list[x]:
            predict_list[x]=predict_list[x-1]
    return predict_list

def timestamp(l):  # [0, 1, 2, 9, 10, 11]
    u=[]
    t=0
    for x in range(1,len(l)):

        if l[x-1]+1==l[x] and x != len(l) - 1:  # 
            t+=1
        else:
            if x == len(l) - 1:
                u.append([l[x-t-1],t+1])
            else:
                u.append([l[x-t-1],t])
            t=0
    return u

def detect_stutter(audio):
    
    model_rep = load_model('models/best_model_rep.h5')
    model_pro = load_model('models/best_model_pro.h5')
    sound_file = AudioSegment.from_wav(audio)
    audio_chunks = sound_file[::1000]
    # ps = 0
    # rs = 0
    mfcc_arr_p = []
    mfcc_arr_r = []
    for i, chunk in enumerate(audio_chunks):
        chunkfile = "chunks_test/chunk{0}.wav".format(i)
        chunk.export(chunkfile, format="wav")
        y, sr = librosa.load(chunkfile)
        mfcc = np.array(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13))
        
        if mfcc.shape[0] == 13 and mfcc.shape[1] == 44:
            a = []
            a.append(mfcc)
            mfcc_arr_r.append(a)
            b = []
            b.append(mfcc[0])
            b.append(mfcc[12])
            mfcc_arr_p.append(b)
            
    mfcc_arr_r = np.array(mfcc_arr_r)  
    mfcc_arr_p = np.array(mfcc_arr_p)    
    
    mfcc_arr_r.reshape(mfcc_arr_r.shape[0], 13, 44, 1)
    mfcc_arr_p.reshape(mfcc_arr_p.shape[0], 2, 44, 1)
    
    prolongation,p_sev = detect_prolongation(mfcc_arr_p,model_pro)
    repetition,r_sev = detect_repetition(mfcc_arr_r,model_rep)

    #send predictions result for cleaning
    prolongation=clean_result(prolongation)
    repetition=clean_result(repetition)

    score = (p_sev+r_sev)/2
    return (prolongation,repetition,score)

def main(ad):
    # current_path=os.getcwd()
    if os.path.exists('chunks_test/'):
        shutil.rmtree('chunks_test')
    os.mkdir('chunks_test/')
    stutter=[]
    files_to_play=[]
    prolongation,repetition,score=detect_stutter(ad)
    for i,(p,r) in enumerate(zip(prolongation,repetition)):
        if p ==1 or r==1:
            stutter.append(i)
    play_ts=timestamp(stutter)
    shutil.rmtree('chunks_test')

    return stutter,play_ts,score


if __name__== "__main__":
    # p_sev, r_sev, o_sev = detect_stutter('/home/cr/Downloads/fv/sa/stutter/all_segregated-20220218T100125Z-001/all_segregated/grep/4(52-58.05).wav')
    # print('Prolongation % : '+str(p_sev))
    # print('Repetition % : '+str(r_sev))
    # print('Overall stutter % : '+str(o_sev))
    # print (main('/home/cr/Downloads/2.wav'))
    print (os.getcwd())