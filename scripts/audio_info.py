import wave
import wave
import matplotlib.pyplot as plt
import numpy as np
# Audio Signal Parameters
# ~ number of channels: Mono, Stereo
# ~ sample width
# ~ framerate/ sample_rate: 44,100Hz
# ~ number of frames
# ~ values of a frame
# ~ Compression type: wav is the best quality but has large size


def info(path="scripts/tikvah.wav"):
    obj = wave.open(path, "rb")
    print("Number of Channels", obj.getnchannels())
    print("sample width", obj.getsampwidth())
    print("frame rate", obj.getframerate())
    print("Number of frames", obj.getnframes())
    print("parameters", obj.getparams())
    # t_audio = obj.getnframes()/obj.getframerate()
    # print(t_audio)
    # frames = obj.readframes(-1)
    # print(type(frames), type(frames[0]))
    # print(len(frames))


def plot(path="../sample_audio/tikvah.wav", save=False):
    obj = wave.open(path, "rb")

    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(-1)
    t_audio = n_samples/sample_freq
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    times = np.linspace(0, t_audio, num=n_samples)

    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title("Audio Signal")
    plt.ylabel("Signal Wave")
    plt.xlabel("Time(s)")
    plt.xlim(0, t_audio)
    plt.show()
    if save:
        plt.savefig("../images/audio_plot.png")
