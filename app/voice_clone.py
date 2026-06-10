import os

os.environ["COQUI_TOS_AGREED"] = "1"



from TTS.api import TTS
import uuid


print("Loading XTTS Model...")

tts = TTS(
    "tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=False,
    gpu=False
)

print("Model Loaded")


def clone_voice(text, speaker_wav):
    
    output_file = f"app/outputs/{uuid.uuid4()}.wav"
    
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language="en",
        file_path=output_file
    )

    return output_file