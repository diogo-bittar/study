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

const fila = [];
let opc = "";

do{

    opc = prompt("Escolha uma opção:\nVIP, REGULAR, ATENDER ou SAIR. ").toUpperCase();

    if(opc === "VIP"){
        let name = prompt("Nome do cliente VIP: ");
        fila.unshift(name);
    } else if(opc === "REGULAR"){
        let name = prompt("Nome do cliente REGULAR: ");
        fila.push(name);
    } else if(opc === "ATENDER"){
        if(fila.length > 0){
            let atendido = fila.shift();
            alert(`Atendendo: ${atendido}.`);
        }else{
            alert("A fila está vazia.");
        }
    }
    if(opc !== "SAIR"){
        console.log(`Fila atual: ${fila}.`)
        alert(`Fila atual: ${fila},\n.`)
    }
} while(opc !== "SAIR");
