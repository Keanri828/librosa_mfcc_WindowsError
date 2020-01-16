import librosa

from scipy.signal import get_window

y, sr = librosa.load('audio/01-01-01-01-01-01-01.mp4',)
meltspec_args = {"n_fft": 160, "hop_length": 80, "window":  get_window("hamming", 160)}
mfccs = librosa.feature.mfcc(y=y, sr=sr, S=None, n_mfcc=12, **meltspec_args)

print(mfccs.shape)
