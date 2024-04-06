import matplotlib.pyplot as plt
import numpy as np

fileObj = open("1kHz_44100Hz_16bit_05sec.wav", mode = "rb")

data = fileObj.read()

file_size_inbytes = data[4:8] 
file_size = int.from_bytes(file_size_inbytes, byteorder="little")

num_chan_inbytes = data[22:24] 
num_chan = int.from_bytes(num_chan_inbytes, byteorder="little")

audio_file_size_inbytes = data[40:44] 
audio_file_size = int.from_bytes(audio_file_size_inbytes, byteorder="little")
sample_rate_in_byte =data[24:28]
sample_rate = int.from_bytes(sample_rate_in_byte, byteorder ="little")

audio_data = []

for i in range(0, audio_file_size,2):
    a=data[44+i:44+i+2]
    a= int.from_bytes(a,byteorder = "little",signed=True)
    audio_data.append(a)


xdatat=np.linspace(0, len(audio_data)/sample_rate, len(audio_data) )

spectre = np.fft.fft(audio_data)
abs_spectre = abs(spectre)

plt.plot(xdatat,audio_data)
plt.show()

pass
