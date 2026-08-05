let produto;
do{
    produto = prompt('Informe o nome do produto: ');
    if(produto === null) produto = '';
    if(produto.length < 2){
        alert('Produto com menos de 2 caracteres não existe.');
    }
}while(produto.length < 2);

let quantidade;
do{
    quantidade = Number(prompt('Qual seria a quantidade deste produto?: '));
    if(isNaN(quantidade) || quantidade < 1){
        alert('Quantidade negativa ou igual a zero (0).');
    }
    else if(quantidade > 1000){
        alert('Quantidade acima do limite.');
    }
}while (isNaN(quantidade) || quantidade < 1 || quantidade > 1000);

let desconto;
do{
    desconto = parseFloat(prompt('Qual o valor do desconto que será aplicado?: '));
    if(isNaN(desconto) || desconto < 0){
        alert('Desconto negativo não pode, tente novamente.');
    }
    else if(desconto > 100){
        alert('Desconto ultrapassou de 100%.');
    }
}while(isNaN(desconto) || desconto < 0 || desconto > 100);

let categoria;
do{
    categoria = prompt('Qual a categoria desse produto? (A / B / C): ');
    if(categoria === null) categoria = '';
    categoria = categoria.toUpperCase();
    if(categoria !== "A" && categoria !== "B" && categoria !== "C"){
        alert('Categoria não encontrada.');
    }
}while(categoria !== "A" && categoria !== "B" && categoria !== "C");

let pagamento;
do{
    pagamento = prompt('Qual seria a forma de pagamento? (D / C / P):');
    if(pagamento === null) pagamento = '';
    pagamento = pagamento.toUpperCase();
    if(pagamento !== "D" && pagamento !== "C" && pagamento !== "P"){
        alert('Forma de pagamento não encontrada.');
    }
}while(pagamento !== "D" && pagamento !== "C" && pagamento !== "P");

alert(`Confira as informações abaixo:\n
    PRODUTO: ${produto}\n
    QUANTIDADE: ${quantidade}\n
    DESCONTO: ${desconto}%\n
    CATEGORIA: ${categoria}\n
    PAGAMENTO: ${pagamento}`);
//-----------------------------------------------------------//
