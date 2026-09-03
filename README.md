# Study

Repositorio pessoal de estudos e exercicios de programacao. O conteudo esta organizado por semestre, curso e disciplina.

## Conteudo

- **1o semestre:** fundamentos de JavaScript e Python, logica de programacao, funcoes, listas, arquivos e exercicios web.
- **2o semestre:** Programacao Orientada a Objetos em Python, funcoes avancadas, desafios em Python e layouts com HTML/CSS.

## Estrutura

```text
exerc-cios/
├── 1-Semestre/
│   ├── estudos - js/       # Fundamentos, logica e exercicios de JavaScript
│   ├── estudos - python/   # Jogos, notas, tarefas e matrizes em Python
│   ├── estudos - udemy/    # Funcoes e fundamentos de Python
│   ├── fiap - nano/        # Cadastro de usuarios e manipulacao de arquivos
│   ├── fiap - python/      # Exercicios de listas, funcoes e numeros
│   └── fiap - webdev/      # JavaScript para paginas web
└── 2-Semestre/
    ├── backend/
    │   ├── java/           # Pasta reservada para exercicios Java
    │   └── python/         # Classes, heranca, encapsulamento e polimorfismo
    ├── curseUdemy/         # Pasta reservada para novos estudos
    └── fiap/
        ├── fiap - edge/   # Exercicios de C
        ├── fiap - frontend/# HTML, CSS Grid e Bootstrap
        └── fiap - python/ # Funcoes avancadas e desafios
```

## Principais assuntos

### Python

- Variaveis, condicionais, lacos e funcoes
- Listas, tuplas, dicionarios e validacao de dados
- CRUD em memoria e persistencia em arquivos de texto
- Jogos, cadastro de alunos, notas e tarefas
- Classes e objetos
- Encapsulamento com `property`
- Heranca e sobrescrita de metodos
- Polimorfismo, incluindo o exemplo de folha de pagamento
- Argumentos `*args`, `**kwargs` e funcoes lambda

Arquivos de referencia no 2o semestre:

- `classObjects.py`: classes, objetos, conta bancaria e estoque
- `encapsulamento.py`: propriedades, validacoes e protecao de atributos
- `heranca.py`: heranca, `super()` e sobrescrita de metodos
- `polimorfismo.py`: animais, formas geometricas e folha de pagamento
- `desafio.py`: sistema de chamados com severidade e estatisticas

### JavaScript

- Variaveis, operadores e entrada de dados
- Condicionais e estruturas de repeticao
- Arrays, strings, funcoes e validacoes
- Exercicios de palindromo, pilha, fila e matrizes
- Interacao com paginas HTML por meio de arquivos `.js`

### HTML e CSS

- Estrutura basica de paginas
- CSS Grid
- Layouts com areas de cabecalho, produtos, servicos, navegacao e rodape
- Uso do sistema de grid do Bootstrap 5 via CDN

### C

Existe um arquivo reservado para exercicio em `2-Semestre/fiap/fiap - edge`, mas ele ainda nao possui implementacao.

## Como executar

### Python

Execute um arquivo a partir da raiz do repositorio:

```powershell
python ".\exerc-cios\2-Semestre\backend\python\polimorfismo.py"
```

Para executar outro exercicio, substitua o caminho pelo arquivo desejado. Alguns programas possuem menus interativos e aguardam informacoes no terminal.

### JavaScript, HTML e CSS

Abra os arquivos `.html` no navegador. Eles carregam os arquivos JavaScript e CSS indicados no proprio HTML.

Os arquivos `.js` que nao dependem de uma pagina tambem podem ser executados com Node.js:

```powershell
node ".\exerc-cios\1-Semestre\estudos - js\teste.js"
```

## Observacoes

Este e um repositorio de estudos, por isso alguns arquivos possuem exercicios comentados, exemplos parciais ou pastas reservadas para conteudo futuro. Os arquivos mais completos podem ser executados individualmente para acompanhar cada assunto.

- `bd.txt` e usado como armazenamento simples em alguns exercicios de cadastro.
- `backend/java/` e `curseUdemy/` ainda estao vazios.
- `test2.c` esta reservado para um exercicio em C.
- `pack.py` possui apenas material introdutorio sobre argumentos.

## Licenca

Este projeto esta sob a licenca [MIT](LICENSE).
