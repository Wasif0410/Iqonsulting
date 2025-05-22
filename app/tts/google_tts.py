from google.cloud import texttospeech

def synthesize_text(text, output_filename):
    """
    Uses Google Cloud TTS to synthesize the given text and save it as a .wav file.
    """
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print(f"✔ Audio written to {output_filename}")
