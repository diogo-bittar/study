export default function Home() {

  // Logica do componente
  const ativo = false;
  const estilo = { padding: '8px', borderRadius: '6px' }
  const url = 'https://react.dev';
  const contagem = 3;

  return (
    <>

      <a href={url} target="_blank" rel="noreferrer">Site</a>
      <p>Você tem {contagem} novas mensagens.</p>
      <button
        style={{ padding: '8px', borderRadius: '6px' }}
        className={ativo ? 'btn btn-primary' : 'btn btn-outline'}
      >
        Botão
      </button>
    </>
  )
}
