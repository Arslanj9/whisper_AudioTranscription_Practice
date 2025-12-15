import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "12px", background: "#eee" }}>
      <Link
        to="/"
        style={{
          marginRight: "12px",
          padding: "8px 16px",
          textDecoration: "none",
          background: "#e6e6e6",
          color: "#333",
          borderRadius: "6px",
          fontSize: "15px",
          border: "1px solid #ccc",
          transition: "0.2s",
        }}
        onMouseEnter={(e) => (e.target.style.background = "#d4d4d4")}
        onMouseLeave={(e) => (e.target.style.background = "#e6e6e6")}
      >
        Transcribe
      </Link>

      <Link
        to="/translate"
        style={{
          marginRight: "12px",
          padding: "8px 16px",
          textDecoration: "none",
          background: "#e6e6e6",
          color: "#333",
          borderRadius: "6px",
          fontSize: "15px",
          border: "1px solid #ccc",
          transition: "0.2s",
        }}
        onMouseEnter={(e) => (e.target.style.background = "#d4d4d4")}
        onMouseLeave={(e) => (e.target.style.background = "#e6e6e6")}
      >
        Translate
      </Link>

      {/* <Link to="/c" style={{ marginRight: "20px" }}>C</Link> */}
      {/* <Link to="/d">D</Link> */}
    </nav>
  );
}
