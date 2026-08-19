'use client'

import { useState } from 'react';

    const FormNome = () => {
        const [nome, setNome] = useState('')
    return (
        <div>
            <input
                value={nome} onChange={e => setNome(e.target.value)} placeholder="Seu Nome"
            />
            <p>
                Olá, {nome || 'Visitante'}!
            </p>
        </div>
    );
}

export default FormNome