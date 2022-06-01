#TAD posicao
def cria_posicao(x,y):
    """
    cria_posicao: int*int -> posicao
    Esta função devolve uma posição com os dois valores introduzidos
    e devolve um erro se os argumentos nao forem corretos
    """
    if type(x)!=int or type(y)!=int or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x,y)

def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    Esta função devolve uma copia da posicao inserida no argumento
    """
    return tuple((pos[0],pos[1]))

def obter_pos_x(pos):
    """
    obter_pos_x : posicao -> int
    Esta função devolve a componente x da posição pos
    """
    return pos[0]

def obter_pos_y(pos):
    """
    obter_pos_y : posicao -> int
    Esta função devolve a componente y da posição pos
    """
    return pos[1]

def eh_posicao(pos):
    """
    eh_posicao: universal -> bool
    Esta função devolve True caso o seu argumento seja um TAD posicao e False caso contrário
    """
    return type(pos)==tuple and\
    type(pos[0])==int and type(pos[1])==int and\
    pos[0]>=0 and pos[1]>=0

def posicoes_iguais(pos1,pos2):#pode ser ==?
    """
    posicoes_iguais: posicao*posicao -> bool
    Esta função devolve True apenas se pos1 e pos2 são posições e são iguais
    """
    return eh_posicao(pos1) and eh_posicao(pos2) and\
    obter_pos_x(pos1)==obter_pos_x(pos2) and obter_pos_y(pos1)==obter_pos_y(pos2)

def posicao_para_str(pos):
    """
    posicao_para_str : posicao -> str
    Esta função devolve a cadeia de caracteres "(x, y)", sendo os valores x e y as coordenadas de pos.
    """
    return str(cria_posicao(pos[0],pos[1]))

def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes: posicao -> tuplo
    Esta função devolve um tuplo com as posições adjacentes a pos, começando pela posição de cima
    e seguindo no sentido horário.
    """
    if obter_pos_x(pos)==0 and obter_pos_y(pos)==0:
        return (1,0),(0,1) 
    elif obter_pos_x(pos)==0:
        return (cria_posicao(obter_pos_x(pos),obter_pos_y(pos)-1),(cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos))),(cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1)))
    elif obter_pos_y(pos)==0:
        return (cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1),cria_posicao(obter_pos_x(pos)-1,obter_pos_y(pos)))
    else:
        return (cria_posicao(obter_pos_x(pos),obter_pos_y(pos)-1),cria_posicao(obter_pos_x(pos)+1,obter_pos_y(pos)),cria_posicao(obter_pos_x(pos),obter_pos_y(pos)+1),cria_posicao(obter_pos_x(pos)-1,obter_pos_y(pos)))

def ordenar_posicoes(tuplo_pos):
    """
    ordenar_posicoes: tuple -> tuple
    Esta função devolve um tuplo contendo as mesmas posiçoes do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado
    """
    ordenar = sorted(tuplo_pos,key=lambda x: (obter_pos_y(x),obter_pos_x(x)))
    return tuple(ordenar)

#TAD animal
def cria_animal(especie,freq_rep,freq_ali):
    """
    cria_animal: str*int*int -> animal
    Esta função devolve um animal formado pela espécie, freq. de reprodução e freq. de alimentação
    e devolve um erro se os argumentos não forem corretos.
    Se a freq_ali for 0, o animal é uma presa, caso contrário é um predador
    """
    if type(especie)!=str or len(especie)==0 or\
    type(freq_rep)!=int or type(freq_ali)!=int or\
    freq_rep<=0 or freq_ali<0:
        raise ValueError("cria_animal: argumentos invalidos")
    if freq_ali>0:
        return {"especie":especie,"idade":0,"freq_rep":freq_rep,"fome":0,"freq_ali":freq_ali}#predador
    else:
        return {"especie":especie,"idade":0,"freq_rep":freq_rep}#presa

def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal
    Esta função recebe um animal e devolve uma nova cópia do animal.
    """
    return animal.copy()

def obter_especie(animal):
    """
    obter_freq_reproducao: animal -> int
    Esta função devolve a frequência de reprodução do animal
    """
    return animal["especie"]

def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int
    Esta função devolve a frequência de reprodução do animal
    """
    return animal["freq_rep"]

def obter_freq_alimentacao(animal):
    """
    obter freq alimentacao: animal -> int
    Esta função devolve a frequência de alimentação do animal
    Se o animal for uma presa, devolve 0
    """
    if "freq_ali" in animal:
        return animal["freq_ali"]
    else:
        return 0

def obter_idade(animal):
    """
    obter_idade: animal -> int
    Esta função devolve a idade do animal
    """
    return animal["idade"]

def obter_fome(animal):
    """
    obter_fome: animal -> int
    Esta função devolve a fome do animal
    Se o animal for uma presa, devolve 0
    """
    if "fome" in animal:
        return animal["fome"]
    else:
        return 0

def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    Esta função modifica destrutivamente o animal aumentando um valor na sua idade, e devolve o animal
    """
    animal["idade"]+=1
    return animal

def reset_idade(animal):
    """
    reset_idade: animal -> animal
    Esta função modifica destrutivamente o animal alterando o valor da sua idade para 0, e devolve o animal.
    """
    animal["idade"]=0
    return animal

def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    Esta função modifica destrutivamente o animal predador aumentando uma unidade no valor da sua fome,
    e devolve o animal. Esta operação não modifica as presas.
    """
    if "fome" in animal:
        animal["fome"]+=1
    return animal

def reset_fome(animal):
    """
    reset_fome: animal -> animal
    Esta função modifica destrutivamente o animal predador alterando o valor da sua fome para 0,
    e devolve o animal. Esta operação não modifica as presas.
    """
    if "fome" in animal:
        animal["fome"]=0
    return animal
    
def eh_animal(animal):
    """
    eh_animal: universal -> bool
    Esta função devolve True se o seu argumento for um TAD animal e False caso contrário.
    """
    if type(animal)==dict and (len(animal)==3 or len(animal)==5) and\
    ("especie" in animal and "idade" in animal and "freq_rep" in animal) and\
    type(animal["especie"])==str and len(animal["especie"])>0 and\
    type(animal["idade"])==int and animal["idade"]>=0 and\
    type(animal["freq_rep"])==int and animal["freq_rep"]>=0:
        if len(animal)==5:
            return "fome" in animal and "freq_ali" in animal and\
            type(animal["fome"])==int and animal["fome"]>=0 and\
            type(animal["freq_ali"])==int and animal["freq_ali"]>=0
        else:
            return True
    return False

def eh_predador(animal):
    """
    eh_predador: universal -> bool
    Esta função devolve True se o seu argumento for um TAD animal do
    tipo predador e False em caso contrário.
    """
    return eh_animal(animal) and len(animal)==5

def eh_presa(animal):
    """
    eh_presa: universal -> bool
    Esta função devolve True se o seu argumento for um TAD animal do
    tipo presa e False em caso contrário.
    """
    return eh_animal(animal) and len(animal)==3

def animais_iguais(a1,a2):
    """
    animais iguais: animal × animal 7→ booleano
    Esta função devolve True apenas se a1 e a2 são animais e iguais
    """
    if eh_animal(a1) and eh_animal(a2) and\
    obter_especie(a1)==obter_especie(a2) and obter_freq_reproducao(a1)==obter_freq_reproducao(a2) and\
    obter_idade(a1)==obter_idade(a2):
        return obter_fome(a1)==obter_fome(a2) and obter_freq_alimentacao(a1)==obter_freq_alimentacao(a2)
    else:
        return False 

def animal_para_char(animal):
    """
    animal_para_char : animal -> str
    Esta função devolve o primeiro caracter da espécie do animal,
    em maiúscula se for predador e em minúscula se for presa
    """
    if eh_presa(animal):
        return animal["especie"][0].lower()
    return animal["especie"][0].upper()

def animal_para_str(animal):
    """
    animal_para_str: animal -> str
    Esta função devolve a cadeia de caracteres que representa o animal
    """
    if eh_presa(animal):
        return f'{animal["especie"]} [{animal["idade"]}/{animal["freq_rep"]}]'
    return f'{animal["especie"]} [{animal["idade"]}/{animal["freq_rep"]};{animal["fome"]}/{animal["freq_ali"]}]'


def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal -> bool
    Esta função devolve True caso o animal tenha atingido a idade de reprodução e False caso contrário.
    """
    return obter_idade(animal)>=obter_freq_reproducao(animal)

def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal -> bool
    Esta função devolve True caso o animal tenha atingindo um valor de
    fome igual ou superior à sua freq. de alimentação e False caso contrário. As
    presas devolvem sempre False
    """
    return eh_predador(animal) and obter_fome(animal)>=obter_freq_alimentacao(animal)

def reproduz_animal(animal):
    """
    reproduz_animal: animal -> animal
    Esta função recebe um animal e devolve um novo animal da mesma espécie com idade e fome igual a 0,
    e modifica destrutivamente o animal passado como argumento alterando a sua idade para 0
    """
    reset_idade(animal)
    return cria_animal(obter_especie(animal),obter_freq_reproducao(animal),obter_freq_alimentacao(animal))


#TAD prado
def cria_prado(pos,tup_roch,tup_ani,tup_pos_ani):#recebe tuplo mas posso por em lista?
    """
    cria_prado: posicao*tuplo*tuplo*tuplo-> prado
    Esta função recebe a posição que a montanha do canto inferior direito do prado ocupa,
    um tuplo roch de 0 ou mais posições correspondentes aos rochedos que não são as montanhas dos limites exteriores do prado,
    um tuplo ani de 1 ou mais animais, e um tuplo pos ani da
    mesma dimensão do tuplo ani com as posições correspondentes ocupadas pelos animais 
    e devolve o prado que representa internamente o mapa e os animais
    presentes. A função também verifica a validade dos argumentos
    """
    if (not eh_posicao(pos)) or obter_pos_x(pos)<2 or obter_pos_y(pos)<2 or\
    type(tup_roch)!=tuple or\
    any(not eh_posicao(i) for i in tup_roch) or any(obter_pos_x(i)==0 or obter_pos_x(i)>=obter_pos_x(pos) for i in tup_roch) or\
    any(obter_pos_y(i)==0 or obter_pos_y(i)>=obter_pos_y(pos) for i in tup_roch) or\
    type(tup_ani)!=tuple or len(tup_ani)<1 or\
    any(not eh_animal(i) for i in tup_ani) or\
    type(tup_pos_ani)!=tuple or len(tup_pos_ani)!=len(tup_ani) or\
    any(not eh_posicao(i) for i in tup_pos_ani):
        raise ValueError("cria_prado: argumentos invalidos")
    return[pos,list(tup_roch),list(tup_ani),list(tup_pos_ani)]

def cria_copia_prado(prado):#duvida
    """
    cria_copia_prado: prado -> prado
    Esta função recebe um prado e devolve uma nova cópia do prado
    """
    pos=prado[0]
    tup_roch=prado[1]
    tup_ani=prado[2]
    tup_pos_ani=prado[3]
    return [pos,list(tup_roch),list(tup_ani),list(tup_pos_ani)]

def obter_tamanho_x(prado):
    """
    obter_tamanho_x: prado -> int
    Esta função devolve o valor inteiro que corresponde à dimensão Nx do prado
    """
    return obter_pos_x(prado[0])+1

def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado -> int
    Esta função devolve o valor inteiro que corresponde à dimensão Ny do prado
    """
    return obter_pos_y(prado[0])+1

def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> int
    Esta função devolve o número de animais predadores no prado
    """
    cont=0
    for i in prado[2]:
        if eh_predador(i):
            cont+=1
    return cont

def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> int
    Esta função devolve o número de animais presa no prado.
    """
    cont=0
    for i in prado[2]:
        if eh_presa(i):
            cont+=1
    return cont

def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado -> tuplo 
    Esta função devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas pela ordem de leitura do prado.
    """
    return ordenar_posicoes(prado[3])

def obter_animal(prado,pos):
    """
    obter_animal: prado*posicao -> animal
    Esta função devolve o animal do prado que se encontra na posição pos
    """
    for i in range(len(prado[3])):
        if posicoes_iguais(prado[3][i],pos):
            return prado[2][i]

def eliminar_animal(prado,pos):
    """
    eliminar_animal: prado*posicao -> prado
    Esta função modifica destrutivamente o prado eliminando o animal da posição pos deixando-a livre e devolve o próprio prado
    """
    prado[2].pop(prado[3].index(pos))
    prado[3].pop(prado[3].index(pos))
    return prado

def mover_animal(prado,pos1,pos2):
    """
    mover_animal: prado*posicao*posicao -> prado
    Esta função modifica destrutivamente o prado movimentando
    o animal da posição pos1 para a nova posição pos2, deixando livre a posição onde
    se encontrava e devolve o próprio prado.
    """
    prado[3][prado[3].index(pos1)]=pos2
    return prado

def inserir_animal(prado,animal,pos):
    """
    inserir_animal: prado*animal*posicao -> prado
    Esta função modifica destrutivamente o prado acrescentando
    na posição pos do prado o animal passado como argumento e devolve o próprio prado
    """
    prado[2].append(animal)
    prado[3].append(pos)
    return prado

def eh_prado(prado):
    """
    eh_prado: universal -> booleano
    Esta função devolve True se o seu argumento for um TAD prado e False em caso contrário
    """
    return type(prado)==list and len(prado)==4 and\
    eh_posicao(prado[0]) and obter_pos_x(prado[0])>=2 and obter_pos_y(prado[0])>=2 and\
    type(prado[1])==list and (eh_posicao(i) for i in prado[1]) and\
    all(obter_pos_x(prado[1][i])==0 and obter_pos_x(prado[1][i])<obter_pos_x(prado[0]) for i in prado[1]) and\
    all(obter_pos_y(prado[1][i])==0 and obter_pos_y(prado[1][i])<obter_pos_y(prado[0]) for i in prado[1]) and\
    type(prado[2])==list and len(prado[2])>=1 and (eh_animal(i) for i in prado[2]) and\
    type(prado[3])==list and len(prado[3])==len(prado[2]) and\
    all(eh_posicao(i) for i in prado[3])

def eh_posicao_animal(prado,pos):
    """
    eh_posicao_animal: prado*posicao -> bool
    Esta função devolve True apenas no caso da posição pos do prado
    estar ocupada por um animal
    """
    return pos in prado[3]

def eh_posicao_obstaculo(prado,pos):
    """
    eh_posicao_obstaculo: prado*posicao -> booleano
    Esta função devolve True apenas no caso da posição pos do prado
    corresponder a uma montanha ou rochedo
    """
    return obter_pos_x(pos)==0 or obter_pos_y(pos)==0 or pos in prado[1] or\
    obter_pos_x(pos)==obter_pos_x(prado[0]) or obter_pos_y(pos)==obter_pos_y(prado[0])

def eh_posicao_livre(prado,pos):
    """
    eh_posicao_livre: prado*posicao -> booleano
    Esta função devolve True apenas no caso da posição pos do prado
    corresponder a um espaçoo livre (sem animais nem obstáculos)
    """
    return (not obter_pos_x(pos)==0) and (not obter_pos_y(pos)==0) and\
    (not obter_pos_x(pos)==obter_pos_x(prado[0])) and (not obter_pos_y(pos)==obter_pos_y(prado[0])) and\
    pos not in prado[1] and pos not in prado[3]

def prados_iguais(prado1,prado2):
    """
    prados_iguais: prado*prado -> bool
    Esta função devolve True apenas se p1 e p2 forem prados e forem iguais
    """
    return prado1==prado2

def prado_para_str(prado):
    """
    prado_para_str : prado -> str
    Esta função devolve uma cadeia de caracteres que representa o prado
    """
    meio=""
    limite_cima="+"+(obter_tamanho_x(prado)-2)*"-"+"+\n"
    limite_baixo="+"+(obter_tamanho_x(prado)-2)*"-"+"+"
    for linha in range(1,obter_tamanho_y(prado)-1):
        meio+="|"
        for coluna in range(1,obter_tamanho_x(prado)-1):
            if (coluna,linha) in prado[1]:
                    meio+="@"
            elif (coluna,linha) in prado[3]:
                    meio+=animal_para_char(prado[2][prado[3].index((coluna,linha))])
            else:
                meio+="."
        meio+="|\n"
    return limite_cima+meio+limite_baixo


def obter_valor_numerico(prado,pos):
    """
    obter_valor_numerico: prado*posicao -> int
    Esta função devolve o valor numérico da posição pos correspondente 
    à ordem de leitura do prado.
    """
    return obter_tamanho_x(prado)*obter_pos_y(pos)+obter_pos_x(pos)

def obter_movimento(prado,pos):
    """
    obter_movimento: prado*posicao -> posicao
    Esta função devolve a posição seguinte do animal na posição pos dentro
    do prado de acordo com as regras de movimento dos animais no prado.
    """
    livres=0
    presas=0
    animal=obter_animal(prado,pos)
    posicoes_possiveis_livres=[]
    posicoes_possiveis_presas=[]
    adjacentes=obter_posicoes_adjacentes(pos)
    for posicao in adjacentes:
        if eh_posicao_livre(prado,posicao):
            posicoes_possiveis_livres+=[posicao]
            livres+=1
        elif (eh_posicao_animal(prado,posicao) and eh_presa(obter_animal(prado,posicao))):
            posicoes_possiveis_presas+=[posicao]
            presas+=1
    if eh_presa(animal):
        if livres>0:
            posicao_escolhida=obter_valor_numerico(prado,pos)%livres
            return posicoes_possiveis_livres[posicao_escolhida]
        else:
            return pos
    elif eh_predador(animal):
        if presas>0:
            posicao_escolhida=obter_valor_numerico(prado,pos)%presas
            return posicoes_possiveis_presas[posicao_escolhida]
        elif livres>0:
            posicao_escolhida=obter_valor_numerico(prado,pos)%livres
            return posicoes_possiveis_livres[posicao_escolhida]
        else:
            return pos

#Função geração
def geracao(prado):
    """
    geracao: prado -> prado 
    Esta função é a função auxiliar que modifica o prado fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio
    prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
    turno de ação de acordo com as regras descritas.
    """
    animais=[]
    posicoes_animais=obter_posicao_animais(prado)
    for pos in posicoes_animais:
        animais+=[obter_animal(prado,pos)]
    for i in range(len(animais)):
            aumenta_idade(animais[i])
            aumenta_fome(animais[i])
            posicao_seguinte=obter_movimento(prado,posicoes_animais[i])
            if eh_predador(animais[i]) and eh_posicao_animal(prado,posicao_seguinte) and eh_presa(obter_animal(prado,posicao_seguinte)):
                change=1
                eliminar_animal(prado,posicao_seguinte)
            else:
                change=0
            mover_animal(prado,posicoes_animais[i],posicao_seguinte)               
            if eh_animal_fertil(animais[i]) and not posicoes_iguais(posicoes_animais[i],posicao_seguinte):
                novo_animal=reproduz_animal(animais[i])
                inserir_animal(prado,novo_animal,posicoes_animais[i])
                reset_idade(animais[i])                
            if eh_predador(animais[i]) and change==1:
                reset_fome(animais[i])
            if eh_animal_faminto(animais[i]):
                eliminar_animal(prado,posicao_seguinte)
    return prado


#Função simula ecossistema
def simula_ecossistema(ficheiro,num,quiet_verboso):
    """
    simula_ecossistema: str*int*booleano -> tuplo
    Esta é a função principal que permite simular o ecossistema de um prado. 
    Recebe uma cadeia de caracteres, um valor inteiro e um valor booleano e devolve o tuplo de dois elementos correspondentes
    ao número de predadores e presas no prado no fim da simulação. A cadeia de caracteres passada por argumento
    corresponde ao nome do ficheiro de configuração da simulação, o valor inteiro num corresponde ao número de gerações a simular
    e o argumento booleano ativa o modo verboso se for True ou o modo quiet se fro False
    No modo quiet o output é o prado, o número de animais e o número de geração no início e após a última
    geração. No modo verboso, após cada geração, o output é igual ao anterior, apenas se o número de animais predadores ou presas se
    tiver alterado
    """
    cont=0
    lista=[]
    animais=[]
    posicoes=[]
    with open(ficheiro,"r") as f:
        for l in f.readlines():
            lista+=[eval(l)]
    for animal in range(2,len(lista)):
        animais.append(cria_animal(lista[animal][0],lista[animal][1],lista[animal][2]))
        posicoes.append(cria_posicao(obter_pos_x(lista[animal][3]),obter_pos_y(lista[animal][3])))
    pos=cria_posicao(obter_pos_x(lista[0]),obter_pos_y(lista[0]))
    tup_roch=tuple(cria_posicao(x,y) for x,y in lista[1])
    tup_ani=tuple(animais)
    tup_pos_ani=tuple(posicoes)
    prado=cria_prado(pos,tup_roch,tup_ani,tup_pos_ani)
    print (f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. 0)\n{prado_para_str(prado)}")
    for i in range(num):
        cont+=1
        prado_antigo=cria_copia_prado(prado)
        geracao(prado)
        if quiet_verboso:
            if (not obter_numero_predadores(prado_antigo)==obter_numero_predadores(prado)) or (not obter_numero_presas(prado_antigo)==obter_numero_presas(prado)):
                print (f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {cont})\n{prado_para_str(prado)}") 
    if not quiet_verboso:
        print (f"Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {num})\n{prado_para_str(prado)}")        
    return (obter_numero_predadores(prado),obter_numero_presas(prado))
