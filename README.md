# librosaTest
## Description
I created this repository to share code and configurations of a small Python script that runs into the following error trying to calculate the MFCC-values of an audio file. This error only occurs on Windows and Google Collab so far. It is caused using the function `librosa.feature.mfcc`. For (maybe) further information please visit: https://stackoverflow.com/questions/58824516/librosa-cannot-provide-window-function-for-mfcc-on-windows

## Traceback
```
Traceback (most recent call last):
  File "C:/Users/Fiona/PycharmProjects/librosaTest/mfcc_test.py", line 7, in <module>
    mfccs = librosa.feature.mfcc(y=y, sr=sr, S=None, n_mfcc=12, **meltspec_args)
  File "C:\Users\Fiona\Anaconda3\envs\librosaTest\lib\site-packages\librosa\feature\spectral.py", line 1442, in mfcc
    S = power_to_db(melspectrogram(y=y, sr=sr, **kwargs))
  File "C:\Users\Fiona\Anaconda3\envs\librosaTest\lib\site-packages\librosa\feature\spectral.py", line 1534, in melspectrogram
    mel_basis = filters.mel(sr, n_fft, **kwargs)
TypeError: mel() got an unexpected keyword argument 'window'
```

## \.yml file
If you are also interested in finding a solution, please consider using the Anaconda3-environment that can be created using the yml-file (to be included in the next commit). For further information on how to create a conda environment based on a yml-file please visit: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

## Information to audio directory
In this example script I used an audio file contained in RAVDESS (https://zenodo.org/record/1188976). This database contains emotional audio and video data that can be used in (e.g.) affective computing research fields. The audio file is not included in this git repository, because it's not relevant for the problem. Any audio or even video files (while creating this example I found out by accident that librosa can also load from \*.mp4). I'll also provide a function using an example audio file from librosa, so there's absolutely no download needed. 
