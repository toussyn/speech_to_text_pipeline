import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
from audio_info import *

wav_loc = "../sample_audios/tikvah.wav"
rate, data = wavfile.read(wav_loc)

data = data / 32768

fig, ax = plt.subplots(figsize=(20,4))
ax.plot(data)
