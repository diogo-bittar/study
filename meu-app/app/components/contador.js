'use client'

import { useState } from 'react';

export default function Contador() {
    const [valor, setValor] = useState(0);

    function incrementar() {
        setValor(valor + 1); // atualização baseada no valor atual
    }

    return (
        <div>
            <p>Valor: {valor}</p>
            <button onClick={incrementar}>Adicionar</button>
        </div>
    );
}