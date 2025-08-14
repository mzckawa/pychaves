#### TITULO DO PROJETO: 
___
PyChaves

#### MEMBROS DA EQUIPE:
___
- Alvaro Alexandre
- João Gabriel Peres
- Luan Gabriel Luck
- Mel Zion Cordeiro
- Tiago do Nascimento Santos
- Yuri Gabryel Cabral da Silva

#### ARQUITETURA DO PROJETO
___

Para facilitar a organização do código e edição das funções do jogo, o código foi separado nos seguintes módulos:

- Créditos
   No módulos dos créditos, criamos uma classe com as propriedades básicas da tela de créditos, definimos a imagem de fundo e carregamos a música que será tocada durante essa tela.

- Main
   Esse é o módulo principal, onde importamos e integramos as demais funções/módulos e rodamos o looping pricipal que garante a funcionalidade do jogo. Aqui carregamos e imprimimos as imagens que aparecerão na tela, estabelecemos as colisões e coleta de coletáveis, decrementando o parâmetro de vida (por conta da colisão com a bola quadrada), aumentando a vida (por conta da colisão com o sanduíche de presunto) e dando imunidade ao personagem por um período de tempo (por conta da colisão com o suco de tamarindo) 

- Menu
   Nesse módulo, definimos a classe do menu, onde ajustamos as propriedades básicas do menu, configuramos a movimentação do setas seletoras (entre as opções "Start" e "Credits"), configuramos a página dos menu e definimos a música que será tocada.

- Personagem
   Nesse módulo, definimos uma classe com as propriedades principais do personagem: movimentação nas 4 direções, impressão da imagem na tela, arrasto da onda (o personagem é jogado para trás pela onda) e a morte por sair da tela (quando ele é completamente arrastado pela onda).

- Tela final
   Esse é o módulo que define as características da tela que aparece indicando o resultado (vitória ou derrota) do jogador ao fim do jogo. Nele definimos propriedades básicas da tela final, imagem de fundo que vai aparecer e música conforme resultado.


#### CAPTURAS DE TELA
___
![alt text](<Tela dos Créditos.png>) 
![alt text](<Tela Inicial.png>) 
![alt text](<Tela Vitória.png>) 
![alt text](<Tela de Derrota.png>) 
![alt text](<Tela de Jogo.png>)

#### FERRAMENTAS, BIBLIOTECAS E FRAMEWORKS UTILIZADAS:
___

- Bibiliotecas: Pygame, Math, Random.

- Linguagem de Marcação Markdown

- Ferramentas de gestão de tarefas:
 - [x] Notion (para planejar, dividir tarefas, guardar materiais e dicas)
 - [x] Discord (para comunicação entre os membros e com os monitores)
 - [x] WhatsApp (para comunicação entre os membros)

- Ferramentas de versionamento:
 - [x] Git (para armazenar as diferentes versões do código, conforme implementação de novas funções)

- Ferramenta de repositório remoto:
 - [x] Github (para criação, acesso e compartilhamento do repositório remoto do projeto)


#### DIVISÃO DO TRABALHO DENTRO DO GRUPO:
___

- Alvaro: desenvolvimento do placar do jogo (aquilo que mostra quantos coletáveis o jogador tem naquele momento);

- João: desenvolvimento da movimentação do jogador em 4 direções, da movimentação do cenário (criando um efeito de cenário infinito) com velocidade acelerada (ele também aplicou essa velocidade na movimentação do personagem), das barreiras limitantes da movimentação do jogador e do efeito de morte quando o jogador desaparece da tela);

- Luan: desenvolvimento da classe dos coletáveis do jogo, incluindo o sistema de captura/colisão, o surgimento aleatório e contínuo dos coletáveis;

- Mel: desenvolvimento da classe dos coletáveis do jogo, incluindo o sistema de captura/colisão, o surgimento aleatório e contínuo dos coletáveis;

- Tiago: criação dos sprites, trilha sonora e auxiliando no desenvolvimento da classe dos coletáveis do jogo;

- Yuri: esenvolvimento do menu do jogo, da tela de créditos do jogo, dos efeitos sonoros em ambos os cenáriose e da dinâmica de "ir e voltar" de ambas as telas.

#### CONCEITOS UTILIZADOS:
___

- [x] Comandos condicionais
- [x] Laços de repetição
- [x] Listas
- [x] Funções
- [x] Dicionários
- [x] Orientação a objetos. 

#### DESAFIOS, ERROS E LIÇÕES APRENDIDAS:
___

- PRINCIPAIS DESAFIOS:
    1. O maior desafio ainda estava se desenhando: dominar o fluxo de trabalho do GitHub. Conforme o código ficava mais complexo, saber salvar as mudanças, certificar-se de que estava alterando um arquivo atualizado, prevenir arquivos de serem sobrescritos inadequadamente e resolver conflitos para conseguir dar merge tornaram-se competências essenciais. Além de recorrermos a pesquisas e vídeos para conhecer mais a ferramenta e sanar dúvidas, os monitores e colegas de sala nos ajudaram muito, dando dicas facilitaram o uso dessa ferramenta.

    2. Aprender os comandos do Pygame, isto é, quais ações poderiam ser feitas com funções próprias do Pygame e quais requereriam desenvolvimento de lógica de programação. Para poder aprender essa função recorremos a pesquisas e vídeos que contribuíram bastante para o aprendizado de funções e lógicas para implementar as funções; 

    3. Dividir as tarefas, até porque precisávamos constantemente da ajuda uns dos outros; isso, porém, foi eventualmente resolvido, e conseguimos organizar as missões sem mitigar a cooperação mútua;

- PRINCIPAIS ERROS:
    1. Não ter estudado Git com a devida antecedência.

    2. Não definir uma organização clara para as branchs, o que dificultou ainda mais o uso do Git.

    3. Ter deixando para fazer alguns ajustes finais próximo à data final do projeto.

- APRENDIZADOS:
    1. Utilizamos muito as funções do Git, o que nos permitiu conhecer mais essa complexa mas incrível ferramenta;

    2. Já nos dias finais, descobrimos o LiveShare, que nos permitia trabalhar nos códigos simultaneamente, o que foi de grande ajuda.

    3. Aprendemos também a separar melhor as funções entre os integrantes, além de acompanhar o andamento do projeto utilizando ferramentas de produtividade como o Kanban dentro do Notion.