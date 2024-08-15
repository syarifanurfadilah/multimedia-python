from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
# Video processing
video = VideoFileClip('vidio.mp4')

# Saving the original video
video.write_videofile('result.mp4')

# Creating a short video clip of the first 10 seconds
short_video = video.subclip(0, 10)
short_video.write_videofile('short_result.mp4')

# Concatenating the original and short video
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# Reversing the short video
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('reversed_result.mp4')

# Speeding up the short video
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('sped_up_result.mp4')

from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('girl.jpg')

# Ubah ukuran gambar jika terlalu besar
image = image.resize((400, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack(side="top", fill="both", expand=True)

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(side="bottom")

# Menjalankan loop acara Tkinter
root.mainloop()
