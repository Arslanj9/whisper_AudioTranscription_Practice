from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from whisper_services.transcribe_module import transcribe_audio
from whisper_services.translate_module import translate_audio

app = FastAPI()

# Allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# -------------------------------
# ------------- ROUTES ----------
# -------------------------------

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    return await transcribe_audio(file)

@app.post("/translate")
async def translate(file: UploadFile = File(...)):
    return await translate_audio(file)
