import shutil
import whisper
from fastapi import UploadFile

# Load Whisper model once (shared within this module)
model = whisper.load_model("base")

async def translate_audio(file: UploadFile):
    # Save uploaded file temporarily
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Load and preprocess audio
    audio = whisper.load_audio(temp_file)
    audio = whisper.pad_or_trim(audio)

    # Translate to English
    result = model.translate(audio)

    # Close file
    file.file.close()

    # Return structured response
    return {
        "detected_language": result.get("language", "unknown"),
        "full_text": result.get("text", ""),
        "segments": [
            {
                "start": seg.get("start"),
                "end": seg.get("end"),
                "text": seg.get("text")
            }
            for seg in result.get("segments", [])
        ]
    }
