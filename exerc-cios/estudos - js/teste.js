function parImpar(number){
    let multiple = number % 2 === 0;
    if(multiple){
        return `${number} é par.`
    }
    return `${number} é ímpar`
}


function saque(valor) {
    if (typeof valor !== "number" || isNaN(valor) || valor <= 0) {
        return "Saque / Valor inválido.";
    }

    if (valor % 10 === 0) {
        return "Saque / Valor aprovado.";
    }

    return "Saque / Valor inválido.";
};

