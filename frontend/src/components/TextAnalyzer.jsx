import { useState } from 'react';
import { submitText } from '../services/api';

export default function TextAnalyzer({ setJobId }) {
  const [text, setText] = useState('');

  const handleSubmit = async () => {
    const res = await submitText(text);
    setJobId(res.jobId);
  };

  return (
    <div>
      <textarea value={text} onChange={e => setText(e.target.value)} />
      <br />
      <button onClick={handleSubmit}>Enviar</button>
    </div>
  );
}
