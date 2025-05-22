import wave

def get_audio_duration(file_path):
    """
    Returns duration (in seconds) of a .wav audio file.
    """
    with wave.open(file_path, 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        return frames / float(rate)
