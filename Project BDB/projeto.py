#exercicio 1

def corrigir_palavra(palavra):
    """
    corrigir_palavras:str->str
    Esta função devolve a palavra corrigida conforme a documentação BDB
    """
    string=""
    i=0
    if not isinstance(palavra,str):
        raise ValueError
    lista=list(palavra)
    res=lista.copy()
    comp=len(palavra)-1
    while i<comp:
        if abs(ord(res[i])-(ord(res[i+1])))!=32: 
            res=res
            i+=1
        else:
            del res[i:i+2]
            comp-=2
            i-=1
    for i in res:
        string+=i
    return string

def eh_anagrama(pal1,pal2):
    """
    eh_anagrama:str*str -> bool
    Esta função devolve True se uma palavra for anagrama da outra
    """
    res1={}
    res2={}
    pal1=pal1.lower()
    pal2=pal2.lower()
    if len(pal1)!=len(pal2):
        return False
    for car in pal1:
        if car not in res1:
            res1[car]=0
        res1[car]+=1
    for car in pal2:
        if car not in res2:
            res2[car]=0
        res2[car]+=1
    return res1==res2

def corrigir_doc(doc):
    """
    corrigir_doc:str -> str
    Esta função recebe uma documentação com erros e devolve a mesma documentação corrigida de acoordo com o BDB e valida os argumentos
    """
    if not isinstance(doc,str) or "  " in doc or doc.endswith(" ") or not all(car.isalpha() or car==" " for car in doc):
        raise ValueError("corrigir_doc: argumento invalido")
    i=0
    listapal=corrigir_palavra(doc).split()
    comp=len(listapal)
    while i<comp:
        j=1
        while j<comp:
            if eh_anagrama(listapal[i],listapal[j]):
                if listapal[i].lower()!=listapal[j].lower():
                    listapal.pop(j)
                    comp=len(listapal)
                    j-=1
            j+=1
        i+=1
    return (" ".join(res for res in listapal))   


#exercicio 2

def obter_posicao(mov,num):
    """
    obter_posicao:str*int -> int
    Esta função define o que acontece a cada número após um movimento(letra)
    """
    constante=num
    if mov=="C":
        if num==1 or num==2 or num==3:
            return num
        num-=3
    elif mov=="B":
        if num==7 or num==8 or num==9:
            return num
        num+=3
    elif mov=="E":
        if num==1 or num==4 or num==7:
            return num
        num-=1
    elif mov=="D":
        if num==3 or num==6 or num==9:
            return num
        num+=1
    if num<=0:
        return constante
    return num

def obter_digito(movs,num):
    """
    obter_digito:str*int -> int
    Esta função define o que acontece a cada número após um conjunto de movimentos(letras)
    """
    for car in movs:
        res=obter_posicao(car,num)
        num=res
    return res

def obter_pin(pin):
    """
    obter_pin:tuple -> tuple
    Esta função devolve o pin em forma de tuplo após todos os conjuntos de movimentos e valida os argumentos
    """
    if type(pin)!=tuple or len(pin)<4 or len(pin)>10 or\
    any(len(i)<1 for i in pin) or any(i not in "CBDE" for car in pin for i in car):
        raise ValueError("obter_pin: argumento invalido")
    res=()
    num=5
    for seq in pin:
        res=res+(obter_digito(seq,num),)
        num=obter_digito(seq,num)
    return res

#exercicio 3

def val_cifra(cifra):
    """
    val_cifra:str -> bool
    Esta função devolve True se a cifra estiver formada corretamente
    """
    return isinstance(cifra,str) and all(car.isalpha() or car=="-" for car in cifra) and\
    not any(car.isupper() for car in cifra) and len(cifra)>0 and\
    not (cifra.startswith("-") or cifra.endswith("-")) and\
    not("--" in cifra)

def val_seq_control(seqc):
    """
    val_seq_control:str -> bool
    Esta função devolve True se a sequência de controlo estiver formada corretamente
    """
    return isinstance(seqc,str) and seqc.startswith('[') and seqc.endswith("]") and\
    len(seqc)==7 and all(car.islower() and car.isalpha() for car in seqc[1:-1])

def val_seq_seguranca(seqs):
    """
    val_seq_seguranca:tuple -> bool
    Esta função devolve True se a sequência de segurança estiver formada corretamente
    """
    return isinstance(seqs,tuple) and len(seqs)>=2 and\
    all(isinstance(car,int) and car>0 for car in seqs)

def eh_entrada(entrada):
    """
    eh_entrada:universal -> bool
    Esta função devolve True se o seu argumento corresponde a uma entrada de BDB
    """
    i=0
    if isinstance(entrada,tuple) and len(entrada)==3:
        if val_cifra(entrada[0]):
            i+=1
        if val_seq_control(entrada[1]):
            i+=1
        if val_seq_seguranca(entrada[2]):
            i+=1
    return i==3 

def validar_cifra(cifra,seqc):
    """"
    validar_cifra:str*srt -> bool
    Esta função devolve True se a cifra for coerente com a sequencia de controlo
    """
    d={}
    res=""
    i=0
    for car in cifra:
        if car not in d:
            d[car]=0
        d[car]+=1
    if "-" in d.keys():
        d.pop("-")
    
    final = []
    while len(d)>0:
        y=max(d,key=d.get)#idientifica a primeira key cujo valor e maximo
        x=d.get(y)#identifica o valor maximo
        inter=[]
        for key in d:
            if d[key]==x:
                inter.append(key)#adiciona as keys cujo valor e maximo 
        inter.sort()#organiza a lista por ordem alfabetica
        final+=inter
        for i in range(len(inter)):
            del d[inter[i]]#elimina os elementos que ja foram avaliados   
        inter=[]
    final=final[0:5]
    for i in range(len(final)):
        res+=f"{final[i][0]}"
    return "["+res+"]"==seqc

def filtrar_bdb(lista):
    """
    filtrar_bdb:list -> list
    Esta função devolve a lista ou listas nas quais a cifra não é coerente com a sequencia de controlo e valida os argumentos
    """
    res=[]
    if type(lista)!=list or len(lista)<1 or all(eh_entrada(j) for j in lista)==False:
        raise ValueError("filtrar_bdb: argumento invalido")
    for i in range(len(lista)):
        if not validar_cifra(lista[i][0],lista[i][1]):
            res.append(lista[i])
    return res

#exercicio 4

def obter_num_seguranca(tuplo):
    """
    obter_num_seguranca:tuple -> int
    Esta função devolve a menor diferença entre os pares de números de um tuplo
    """
    i=0
    lista=[]
    while i<len(tuplo):
        j=i+1
        while j<len(tuplo):
            dif=abs(tuplo[i]-tuplo[j])
            lista.append(dif)#lista que contem as diferenças entre todos os numeros da lista
            j+=1
        i+=1
    return min(lista)

def decifrar_texto(cifra,numseg):
    """
    decifrar_texto:str*int -> str
    Esta função devolve a cifra decifrada de acordo com o numero de seguranca
    """
    res=""
    numseg=numseg%26
    if val_cifra(cifra):
        for i in range(len(cifra)):
            if cifra[i].isalpha():
                if i%2==0:
                    novo=chr(ord(cifra[i])+numseg+1)
                else:
                    novo=chr(ord(cifra[i])+numseg-1)
                if ord(novo)>122:
                    res+=chr(ord(novo)-26)#ao retirar 26, que é o tamanho do abcedario, a ord da nova letra, estamos a adicionar a ord de a o mesmo numero de unidades que a ord da nova letra excede a ordem de z
                else:
                    res+=novo
            else:
                res+=" "
        return res

def decifrar_bdb(lista):
    """
    decifrar_bdb:list -> list
    Esta função devolve uma lista com as entradas decifradas na mesma ordem e valida os argumentos
    """
    res=[]
    if not isinstance(lista,list):
        raise ValueError("decifrar_bdb: argumento invalido")
    for i in range(len(lista)):
        if not (eh_entrada(lista[i])):
            raise ValueError("decifrar_bdb: argumento invalido")
        else:
            numseg=obter_num_seguranca(lista[i][2])
            res+=[f"{decifrar_texto((lista[i][0]),numseg)}"]
    return res


#exercicio 5


def eh_utilizador(utilizador):
    """
    eh_utilizador:universal -> bool
    Esta função devolve True se o seu argumento corresponde a um dicionario contendo a informacao de utilizador conforme o BDB
    """
    return isinstance(utilizador,dict) and len(utilizador)==3 and\
    "name" in utilizador and "pass" in utilizador and "rule" in utilizador and\
    "vals" in utilizador["rule"] and "char" in utilizador["rule"] and\
    isinstance(utilizador["name"],str) and isinstance(utilizador["pass"],str) and\
    len(utilizador["rule"])==2 and isinstance(utilizador["rule"],dict) and\
    len(utilizador["name"])>0 and len(utilizador["pass"])>0 and\
    isinstance(utilizador["rule"]["vals"],tuple) and isinstance(utilizador["rule"]["char"],str) and\
    len(utilizador["rule"]["vals"])==2 and len(utilizador["rule"]["char"])==1 and\
    isinstance(utilizador["rule"]["vals"][0],int) and isinstance(utilizador["rule"]["vals"][1],int) and\
    utilizador["rule"]["vals"][0]>0 and utilizador["rule"]["vals"][1]>0 and\
    utilizador["rule"]["vals"][0]<=utilizador["rule"]["vals"][1]

def eh_senha_valida(senha,regras):
    """
    eh_senha_valida:str*dict -> bool
    Esta função devolve True se a senha cumpre com as regras gerais e individuais
    """
    cont=0
    j=0
    i=0
    d={}
    for car in senha:
        if car in "aeiou":
            i+=1
        if car not in d:
            d[car]=0
        d[car]+=1#forma um dicionario com o numero de ocorrencias de cada caracter
    while cont<len(senha)-1:
        if senha[cont]==senha[cont+1]:
            j=1#verifica se existem duas letras iguais seguidas
        cont+=1
    return i>=3 and j==1 and regras["char"] in senha and\
    d[regras["char"]]>=regras["vals"][0] and d[regras["char"]]<=regras["vals"][1]

def filtrar_senhas(lista):
    """
    filtrar_senhas:list -> list
    Esta função devolve uma lista ordenada alfabeticamente com os nomes dos utilizadores com senhas erradas e valida os argumentos
    """
    res=[]
    if not isinstance(lista,list) or len(lista)<1  or not all(eh_utilizador(i) for i in lista): 
        raise ValueError("filtrar_senhas: argumento invalido")
    for i in lista:
        if not eh_senha_valida(i["pass"],i["rule"]):
            res+=[i["name"]]
            res.sort()
    return res