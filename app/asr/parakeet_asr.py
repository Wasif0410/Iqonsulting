import nemo.collections.asr as nemo_asr



# Load Parakeet ASR model once
asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="nvidia/parakeet-tdt-0.6b-v2")

def transcribe_audio(audio_file_path):
    """
    Transcribes the given audio file using NVIDIA's Parakeet ASR model.
    """
    result = asr_model.transcribe([audio_file_path])
    return result[0]
