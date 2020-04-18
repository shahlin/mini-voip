from utils.Log import Log
import pyaudio
import wave
import time
import threading

class AudioListener: 
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024

    def __init__(self):
        self.audio = pyaudio.PyAudio()
    
        # start Recording
        self.input_stream = self.audio.open(format=AudioListener.FORMAT, channels=AudioListener.CHANNELS,
                        rate=AudioListener.RATE, input=True,
                        frames_per_buffer=AudioListener.CHUNK)
        
        self.output_stream = self.audio.open(format=AudioListener.FORMAT, channels=AudioListener.CHANNELS,
                        rate=AudioListener.RATE, output=True,
                        frames_per_buffer=AudioListener.CHUNK)
        self.frames = []
        self.stream_data = bytes()
        
        self.stop_recording = False

    def listen(self):
        listener_thread = threading.Thread(name='background_listener', target=self.run_listener)
        listener_thread.setDaemon(True)
        listener_thread.start()

        print("Started listening")

        while True:
            self.output_stream.write(self.stream_data)

    def run_listener(self):
        counter = 0
        while not self.stop_recording:
            self.stream_data = self.input_stream.read(AudioListener.CHUNK)
            self.frames.append(self.stream_data)
            # time.sleep(2)

            # Log.debug(counter)
            counter += 1
    
    def stop_listening(self):
        # Stop Recording
        self.stop_recording = True

        self.input_stream.stop_input_stream()
        self.input_stream.close()
        self.audio.terminate()
    
    def save_to_file(self):
        waveFile = wave.open('test.wav', 'wb')
        waveFile.setnchannels(AudioListener.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(AudioListener.FORMAT))
        waveFile.setframerate(AudioListener.RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()