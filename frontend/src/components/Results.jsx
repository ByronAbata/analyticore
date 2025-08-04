export default function Results({ data }) {
  return (
    <div>
      <h3>Resultados:</h3>
      <p>Sentimiento: {data.sentiment_score}</p>
      <p>Palabras clave: {data.keywords.join(', ')}</p>
    </div>
  );
}
