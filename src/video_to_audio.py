from moviepy.editor import VideoFileClip

def extract_audio(video_path: str, audio_filename: str = "audio.wav") -> str:
    """
    Extracts audio from the given video and saves it as a WAV file.
    """
    print("🔊 Extracting audio from video...")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_filename)
    print(f"Audio saved as {audio_filename}")
    return audio_filename
