import numpy as np
import pyaudio
import wave
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# Start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("Recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Finished Recording")
# Convert the byte list into a string on integers
f = b''.join(frames)

# Stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
f = np.linspace(0, rate/2.0, len(p))
fig2 = plt.figure()
s2 = fig.add_subplot(111)
s2.plot(f)
fig.savefig("audio_freq.png")

# fig = plt.figure()
# s = fig.add_subplot(111)
# amplitude = np.fromstring(f, np.int16)
# s.plot(amplitude)
# fig.savefig("audio_amp.png")

waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(f)
waveFile.close()
