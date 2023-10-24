import sounddevice as sd
import wavio
import tkinter as tk


class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Recorder")

        self.label = tk.Label(
            master,
            text="Enter the file name to save the recording (include .wav extension):",
        )
        self.label.pack()

        self.file_name_entry = tk.Entry(master)
        self.file_name_entry.pack()

        self.duration_label = tk.Label(
            master, text="Enter the duration of the recording in seconds:"
        )
        self.duration_label.pack()

        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()

        self.record_button = tk.Button(master, text="Record", command=self.record)
        self.record_button.pack()

    def record_audio(self, file_name, duration, sample_rate):
        print("Recording audio...")
        recording = sd.rec(
            int(duration * sample_rate), samplerate=sample_rate, channels=2
        )
        sd.wait()
        wavio.write(file_name, recording, sample_rate, sampwidth=2)
        print(f"Recording saved as {file_name}")

    def record(self):
        file_name = self.file_name_entry.get()
        duration = int(self.duration_entry.get())
        sample_rate = 44100  # standard sample rate
        self.record_audio(file_name, duration, sample_rate)


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
