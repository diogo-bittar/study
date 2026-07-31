// // 1)
// let array = prompt("Retorne um nome: ");
// let arrayInverse = "";
// for(let i = array.length -1; i >= 0; i--){
//     arrayInverse += array[i];
// }

// alert(arrayInverse);

// 2)
// let expressao = prompt("Digite a expressão matemática: ");
// let list = [];
// let eValida = true; 

// for(let i = 0; i < expressao.length; i++){
//     let caractere = expressao[i];

//     if(caractere == "(" || caractere == "[" || caractere == "{"){
//         list.push(caractere);
//     } else if(caractere == ")" || caractere == "]" || caractere == "}"){
//         let topo = list.pop();

//         if(
//             (caractere == ")" && topo != "(") ||
//             (caractere == "]" && topo != "[") ||
//             (caractere == "}" && topo != "{")
//         ){
//             eValida = false;
//             break;
//         }
//     }
// }


// if(eValida && list.length === 0) {
//     alert("Expressão válida.");
// } else {
//     alert("Expressão inválida.");
// }


// 4)
// const isPallindrome = prompt("Informe a palavra: ");
// const result = isPallindrome.replace(/\s+/g, '').toLowerCase();

// let inverse = "";

// for(let i = result.length - 1; i >= 0; i--){
//     inverse += result[i]
// }

// if(result === inverse){
//     alert("É um palíndromo!");
// }else {
//     alert("Não é um palíndromo!");
// }

// 5)

// const fila = [];
// let opc = "";

// do{

//     opc = prompt("Escolha uma opção:\nVIP, REGULAR, ATENDER ou SAIR. ").toUpperCase();

//     if(opc === "VIP"){
//         let name = prompt("Nome do cliente VIP: ");
//         fila.unshift(name);
//     } else if(opc === "REGULAR"){
//         let name = prompt("Nome do cliente REGULAR: ");
//         fila.push(name);
//     } else if(opc === "ATENDER"){
//         if(fila.length > 0){
//             let atendido = fila.shift();
//             alert(`Atendendo: ${atendido}.`);
//         }else{
//             alert("A fila está vazia.");
//         }
//     }
//     if(opc !== "SAIR"){
//         console.log(`Fila atual: ${fila}.`)
//         alert(`Fila atual: ${fila},\n.`)
//     }
// } while(opc !== "SAIR");


// ex 6

// Enunciado: Dada uma matriz 3 x 3 com números inteiros (positivos e negativos), itere pela matriz para calcular a soma dos elementos da diagonal principal e, simultaneamente, conte quantos números negativos existem na matriz inteira.
// Recursos que devem ser utilizados:Matriz bidimensional (array de arrays).
// Duas variáveis numéricas de estado inicializadas em zero (soma e contador).
// Dois laços de repetição aninhados (controle de índice de linha e coluna).
// Estrutura condicional para comparar a equivalência dos índices (diagonal).Estrutura condicional para avaliar se o valor armazenado na coordenada é menor que zero.

// const matriz = [
//   [1, 2, 10],
//   [4, 2, 1],
//   [3, -1, 3]
// ];

// let soma = 0;
// let contador = 0;

// for(let i = 0; i < matriz.length; i++){
//     for(let j = 0; j < matriz[i].length; j++){
//         if(i === j){
//             soma += matriz[i][j];
//         }
//         if(matriz[i][j] < 0){
//             contador++
//         }
//     }
// }

// alert(`Soma da diagonal: ${soma}`);
// alert(`Qtd de números negativos: ${contador}`);

// ex 7

// Enunciado: Dado um vetor de números desordenado, identifique e exiba o segundo maior valor presente na estrutura.
// Restrição obrigatória: É expressamente proibido o uso de funções nativas de ordenação ou busca, como .sort() ou Math.max().
//  A resolução deve ser construída manualmente utilizando laço de repetição e lógica condicional.

// const vetor = [12, 35, 1, 10, 34, 1];

// let maior = vetor[0];
// let segundoMaior = Infinity;

// for(let i = 0; i < vetor.length; i++){
//     if(vetor[i] > maior){
//         segundoMaior = maior;
//         maior = vetor[i];
//     }else if(vetor[i] > segundoMaior && vetor[i] !== maior){
//         segundoMaior = vetor[i];
//     }
// }

// console.log(segundoMaior);

// ex 8

// Enunciado: Mova todos os zeros de um vetor para o final, mantendo a ordem original dos outros elementos não-nulos.

// O que usar: Dois ponteiros (índices) ou um loop e manipulação direta de posições sem criar um vetor novo.

// Dica: Vá jogando os elementos que não são zero para a primeira posição disponível no início do vetor.

const vetorEx8 = [0, 1, 6, 3, 12];
let lastZero = 0;

console.log(vetorEx8)
for (let i = 0; i < vetorEx8.length; i++) {
    if (vetorEx8[i] !== 0) {
        let temp = vetorEx8[i];
        vetorEx8[i] = vetorEx8[lastZero];
        vetorEx8[lastZero] = temp;
        lastZero++;
    }
}

console.log(vetorEx8); // Retorno: [1, 3, 12, 0, 0]