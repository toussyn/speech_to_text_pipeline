import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])



audio_file = "scripts/tikvah.wav"
# Play audio file works in notebooks
# ipd.Audio(audio_file)

y, sr = librosa.load(audio_file)
def plot_audio(y,sr):
    print(f'y: {y[:10]}')
    print(f'shape y: {y.shape}')
    print(f'sr: {sr}')

    pd.Series(y).plot(figsize=(10, 5),
                    lw=1,
                    title='Raw Audio Example',
                    color=color_pal[0])
    plt.show()  

def trim_audio(y):
    # Trimming leading/lagging silence
    y_trimmed, _ = librosa.effects.trim(y, top_db=20)
    pd.Series(y_trimmed).plot(figsize=(10, 5),
                    lw=1,
                    title='Raw Audio Trimmed Example',
                    color=color_pal[1])
    plt.show() 

