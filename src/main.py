from video_to_audio import extract_audio
from speech_to_text import audio_to_text
from nova_summarizer import summarize_with_nova

import os

def main():
    # VIDEO PATH
    video_path = os.path.join("assets", "sample_video.mp4")

    # STEP 1: Extract audio
    audio_path = extract_audio(video_path)

    # STEP 2: Convert audio to text
    transcript = audio_to_text(audio_path)
    if not transcript:
        print("⚠️ No transcript generated. Exiting.")
        return

    # STEP 3: Summarize using Nova
    final_summary = summarize_with_nova(transcript)

    # STEP 4: Print final summary
    print("\n==============================")
    print("FINAL VIDEO SUMMARY")
    print("==============================\n")
    print(final_summary)

if __name__ == "__main__":
    print("🎥 Video summarization started...")
    main()
