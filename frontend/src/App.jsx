import { Routes, Route, BrowserRouter } from "react-router-dom";
import Transcribe from "./pages/Transcribe";
import Navbar from "./components/Navbar";
import Translate from "./pages/Translate";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Transcribe />} />
        <Route path="/translate" element={<Translate />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
