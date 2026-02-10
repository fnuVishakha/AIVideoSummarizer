import whisper

def audio_to_text(audio_path):
    print("📝 Converting audio to text with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]
