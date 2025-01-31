# prog-art

## Proposta do projeto
Visa-se, neste projeto, a implementação de conceitos de linguagens formais e autômatos para concepção de um compilador nos seguintes moldes: reconhecimento léxico, sintático e semântico de uma linguagem capaz de programar desenhos, seguido, então, da geração de um código capaz de representar o desenho codificado.

## Funcionamento
### Visão geral
Em um panorama geral: o compilador lê na entrada um arquivo texto contendo o código do desenho; processa, em seguida, essa entrada aceitando ou rejeitando-a; por fim, no caso de aceitação, gera na saída um código em python, com uso da biblioteca tkinter, e o roda automaticamente, apresentando, então, o desenho. 

### Detalhes e definições
Em mais detalhes, o processamento se da desta forma: 
- Realiza-se primeiro um reconhecimento léxico, isto é, dos conjuntos isolados de caracteres (palavras, números etc) -- conforme uma gramática regular --, com uso de um autômato finito determinístico; e realiza-se, em seguida, uma categorização. Estas são as definições formais:
    - Gramática: G = (Vn, Vt, P, S)
        - Vn = {S0, S1, S2, S3, S4, S5}
        - Vt = {a...z , 0...9 , '[' , ']' , '(' , ')' , ':' , '-'}
        - P = { S0 -> ':'S1 , S0 -> '-'S2 , S0 -> a...z , S0 -> (a...z)S3 , S0 -> 0...9 , S0 -> (0...9)S4 , S0 -> '[' , S0 -> ']' , S0 -> '(' , S0 -> ')' , S1 -> a...z , S1 -> (a...z)S5 , S2 -> 0...9 , S2 -> (0...9)S4 , S3 -> a...z , S3 -> (a...z)S3 , S4 -> 0...9 , S4 -> (0...9)S4 , S5 -> a...z , S5 -> (a...z)S5 }
        - S = {S0}
    - Autômato: M = (K, A, f, qo, F)
        - K = {q0, q1, q2, qf1, qf2, qf3, qf4, qf5, qf6, qf7}
        - A = {a...z , 0...9 , '[' , ']' , '(' , ')' , ':' , '-'}
        - f = { f(q0, a...9) = qf1 , f(q0, ':') = q1 , f(q0, '-') = q2 , f(q0, 0...9) = qf2 , f(q0, '[') = qf3 , f(q0, ']') = qf4 , f(q0, '(') = qf5 , f(q0, ')') = qf6 , f(q1, a...z) = qf7 , f(q2, 0...9) = qf2 , f(qf1, a...z) = qf1 , f(qf2, 0...9) = qf2 , f(qf7, a...z) = qf7 }
        - F = {qf1, qf2, qf3, qf4, qf5, qf6, qf7}
    - Categorização:
        - palavras reservadas => inicio, fim, pf, pt, pd, pe, repita, aprenda, un, ul, ub, pc, mudex, mudey, mudepos, arco, rotule, mudecl, mudecf 
        - a...z => nome *exceto palavras reservadas
        - :(a...z) => param
        - 0...9 ou -(0...9) => nro
        - '[' => abre
        - ']' => fecha
        - '(' => abre_par
        - ')' => fecha_par
- realiza-se, então, o reconhecimento da sintaxe -- conforme uma gramática livre de contexto -- por um autômato com pilha. Estas são as definições formais:
    - Gramática: G = (Vn, Vt, P, S)
        - Vn = {S0, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13}
        - Vt = {inicio, fim, pf, pt, pd, pe, repita, aprenda, un, ul, ub, pc, mudex, mudey, mudepos, arco, rotule, mudecl, mudecf, nome, param, nro, abre, fecha, abre_par, fecha_par}
        - P = { S0 -> inicio S1 , S1 -> fim , S1 -> un S1 , S1 -> ul S1 , S1 -> ub S1 , S1 -> pc S1 , S1 -> pf S2 S1 , S1 -> pt S2 S1 , S1 -> pd S2 S1 , S1 -> pe S2 S1 , S1 -> mudex S2 S1 , S1 -> mudey S2 S1 , S1 -> mudepos S3 S2 S2 S4 S1 , S1 -> arco S2 S2 S1 , S1 -> rotule S3 S5 S4 S1 , S1 -> mudecl S3 S2 S2 S2 S4 S1 , S1 -> mudecf S3 S2 S2 S2 S4 S1 , S1 -> repita S2 S3 S6 S1 , S1 -> nome S7 S8 S1 , S1 -> aprenda S5 S9 S1 , S2 -> nro , S3 -> abre , S4 -> fecha , S5 -> nome , S6 -> pf S2 S6 , S6 -> pt S2 S6 , S6 -> pd S2 S6 , S6 -> pe S2 S6 , S6 -> fecha , S7 -> abre_par , S8 -> nro S8 , S8 -> fecha_par , S9 -> param S9 , S9 -> fim , S9 -> un S10 , S9 -> ul S10 , S9 -> ub S10 , S9 -> pc S10 , S9 -> pf S11 S10 , S9 -> pt S11 S10 , S9 -> pd S11 S10 , S9 -> pe S11 S10 , S9 -> mudex S11 S10 , S9 -> mudey S11 S10 , S9 -> mudepos S3 S11 S11 S4 S10 , S9 -> arco S11 S11 S10 , S9 -> rotule S3 S5 S4 S10 , S9 -> mudecl S3 S11 S11 S11 S4 S10 , S9 -> mudecf S3 S11 S11 S11 S4 S10 , S9 -> repita S11 S4 S12 S10 , S9 -> nome S7 S13 S10 , S10 -> fim , S10 -> un S10 , S10 -> ul S10 , S10 -> ub S10 , S10 -> pc S10 , S10 -> pf S11 S10 , S10 -> pt S11 S10 , S10 -> pd S11 S10 , S10 -> pe S11 S10 , S10 -> mudex S11 S10 , S10 -> mudey S11 S10 , S10 -> mudepos S3 S11 S11 S4 S10 , S10 -> arco S11 S11 S10 , S10 -> rotule S3 S5 S4 S10 , S10 -> mudecl S3 S11 S11 S11 S4 S10 , S10 -> mudecf S3 S11 S11 S11 S4 S10 , S10 -> repita S11 S4 S12 S10 , S10 -> nome S7 S13 S10 , S11 -> nro , S11 -> param , S12 -> pf S11 S12 , S12 -> pt S11 S12 , S12 -> pd S11 S12 , S12 -> pe S11 S12 , S12 -> fecha , S13 -> nro S13 , S13 -> param S13 , S13 -> fecha_par }
        - S = {S0}
    - Autômato: M = (K, Ae, Ap, f, q0, S, F)
        - K = {q0, q1, qf}
        - Ae = {INICIO, FIM, PF, PT, PD, PE, REPITA, APRENDA, UN, UL, UB, PC, MUDEX, MUDEY, MUDEPOS, ARCO, ROTULE, MUDECL, MUDECF, NOME, PARAM, NRO, ABRE, FECHA, ABRE_PAR, FECHA_PAR}
        - Ap = {S, COMANDOS, NRO, ABRE, FECHA, NOME, LISTA, ABRE_PAR, CITA_PARAM, DEF_APRENDA, MAIS_COMANDO, VALOR, LISTA_APRENDA, CITA_PARAM_APRENDA}
        - f = { f(q1, INICIO, S) = {q1, COMANDOS} , f(q1, FIM, COMANDOS) = {qf, []} , f(q1, UN, COMANDOS) = {q1, COMANDOS} , f(q1, UL, COMANDOS) = {q1, COMANDOS} , f(q1, UB, COMANDOS) = {q1, COMANDOS} , f(q1, PC, COMANDOS) = {q1, COMANDOS} , f(q1, PF, COMANDOS) = {q1, NRO COMANDOS} , f(q1, PT, COMANDOS) = {q1, NRO COMANDOS} , f(q1, PD, COMANDOS) = {q1, NRO COMANDOS} , f(q1, PE, COMANDOS) = {q1, NRO COMANDOS} , f(q1, MUDEX, COMANDOS) = {q1, NRO COMANDOS} , f(q1, MUDEY, COMANDOS) = {q1, NRO COMANDOS} , f(q1, MUDEPOS, COMANDOS) = {q1, ABRE NRO NRO FECHA COMANDOS} , f(q1, ARCO, COMANDOS) = {q1, NRO NRO COMANDOS} , f(q1, ROTULE, COMANDOS) = {q1, ABRE NOME FECHA COMANDOS} , f(q1, MUDECL, COMANDOS) = {q1, ABRE NRO NRO NRO FECHA COMANDOS} , f(q1, MUDECF, COMANDOS) = {q1, ABRE NRO NRO NRO FECHA COMANDOS} , f(q1, REPITA, COMANDOS) = {q1, NRO ABRE LISTA COMANDOS} , f(q1, NOME, COMANDOS) = {q1, ABRE_PAR CITA_PARAM COMANDOS} , f(q1, APRENDA, COMANDOS) = {q1, NOME DEF_APRENDA COMANDOS} , f(q1, NRO, NRO) = {q1, []} , f(q1, ABRE, ABRE) = {q1, []} , f(q1, FECHA, FECHA) = {q1, []} , f(q1, NOME, NOME) = {q1, []} , f(q1, PF, LISTA) = {q1, NRO LISTA} , f(q1, PT, LISTA) = {q1, NRO LISTA} , f(q1, PD, LISTA) = {q1, NRO LISTA} , f(q1, PE, LISTA) = {q1, NRO LISTA} , f(q1, FECHA, LISTA) = {q1, []} , f(q1, ABRE_PAR, ABRE_PAR) = {q1, []} , f(q1, NRO, CITA_PARAM) = {q1, CITA_PARAM} , f(q1, FECHA_PAR, CITA_PARAM) = {q1, []} , f(q1, PARAM, DEF_APRENDA) = {q1, DEF_APRENDA} , f(q1, FIM, DEF_APRENDA) = {q1, []} , f(q1, UN, DEF_APRENDA) = {q1, MAIS_COMANDOS} , f(q1, UL, DEF_APRENDA) = {q1, MAIS_COMANDOS} , f(q1, UB, DEF_APRENDA) = {q1, MAIS_COMANDOS} , f(q1, PC, DEF_APRENDA) = {q1, MAIS_COMANDOS} , f(q1, PF, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, PT, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, PD, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, PE, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEX, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEY, DEF_APRENDA) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEPOS, DEF_APRENDA) = {q1, ABRE VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, ARCO, DEF_APRENDA) = {q1, VALOR VALOR MAIS_COMANDOS} , f(q1, ROTULE, DEF_APRENDA) = {q1, ABRE NOME FECHA MAIS_COMANDOS} , f(q1, MUDECL, DEF_APRENDA) = {q1, ABRE VALOR VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, MUDECF, DEF_APRENDA) = {q1, ABRE VALOR VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, REPITA, DEF_APRENDA) = {q1, VALOR ABRE LISTA_APRENDA MAIS_COMANDOS} , f(q1, NOME, DEF_APRENDA) = {q1, ABRE_PAR CITA_PARAM_APRENDA MAIS_COMANDOS} , f(q1, FIM, MAIS_COMANDOS) = {q1, []} , f(q1, UN, MAIS_COMANDOS) = {q1, MAIS_COMANDOS} , f(q1, UL, MAIS_COMANDOS) = {q1, MAIS_COMANDOS} , f(q1, UB, MAIS_COMANDOS) = {q1, MAIS_COMANDOS} , f(q1, PC, MAIS_COMANDOS) = {q1, MAIS_COMANDOS} , f(q1, PF, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, PT, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, PD, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, PE, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEX, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEY, MAIS_COMANDOS) = {q1, VALOR MAIS_COMANDOS} , f(q1, MUDEPOS, MAIS_COMANDOS) = {q1, ABRE VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, ARCO, MAIS_COMANDOS) = {q1, VALOR VALOR MAIS_COMANDOS} , f(q1, ROTULE, MAIS_COMANDOS) = {q1, ABRE NOME FECHA MAIS_COMANDOS} , f(q1, MUDECL, MAIS_COMANDOS) = {q1, ABRE VALOR VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, MUDECF, MAIS_COMANDOS) = {q1, ABRE VALOR VALOR VALOR FECHA MAIS_COMANDOS} , f(q1, REPITA, MAIS_COMANDOS) = {q1, VALOR ABRE LISTA_APRENDA MAIS_COMANDOS} , f(q1, NOME, MAIS_COMANDOS) = {q1, ABRE_PAR CITA_PARAM_APRENDA MAIS_COMANDOS} , f(q1, NRO, VALOR) = {q1, []} , f(q1, PARAM, VALOR) = {q1, []} , f(q1, PF, LISTA_APRENDA) = {q1, VALOR LISTA_APRENDA} , f(q1, PT, LISTA_APRENDA) = {q1, VALOR LISTA_APRENDA} , f(q1, PD, LISTA_APRENDA) = {q1, VALOR LISTA_APRENDA} , f(q1, PE, LISTA_APRENDA) = {q1, VALOR LISTA_APRENDA} , f(q1, FECHA, LISTA_APRENDA) = {q1, []} , f(q1, NRO, CITA_PARAM_APRENDA) = {q1, CITA_PARAM_APRENDA} , f(q1, PARAM, CITA_PARAM_APRENDA) = {q1, CITA_PARAM_APRENDA} , f(q1, FECHA_PAR, CITA_PARAM_APRENDA) = {q1, []} }
        - F = {qf}
- Em conjunto com a análise sintática, faz-se uma análise semântica, que consiste, em suma, em uma verificação da consistência interna na entrada. Verificam-se coisas como:
    - se o cursor ultrapassará, em algum momento, os limites da tela;
    - se foi utilizado algum número negativo em comandos que não o suportam (ex: pf, pt, pd, pe, arco etc);
    - se, ao definir um procedimento, existe algo já definido com o mesmo nome;
    - se, ao chamar um procedimento, ele já havia sido definido anteriormente;
    - se, ao chamar um procedimento, explicitaram-se a quantidade de parâmetros com que ele foi definido;
    - se, em comandos relacionados a valores RGB (mudecl e mudecl), os valores dados encontram-se entre 0 e 255.
- Antes da efetiva geração do código de saída, realiza-se uma formatação intermediária; no caso, separa-se as instruções do comando repita em um conjunto de instruções simples em sequência.
- Gera-se, enfim, o código. Colocam-se, a princípio, os elementos iniciais -- import das bibliotecas (tkinter e math), definição do tamanho da tela (1280x720), definição de variáveis e funções auxiliares --; então, posteriormente, verifica-se o código de entrada já reformatado e, para cada instrução nele presente, estrutura-se uma instrução equivalente, isto é, de mesmo resultado, no tekinter. Alguns cuidados, ademais, tiveram de ser tomados, como:
    - Atentar-se à diferença referencial das coordenadas -- coordenada (0,0), na entrada, está no centro, enquanto no tkinter, no canto superior esquerdo --;
    - Manter o registro contínuo da posição e rotação do cursor;
    - No caso da definição de procedimentos, atentar-se à indentação na saída;
    - No caso de comandos com parâmetros distintos -- a exemplo do comando arco en relação ao create_arc --, encontrar, por meio de cálculos geométricos e trigonométricos, equivalências entre eles.

## Como usar
Crie um arquivo texto, no mesmo diretório em que se encontra programa prog-art, com o nome entrada.txt e nele escreva o código para o que se deseja desenhar. No código, deve-se colocar 'inicio' antes de tudo e, ao final, 'fim'; e entre eles, escreve-se, então, os comandos referentes ao desenho. Escrito o código, basta executar o programa prog-art e ver na tela o resultado.
### Lista de comandos
- pf n
    - Faz o cursor andar para frente -- na direção que ele estiver apontando -- n unidades.
- pt n
    - Faz o cursor andar para trás -- na direção que ele estiver apontando -- n unidades.
- pd n
    - Gira o cursor no sentido horário n graus. 
- pe n
    - Gira o cursor no sentido anti-horário n graus.
- repita n [ lista_de_comandos ] 
    - Executa n vezes os comandos contidos em lista de comandos; são permitidos apenas os comandos pf, pt, pd e pe.
- aprenda nome lista_de_comandos fim
    - Cria um procedimento identificado por nome, contendo uma lista de comandos. Ex: aprenda quadrado repita 4 [ pf 100 pd 90 ] fim
    - Executa-se o procedimento chamando seu nome seguido de parênteses. Ex: quadrado ( )
- aprenda nome :paramento1 :paramentro2 comandos fim
    - Cria um procedimento identificado por nome, contendo uma lista de comandos; possui, neste caso, um ou mais parâmetros. Ex:  aprenda quadrado :tamanho :angulo repita 4 [ pf :tamanho pd :angulo ] fim 
    - Executa-se o procedimento chamando seu nome seguido dos parâmetros entre parênteses. Ex: quadrado ( 100 90 )
- un
    - Desabilita o traçado do cursor.
- ul 
    - Habilita o traçado do cursor; por padrão, o traçado está na cor preta.
- ub
    - Habilita o traçado do cursor como borracha.
- pc
    - Cursor retorna à origem das coordenadas, ou seja, à posição (0,0).
- mudex n
    - Desloca o cursor, em x, n posições.
- mudey n
    - Desloca o cursor, em y, n posições.
- mudepos [ n m ]
    - Desloca o cursor para posição (n,m).
- arco n m
    - Desenha arco de angulo n (em graus) e raio m; será sempre desenhado no sentido horário.
- rotule [ texto ]
    - Insere um texto na direção e no lado direito do eixo de simetria do cursor. Ex: pd 90 rotule [ traçado ]
- mudecl [ n m k ]
    - Muda cor do traçado para cor RGB(n,m,k).
- mudecf [ n m k ]
    - Muda cor do fundo de tela para cor RGB(n,m,k).