# ------- This Whisper model is free and open source and uses local machine's resources to compute the results of transcription

import whisper

model = whisper.load_model("base")

audio = whisper.load_audio("audio2.mp3")

result = model.transcribe(audio)
print(result["text"])



# ------------This OPEN AI method will use the OPEN AI's hardware and resources in order to compute the results of transcription
# from openai import OpenAI

# client = OpenAI()
# audio_file= open("/path/to/file/audio.mp3", "rb")

# transcription = client.audio.transcriptions.create(
#     model="gpt-4o-transcribe", 
#     file=audio_file
# )

# print(transcription.text)