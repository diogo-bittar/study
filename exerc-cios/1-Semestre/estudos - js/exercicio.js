function pedirProduto() {
    let produto;
    let produtos = [];
    let mensagem = "Informe um produto ou digite 'sair' para finalizar:";

    do {
        produto = prompt(mensagem);

        if (produto === "") {
            alert("Produto inválido.");
            continue;
        }

        if (!/^[A-Za-zÀ-ÿ\s]+$/.test(produto) && produto.toLowerCase() !== "sair") {
            alert("Use apenas letras.");
            continue;
        }

        if (produto.toLowerCase() !== "sair") {
            produtos.push(produto);
            mensagem = "Deseja informar outro produto? Digite ou escreva 'sair'.";
        }

    } while (produto.toLowerCase() !== "sair");

    produtos.sort((a, b) => a.localeCompare(b));

    alert(`Confira abaixo os produtos adicionados: ${produtos}`);
}

pedirProduto()