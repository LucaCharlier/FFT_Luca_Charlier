
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

import matplotlib.pyplot as plt
import numpy as np

from scipy.fft import rfft, rfftfreq

###################################

data_dir = pjoin(dirname(__file__))
wav_fname = pjoin(data_dir, 'equinox-8KHz-alias.wav')

###################################

samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")

time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")#plt.plot(time, data[:, 1], label="Right channel")
plt.plot(rfftfreq(data.shape[0],1/samplerate),rfft(data[:,0]))
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()