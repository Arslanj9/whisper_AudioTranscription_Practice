import shutil
import whisper
import matplotlib.pyplot as plt
from fastapi import UploadFile

# <------------------------- START ------------------------------>
# <------------ TRANSCRIBE MODULE with Visualization ------------>


# Load Whisper model once (shared within this module)
model = whisper.load_model("base")

# async def transcribe_audio(file: UploadFile):
#     # Save uploaded file temporarily
#     temp_file = f"temp_{file.filename}"
#     with open(temp_file, "wb") as f:
#         shutil.copyfileobj(file.file, f)

#     # Load audio
#     audio = whisper.load_audio(temp_file)
#     original_length = len(audio)

#     # Apply pad_or_trim
#     padded_audio = whisper.pad_or_trim(audio)
#     padded_length = len(padded_audio)

#     # Visualization
#     plt.figure(figsize=(12, 4))
#     plt.plot(audio, label=f"Original ({original_length} samples)")
#     plt.plot(padded_audio, label=f"Padded/Trimmed ({padded_length} samples)", alpha=0.7)
#     plt.legend()
#     plt.title("Effect of pad_or_trim on audio")
#     plt.xlabel("Sample Index")
#     plt.ylabel("Amplitude")
#     plt.show()

#     # Transcribe
#     result = model.transcribe(padded_audio)

#     file.file.close()
#     return {
#         "transcription": result["text"],
#         "original_samples": original_length,
#         "processed_samples": padded_length
#     }


# <------------ END -------------------------------------------->



# <-----------------  START ------------------------------------>
# <------------ TRANSLATE MODULE ------------------------------->

async def transcribe_audio(file: UploadFile):
    # Save uploaded file temporarily
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Load audio
    audio = whisper.load_audio(temp_file)
    original_length = len(audio)

    # Apply pad_or_trim
    padded_audio = whisper.pad_or_trim(audio)
    padded_length = len(padded_audio)

    # Transcribe
    result = model.transcribe(padded_audio)

    file.file.close()
    return {
        "transcription": result["text"],
        "detected_language": result.get("language", "unknown"),
        "original_samples": original_length,
        "processed_samples": padded_length
    }


# <------------ END -------------------------------------------->




