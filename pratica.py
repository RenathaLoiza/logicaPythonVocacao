import random

def gerar_nome():
    sorteioNome=["renatha","Olivia","ana","natan"]
    return random.choice(sorteioNome)


def gerar_idade():
    sorteiaIdade=[40,31,39,46]
    return random.choice(sorteiaIdade)

def gerar_Profissao():
    sorteiaProfissao=["Medico","Professor","Nutricionista","Veterinario"]
    return random.choice(sorteiaProfissao)

def  gerar_historia():
    introducao = gerar_nome()
    desenvolvimento = gerar_idade()
    final = gerar_Profissao()

    historia = f"Meu nome é {introducao} tenho {desenvolvimento} anos e sou {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())