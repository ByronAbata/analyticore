import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000/api/v1';

export const submitText = async (text) => {
  const res = await axios.post(`${API_URL}/submit`, { text });
  return res.data;
};

export const getJobStatus = async (jobId) => {
  const res = await axios.get(`${API_URL}/status/${jobId}`);
  return res.data;
};
