import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("audio_example.mp3")

# Output the transcription
print(result["text"])