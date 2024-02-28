import { useEffect, useState } from "react";
import "./App.css";
import { io } from "socket.io-client";

const backend = import.meta.env.DEV ? "http://localhost:9999" : "";
console.log("backend:", backend);
const socket = io(backend);

function App() {
  const [msg, setMsg] = useState<string[]>([]);

  useEffect(() => {
    socket.on("message", (msg: string) => {
      setMsg((prev) => [...prev, msg]);
    });
    return () => {
      socket.off("message");
    };
  }, []);

  return (
    <div>
      {msg.map((m, i) => (
        <p key={i}>{m}</p>
      ))}
    </div>
  );
}

export default App;
