import math
import os

#----------------------- Gerador de Código ----------------------------------

def gera_codigo(fita):
    
    # Elementos iniciais do código: imports, definição de funções, inicialização de variáveis
    codigo = 'from tkinter import *\n'
    codigo = codigo + 'import math\n'
    codigo = codigo + 'tela = Tk()\n'
    codigo = codigo + 'tela.title("Prog-art - arte programada")\n'
    codigo = codigo + 'tela.geometry("1280x720")\n'
    codigo = codigo + 'def corRGB(r, g, b):\n'
    codigo = codigo + '\treturn f"#{r:02x}{g:02x}{b:02x}"\n'
    codigo = codigo + 'canvas = Canvas(tela, width = 1280, height = 720, bg = corRGB(255, 255, 255))\n'
    codigo = codigo + 'canvas.pack()\n'
    codigo = codigo + 'corFundo = corRGB(255, 255, 225)\n'
    codigo = codigo + 'corLapis = corRGB(0, 0, 0)\n'
    codigo = codigo + 'posicao = [640.0, 360.0]\n'
    codigo = codigo + 'giro = 0\n'
    codigo = codigo + 'apagados = []\n'

    # Flags e variáveis auxiliáres
    defAprenda = False
    inAprenda = False
    firstParam = False
    qtdParam = 0
    desenha = True
    apaga = True
    chamaFunc = False
    mudecl = False
    mudeclcount = 0
    mudecf = False
    mudecfcount = 0
    pf = False
    pt = False
    pe = False
    pd = False
    rotule = False
    arco = False
    arcoaux = 0
    arcoangulo = ''
    mudex = False
    mudey = False
    mudepos = False
    mudeposcount = 0

    # Verificação de cada elemento da tabela [lexema, token] gerada após o processo intermediário - transformação dos comandos repita em operações elementares repetidas
    for terminal in fita:
        # Permitindo o uso das variáveis globais, já inicializadas, dentro da função
        if terminal[1] != 'PARAM' and terminal[1] != 'NOME' and terminal[1] != 'APRENDA' and defAprenda:
                codigo = codigo + '):\n\tglobal posicao\n\tglobal giro\n\tglobal corFundo\n\tglobal corLapis\n\tglobal corPinta\n\tglobal apagados\n'
                defAprenda = False

        if terminal[1] == 'APRENDA':
            codigo = codigo + 'def '
            defAprenda = True
            inAprenda = True
            firstParam = True
            qtdParam = 0

        if terminal[1] == 'NOME':
            if defAprenda:
                codigo = codigo + f'{terminal[0]} ('
            else:
                if rotule:
                    codigo = codigo + f'{terminal[0]}")\n'
                    rotule = False
                else:
                    if inAprenda:
                        codigo = codigo + f'\t{terminal[0]} ('
                    else:
                        codigo = codigo + f'{terminal[0]} ('
                    chamaFunc = True
                    qtdParam = 0

        if terminal[1] == 'FECHAPAR':
            codigo = codigo + ')\n'
            chamaFunc = False

        if terminal[1] == 'PARAM':
            if defAprenda:
                if qtdParam == 0:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]}'
                    qtdParam = qtdParam + 1
                else:
                    codigo = codigo + f', {terminal[0][1:len(terminal[0])]}'

            if mudecl:
                if mudeclcount < 2:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]}, '
                    mudeclcount = mudeclcount + 1
                else:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]})\n'
                    mudecl = False

            if mudecf:
                if mudecfcount < 2:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]}, '
                    mudecfcount = mudecfcount + 1
                else:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]})\n'
                    codigo = codigo + f'\tcanvas.configure(bg = corFundo)\n'
                    codigo = codigo + f'\tfor apagado in apagados:\n\t\tcanvas.itemconfig(apagado, fill = corFundo)\n'
                    mudecf = False

            if pf:
                if desenha:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] + {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] - {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro)), fill = corLapis)\n'
                elif apaga:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] + {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] - {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro)), fill = corLapis))\n'
                codigo = codigo + f'\tposicao = [posicao[0] + {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), posicao[1] - {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro))]\n'
                pf = False

            if pt:
                if desenha:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro)), fill = corLapis)\n'
                elif apaga:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro)), fill = corLapis))\n'    
                codigo = codigo + f'\tposicao = [posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro)), posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro))]\n'
                pt = False

            if pe:
                codigo = codigo + f'{terminal[0][1:len(terminal[0])]}\n'
                pe = False
                
            if pd:
                codigo = codigo + f'{terminal[0][1:len(terminal[0])]}\n'
                pd = False

            if chamaFunc:
                if qtdParam == 0:
                    codigo = codigo + f'{terminal[0]}'
                else:
                    codigo = codigo + f', {terminal[0]}'
                qtdParam = qtdParam + 1

            if arco:
                if arcoaux < 1:
                    arcoangulo = terminal[0]
                    arcoangulo = arcoangulo[1:len(arcoangulo)]
                    arcoaux = arcoaux + 1
                else:
                    if desenha:
                        codigo = codigo + f'(posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90))) - {terminal[0][1:len(terminal[0])]}, (posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90))) - {terminal[0][1:len(terminal[0])]}, \n\t\t\t'
                        codigo = codigo + f'(posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90))) + {terminal[0][1:len(terminal[0])]}, (posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90))) + {terminal[0][1:len(terminal[0])]}, \n\t\t\t'
                        codigo = codigo + f'start = giro - 90, extent = {arcoangulo}, style = "arc", outline = corLapis)\n'
                    elif apaga:
                        codigo = codigo + f'(posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90))) - {terminal[0][1:len(terminal[0])]}, (posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90))) - {terminal[0][1:len(terminal[0])]}, \n\t\t\t'
                        codigo = codigo + f'(posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90))) + {terminal[0][1:len(terminal[0])]}, (posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90))) + {terminal[0][1:len(terminal[0])]}, \n\t\t\t'
                        codigo = codigo + f'start = giro - 90, extent = {arcoangulo}, style = "arc", outline = corLapis))\n'
                    codigo = codigo + f'\tposicao = [(posicao[0] - {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90))) + {terminal[0][1:len(terminal[0])]} * math.cos(math.radians(giro - 90 + {arcoangulo})), \n\t\t\t'
                    codigo = codigo + f'(posicao[1] + {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90))) - {terminal[0][1:len(terminal[0])]} * math.sin(math.radians(giro - 90 + {arcoangulo}))]\n'
                    codigo = codigo + f'\tgiro = giro + {arcoangulo}\n'
                    arco = False

            if mudex:
                codigo = codigo + f'{terminal[0][1:len(terminal[0])]} + 640\n'
                mudex = False

            if mudey:
                codigo = codigo + f'-{terminal[0][1:len(terminal[0])]} + 360\n'
                mudey = False

            if mudepos:
                if mudeposcount < 1:
                    codigo = codigo + f'{terminal[0][1:len(terminal[0])]} + 640, '
                    mudeposcount = mudeposcount + 1
                else:
                    codigo = codigo + f'-{terminal[0][1:len(terminal[0])]} + 360]\n'
                    mudepos = False

        if terminal[1] == 'FIM':
            inAprenda = False
                    
        if terminal[1] == 'UN':
            desenha = False
            apaga = False

        if terminal[1] == 'UL':
            desenha = True
            apaga = False
            if inAprenda:
                codigo = codigo + '\tcorLapis = corRGB(0, 0, 0)\n'
            else:
                codigo = codigo + 'corLapis = corRGB(0, 0, 0)\n'

        if terminal[1] == 'UB':
            desenha = False
            apaga = True
            if inAprenda:
                codigo = codigo + '\tcorLapis = corFundo\n'
            else:
                codigo = codigo + 'corLapis = corFundo\n'

        if terminal[1] == 'PC':
            if inAprenda:
                codigo = codigo + '\tposicao = [640, 360]\n'
            else:
                codigo = codigo + 'posicao = [640, 360]\n'

        if terminal[1] == 'MUDECL':
            if inAprenda:
                codigo = codigo + '\tcorLapis = corRGB('
            else:
                codigo = codigo + 'corLapis = corRGB('
            mudecl = True
            mudeclcount = 0

        if terminal[1] == 'MUDECF':
            if inAprenda:
                codigo = codigo + '\tcorFundo = corRGB('
            else:
                codigo = codigo + 'corFundo = corRGB('
            mudecf = True
            mudecfcount = 0

        if terminal[1] == 'NRO':
            if mudecl:
                if mudeclcount < 2:
                    codigo = codigo + f'{terminal[0]}, '
                    mudeclcount = mudeclcount + 1
                else:
                    codigo = codigo + f'{terminal[0]})\n'
                    mudecl = False

            if mudecf:
                if mudecfcount < 2:
                    codigo = codigo + f'{terminal[0]}, '
                    mudecfcount = mudecfcount + 1
                else:
                    codigo = codigo + f'{terminal[0]})\n'
                    if inAprenda:
                        codigo = codigo + f'\tcanvas.configure(bg = corFundo)\n'
                        codigo = codigo + f'\tfor apagado in apagados:\n\t\tcanvas.itemconfig(apagado, fill = corFundo)\n'
                    else:
                        codigo = codigo + f'canvas.configure(bg = corFundo)\n'
                        codigo = codigo + f'for apagado in apagados:\n\tcanvas.itemconfig(apagado, fill = corFundo)\n'
                    mudecf = False

            if pf:
                if desenha:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] + {terminal[0]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] - {terminal[0]} * math.sin(math.radians(giro)), fill = corLapis)\n'
                elif apaga:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] + {terminal[0]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] - {terminal[0]} * math.sin(math.radians(giro)), fill = corLapis))\n'
                if inAprenda:
                    codigo = codigo + f'\tposicao = [posicao[0] + {terminal[0]} * math.cos(math.radians(giro)), posicao[1] - {terminal[0]} * math.sin(math.radians(giro))]\n'
                else:
                    codigo = codigo + f'posicao = [posicao[0] + {terminal[0]} * math.cos(math.radians(giro)), posicao[1] - {terminal[0]} * math.sin(math.radians(giro))]\n'
                pf = False

            if pt:
                if desenha:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] - {terminal[0]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] + {terminal[0]} * math.sin(math.radians(giro)), fill = corLapis)\n'
                elif apaga:
                    codigo = codigo + f'posicao[0], posicao[1], posicao[0] - {terminal[0]} * math.cos(math.radians(giro)), \n\t\t\tposicao[1] + {terminal[0]} * math.sin(math.radians(giro)), fill = corLapis))\n'
                if inAprenda:
                    codigo = codigo + f'\tposicao = [posicao[0] - {terminal[0]} * math.cos(math.radians(giro)), posicao[1] + {terminal[0]} * math.sin(math.radians(giro))]\n'
                else:
                    codigo = codigo + f'posicao = [posicao[0] - {terminal[0]} * math.cos(math.radians(giro)), posicao[1] + {terminal[0]} * math.sin(math.radians(giro))]\n' 
                pt = False

            if pe:
                codigo = codigo + f'{terminal[0]}\n'
                pe = False
                
            if pd:
                codigo = codigo + f'{terminal[0]}\n'
                pd = False

            if chamaFunc:
                if qtdParam == 0:
                    codigo = codigo + f'{terminal[0]}'
                else:
                    codigo = codigo + f', {terminal[0]}'
                qtdParam = qtdParam + 1

            if arco:
                if arcoaux < 1:
                    arcoangulo = terminal[0]
                    arcoaux = arcoaux + 1
                else:
                    if desenha:
                        codigo = codigo + f'(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) - {terminal[0]}, (posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) - {terminal[0]}, \n\t\t\t'
                        codigo = codigo + f'(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) + {terminal[0]}, (posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) + {terminal[0]}, \n\t\t\t'
                        codigo = codigo + f'start = giro - 90, extent = {arcoangulo}, style = "arc", outline = corLapis)\n'
                    elif apaga:
                        codigo = codigo + f'(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) - {terminal[0]}, (posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) - {terminal[0]}, \n\t\t\t'
                        codigo = codigo + f'(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) + {terminal[0]}, (posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) + {terminal[0]}, \n\t\t\t'
                        codigo = codigo + f'start = giro - 90, extent = {arcoangulo}, style = "arc", outline = corLapis))\n'
                    if inAprenda:
                        codigo = codigo + f'\tposicao = [(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) + {terminal[0]} * math.cos(math.radians(giro - 90 + {arcoangulo})), \n\t\t\t'
                        codigo = codigo + f'(posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) - {terminal[0]} * math.sin(math.radians(giro - 90 + {arcoangulo}))]\n'
                        codigo = codigo + f'\tgiro = giro + {arcoangulo}\n'
                    else:
                        codigo = codigo + f'posicao = [(posicao[0] - {terminal[0]} * math.cos(math.radians(giro - 90))) + {terminal[0]} * math.cos(math.radians(giro - 90 + {arcoangulo})), \n\t\t\t'
                        codigo = codigo + f'(posicao[1] + {terminal[0]} * math.sin(math.radians(giro - 90))) - {terminal[0]} * math.sin(math.radians(giro - 90 + {arcoangulo}))]\n'
                        codigo = codigo + f'giro = giro + {arcoangulo}\n'
                    arco = False

            if mudex:
                codigo = codigo + f'{terminal[0]} + 640\n'
                mudex = False

            if mudey:
                codigo = codigo + f'-{terminal[0]} + 360\n'
                mudey = False

            if mudepos:
                if mudeposcount < 1:
                    codigo = codigo + f'{terminal[0]} + 640, '
                    mudeposcount = mudeposcount + 1
                else:
                    codigo = codigo + f'-{terminal[0]} + 360]\n'
                    mudepos = False
                    

        if terminal[1] == 'PF':
            if desenha:
                if inAprenda:
                    codigo = codigo + '\tcanvas.create_line('
                else:
                    codigo = codigo + 'canvas.create_line('
            elif apaga:
                if inAprenda:
                    codigo = codigo + '\tapagados.append(canvas.create_line('
                else:
                    codigo = codigo + 'apagados.append(canvas.create_line('
            pf = True

        if terminal[1] == 'PT':
            if desenha:
                if inAprenda:
                    codigo = codigo + '\tcanvas.create_line('
                else:
                    codigo = codigo + 'canvas.create_line('
            elif apaga:
                if inAprenda:
                    codigo = codigo + '\tapagados.append(canvas.create_line('
                else:
                    codigo = codigo + 'apagados.append(canvas.create_line('
            pt = True

        if terminal[1] == 'PE':
            if inAprenda:
                codigo = codigo + '\tgiro = giro + '
            else:
                codigo = codigo + 'giro = giro + '
            pe = True

        if terminal[1] == 'PD':
            if inAprenda:
                codigo = codigo + '\tgiro = giro - '
            else:
                codigo = codigo + 'giro = giro - '
            pd = True

        if terminal[1] == 'ROTULE':
            if inAprenda:
                codigo = codigo + '\tcanvas.create_text(posicao[0], posicao[1], text = "'
            else:
                codigo = codigo + 'canvas.create_text(posicao[0], posicao[1], text = "'
            rotule = True

        if terminal[1] == 'ARCO':
            if desenha: 
                if inAprenda:
                    codigo = codigo + '\tcanvas.create_arc('
                else:
                    codigo = codigo + 'canvas.create_arc('
            elif apaga:
                if inAprenda:
                    codigo = codigo + '\tapagados.append(canvas.create_arc('
                else:
                    codigo = codigo + 'apagados.append(canvas.create_arc('
            arco = True
            arcoaux = 0

        if terminal[1] == 'MUDEX':
            if inAprenda:
                codigo = codigo + '\tposicao[0] = '
            else:
                codigo = codigo + 'posicao[0] = '
            mudex = True

        if terminal[1] == 'MUDEY':
            if inAprenda:
                codigo = codigo + '\tposicao[1] = '
            else:
                codigo = codigo + 'posicao[1] = '
            mudey = True

        if terminal[1] == 'MUDEPOS':
            if inAprenda:
                codigo = codigo + '\tposicao = ['
            else:
                codigo = codigo + 'posicao = ['
            mudepos = True
            mudeposcount = 0
            
    codigo = codigo + 'tela.mainloop()'

    arquivo = open('saida.py', 'w')
    arquivo.write(codigo)
    arquivo.close()
    # Executa-se o resultado da saída
    os.system('python saida.py')
    
#----------------------------------------

def intermediario(tabela_simbolos):

    # Reestruturação do REPITA
    # Separação do REPITA na repetição explícita de comandos simples
    
    if ['repita','REPITA'] in tabela_simbolos:
        aux = []
        pos = 0
        for pos in range(0, len(tabela_simbolos)):
            elemento = tabela_simbolos[pos]
            if elemento[1] == 'REPITA':
                pos = pos + 1
                elemento = tabela_simbolos[pos] # ['valor','NRO']
                limite = int(elemento[0])
                aux_rep = []
                pos = pos + 1; # Descarta o '['
                pos = pos + 1 # Primeiro comando de repitição
                elemento = tabela_simbolos[pos]
                
                while elemento[1] not in ('FECHA'):
                    aux_rep.append(elemento)
                    pos = pos + 1 # Lê-se o próximo elemento
                    elemento = tabela_simbolos[pos]
                    
                for i in range(limite-1): # Gera-se a repetição dos comandos
                    aux.extend(aux_rep)

                pos = pos + 1 # Elemento FECHA                            
                
            else:    
                aux.append(elemento)
                pos = pos + 1;
    
        print(aux)
        print('\n')
        gera_codigo(aux)
        return

    else:
        print(tabela_simbolos)
        print('\n')
        gera_codigo(tabela_simbolos)
        return

#----------------------- sintático ----------------------------------

# Definiçao da função transição - { CLASSIFICAÇÃO : { LIDO_NA_PILHA : [ACRESCENTA_NA_PILHA] }
transicao_pilha = { 'INICIO' : { 'S' : [ 'COMANDOS' ] },

    'FIM' : {'COMANDOS' : [ ], 'DEF_APRENDA': [ ], 'MAIS_COMANDOS': [ ]},

    'PF' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'LISTA': ['NRO', 'LISTA'],
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'LISTA_APRENDA': ['VALOR', 'LISTA_APRENDA'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'ABRE' : {'ABRE' : [  ]},

    'FECHA' : { 'FECHA' : [ ],
            'LISTA' : [ ],
            'LISTA_APRENDA' : [ ]},

    'PD' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'LISTA': ['NRO', 'LISTA'],
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'LISTA_APRENDA': ['VALOR', 'LISTA_APRENDA'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'PT' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'LISTA': ['NRO', 'LISTA'],
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'LISTA_APRENDA': ['VALOR', 'LISTA_APRENDA'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'PE' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'LISTA': ['NRO', 'LISTA'],
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'LISTA_APRENDA': ['VALOR', 'LISTA_APRENDA'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'MUDEX' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'MUDEY' : { 'COMANDOS' : ['NRO', 'COMANDOS'], 
            'DEF_APRENDA': ['VALOR', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['VALOR', 'MAIS_COMANDOS']},

    'MUDECL' : { 'COMANDOS' : ['ABRE', 'NRO', 'NRO', 'NRO', 'FECHA', 'COMANDOS'], 
            'DEF_APRENDA': ['ABRE', 'VALOR', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['ABRE', 'VALOR', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS']},

    'MUDECF' : { 'COMANDOS' : ['ABRE', 'NRO', 'NRO', 'NRO', 'FECHA', 'COMANDOS'], 
            'DEF_APRENDA': ['ABRE', 'VALOR', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['ABRE', 'VALOR', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS']},

    'ARCO' : { 'COMANDOS' : ['NRO', 'NRO', 'COMANDOS'],
            'DEF_APRENDA': ['VALOR', 'VALOR', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['VALOR', 'VALOR', 'MAIS_COMANDOS']},

    'UN' : { 'COMANDOS' : [ 'COMANDOS' ], 
            'DEF_APRENDA' : [ 'MAIS_COMANDOS'], 
            'MAIS_COMANDOS' : [ 'MAIS_COMANDOS']},

    'UL' : { 'COMANDOS' : [ 'COMANDOS' ], 
            'DEF_APRENDA' : [ 'MAIS_COMANDOS'], 
            'MAIS_COMANDOS' : [ 'MAIS_COMANDOS']},

    'UB' : { 'COMANDOS' : [ 'COMANDOS' ], 
            'DEF_APRENDA' : [ 'MAIS_COMANDOS'], 
            'MAIS_COMANDOS' : [ 'MAIS_COMANDOS']},


    'PC' : { 'COMANDOS' : [ 'COMANDOS' ], 
            'DEF_APRENDA' : [ 'MAIS_COMANDOS'], 
            'MAIS_COMANDOS' : [ 'MAIS_COMANDOS']},

    'ROTULE' : { 'COMANDOS' : ['ABRE', 'NOME', 'FECHA', 'COMANDOS'],  
            'DEF_APRENDA' : ['ABRE', 'NOME', 'FECHA', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS' : ['ABRE', 'NOME', 'FECHA', 'COMANDOS'],},

    'MUDEPOS' : { 'COMANDOS' : ['ABRE', 'NRO', 'NRO', 'FECHA', 'COMANDOS'], 
            'DEF_APRENDA' : ['ABRE', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS' : ['ABRE', 'VALOR', 'VALOR', 'FECHA', 'MAIS_COMANDOS'],},
                   
    'REPITA': { 
            'COMANDOS': ['NRO', 'ABRE', 'LISTA', 'COMANDOS'],
            'DEF_APRENDA': ['VALOR', 'ABRE', 'LISTA_APRENDA', 'MAIS_COMANDOS'],
            'MAIS_COMANDOS': ['VALOR', 'ABRE', 'LISTA_APRENDA', 'MAIS_COMANDOS'],
    },
    
    'APRENDA': {
            'COMANDOS': ['NOME', 'DEF_APRENDA', 'COMANDOS']
    },

    'ABREPAR': {
            'ABREPAR': [ ]
    },

    'FECHAPAR': {
            'CITA_PARAM': [ ],
            'CITA_PARAM_APRENDA': [ ] 
    },

    'NRO': {
            'NRO': [ ],
            'CITA_PARAM': ['CITA_PARAM'],
            'VALOR': [ ],
            'CITA_PARAM_APRENDA': ['CITA_PARAM_APRENDA'],
    },

    'PARAM': {
            'DEF_APRENDA': ['DEF_APRENDA'],
            'VALOR': [ ],
            'CITA_PARAM_APRENDA': ['CITA_PARAM_APRENDA'],

    },
                    
    'NOME': {
            'NOME': [ ],
            'COMANDOS': ['ABREPAR', 'CITA_PARAM', 'COMANDOS'],
            'DEF_APRENDA': ['ABREPAR', 'CHAMA_PARAM', 'DEF_APRENDA'],
            'MAIS_COMANDOS': ['ABREPAR', 'CHAMA_PARAM_APRENDA', 'MAIS_COMANDOS'],
    }

}

#----------------------------------------

# Tratamento de erros específicos
def trata_erro(topo,terminal):

    if topo == 'S':
        return f'Espera-se a palavra início ao invés de {terminal}'
    elif topo == 'COMANDOS':
        return f'Espera-se um comando (un, ul, ub, pc, pf, pt, pd, pe, mudex, mudey, mudepos, arco, rotule, mudecl, mudecf, repita, nome de função, aprenda) ou a palavra fim ao invés de {terminal}'
    elif topo == 'NRO':
        return f'Espera-se um número ao invés de {terminal}'
    elif topo == 'ABRE':
        return f'Espera-se o símbolo [ ao invés de {terminal}'
    elif topo == 'FECHA':
        return f'Espera-se o símbolo ] ao invés de {terminal}'
    elif topo == 'NOME':
        return f'Espera-se um nome ao invés de {terminal}'
    elif topo == 'LISTA':
        return f'Espera-se uma comando (pf, pt, pd, pe) ou o símbolo ] ao invés de {terminal}'
    elif topo == 'ABREPAR':
        return f'Espera-se o símbolo ( ao invés de {terminal}'
    elif topo == 'CITA_PARAM':
        return f'Espera-se um numero ou o símbolo ) ao invés de {terminal}'
    elif topo == 'DEF_APRENDA':
        return f'Espera-se um parâmetro, um comando (un, ul, ub, pc, pf, pt, pd, pe, mudex, mudey, mudepos, arco, rotule, mudecl, mudecf, repita, nome de função, aprenda) ou a palavra fim ao invés de {terminal}'
    elif topo == 'VALOR':
        return f'Espera-se um número ou parametro ao invés de {terminal}'
    elif topo == 'LISTA_APRENDA':
        return f'Espera-se uma comando (pf, pt, pd, pe) ou o símbolo ] ao invés de {terminal}'
    elif topo == 'CITA_PARAM_APRENDA':
        return f'Espera-se um numero, um parâmetro ou o símbolo ) ao invés de {terminal}'
    elif topo == 'MAIS_COMANDOS':
        return f'Espera-se um comando (un, ul, ub, pc, pf, pt, pd, pe, mudex, mudey, mudepos, arco, rotule, mudecl, mudecf, repita, nome de função, aprenda) ou a palavra fim ao invés de {terminal}'

#----------------------------------------

# Definição do automo com pilha
def automato_pilha(fita):

    # Transições do autômato com pilha ocorrem no estado q1
    estado = 'q1'

    # Transição de q0 para q1; acrescenta a variável S no topo pilha
    pilha = ['S']

    # Flags e variáveis auxiliares para o analisador semântico
    defFunc = []
    paramDefFunc = []
    inParamDefFunc = False
    chamaFunc = False
    qtdParam = 0
    auxNome = ''
    posicao = [0.0, 0.0]
    giro = 0
    pf = False
    pt = False
    pe = False
    pd = False
    arco = False
    auxarco = 0
    arcoangulo = 0
    cor = False
    auxcor = 0
    mudex = False
    mudey = False
    mudepos = False
    mudeposaux = 0

    try:
        # percorrer-se-á os terminais da cadeia de entrada buscando sempre uma transição definida para o terminal
        for terminal in fita:
            
            topo = pilha[-1] 

            pilha.pop()

            print(f'terminal:[{terminal[0]},{terminal[1]}], topo da pilha:{topo}')

            pilha.extend(reversed(transicao_pilha[terminal[1]][topo]))

            #----------------------------------------

            # Definição do analisador semântico
            if terminal[1] == 'APRENDA':
                inParamDefFunc = True
                paramDefFunc = []
                qtdParam = 0

            # Evitando conflito de nomes iguais em funções
            if terminal[1] == 'NOME' and inParamDefFunc:
                for func in defFunc:
                    if terminal[0] in func:
                        print(f'Função {terminal[0]} já existe')
                        print('rejeitado \n')
                        return
                auxNome = terminal[0]
                
            # Controle da quantidade de parâmetros da função
            if terminal[1] == 'PARAM' and inParamDefFunc:
                paramDefFunc.append(terminal[0])
                qtdParam = qtdParam + 1

            if terminal[1] != 'APRENDA' and terminal[1] != 'PARAM' and terminal[1] != 'NOME' and inParamDefFunc:
                inParamDefFunc = False
                defFunc.append([auxNome, qtdParam])
                
            # Verificação se o parametro usado já foi definido
            if terminal[1] == 'PARAM' and not inParamDefFunc:
                if terminal[0] not in paramDefFunc:
                    print(f'Parâmetro {terminal[0]} não definido')
                    print('rejeitado \n')
                    return

            # Função chamada deve estar definida num aprenda
            if terminal[1] == 'NOME' and (topo == 'COMANDOS' or topo == 'DEF_APRENDA' or topo == 'MAIS_COMANDOS'):
                chamaFunc = True
                auxNome = terminal[0]
                qtdParam = 0
                funcExiste = False
                for func in defFunc:
                    if terminal[0] in func:
                        funcExiste = True
                if funcExiste == False:
                    print(f'Função {terminal[0]} não definida')
                    print('rejeitado \n')
                    return

            if (terminal[1] == 'NRO' or terminal[1] == 'PARAM') and chamaFunc:
                qtdParam = qtdParam + 1
                
            # Na chamada de função, a quantidade de parâmetros deve estar de acordo com a definição
            if terminal[1] != 'NOME' and terminal[1] != 'NRO' and terminal[1] != 'PARAM' and terminal[1] != 'ABREPAR' and chamaFunc:
                chamaFunc = False
                paramExiste = False
                for func in defFunc:
                    if qtdParam in func:
                        paramExiste = True
                if paramExiste == False:
                    print(f'Quantidade de parâmetro em {auxNome} inválida')
                    print('rejeitado \n')
                    return

            if terminal[1] == 'PF':
                pf = True

            if terminal[1] == 'PT':
                pt = True

            if terminal[1] == 'PE':
                pe = True

            if terminal[1] == 'PD':
                pd = True

            if terminal[1] == 'ARCO':
                arco = True
                auxarco = 0

            if terminal[1] == 'MUDECL' or terminal[1] == 'MUDECF' or terminal[1] == 'MUDECP':
                cor = True
                auxcor = 0

            if terminal[1] == 'MUDEX':
                mudex = True

            if terminal[1] == 'MUDEY':
                mudey = True

            if terminal[1] == 'MUDEPOS':
                mudepos = True
                mudeposaux = 0

            if terminal[1] == 'PARAM':
                if pf:
                    pf = False

                if pt:
                    pt = False

                if pe:
                    pe = False

                if pd:
                    pd = False

                if arco:
                    arco = False

                if cor:
                    cor = False

                if mudex:
                    mudex = False

                if mudey:
                    mudey = False

                if mudepos:
                    mudepos = False

            if terminal[1] == 'NRO':
                # No movimento, deslocamento deve ser não negativo
                if pf:
                    if int(terminal[0]) < 0 or int(terminal[0]) > 1468: # 1468 =~ diagonal da tela. Maior deslocamento possível
                        print(f'Deslocamento inválido')
                        print('rejeitado \n')
                        return
                    pf = False

                if pt:
                    if int(terminal[0]) < 0 or int(terminal[0]) > 1468: # 1468 =~ diagonal da tela. Maior deslocamento possível
                        print(f'Deslocamento inválido')
                        print('rejeitado \n')
                        return
                    pt = False

                # No giro, ângulo deve ser não negativo
                if pe or pd:
                    if int(terminal[0]) < 0:
                        print(f'Ângulo negativo inválido')
                        print('rejeitado \n')
                        return
                    pe = False
                    pd = False

                # Na definição do arco, ambos - ângulo e raio devem ser não negativos
                if arco:
                    if auxarco < 1:
                        arcoangulo = int(terminal[0])
                        if arcoangulo < 0:
                            print(f'Ângulo negativo inválido')
                            print('rejeitado \n')
                            return
                        auxarco = auxarco + 1
                    else:
                        if int(terminal[0]) < 0:
                            print(f'Raio negativo inválido')
                            print('rejeitado \n')
                            return
                        arco = False

                # Margem do valor RGB: [0, 255]
                if cor:
                    if auxcor < 2:
                        if int(terminal[0]) < 0 or int(terminal[0]) > 255:
                            print(f'valor RGB inválido')
                            print('rejeitado \n')
                            return
                        auxcor = auxcor + 1
                    else:
                        if int(terminal[0]) < 0 or int(terminal[0]) > 255:
                            print(f'valor RGB inválido')
                            print('rejeitado \n')
                            return
                        cor = False

                # Posição 0x0 no centro da tela (640x360 no canvas)
                # Margens:
                #   [-640, 640] em x ([0, 1280] no canvas)
                #   [-360, 360] em y ([0, 720] no canvas)
                if mudex:
                    if int(terminal[0]) < -640 or int(terminal[0]) > 640:
                        print(f'Limites da tela ultrapassados')
                        print('rejeitado \n')
                        return
                    mudex = False

                if mudey:
                    if int(terminal[0]) < -360 or int(terminal[0]) > 360:
                        print(f'Limites da tela ultrapassados')
                        print('rejeitado \n')
                        return
                    mudey = False

                if mudepos:
                    if mudeposaux < 1:
                        if int(terminal[0]) < -640 or int(terminal[0]) > 640:
                            print(f'Limites da tela ultrapassados')
                            print('rejeitado \n')
                            return
                        mudeposaux = mudeposaux + 1
                    else:
                        if int(terminal[0]) < -360 or int(terminal[0]) > 360:
                            print(f'Limites da tela ultrapassados')
                            print('rejeitado \n')
                            return
                        mudepos = False

        # Percorreu-se todos os terminais da cadeia - a cadeia, pois, está vazia
        # Verificação se a pilha também está vazia
        if len(pilha) == 0:
            estado = 'qf'

        # Se foi lida a cadeia, mas a pilha não estiver vazia, não se alcança qf e rejeita-se a cadeia
        if estado != 'qf':
            print(trata_erro(topo, terminal[0]))
            print('rejeitado \n')
            return

    # Caso seja lido um terminal sem nenhuma transição definida, interrompe-se a leitura
    except:
        print(trata_erro(topo, terminal[0]))
        print('rejeitado \n')
        return

    print('aceito \n')
    intermediario(fita)
    return

#----------------------- léxico ----------------------------------

# Definição da função transição: um dicionário dentro de outro - [ estado, lexema, próximo_estado ]
transicao = { 'q0' :  { 'a' : 'qf1',
                        'b' : 'qf1',
                        'c' : 'qf1',
                        'd' : 'qf1',
                        'e' : 'qf1',
                        'f' : 'qf1',
                        'g' : 'qf1',
                        'h' : 'qf1',
                        'i' : 'qf1',
                        'j' : 'qf1',
                        'k' : 'qf1',
                        'l' : 'qf1',
                        'm' : 'qf1',
                        'n' : 'qf1',
                        'o' : 'qf1',
                        'p' : 'qf1',
                        'q' : 'qf1',
                        'r' : 'qf1',
                        's' : 'qf1',
                        't' : 'qf1',
                        'u' : 'qf1',
                        'v' : 'qf1',
                        'w' : 'qf1',
                        'x' : 'qf1',
                        'y' : 'qf1',
                        'z' : 'qf1',
                        '0' : 'qf2',
                        '1' : 'qf2',
                        '2' : 'qf2',
                        '3' : 'qf2',
                        '4' : 'qf2',
                        '5' : 'qf2',
                        '6' : 'qf2',
                        '7' : 'qf2',
                        '8' : 'qf2',
                        '9' : 'qf2',
                        '[' : 'qf3',
                        ']' : 'qf4',
                        '(' : 'qf5',
                        ')' : 'qf6',
                        ':' : 'q1',
                        '-' : 'q2'},
              
             'qf1' :  { 'a' : 'qf1',
                        'b' : 'qf1',
                        'c' : 'qf1',
                        'd' : 'qf1',
                        'e' : 'qf1',
                        'f' : 'qf1',
                        'g' : 'qf1',
                        'h' : 'qf1',
                        'i' : 'qf1',
                        'j' : 'qf1',
                        'k' : 'qf1',
                        'l' : 'qf1',
                        'm' : 'qf1',
                        'n' : 'qf1',
                        'o' : 'qf1',
                        'p' : 'qf1',
                        'q' : 'qf1',
                        'r' : 'qf1',
                        's' : 'qf1',
                        't' : 'qf1',
                        'u' : 'qf1',
                        'v' : 'qf1',
                        'w' : 'qf1',
                        'x' : 'qf1',
                        'y' : 'qf1',
                        'z' : 'qf1'} ,
              
              'q2' :  { '0' : 'qf2',
                        '1' : 'qf2',
                        '2' : 'qf2',
                        '3' : 'qf2',
                        '4' : 'qf2',
                        '5' : 'qf2',
                        '6' : 'qf2',
                        '7' : 'qf2',
                        '8' : 'qf2',
                        '9' : 'qf2'},
              
             'qf2' :  { '0' : 'qf2',
                        '1' : 'qf2',
                        '2' : 'qf2',
                        '3' : 'qf2',
                        '4' : 'qf2',
                        '5' : 'qf2',
                        '6' : 'qf2',
                        '7' : 'qf2',
                        '8' : 'qf2',
                        '9' : 'qf2'},

              'q1' :  { 'a' : 'qf7',
                        'b' : 'qf7',
                        'c' : 'qf7',
                        'd' : 'qf7',
                        'e' : 'qf7',
                        'f' : 'qf7',
                        'g' : 'qf7',
                        'h' : 'qf7',
                        'i' : 'qf7',
                        'j' : 'qf7',
                        'k' : 'qf7',
                        'l' : 'qf7',
                        'm' : 'qf7',
                        'n' : 'qf7',
                        'o' : 'qf7',
                        'p' : 'qf7',
                        'q' : 'qf7',
                        'r' : 'qf7',
                        's' : 'qf7',
                        't' : 'qf7',
                        'u' : 'qf7',
                        'v' : 'qf7',
                        'w' : 'qf7',
                        'x' : 'qf7',
                        'y' : 'qf7',
                        'z' : 'qf7' },
                        
             'qf7' :  { 'a' : 'qf7',
                        'b' : 'qf7',
                        'c' : 'qf7',
                        'd' : 'qf7',
                        'e' : 'qf7',
                        'f' : 'qf7',
                        'g' : 'qf7',
                        'h' : 'qf7',
                        'i' : 'qf7',
                        'j' : 'qf7',
                        'k' : 'qf7',
                        'l' : 'qf7',
                        'm' : 'qf7',
                        'n' : 'qf7',
                        'o' : 'qf7',
                        'p' : 'qf7',
                        'q' : 'qf7',
                        'r' : 'qf7',
                        's' : 'qf7',
                        't' : 'qf7',
                        'u' : 'qf7',
                        'v' : 'qf7',
                        'w' : 'qf7',
                        'x' : 'qf7',
                        'y' : 'qf7',
                        'z' : 'qf7' }
             
                        
            }

#----------------------------------------

# Classificação pelo estado final
classificacao = { 'qf2' : 'NRO',
                  'qf3' : 'ABRE',
                  'qf4' : 'FECHA',
                  'qf5' : 'ABREPAR',
                  'qf6' : 'FECHAPAR',
                  'qf7' : 'PARAM'}

#------------------------------------------

# Lista de palavras reservadas para classificação
# Quaisquer palavras fora estas será tratado como nome ou texto
def reservado(palavra):

    if (palavra == 'inicio'):
        return 'INICIO'
    elif (palavra == 'pf'):
        return 'PF'
    elif (palavra == 'pt'):
        return 'PT'
    elif (palavra == 'pd'):
        return 'PD'
    elif (palavra == 'pe'):
        return 'PE'
    elif (palavra == 'repita'):
        return 'REPITA'
    elif (palavra == 'aprenda'):
        return 'APRENDA'
    elif (palavra == 'fim'):
        return 'FIM'
    elif (palavra == 'un'):
        return 'UN'
    elif (palavra == 'ul'):
        return 'UL'
    elif (palavra == 'ub'):
        return 'UB'
    elif (palavra == 'pc'):
        return 'PC'
    elif (palavra == 'mudex'):
        return 'MUDEX'
    elif (palavra == 'mudey'):
        return 'MUDEY'
    elif (palavra == 'mudepos'):
        return 'MUDEPOS'
    elif (palavra == 'arco'):
        return 'ARCO'
    elif (palavra == 'rotule'):
        return 'ROTULE'
    elif (palavra == 'mudecl'):
        return 'MUDECL'
    elif (palavra == 'mudecf'):
        return 'MUDECF'
    else:
        return 'NOME'

#------------------------------------------

def trataErro(estado):
    if(estado) == 'q1':
        return 'Erro na definição do parâmetro, esperada letra depois de :'
    if(estado) == 'q2':
        return 'Erro na definição do número, esperado valor depois de -'
    
#------------------------------------------
    
def lexico(lista):

    erro = False

    # Inicialização da tabela de símbolos como uma lista vazia
    tabela_simbolos = []

    # Definição dos estados finais
    F = ['qf2','qf3','qf4','qf5','qf6','qf7']    

    for lexema in lista:


        # Definição do estado inicial
        estado = 'q0'
        
        try:
            for caracter in lexema:
                estado = transicao[estado][caracter]
        
            if (estado in F):
                tabela_simbolos.append([lexema,
                                        classificacao[estado]]) 
            elif (estado == 'qf1'):
                tabela_simbolos.append([lexema,
                                            reservado(lexema)])
            else:
                print(trataErro(estado))
                erro = True
                break


        # Caso não exista transição definida, interrompe-se a leitura 
        except: 
                print(f'Caractere {caracter} não definido na palavra {lexema}')
                erro = True
                break  

    print(tabela_simbolos)
    if not erro:
        print('aceito \n')
        automato_pilha(tabela_simbolos)
    else:
        print('rejeitado \n')
    return

#-----------------------------------------------------------


# ------------------------  Entrada ------------------------

# Lê-se a cadeia de entrada
arquivo = open("entrada.txt","r")

lexemas = []

for linha in arquivo.readlines():
    lexemas.extend(linha.split()) 

arquivo.close()

lexico(lexemas)









