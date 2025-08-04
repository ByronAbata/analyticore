import { useEffect, useState } from 'react';
import { getJobStatus } from '../services/api';
import Results from './Results';

export default function JobStatus({ jobId }) {
  const [status, setStatus] = useState('PENDING');
  const [result, setResult] = useState(null);

  useEffect(() => {
    const interval = setInterval(async () => {
      const res = await getJobStatus(jobId);
      setStatus(res.status);
      if (res.status === 'COMPLETED') {
        setResult(res);
        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [jobId]);

  return (
    <div>
      <p>Estado: {status}</p>
      {result && <Results data={result} />}
    </div>
  );
}
