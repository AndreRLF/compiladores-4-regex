import re

def q01(frase): #Receba uma frase e retorne a lista de palavras daquela frase, ou seja quebre a frase nos espaços.
    return frase.split(" ")

def q02(frase): #Substitui todas as letras A de uma frase pela letra O.
    frase = re.sub("a", "o", frase)
    frase = re.sub("A", "O", frase)
    return frase

def q03(frase): #Insere a letra s no final das palavras que terminam com a letra O.
    frase = re.sub("o\s", "os ", frase)
    frase = re.sub("O\s", "Os ", frase)
    return frase

def q04(frase): #Incrementa todos os números em uma frase
    for m in reversed(list(re.finditer(r"([0-9]+)", frase))):
        operacao = int(frase[m.start():m.end()])
        start = m.start()

        if frase[m.start()-1] == "-":
            resultado = 1 - operacao
            start -= 1
        else:
            resultado = operacao + 1

        frase = frase[:start] + str(resultado) + frase[m.end():]

    return frase

def q05(numero): #Expressão regular que reconhece números decimais
    return (True if re.fullmatch(r"[0-9]+[.,][0-9]+", numero) is not None else False)

def q06(texto): #Reconhece tags html
    return [m.group(1) for m in re.finditer(r"<(\w+)", texto)]

def q07(texto): #Reconheçer o comentários de bloco (/* */)
    return [m.group(1) for m in re.finditer(r".*/\*(.+)\*/.*", texto)]

def q08(texto): #Inverta a ordem dos texto:
    for m in re.finditer(r"(.*): (.*)", texto):
        return m.group(2) + ": " + m.group(1)

def q09(falas): #Faça com que a fala de joão venha antes da de cleber:
    result = ""
    joaoFalou = False
    falaCleber = ""

    for m in re.finditer(r"\W*(.*): (.*)\W*", falas):
        nome = m.group(1)
        fala = m.group(2)
        if m.group(1) == "Cleber" and not joaoFalou:
            falaCleber = m.group(0)
        elif m.group(1) == "João" and falaCleber != "":
            result += m.group(0) + falaCleber
        else:
            result += m.group(0)

    return result

def q10(texto): #Verifique se uma estrutura de parênteses está correta.
    abertos = 0

    for m in re.finditer(r"[)(]", texto):
        if m.group(0) == "(":
            abertos += 1
        elif m.group(0) == ")":
            abertos -= 1

        if abertos < 0:
            return False

    return True if abertos == 0 else False

def q11(texto): #verifique se uma frase contém uma quantidade ímpar de letras a
    count = 0
    for m in re.finditer(r"a", texto):
        count += 1

    return True if count%2==1 else False


if __name__ == '__main__':
    #Questão 01
    frase1 = "Está é a frase da primeira questão !"
    print("#1: " + str(q01(frase1)))

    # Questão 02
    frase2 = "A segunda questão tem essa frase!"
    print("#2: " + q02(frase2))

    # Questão 03
    frase3 = "Retono do O no final das frases"
    print("#3: " + q03(frase3))

    # Questão 04
    frase4 = "frase com 4 numeros 12, 9, -2, 0 = -9"
    print("#4: " + q04(frase4))

    #Questão 05
    frase5 = ["1", "12.4", "2,7", "0,02", ".03", "12."]

    print("\n#05:")
    for s in frase5:
        print(s + (" é decimal!" if q05(s) else " não é decimal!"))
    print("")

    # Questão 06
    texto6 = """<html lang="en">
                <head>
                  <title>Title of the document</title>
                </head>
                <body>
                
                <h1>This is a heading</h1>
                <p>This is a paragraph.</p>
                
                </body>
                </html>"""
    print("#6: " + str(q06(texto6)))

    # Questão 07
    texto7 = """testando reconhecimen de comentario em bloco 
    /* comentário em Bloco 1 */
    Mais texto fora de bloco /*Cometário em bloco 2*/"""
    print("#7: " + str(q07(texto7)))

    # Questão 08
    textos8 = ["Key1: 11224", "Key2: 524", "Key3: 5125", "Abc: 51252"]

    print("\n#08:")
    for t in textos8:
        print(q08(t))
    print("")

    # Questão 09
    texto9 = """
    Maria: eu bebo água.
    
    Cleber: nem sei oq faço.

    João: fica tranquilo.

    Pedro: eu não sei se isso acontece
    """
    print("#9: " + q09(texto9))

    #Questão 10
    texto10 = "some text(text here(possible text)text(possible text(more text))end text"
    print("#10: " + str(q10(texto10)))

    # Questão 11
    texto11 = "Testando se quantidade de as no texto é ímpar" #5
    print("#11: " + str(q11(texto11)))


