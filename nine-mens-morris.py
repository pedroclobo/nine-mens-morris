"""
FP2020/2021 @ IST - Projeto 2 - Jogo do Moinho

Neste projeto de Fundamentos da Programacao pretende-se desenvolver funcoes de
forma a implementar um programa em Python que permita a um jogador humano jogar
o Jogo do Moinho contra o computador.

Pedro Lobo
99115
"""

"""
TAD Posicao
Representacao interna: lista [c, l] com c coluna e l linha da posicao.

-> Construtores
cria_posicao: cadeia de caracteres x cadeia de caracteres -> posicao
cria_copia_posicao: posicao -> posicao

-> Seletores
obter_pos_c: posicao -> cadeia de caracteres
obter_pos_l: posicao -> cadeia de caracteres

-> Reconhecedor
eh_posicao: universal -> valor logico

-> Teste
posicoes_iguais: posicao x posicao -> valor logico

-> Transformador
posicao_para_str : posicao -> cadeia de caracteres
"""

def cria_posicao(c, l):
    """Cria uma posicao.

    :param c: cadeia de carateres, coluna
    :param l: cadeia de carateres, linha
    :return: posicao

    Recebe duas cadeias de carateres correspondentes a linha l e a coluna c duma
    posicao e devolve a o TAD posicao correspondente.
    """
    if not (isinstance(c, str) and isinstance(l, str) and
            c in ('a', 'b', 'c') and
            l in ('1', '2', '3')):
        raise ValueError('cria_posicao: argumentos invalidos')

    return [c, l]


def cria_copia_posicao(p):
    """Recebe uma posicao e devolve uma copia nova da posicao.

    :param p: posicao
    :return: posicao
    """
    return p.copy()


def obter_pos_c(p):
    """Devolve a componente coluna c da posicao p.

    :param p: posicao
    :return: cadeia de caracteres, coluna
    """
    return p[0]


def obter_pos_l(p):
    """Devolve a componente linha l da posicao p.

    :param p: posicao
    :return: cadeia de caracteres, linha
    """
    return p[1]


def eh_posicao(arg):
    """Reconhece um TAD posicao.

    :param arg: universal
    :return: valor logico
    """
    return isinstance(arg, list) and len(arg) == 2 and \
           isinstance(arg[0], str) and isinstance(arg[1], str) and \
           arg[0] in ('a', 'b', 'c') and arg[1] in ('1', '2', '3')


def posicoes_iguais(p1, p2):
    """Reconhece se duas posicoes sao iguais.

    :param p1: posicao
    :param p2: posicao
    :return: valor logico
    """
    return eh_posicao(p1) and eh_posicao(p2) and \
           cria_copia_posicao(p1) == cria_copia_posicao(p2)


def posicao_para_str(p):
    """Devolve a representacao externa da posicao.

    :param p: posicao
    :return: cadeia de caracteres, representacao externa da posicao

    Devolve a cadeia de caracteres 'cl' que representa o seu argumento, sendo
    os valores c e l as componentes coluna e linha de p, respetivamente.
    """
    return obter_pos_c(p) + obter_pos_l(p)


def obter_posicoes_adjacentes(p):
    """Devolve as posicoes adjacentes a posicao p.

    :param p: posicao
    :return: tuplo, contem posicoes adjacentes a posicao p

    Devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
    ordem de leitura do tabuleiro. Uma posicao tem outra como adjacente se
    tiver a ultima conectada por uma linha horizontal, vertical ou diagonal.
    """
    if posicoes_iguais(p, cria_posicao('a', '1')):
        pos_adj = ('b1', 'a2', 'b2')
    elif posicoes_iguais(p, cria_posicao('b', '1')):
        pos_adj = ('a1', 'c1', 'b2')
    elif posicoes_iguais(p, cria_posicao('c', '1')):
        pos_adj = ('b1', 'b2', 'c2')
    elif posicoes_iguais(p, cria_posicao('a', '2')):
        pos_adj = ('a1', 'b2', 'a3')
    elif posicoes_iguais(p, cria_posicao('b', '2')):
        pos_adj = ('a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3')
    elif posicoes_iguais(p, cria_posicao('c', '2')):
        pos_adj = ('c1', 'b2', 'c3')
    elif posicoes_iguais(p, cria_posicao('a', '3')):
        pos_adj = ('a2', 'b2', 'b3')
    elif posicoes_iguais(p, cria_posicao('b', '3')):
        pos_adj = ('b2', 'a3', 'c3')
    elif posicoes_iguais(p, cria_posicao('c', '3')):
        pos_adj = ('b2', 'c2', 'b3')

    return tuple(cria_posicao(pos[0], pos[1]) for pos in pos_adj)


def eh_posicao_adjacente(p1, p2):
    """Reconhece se a posicao p1 e adjacente a posicao p2.

    :param p1: posicao
    :param p2: posicao
    :return: valor logico
    """
    return eh_posicao(p1) and eh_posicao(p2) and \
           any(posicoes_iguais(p1, pa) for pa in obter_posicoes_adjacentes(p2))



"""
TAD Peca
Representacao interna: lista [s] com s correspondente ao jogador da peca:
                       'X', 'O' ou ' ', se nao corresponder a nennhum jogador

-> Construtores
cria_peca: cadeia de caracteres -> peca
cria_copia_peca: peca -> peca

-> Reconhecedor
eh_peca: universal -> valor logico

-> Teste
pecas_iguais: peca x peca -> valor logico

-> Transformador
peca_para_str : peca -> cadeia de caracteres
"""

def cria_peca(s):
    """Cria uma peca.

    :param s: cadeia de carateres
    :return: peca

    Recebe uma cadeia de carateres correspondente ao identificador de um dos
    dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve o TAD peca.
    """
    if not (isinstance(s, str) and
            s in ('X', 'O', ' ')):
        raise ValueError('cria_peca: argumento invalido')

    return [s]


def cria_copia_peca(j):
    """Copia uma peca.

    :param j: peca
    :return: peca

    Recebe uma peca e devolve uma copia nova da peca.
    """
    return j.copy()


def eh_peca(arg):
    """Reconhece uma peca.

    :param arg: universal
    :return: valor logico
    """
    return isinstance(arg, list) and len(arg) == 1 and \
           arg[0] in ('X', 'O', ' ')


def pecas_iguais(j1, j2):
    """Reconhece se duas pecas sao iguais.

    :param j1: peca
    :param j2: peca
    :return: valor logico
    """
    return eh_peca(j1) and eh_peca(j2) and \
           cria_copia_peca(j1) == cria_copia_peca(j2)


def peca_para_str(j):
    """Representacao externa da peca.

    :param j: peca
    :return: cadeia de carateres, representacao externa da peca

    A peca do jogador 'X' e representada por '[X]', a do jogador 'O', por '[O]'
    e a peca livre por '[ ]'.
    """
    if pecas_iguais(j, cria_peca('X')):
        return '[X]'
    elif pecas_iguais(j, cria_peca('O')):
        return '[O]'
    elif pecas_iguais(j, cria_peca(' ')):
        return '[ ]'


def peca_para_inteiro(j):
    """Devolve o inteiro correspondente a peca.

    :param j: peca
    :return: inteiro, representacao externa da peca

    Devolve um inteiro valor 1, -1 ou 0, dependendo se a peca e do jogador 'X',
    'O' ou livre, respetivamente.
    """
    if pecas_iguais(j, cria_peca('X')):
        return 1
    elif pecas_iguais(j, cria_peca('O')):
        return -1
    elif pecas_iguais(j, cria_peca(' ')):
        return 0


def peca_adversaria(p):
    """Devolve a peca do jogador adversario ao jogador da peca especificada.

    :param p: peca
    """
    if pecas_iguais(p, cria_peca('X')):
        return cria_peca('O')
    elif pecas_iguais(p, cria_peca('O')):
        return cria_peca('X')


"""
TAD Tabuleiro
Representacao interna: dicionario: contem as cadeias de caracteres que
                       representam as posicoes como chaves que indexam
                       os TAD peca

-> Construtores
cria_tabuleiro: void -> tabuleiro
cria_copia_tabuleiro: tabuleiro -> tabuleiro

-> Seletores
obter_peca: tabuleiro x posicao -> peca
obter_vetor: tabuleiro x cadeia de caracteres -> tuplo de pecas

-> Modificadores
coloca_peca: tabuleiro x peca x posicao -> tabuleiro
remove_peca: tabuleiro x posicao -> tabuleiro
move_peca: tabuleiro x posicao x posicao -> tabuleiro

-> Reconhecedores
eh_tabuleiro: universal -> valor logico
eh_posicao_livre: tabuleiro x posicao -> valor logico

-> Teste
tabuleiros_iguais: tabuleiro x tabuleiro -> valor logico

-> Transformadores
tabuleiro_para_str: tabuleiro -> cadeia de caracteres
tuplo_para_tabuleiro: tuplo -> tabuleiro
"""

def cria_tabuleiro():
    """Cria um tabuleiro vazio.

    :return: tabuleiro

    Cria um tabuleiro sem posicoes ocupadas pelos jogadores.
    """
    # Chaves do dicionario,
    # contem as representacoes externas de todas as posicoes
    k = (posicao_para_str(cria_posicao(c, l))
         for l in ('1', '2', '3') for c in ('a', 'b', 'c'))

    # Valores do dicionario
    v = 9*(cria_peca(' '), )

    # Cria o dicionario com as chaves em k e valores em v
    return dict(zip(k, v))


def cria_copia_tabuleiro(t):
    """Copia um tabuleiro.

    :param t: tabuleiro
    :return: tabuleiro
    """
    return t.copy()


def obter_peca(t, p):
    """Devolve a peca na posicao p do tabuleiro.

    :param t: tabuleiro
    :param p: posicao
    """
    return cria_copia_peca(t[posicao_para_str(p)])


def obter_vetor(t, s):
    """Devolve todas as pecas da linha ou coluna especificada.

    :param t: tabuleiro
    :param s: cadeia de caracteres, linha ou coluna
    :return: tuplo, contem as pecas da linha ou coluna
    """
    # Se s for uma coluna
    if s in ('a', 'b', 'c'):
        return (obter_peca(t, cria_posicao(s, '1')),
                obter_peca(t, cria_posicao(s, '2')),
                obter_peca(t, cria_posicao(s, '3')))

    # Se s for uma linha
    if s in ('1', '2', '3'):
        return (obter_peca(t, cria_posicao('a', s)),
                obter_peca(t, cria_posicao('b', s)),
                obter_peca(t, cria_posicao('c', s)))


def coloca_peca(t, j, p):
    """Coloca a peca j na posicao p do tabuleiro.

    :param t: tabuleiro
    :param j: peca
    :param p: posicao
    :return: tabuleiro, com a peca j na posicao p
    """
    t[posicao_para_str(p)] = j

    return t


def remove_peca(t, p):
    """Remove a peca j na posicao p do tabuleiro.

    :param t: tabuleiro
    :param p: posicao
    :return: tabuleiro, com a posicao p livre
    """
    # Remover uma peca equivale a colocar uma peca livre
    return coloca_peca(t, cria_peca(' '), p)


def move_peca(t, p1, p2):
    """Move a peca da posicao p1 para a posicao p2 do tabuleiro.

    :param t: tabuleiro
    :param p1: posicao
    :param p2: posicao
    :return: tabuleiro, com a peca da posicao p1 na posicao p2
    """
    # Se as posicoes coincidirem o tabuleiro permanece igual
    if posicoes_iguais(p1, p2):
        return t

    # Caso contrario, equivale a colocar a peca da posicao1 na posicao2
    # e, de seguida, remover a peca da posicao1
    return remove_peca(coloca_peca(t, obter_peca(t, p1), p2), p1)


def eh_tabuleiro(arg):
    """Reconhece um tabuleiro.

    :param arg: universal
    :return: valor logico

    Um tabuleiro valido corresponde a um TAD tabuleiro, contem apenas pecas
    validas, cada jogador tem 3 ou menos pecas no tabuleiro, a diferenca do
    numero de pecas entre os jogadores nao e maior que 1 e apenas existe um so
    ganhador.
    """
    # As condicoes verificadas abaixo sao:
    # Trata-se de um TAD tabuleiro;
    # Todas as pecas do tabuleiro correpondem a pecas validas;
    # Cada jogador tem 3 ou menos pecas no tabuleiro;
    # A diferenca do numero de pecas entre os jogadores nao e maior do que 1;
    # So existe um ganhador
    return isinstance(arg, dict) and len(arg) == 9 and \
           all(posicao_para_str(cria_posicao(c, l)) in arg for c in ('a', 'b', 'c') for l in ('1', '2', '3')) and \
           all(eh_peca(obter_peca(arg, cria_posicao(c, l))) for c in ('a', 'b', 'c') for l in ('1', '2', '3')) and \
           all(obter_num_pecas(arg, cria_peca(j)) <= 3 for j in ('X', 'O')) and \
           abs(obter_num_pecas(arg, cria_peca('X')) - obter_num_pecas(arg, cria_peca('O'))) <= 1 and \
           not not obter_ganhador(arg)


def eh_posicao_livre(t, p):
    """Reconhece posicoes livres.

    :param t: tabuleiro
    :param p: posicao
    :return: valor logico
    """
    # Uma posicao livre contem a peca livre
    return pecas_iguais(obter_peca(t, p), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    """Reconhece se dois tabuleiro sao iguais.

    :param t1: tabuleiro
    :param t2: tabuleiro
    :return: valor logico
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and \
           all(pecas_iguais(obter_peca(t1, cria_posicao(c, l)),
                            obter_peca(t2, cria_posicao(c, l))) \
               for c in ('a', 'b', 'c') for l in ('1', '2', '3'))


def tabuleiro_para_str(t):
    """Devolve a representacao externa do tabuleiro.

    :param t: tabuleiro
    :return: cadeia de caracteres, representacao externa do tabuleiro
    """
    s = ''

    # Sep contem as cadeias de caracteres que antecedem cada linha do tabuleiro
    sep = ('   a   b   c', '\n   | \\ | / |', '\n   | / | \\ |')

    for l in ('1', '2', '3'):
        s += sep[eval(l)-1] + '\n' + \
            str(eval(l)) + ' ' + \
            str(peca_para_str(obter_vetor(t, l)[0])) + '-' + \
            str(peca_para_str(obter_vetor(t, l)[1])) + '-' + \
            str(peca_para_str(obter_vetor(t, l)[2]))

    return s


def tuplo_para_tabuleiro(t):
    """Devolve o tabuleiro representado pelo tuplo t.

    :param t: tuplo
    :return: tabuleiro

    O tuplo e constituido por 3 tuplos, cada um deles com 3 pecas,
    correspondentes a peca do jogador, em cada uma das posicoes.
    """
    def inteiro_para_peca(i):
        """Converte um inteiro entre 0 e 8 para a respetiva posicao.

        :param i: inteiro
        :return: posicao
        """
        if i == 1:
            return cria_peca('X')
        elif i == -1:
            return cria_peca('O')
        elif i == 0:
            return cria_peca(' ')

    tab = cria_tabuleiro()

    for l in ('1', '2', '3'):
        # Por cada inteiro na linha do tuplo, coloca no tabuleiro a peca
        # correspondente ao inteiro, na posicao correta
        for i, c in zip(t[eval(l)-1], ('a', 'b', 'c')):
            coloca_peca(tab, inteiro_para_peca(i), cria_posicao(c, l))

    return tab


def obter_ganhador(t):
    """Devolve a peca do jogador ganhador.

    :param t: tabuleiro
    :return: peca

    Devolve uma peca do jogador que tenha as suas 3 pecas em linha na vertical
    ou na horizontal. Se nao existir jogador ganhador, devolve uma peca livre.
    """
    # Se existir 3 pecas do jogador 'X' em linha na vertical ou horizontal
    # e nao existirem 3 pecas em linha na vertical ou horizontal para o
    # jogador 'O', o jogador 'X' e ganhador.
    if any(all(pecas_iguais(p, cria_peca('X')) for p in obter_vetor(t, v))
           for v in ('1', '2', '3', 'a', 'b', 'c')) and \
       all(any(not pecas_iguais(p, cria_peca('O')) for p in obter_vetor(t, v))
           for v in ('1', '2', '3', 'a', 'b', 'c')):
        return cria_peca('X')

    # Idem em relacao ao jogador 'O'
    if any(all(pecas_iguais(p, cria_peca('O')) for p in obter_vetor(t, v))
           for v in ('1', '2', '3', 'a', 'b', 'c')) and \
       all(any(not pecas_iguais(p, cria_peca('X')) for p in obter_vetor(t, v))
           for v in ('1', '2', '3', 'a', 'b', 'c')):
        return cria_peca('O')

    # Se nao existir 3 pecas em linha na vertical ou horizontal para
    # qualquer um dos 2 jogadores, nao existe jogador ganhador.
    if all(any(not pecas_iguais(p, cria_peca('O')) for p in obter_vetor(t, v)) and \
           any(not pecas_iguais(p, cria_peca('X')) for p in obter_vetor(t, v))
           for v in ('1', '2', '3', 'a', 'b', 'c')):
        return cria_peca(' ')


def obter_posicoes_livres(t):
    """Devolve um tuplo ordenado das posicoes livres do tabuleiro.

    :param t: tabuleiro
    :return: tuplo
    """
    # Uma posicao livre contem a peca livre
    return obter_posicoes_jogador(t, cria_peca(' '))


def obter_posicoes_jogador(t, j):
    """Devolve um tuplo ordenado com as posicoes ocupadas pelo jogador j.

    :param t: tabuleiro
    :param j: peca
    :return: tuplo
    """
    pos = ()

    for l in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):
            # Se na posicao estiver uma peca do jogador,
            # essa posicao e adicionada ao resultado
            if pecas_iguais(obter_peca(t, cria_posicao(c, l)), j):
                pos += (cria_posicao(c, l), )

    return pos


def obter_num_pecas(t, p, v='todos'):
    """Devolve o numero de pecas de um jogador no vetor especificado.

    :param t: tabuleiro
    :param p: peca
    :param v: cadeia de caracteres, linha ou coluna
    :return: inteiro

    Se nenhum vetor for especificado e calculado o numero de pecas do jogador
    em todo o tabuleiro.
    """
    n_pecas = 0

    # Se o vetor corresponder a uma linha
    if v in ('1', '2', '3'):
        for c in ('a', 'b', 'c'):
            if pecas_iguais(obter_peca(t, cria_posicao(c, v)), p):
                n_pecas += 1

    # Se o vetor corresponder a uma coluna
    elif v in ('a', 'b', 'c'):
        for l in ('1', '2', '3'):
            if pecas_iguais(obter_peca(t, cria_posicao(v, l)), p):
                n_pecas += 1

    # Se o vetor nao for especificado
    elif v == 'todos':
        for c in ('a', 'b', 'c'):
            for l in ('1', '2', '3'):
                if pecas_iguais(obter_peca(t, cria_posicao(c, l)), p):
                    n_pecas += 1

    return n_pecas


def ha_ganhador(t):
    """Reconhece se existe um ganhador.

    :param t: tabuleiro
    :return: valor logico
    """
    return not pecas_iguais(obter_ganhador(t), cria_peca(' '))


def eh_fase_colocacao(t):
    """Reconhece se o jogo se encontra na fase de colocacao.

    :param t: tabuleiro
    :return: valor logico

    O jogo encontra-se na fase de colocacao se ambos os jogadores ainda nao
    tiverem colocado 3 pecas no tabuleiro e se nao existir ganhador.
    """
    return not all(obter_num_pecas(t, cria_peca(j)) == 3 for j in ('X', 'O')) and \
               not ha_ganhador(t)


def eh_fase_movimento(t):
    """Reconhece se o jogo se encontra na fase de movimento.

    :param t: tabuleiro
    :return: valor logico

    O jogo encontra-se na fase de movimento se ambos os jogadores tiverem
    colocado 3 pecas no tabuleiro e se nao existir ganhador.
    """
    return all(obter_num_pecas(t, cria_peca(j)) == 3 for j in ('X', 'O')) and \
           not ha_ganhador(t)


def obter_movimento_manual(t, p):
    """Funcao auxiliar que recebe um tabuleiro e uma peca de um jogador, e
    devolve um tuplo com uma ou duas posicoes que representam uma posicao
    ou um movimento introduzido manualmente pelo jogador.

    :param t: tabuleiro
    :param p: peca
    :return: tuplo
    """
    posicoes = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')

    # Input do utilizador
    if eh_fase_colocacao(t):
        pos = input('Turno do jogador. Escolha uma posicao: ')

        # O input tera de corresponder a representacao externa duma posicao
        if not (isinstance(pos, str) and len(pos) == 2 and pos in posicoes):
            raise ValueError('obter_movimento_manual: escolha invalida')

        p = cria_posicao(pos[0], pos[1])

        # Se a posicao de destino nao corresponder a uma posicao livre,
        # trata-se de uma escolha invalida
        if not eh_posicao_livre(t, p):
            raise ValueError('obter_movimento_manual: escolha invalida')

        return (p, )

    # Input do utilizador
    elif eh_fase_movimento(t):
        mov = input('Turno do jogador. Escolha um movimento: ')

        # O input tera de ser da forma 'p1p2' com p1 e p2 represetancoes externas
        # de posicoes
        if not (isinstance(mov, str) and len(mov) == 4 and
                mov[:2] in posicoes and mov[2:] in posicoes):
            raise ValueError('obter_movimento_manual: escolha invalida')

        p1, p2 = cria_posicao(mov[0], mov[1]), cria_posicao(mov[2], mov[3])

        # Uma escolha e valida se na posicao de origem estiver uma peca do jogador e
        # se a posicao de destino corresponder a uma posicao adjacente livre
        # ou
        # Se a posicao de origem coincidir com a posicao de destino e o jogador
        # nao tiver posicoes adjacentes a primeira para a qual possa mover a segunda
        if not (pecas_iguais(obter_peca(t, p1), p) and eh_posicao_livre(t, p2) and
                eh_posicao_adjacente(p2, p1) or
                (posicoes_iguais(p1, p2) and pecas_iguais(obter_peca(t, p1), p) and
                 not any(eh_posicao_livre(t, p) for p in obter_posicoes_adjacentes(p1)))):
            raise ValueError('obter_movimento_manual: escolha invalida')

        return (p1, p2)


def eh_nivel_dificuldade(d):
    """Reconhece um nivel de dificuldade.

    :param d: cadeia de caracteres, nivel de dificuldade
    :return: valor logico
    """
    return isinstance(d, str) and d in ('facil', 'normal', 'dificil')


def obter_movimento_auto(t, p, d):
    """Funcao auxiliar que recebe um tabuleiro, uma peca de um jogador e uma cadeia de
    carateres representando o nivel de dificuldade do jogo, e devolve um tuplo com uma ou
    duas posicoes que representam uma posicao ou um movimento escolhido automaticamente.

    :param t: tabuleiro
    :param p: peca
    :param d: cadeia de caracteres, nivel de dificuldade
    """
    def vitoria(t, p):
        """Devolve a posicao a jogar segundo a estrategia 'vitoria'.

        :param t: tabuleiro
        :param p: peca
        :return: posicao

        Se o jogador tiver duas das suas pecas em linha e uma posicao livre, entao deve
        marcar na posicao livre (ganhando o jogo).
        """
        for v in ('1', '2', '3', 'a', 'b', 'c'):
            # Se algum vetor tiver 2 pecas do jogador
            if obter_num_pecas(t, p, v) == 2:
                # Se o vetor for uma linha
                if v in ('1', '2', '3'):
                    for c in ('a', 'b', 'c'):
                        # Devolve a posicao livre nessa mesma linha
                        if eh_posicao_livre(t, cria_posicao(c, v)):
                            return (cria_posicao(c, v), )
                # Se o vetor for uma coluna
                elif v in ('a', 'b', 'c'):
                    for l in ('1', '2', '3'):
                        # Devolve a posicao livre nessa mesma linha
                        if eh_posicao_livre(t, cria_posicao(v, l)):
                            return (cria_posicao(v, l), )


    def bloqueio(t, p):
        """Devolve a posicao a jogar segundo a estrategia 'bloqueio'.

        :param t: tabuleiro
        :param p: peca
        :return: posicao

        Se o adversario tiver duas das suas pecas em linha e uma posicao livre, entao
        deve marcar na posicao livre (para bloquear o adversario).
        """
        return vitoria(t, peca_adversaria(p))


    def centro(t):
        """Devolve a posicao a jogar segundo a estrategia 'centro'.

        :param t: tabuleiro
        :return: posicao

        Se a posicao central estiver livre, entao jogar na posicao central.
        """
        if eh_posicao_livre(t, cria_posicao('b', '2')):
            return (cria_posicao('b', '2'), )


    def canto_vazio(t):
        """Devolve a posicao a jogar segundo a estrategia 'canto vazio'.

        :param t: tabuleiro
        :return: posicao

        Se um canto for uma posicao livre, entao jogar nesse canto.
        """
        for l in ('1', '3'):
            for c in ('a', 'c'):
                if eh_posicao_livre(t, cria_posicao(c, l)):
                    return (cria_posicao(c, l), )


    def lateral_vazio(t):
        """Devolve a posicao a jogar segundo a estrategia 'lateral vazio'.

        :param t: tabuleiro
        :return: posicao

        Se uma posicao lateral (que nem e o centro, nem um canto) for livre,
        entao jogar nesse lateral.
        """
        if eh_posicao_livre(t, cria_posicao('b', '1')):
            return (cria_posicao('b', '1'), )
        elif eh_posicao_livre(t, cria_posicao('a', '2')):
            return (cria_posicao('a', '2'), )
        elif eh_posicao_livre(t, cria_posicao('c', '2')):
            return (cria_posicao('c', '2'), )
        elif eh_posicao_livre(t, cria_posicao('b', '3')):
            return (cria_posicao('b', '3'), )


    def minimax(t, p, prof, seq):
        """Algoritmo que explora todos os movimentos legais desse jogador chamando
        a funcao recursiva com o tabuleiro modificado com um dos movimentos e o
        jogador adversario como novos parametros. No caso geral, o algoritmo devolvera
        o movimento que mais favoreca o jogador do turno atual.

        :param t: tabuleiro
        :param p: peca
        :param prof: inteiro, profundidade da recursao
        :param seq: tuplo, contem melhores resultado e sequencia de movimentos

        :return: tuplo de posicoes
        """
        def valor_tabuleiro(t):
            """Devolve o valor do tabuleiro.

            :param t: tabuleiro
            :return: inteiro (-1, 0 ou 1)

            O valor do tabuleiro e 1 se o jogador ganhador for 'X',
            -1 se o ganhador for 'O' e 0 se nao existir ganhador.
            """
            return peca_para_inteiro(obter_ganhador(t))


        def melhor_resultado(p):
            """Corresponde ao valor do tabuleiro em que o jogador da peca espeficada
            e derrotado.

            :param p: peca
            :return: inteiro (-1, 0 ou 1)
            """
            if pecas_iguais(p, cria_peca('X')):
                return -1
            elif pecas_iguais(p, cria_peca('O')):
                return 1

        # Se existe um ganhador ou a profundidade e 0
        if ha_ganhador(t) or prof == 0:
            return valor_tabuleiro(t), seq

        else:
            # O melhor resultado e a derrota
            m_res = melhor_resultado(p)
            m_seq = []

            # Por cada peca do jogador
            for pos in obter_posicoes_jogador(t, cria_copia_peca(p)):
                # Por cada posicao adjacente a peca
                for pos_adj in obter_posicoes_adjacentes(cria_copia_posicao(pos)):
                    # Se a posicao adjacente e posicao livre
                    if eh_posicao_livre(t, pos_adj):
                        # Cria copia do tabuleiro e atualiza-o
                        novo_tab = cria_copia_tabuleiro(t)
                        novo_tab = move_peca(novo_tab, pos, pos_adj)
                        # Atualiza o novo resultado e nova sequencia
                        n_res, n_seq = minimax(novo_tab, peca_adversaria(p), prof-1, seq + [pos, pos_adj])

                        # Se a melhor sequencia nao estiver definida ou o novo resultado e melhor
                        # do que o melhor resultado:
                        if not m_seq or \
                           (pecas_iguais(cria_copia_peca(p), cria_peca('X')) and n_res > m_res) or \
                           (pecas_iguais(cria_copia_peca(p), cria_peca('O')) and n_res < m_res):
                            # Atualiza o melhor resultado e melhor sequencia
                            m_res, m_seq = n_res, n_seq

            return m_res, tuple(m_seq[:2])


    def facil(t, p):
        """Devolve a posicao a jogar segundo o nivel de dificuldade 'facil'.

        :param t: tabuleiro
        :param p: peca
        :return: tuplo de posicoes, posicao de origem e posicao de destino

        A peca a movimentar e sempre a que ocupa a primeira posicao em ordem de
        leitura do tabuleiro que tenha alguma posicao adjacente livre. A posicao
        de destino e a primeira posicao adjacente livre.
        """
        for pos in obter_posicoes_jogador(t, p):
            # Se existirem posicoes adjacentes a p
            if obter_posicoes_adjacentes(pos):
                for pos_adj in obter_posicoes_adjacentes(pos):
                    # Se a posicao adjacente estiver livre
                    if eh_posicao_livre(t, pos_adj):
                        return (pos, pos_adj)


    def normal(t, p):
        """Devolve a posicao a jogar segundo o nivel de dificuldade 'facil'.

        :param t: tabuleiro
        :param p: peca
        :return: tuplo de posicoes, posicao de origem e posicao de destino

        O movimento e escolhido utilizando o algoritmo minimax com nivel de
        profundidade maximo de recursao igual a 1.
        """
        return minimax(t, cria_copia_peca(p), 1, [])[1]


    def dificil(t, p):
        """Devolve a posicao a jogar segundo o nivel de dificuldade 'facil'.

        :param t: tabuleiro
        :param p: peca
        :return: tuplo de posicoes, posicao de origem e posicao de destino

        O movimento e escolhido utilizando o algoritmo minimax com nivel de
        profundidade maximo de recursao igual a 5.
        """
        return minimax(t, cria_copia_peca(p), 5, [])[1]

    # Hierarquia de estrategias na fase de colocacao
    if eh_fase_colocacao(t):
        if vitoria(t, p) != None:
            return vitoria(t, p)
        elif bloqueio(t, p) != None:
            return bloqueio(t, p)
        elif centro(t) != None:
            return centro(t)
        elif canto_vazio(t) != None:
            return canto_vazio(t)
        elif lateral_vazio(t) != None:
            return lateral_vazio(t)

    # Hierarquia de estrategias na fase de movimento
    elif eh_fase_movimento(t):
        if d == 'facil':
            return facil(t, p)
        elif d == 'normal':
            return normal(t, p)
        elif d == 'dificil':
            return dificil(t, p)


def moinho(p, d):
    """Funcao principal que permite jogar um jogo completo do jogo do moinho de
    um jogador contra o computador.

    :param p: cadeia de caracteres, representacao externa da peca ('[X]' ou '[O]')
    :param d: cadeia de caracteres, nivel de dificuldade

    A funcao recebe duas cadeias de caracteres e devolve a representacao externa
    da peca ganhadora ('[X]' ou '[O]').
    """
    if not (p in ('[X]', '[O]') and eh_nivel_dificuldade(d)):
        raise ValueError('moinho: argumentos invalidos')

    # Inicio do jogo
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + d + '.')
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))

    # Fase de colocacao
    while eh_fase_colocacao(t):
        if p == '[X]':
            m = obter_movimento_manual(t, cria_peca('X'))
            t = coloca_peca(t, cria_peca('X'), m[0])
            print(tabuleiro_para_str(t))

            # Assim que exista ganhador, o jogo acaba
            if ha_ganhador(t):
                break

            print('Turno do computador (', d, '):', sep='')
            m = obter_movimento_auto(t, cria_peca('O'), d)
            t = coloca_peca(t, cria_peca('O'), m[0])
            print(tabuleiro_para_str(t))

        elif p == '[O]':
            print('Turno do computador (', d, '):', sep='')
            m = obter_movimento_auto(t, cria_peca('X'), d)
            t = coloca_peca(t, cria_peca('X'), m[0])
            print(tabuleiro_para_str(t))

            if ha_ganhador(t):
                break

            m = obter_movimento_manual(t, cria_peca('O'))
            t = coloca_peca(t, cria_peca('O'), m[0])
            print(tabuleiro_para_str(t))

    # Fase de movimento
    while eh_fase_movimento(t):
        if p == '[X]':
            m = obter_movimento_manual(t, cria_peca('X'))
            t = move_peca(t, m[0], m[1])
            print(tabuleiro_para_str(t))

            if ha_ganhador(t):
                break

            print('Turno do computador (', d, '):', sep='')
            m = obter_movimento_auto(t, cria_peca('O'), d)
            t = move_peca(t, m[0], m[1])
            print(tabuleiro_para_str(t))

        elif p == '[O]':
            print('Turno do computador (', d, '):', sep='')
            m = obter_movimento_auto(t, cria_peca('X'), d)
            t = move_peca(t, m[0], m[1])
            print(tabuleiro_para_str(t))

            if ha_ganhador(t):
                break

            m = obter_movimento_manual(t, cria_peca('O'))
            t = move_peca(t, m[0], m[1])
            print(tabuleiro_para_str(t))

    # Devolve a represetancao externa do jogador ganhador
    return peca_para_str(obter_ganhador(t))
