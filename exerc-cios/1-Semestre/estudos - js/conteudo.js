// CONTEÚDO DE JAVASCRIPT;
// //----------------------//
// 1.
// Tipos de alerta;
alert();
prompt();
confirm();

//----------------------//
// Console.log vai ser o mais utilizado na CP
// Console.log() --> serve para interagir em tempo real com o JS em uma página WEB

//----------------------//

// Variáveis;
let // var // const

var name = "diogo";
let age = "18";  //o valor pode variar
const pi = 3.142; //valor fixo
// -----------------------------------------
// Exercício pós sessão;
let nome = prompt('Informe o seu nome: ');

let idade = Number(prompt('Informe a sua idade: '));

let profissao = prompt('Qual a sua profissão?: ');

alert(`Olá ${nome}, você tem ${idade} anos e a sua profissão é ${profissao}.`);

//----------------------------------------//
// 2. Operadores e condicionais.
// Operadores de Comparação em JavaScript

// ==   → Igual a (só valor)
// ===  → Igual em valor E tipo
// !=   → Diferente (só valor)
// !==  → Diferente em valor OU tipo
// <    → Menor que
// >    → Maior que
// <=   → Menor ou igual a
// >=   → Maior ou igual a
// %% 'e'
// || "ou"
// ! "não"
// ex 1

let distanciaMetros = Number(prompt('Informe uma distância em metros: '));

let distanciaCentimetros = distanciaMetros * 100;

alert(`Distância em cm: ${distanciaCentimetros}cm.`);
//--------------------------------------------//
// === ENTRADA ===
let peso = Number(prompt("Digite seu peso em kg:"));
let altura = Number(prompt("Digite sua altura em metros:"));

// === PROCESSAMENTO ===
let imc = peso / (altura * altura);

// === SAÍDA ===
alert(`Seu IMC é: ${imc.toFixed(2)}`);

// 0bs: o toFixed(2) é usado para limitar o número de casas decimais a 2,
// tornando a saída mais legível.

// Operadores - ex 2
let peso = Number(prompt("Informe o peso do produto em gramas (g): "));

let preco = (peso / 100) * 5;

alert(`Total: ${preco.toFixed(2)}.`);


//--------------------------------------//
//ex 3
let usuario = prompt('Qual o seu usuário?: ');
let senha = prompt('Agora informe a sua senha: ');

if(usuario === "1234" && senha === "1234"){
    alert('Seja bem-vindo(a).');

}
else{
    alert('usuario ou senha incorretos.')
}


//ex de ordem alfabetica
let nome1 = "Carlos";
let nome2 = "Ana";
let nome3 = "Bruno";
// Vamos comparar os nomes dois a dois para descobrir a ordem alfabética
let primeiro, segundo, terceiro;

if (nome1 < nome2 && nome1 < nome3) {
	primeiro = nome1;
	if (nome2 < nome3) {
		segundo = nome2;
		terceiro = nome3;
	} else {
		segundo = nome3;
		terceiro = nome2;
	}
} else if (nome2 < nome1 && nome2 < nome3) {
	primeiro = nome2;
	if (nome1 < nome3) {
		segundo = nome1;
		terceiro = nome3;
	} else {
		segundo = nome3;
		terceiro = nome1;
	}
} else {
	primeiro = nome3;
	if (nome1 < nome2) {
		segundo = nome1;
		terceiro = nome2;
	} else {
		segundo = nome2;
		terceiro = nome1;
	}
}

console.log(`Ordem alfabética: ${primeiro}, ${segundo}, ${terceiro}`);

