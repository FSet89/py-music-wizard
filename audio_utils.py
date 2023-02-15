import librosa
#import essentia
import pydub
import numpy as np

def load(path):
	try:
		y, sr = librosa.load(path)
		return y, sr
	except(Exception) as e:
		print("Could not load file: "+str(e))
		return None, None

def write(f, sr, x, normalized=True):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")