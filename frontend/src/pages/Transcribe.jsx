import { useState } from "react";

export default function Transcribe() {
  const [file, setFile] = useState(null);
  const [transcription, setTranscription] = useState("");
  const [detectedLanguage, setDetectedLanguage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/transcribe", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);

    setTranscription(data.transcription);
    setDetectedLanguage(data.detected_language); // <-- store detected language
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Whisper Audio Transcription</h1>

      <input
        type="file"
        accept="audio/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>Transcribe</button>

      <h2>Transcription:</h2>
      <p>{transcription}</p>

      <h2>Detected Language:</h2>
      <p>{detectedLanguage}</p> {/* <-- display detected language */}
    </div>
  );
}
