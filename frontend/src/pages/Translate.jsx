import { useState } from "react";
import axios from "axios";

export default function Translate() {
  const [file, setFile] = useState(null);
  const [translation, setTranslation] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://127.0.0.1:8000/translate",
      formData
    );

    setTranslation(response.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Whisper Audio Translation</h1>
      <input
        type="file"
        accept="audio/*"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Translate</button>

      {translation && (
        <div style={{ marginTop: 20 }}>
          <h2>Detected Language: {translation.detected_language}</h2>
          <h2>Full English Translation:</h2>
          <p>{translation.full_text}</p>

          <h3>Segments:</h3>
          <ul>
            {translation.segments.map((seg, index) => (
              <li key={index}>
                {seg.start}s - {seg.end}s : {seg.text}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
