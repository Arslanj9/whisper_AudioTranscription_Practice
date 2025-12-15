from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
import shutil

app = FastAPI()

# Allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load Whisper model once
model = whisper.load_model("base")



#  --------------------------------------
#  -------------  TRANSCRIBE -------------

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        shutil.copyfileobj(file.file, f)

    audio = whisper.load_audio(temp_file)
    audio = whisper.pad_or_trim(audio)
    result = model.transcribe(audio)

    file.file.close()
    return {"transcription": result["text"]}



# --------------------------------------
# -------------  TRANSLATE -------------

@app.post("/translate")
async def translate(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
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
    response = {
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

    return response