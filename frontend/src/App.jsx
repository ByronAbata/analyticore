import React, { useState } from 'react';
import TextAnalyzer from './components/TextAnalyzer';
import JobStatus from './components/JobStatus';

function App() {
  const [jobId, setJobId] = useState(null);

  return (
    <div className="App">
      <h1>AnalytiCore</h1>
      <TextAnalyzer setJobId={setJobId} />
      {jobId && <JobStatus jobId={jobId} />}
    </div>
  );
}

export default App;
