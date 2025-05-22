from tts.google_tts import synthesize_text
from asr.parakeet_asr import transcribe_audio
from utils.audio_utils import get_audio_duration

def main():
    text = "Hello, this is a test of the AI avatar system."
    audio_file = "output.wav"

    print("🔊 Synthesizing speech...")
    synthesize_text(text, audio_file)

    print("📏 Getting duration...")
    duration = get_audio_duration(audio_file)
    print(f"Duration: {duration:.2f} seconds")

    print("🧠 Transcribing audio...")
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)

if __name__ == "__main__":
    main()
