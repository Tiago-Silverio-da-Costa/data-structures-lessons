def sauda(nome):
    print("olá, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()
    
def sauda2(nome):
    print("Como vai "+ nome + "?")
    
def tchau():
    print("ok, tchau!")
    
sauda("Tiago")