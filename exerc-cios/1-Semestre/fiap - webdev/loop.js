//Aula JS sobre loops

//while 
function aumentarNumero(numero){
    while(numero < 10){
        console.log(numero);
        numero++; //somando até chegar em 10
        //i-- diminui
        //i+=2 soma de dois em dois
    }
}

//-----------------------------------------------------------//
//exercício 
//function numeroRegressivo(numer){
    //while (numer >= 1){
        //console.log(numer)
        //numer--
    //}
//}
//const numer = Number(prompt('Informe um número por favor: '))

//------------------------------------------------------------//

//do while
let count = 0; //criar variável fora
do{
    console.log(count);
    count++;
} while(count < 5)
//------------------------------------------------------------//
let nome;
let idade;
let salario;
let genero;
let civil;

//nome
do{
    nome = prompt('Qual o seu nome?: ');
    if(nome.length < 3){
        alert('O nome precisa ter mais de 2 caracteres.');
    }
}while(nome.length < 3)

//idade
do{
    idade = Number(prompt('E qual é a sua idade?: '));
    if(isNaN(idade) || idade <= 0){
        alert('Idade não encontrada');
    }
    else if(idade > 150){
        alert('Idade ultrapassou o limite fornecido.');
    }
}while(isNaN(idade) || idade <= 0 || idade > 150);

//salário
do{
    salario = parseFloat(prompt('Qual seria o seu salário atualmente?: '));
    if(isNaN(salario) || salario <= 0){
        alert('O valor precisa ser positivo.');
    }
}while(isNaN(salario) || salario <= 0);

//gênero
do{
    genero = prompt('Informe o seu gênero (F / M): ').toUpperCase();
    if(genero !== "F" && genero !== "M"){
        alert('Gênero não encontrado.')
    }
}while(genero !== "F" && genero !== "M");

//civil 
do{
    civil = prompt('Por fim, informe o seu estado civil (S / C / V / D): ').toUpperCase();
    if(civil !== "S" && civil !== "C" && civil !== "V" && civil !== "D"){
        alert('Estado civil inválido.');
    }
}while(civil !== "S" && civil !== "C" && civil !== "V" && civil !== "D");

alert(`Suas informações abaixo, confere:\n
    NOME:${nome}\n
    IDADE:${idade}\n
    SALÁRIO:${salario}\n
    GÊNERO:${genero}\n
    ESTADO CIVIL:${civil}`)

//for

//loops infinitos