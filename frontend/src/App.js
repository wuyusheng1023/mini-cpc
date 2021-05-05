import { useEffect, useRef} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const ws = useRef(null);

  useEffect(() => {
    return () => {
      ws.current.close();
    };
  }, []);

  ws.current = new WebSocket("ws://localhost:8765");
  ws.current.onopen = () => console.log("ws opened");
  ws.current.onclose = () => console.log("ws closed");

  ws.current.onmessage = e => {
    const message = JSON.parse(e.data);
    console.log("e", message);
  };

  return (
    <div>
    </div>
  );
}

export default App;
