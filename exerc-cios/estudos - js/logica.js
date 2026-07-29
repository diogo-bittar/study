// // 1)
// let array = prompt("Retorne um nome: ");
// let arrayInverse = "";
// for(let i = array.length -1; i >= 0; i--){
//     arrayInverse += array[i];
// }

// alert(arrayInverse);

// 2)
let expressao = prompt("Digite a expressão matemática: ");
let list = [];
let eValida = true; 

for(let i = 0; i < expressao.length; i++){
    let caractere = expressao[i];

    if(caractere == "(" || caractere == "[" || caractere == "{"){
        list.push(caractere);
    } else if(caractere == ")" || caractere == "]" || caractere == "}"){
        let topo = list.pop();

        if(
            (caractere == ")" && topo != "(") ||
            (caractere == "]" && topo != "[") ||
            (caractere == "}" && topo != "{")
        ){
            eValida = false;
            break;
        }
    }
}


if(eValida && list.length === 0) {
    alert("Expressão válida.");
} else {
    alert("Expressão inválida.");
}