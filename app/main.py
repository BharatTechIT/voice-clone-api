from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from fastapi.responses import FileResponse

import uuid
import shutil

from  .voice_clone import clone_voice

app = FastAPI(
    title="Voice Clone API",
    version="1.0"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Voice Clone API Running"
    }


@app.post("/clone")
async def clone(
    text: str = Form(...),
    audio: UploadFile = File(...)
):

    file_name = f"app/uploads/{uuid.uuid4()}.wav"

    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    generated_audio = clone_voice(
        text=text,
        speaker_wav=file_name
    )

    return FileResponse(
        generated_audio,
        media_type="audio/wav",
        filename="output.wav"
    )