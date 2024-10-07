from pydub import AudioSegment
from random import randrange, uniform
import os

base_dir = 'C:/Users/user/Desktop/Dataset/PhoneCall/CallHome/'
dir = os.listdir('C:/Users/user/Desktop/Dataset/PhoneCall/CallHome')
output_dir = 'C:/Users/user/Desktop/Dataset/PhoneCall/CallHome/new/'

postfix = 1
for file in dir:
    audio = AudioSegment.from_wav(base_dir + file)
    file_duration = audio.duration_seconds

    t1 = 0

    t2 = randrange(30,60)
    t2 = t2 * 1000

    if file_duration > 60:
        while t2/1000 < file_duration:
            newAudio = AudioSegment.from_wav(base_dir + file)
            newAudio = newAudio[t1 : t2]
            newAudio.export(output_dir + 'CallHome_' + format(postfix, '03d') + '.wav', format="wav") #Exports to a wav file in the current path.

            postfix += 1
            t1 = t2
            rand_duration = randrange(30, 60)
            rand_duration *= 1000
            t2 = t2 + rand_duration




    # # randrange gives you an integral value
    # t1 = randrange(30, 60)
    # t1 = t1 * 1000 #Works in milliseconds

    # newAudio = AudioSegment.from_wav(base_dir + file)
    # newAudio = newAudio[0 : t1]
    # newAudio.export(base_dir + file + '1.wav', format="wav") #Exports to a wav file in the current path.

    # newAudio = AudioSegment.from_wav(base_dir + file)
    # newAudio = newAudio[t1 : t1+t2]
    # newAudio.export(base_dir + file + '2.wav', format="wav") #Exports to a wav file in the current path.
