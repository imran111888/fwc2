from scipy.fftpack import fft,fftshift
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# Load WAV file
sample_rate, audio = wavfile.read('/home/imran/FM TEST/Sound.wav')

# Perform FFT on signal
fft = np.fft.fft(audio)

# Calculate power spectral density
psd = np.abs(fft)**2

# Calculate frequency range
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Plotting input spectrum using power vs freq
plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Input Signal')
plt.show()

# Find frequency range with significant power
mask = psd > 0.1*np.max(psd)
freq_range = freqs[mask]
bandwidth = max(freq_range) - min(freq_range)

print('Bandwidth:', bandwidth,'Hz')

