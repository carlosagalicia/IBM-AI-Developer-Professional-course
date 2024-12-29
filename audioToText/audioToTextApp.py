from flask import Flask, request
import whisper

app = Flask(__name__)
model = whisper.load_model("base")


@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return {"error": "No audio file provided"}, 400

    audio_file = request.files["audio"]
    # Save the audio file temporarily
    audio_path = "temp_audio.mp3"
    audio_file.save(audio_path)

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Return the transcription
    return {"transcription": result["text"]}


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=8000)
