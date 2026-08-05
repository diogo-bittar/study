/******************************************************************************
 * GUIA COMPLETO: MANIPULAÇÃO DE DADOS E ESTRUTURAS DE REPETIÇÃO
 * Fontes: Apostila de Objetos Pré-definidos & Slides de Loops
 ******************************************************************************
 * 
 * --- PARTE 1: CONTEÚDO ESCRITO (TEORIA E MÉTODOS) ---
 * 
 * 1. STRINGS (IMUTÁVEIS):
 *    - Busca: .includes() (existe?), .startsWith()/.endsWith() (valida extensões), 
 *      .indexOf() (posição ou -1).
 *    - Limpeza: .trim(), .trimStart(), .trimEnd() (removem espaços).
 *    - Caixa: .toLowerCase(), .toUpperCase() (normalização para busca).
 *    - Troca: .replace() (1ª ocorrência) e .replaceAll() ou regex /g (todas).
 *    - Formatação: .padStart(total, char) e .padEnd() (ex: formatar "05:01").
 *    - Extração: .slice(inicio, fim) e .split(separador) para gerar Arrays.
 * 
 * 2. NUMBER & MATH:
 *    - Nuance: JS usa IEEE 754 (floats 64 bits), logo 0.1 + 0.2 !== 0.3.
 *    - Number: Use Number.isNaN() (não converte) em vez do global isNaN(). 
 *      .toFixed(n) formata decimais mas RETORNA STRING.
 *    - Math: .round (próximo), .ceil (teto), .floor (chão), .trunc (corta decimais).
 *      .random() gera 0-1. Fórmula p/ inteiros: Math.floor(Math.random() * (max - min + 1)) + min.
 * 
 * 3. DATE VS TEMPORAL:
 *    - Date: Mutável (perigoso!). Meses 0-indexed (Janeiro = 0). 
 *      Comparar datas requer .getTime() pois objetos são diferentes.
 *    - Temporal (Novo): Imutável. Meses 1-indexed (Janeiro = 1). 
 *      Aritmética legível com .add({ days: 3 }) e .subtract().
 * 
 * 4. LOOPS E LÓGICA:
 *    - While: Teste no início (repetição incerta).
 *    - Do While: Teste no fim (executa pelo menos 1 vez).
 *    - For: Ciclo fechado (inicialização; condição; incremento).
 *    - Operadores: +=, -=, *=, /=, %= (resto), ++, --.
 *    - Curto-Circuito: || (primeiro truthy), ?? (primeiro definido/não-null).
 *    - Falsy: false, 0, "", null, undefined, NaN.
 ******************************************************************************/

/******************************************************************************
 * --- PARTE 2: CÓDIGOS COM EXERCÍCIOS E RESOLUÇÕES ---
 ******************************************************************************/

// --- EXEMPLO PRÁTICO: FORMATAÇÃO DE DADOS ---
function exemploDados() {
    const nomeBruto = "   ANA MARIA   ";
    const nomeLimpo = nomeBruto.trim().toLowerCase(); // "ana maria"
    
    const preco = 15.5;
    console.log(`R$ ${preco.toFixed(2).replace(".", ",")}`); // "R$ 15,50"
    
    // Temporal: Próxima segunda-feira
    const hoje = Temporal.Now.plainDateISO();
    const diasParaSeg = (8 - hoje.dayOfWeek) % 7 || 7;
    console.log("Próxima Seg:", hoje.add({ days: diasParaSeg }).toLocaleString("pt-BR"));
}

// --- RESOLUÇÃO DOS 5 DESAFIOS (PASSO A PASSO) ---

/**
 * DESAFIO 1: Contagem Regressiva
 * Lógica: Validar se é número, se é positivo e inteiro. Loop while decrementando.
 */
function desafio1() {
    const num = Number(prompt('Informe um número: '));
    if (Number.isNaN(num) || num <= 0 || !Number.isInteger(num)) {
        console.error("Número inválido! Digite um inteiro positivo.");
        return;
    }
    let i = num;
    while (i >= 1) {
        console.log(i);
        i--;
    }
}

/**
 * DESAFIO 2: Validação de Formulário
 * Lógica: Bloquear o usuário em loops do...while até que os critérios sejam aceitos.
 */
function desafio2() {
    let nome, idade, salario, genero, estadoCivil;

    do { nome = prompt("Nome (> 3 letras):"); } while (!nome || nome.length <= 3);
    do { idade = Number(prompt("Idade (0-150):")); } while (isNaN(idade) || idade < 0 || idade > 150);
    do { salario = Number(prompt("Salário (> 0):")); } while (isNaN(salario) || salario <= 0);
    do { genero = prompt("Gênero (f/m):").toLowerCase(); } while (genero !== 'f' && genero !== 'm');
    do { 
        estadoCivil = prompt("Estado Civil (s/c/v/d):").toLowerCase(); 
    } while (!['s', 'c', 'v', 'd'].includes(estadoCivil));

    alert(`Cadastro sucesso! Salário formatado: R$ ${salario.toFixed(2)}`);
}

/**
 * DESAFIO 3: Jogo de Adivinhação
 * Lógica: Sorteio inicial. Loop do...while comparando palpite com o sorteado.
 */
function desafio3() {
    const sorteado = Math.floor(Math.random() * 10) + 1;
    let palpite, tentativas = 0;

    do {
        palpite = Number(prompt("Chute de 1 a 10:"));
        tentativas++;
        if (palpite < sorteado) alert("Maior!");
        else if (palpite > sorteado) alert("Menor!");
    } while (palpite !== sorteado);

    alert(`Parabéns! Levou ${tentativas} tentativas.`);
}

/**
 * DESAFIO 4: Tabuada
 * Lógica: Loop for de 1 a 10, acumulando resultados em uma string para exibição única.
 */
function desafio4(n) {
    let output = `Tabuada do ${n}:\n`;
    for (let i = 1; i <= 10; i++) {
        output += `${n} x ${i} = ${n * i}\n`;
    }
    console.log(output);
}

/**
 * DESAFIO 5: Divisores de um Número
 * Lógica: Percorrer de 1 até N. O operador de módulo (%) identifica se o resto é 0.
 */
function desafio5(n) {
    let lista = "";
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) lista += i + " ";
    }
    console.log(`Os divisores de ${n} são: ${lista}`);
}


