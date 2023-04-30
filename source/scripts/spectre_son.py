
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

import matplotlib.pyplot as plt
import numpy as np

from scipy.fft import rfft, rfftfreq

###################################

data_dir = pjoin(dirname(__file__))
wav_fname = pjoin(data_dir, 'sample.wav')

###################################

samplerate, data = wavfile.read(wav_fname)
print(f"nombre de canaux = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"longueur = {length}s")

time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Canal gauche")#plt.plot(time, data[:, 1], label="Canal droit")
plt.plot(rfftfreq(data.shape[0],1/samplerate),rfft(data[:,0]))
plt.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Amplitude")
plt.show()