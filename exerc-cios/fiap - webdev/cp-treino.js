// ## Calculadora de Desconto (2 pontos)
// **Enunciado:**
// Implemente a função calcularDesconto, que recebe preco e desconto 
// (percentual de 0 a 100).
// A função deve:
// - Retornar "Preço inválido." se preco não for número ou for menor que 0.
// - Retornar "Desconto inválido." se desconto não for número, for menor que 0 
// ou maior que 100.
// - Caso válido, calcular precoFinal = preco - (preco * desconto / 100)
//   e retornar a string: "De R$ <preco> por R$ <precoFinal>."
//   onde precoFinal deve ter 2 casas decimais.
//
// Exemplos:
//   calcularDesconto(100, 20)  → "De R$ 100 por R$ 80.00."
//   calcularDesconto(49.9, 10) → "De R$ 49.9 por R$ 44.91."
//   calcularDesconto(-10, 20)  → "Preço inválido."
//   calcularDesconto(100, 110) → "Desconto inválido."


function calculeDesconto(preco, desconto){
  if(typeof preco !== "number" || preco <= 0 ){
    return 'Preço inválido.'
  };
  if(typeof desconto !== "number" || desconto < 0 || desconto > 100){
    return "Desconto inválido."
  };
  const precoFinal = preco - (preco * desconto / 100);
  return `De R$ ${preco} por R$ ${precoFinal.toFixed(2)}.`
};

//

// ## Debug: Calculadora de Multa por Atraso (2 pontos)
// **Enunciado:**
// A função abaixo deveria calcular o valor total de uma conta com multa por atraso.
// Ela recebe valorOriginal (número) e diasAtraso (número) e deve:
// - Retornar "Valor inválido." se valorOriginal OU diasAtraso não for número.
// - Retornar "Valor inválido." se valorOriginal OU diasAtraso menor que 0.
// - Se diasAtraso maior que 0, usar um loop DO WHILE para somar R$10 de multa por cada dia de atraso.
// - Retornar a string "Total: R$ <valor>" onde valor tem 2 casas decimais.
//
// O código abaixo contém 5 erros. Encontre e corrija todos eles.
//
// Exemplos esperados após a correção:
//   calcularMulta(100, 3)   → "Total: R$ 130.00"
//   calcularMulta(50, 0)    → "Total: R$ 50.00"
//   calcularMulta(200, 1)   → "Total: R$ 210.00"
//   calcularMulta(-10, 3)   → "Valor inválido."
//   calcularMulta(100, -1)  → "Valor inválido."
//   calcularMulta("100", 3) → "Valor inválido."

function calcularMulta(valorOriginal, diasAtraso){
  if(typeof valorOriginal !== "number" || typeof diasAtraso !== "number" || isNaN(valorOriginal) || isNaN(diasAtraso)){
    return "Valor inválido.";
  };
  if(valorOriginal < 0 || diasAtraso < 0){
    return "Valor inválido.";
  };
  let total = valorOriginal;
  let dia = 1;

  if(diasAtraso > 0){
    do{
      total += 10;
      dia++
    }while(dia <= diasAtraso);
  };
  return `Total: R$ ${total.toFixed(2)}`;
};

// ## Conversor de Moeda (2 pontos)
// **Enunciado:**
// Implemente a função converterMoeda, que recebe:
// valor, moeda atual, moeda a ser convertida (caso nenhum valor 
// seja fornecido em moeda a ser convertida, o padrão deve ser "USD").
//
// Taxas de conversão a partir de BRL:
//   BRL → USD: dividir por 5.70
//   BRL → EUR: dividir por 6.20
//   BRL → GBP: dividir por 7.10
//
// A função deve:
// - Retornar "Valor inválido." se valor não for número ou for menor que 0.
// - Retornar "Moeda de origem inválida." se moeda atual não for "BRL".
// - Retornar "Moeda de destino inválida." se moeda a ser convertida não for "USD", "EUR" ou "GBP".
// - Caso válido, retornar: "R$ <valor> = <resultado> <moeda_a_ser_convertida>"
//   onde resultado tem 2 casas decimais.
//
// Exemplos:
//   converterMoeda(100, "BRL")        → "R$ 100 = 17.54 USD"
//   converterMoeda(100, "BRL", "EUR") → "R$ 100 = 16.13 EUR"
//   converterMoeda(-50, "BRL")        → "Valor inválido."
//   converterMoeda(100, "USD")        → "Moeda de origem inválida."

function converterMoeda(valor, moedaAtual, moedaDestino = "USD"){
  if(typeof valor !== "number" || valor <= 0){
    return "Valor inválido.";
  };
  if(moedaAtual !== "BRL"){
    return "Moeda de origem inválida.";
  };
  const moedas ={
    USD: 5.70,
    EUR: 6.20,
    GBP: 7.10
  };
  if(!moedas[moedaDestino]){
    return "Moeda de destino inválida.";
  };
  const resultado = (valor / moedas[moedaDestino]).toFixed(2);
  return `R$ ${valor} = ${resultado} ${moedaDestino}`;
//

// ## Descrição de Soma (2 pontos)
// **Enunciado:**
// Implemente a função descreverSoma, que recebe dois valores: a e b.
// A função deve:
// - Verificar se AMBOS são números.
// - Retornar "Valores inválidos." se qualquer um não for número.
// - Retornar a string "A soma de <a> e <b> é <resultado>." caso válido.
//
// Exemplos:
//   descreverSoma(3, 7)    → "A soma de 3 e 7 é 10."
//   descreverSoma("3", 7)  → "Valores inválidos."
//   descreverSoma(5, true) → "Valores inválidos."

function descreverSoma(a, b){
  if(typeof a !== "number" || typeof b !== "number" || isNaN(a) || isNaN(b)){
    return "Valores inválidos.";
  }
  const resultado = a + b;

  return `A soma de ${a} e ${b} é ${resultado}.`;
}

// 

// ## Lançador de Dados (2 pontos)
// **Enunciado:**
// Implemente a função lancarDados, que recebe um número inteiro n
// (quantidade de lançamentos de um dado de 6 faces).
//
// A função deve:
// - Retornar "Inválido." se n não for número, for NaN, menor que 0 ou não inteiro.
// - Caso válido, usar um loop FOR para simular n lançamentos,
//   gerando números inteiros aleatórios de 1 a 6.
// - Retornar a string:
//   "Lançamentos: <n> | Soma: <soma> | Maior: <maior> | Menor: <menor>"
//
// Exemplos (valores aleatórios, mas formato sempre igual):
//   lancarDados(5) → "Lançamentos: 5 | Soma: 18 | Maior: 6 | Menor: 2"
//   lancarDados(0) → "Inválido."
//   lancarDados(1.5) → "Inválido."

function lancarDados(n){
  if(typeof n !== "number" || isNaN(n) || n <= 0 || n % 1 !== 0){
    return "Inválido.";
  }

  let soma = 0;
  let maior = 0;
  let menor = 6;

  for(let i = 0; i < n; i++){
    let resultado = Math.floor(Math.random() * 6) + 1;

    soma += resultado;

    if(resultado > maior){
      maior = resultado;
    };
    if(resultado < menor){
      menor = resultado;
    };
  };

  return `Lançamentos: ${n} | Soma: ${soma} | Maior: ${maior} | Menor: ${menor}`;
};

// ## Lançador de Dados (2 pontos)
// **Enunciado:**
// Implemente a função lancarDados, que recebe um número inteiro n
// (quantidade de lançamentos de um dado de 6 faces).
//
// A função deve:
// - Retornar "Inválido." se n não for número, for NaN, menor que 0 ou não inteiro.
// - Caso válido, usar um loop FOR para simular n lançamentos,
//   gerando números inteiros aleatórios de 1 a 6.
// - Retornar a string:
//   "Lançamentos: <n> | Soma: <soma> | Maior: <maior> | Menor: <menor>"
//
// Exemplos (valores aleatórios, mas formato sempre igual):
//   lancarDados(5) → "Lançamentos: 5 | Soma: 18 | Maior: 6 | Menor: 2"
//   lancarDados(0) → "Inválido."
//   lancarDados(1.5) → "Inválido."
function lancarDados(n){
  if(typeof n !== "number" || isNaN(n) || n <= 0 || n % 1 !== 0){
    return "Inválido.";
  }

  let soma = 0;
  let maior = 0;
  let menor = 6;

  for(let i = 0; i < n; i++){
    let resultado = Math.floor(Math.random() * 6) + 1;

    soma += resultado;

    if(resultado > maior){
      maior = resultado;
    }
    if(resultado < menor){
      menor = resultado;
    }
  }

  return `Lançamentos: ${n} | Soma: ${soma} | Maior: ${maior} | Menor: ${menor}`;
}
