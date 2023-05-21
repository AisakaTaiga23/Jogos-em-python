def tentativa(vxb,vyb,g,xt,yt)->bool:
    """ESSA FUNÇÃO RECEBE COMO :PARAM: VXB, VYB(QUE REPRESENTA A POSIÇÃO DO EIXO X E Y DA POSIÇÃO FINAL"""
    """DA BOLA NO INSTANTE QUE ELA TOCA O CHÃO), :PARAM: XT E YT (QUE REPRESENTA A POSIÇÃO DO EIXO DE  """""
    """LANÇAMENTO DO TREINADOR) E O :PARAM: G E T QUE REFERENCIAM A VELOCIDADE E O TEMPO RESPECTIVAMENTE"""
    t=0
    xb=xt
    yb=yt
    while(yb>0):
        """CAUCULA SEGUNDO A SEGUNDO, DENTRO DESSE LAÇO, ATE A BOLA PARAR"""
        print("t=   ",t,"   vy=   ",vyb,"    x=    ",xb,"    y=    ",yb)
        if(xb==xp and yb==yp):
            print("O pokemon foi capturado!")
            return True
        """ATUALIZA :PARAM: SEGUNDO A SEGUNDO."""
        t=t+1
        xb=xb+vxb
        yb=yb+vyb-g/2
        vyb=vyb-g
    print("a pokebola nao atingiu o pokemon.")
    return False
    """:return: se retornar False, repetir o programa; se retornar True, o sistema foi concluído
                         com êxito com o resultado esperado, ou acabaram o número de tentativas do programa."""

def captura(N,xp,yp,g)->bool:
    """RECEBE N,XP,YP E G COMO :PARAM:"""
    """:PARAM: N RECEBE O NUMERO DE TENTATIVAS"""
    """:PARAM: XP RECEBE A COORDENADA DO EIXO  X DO POKEMON"""
    """:PARAM: YP RECEBE A COODENADA DO EIXO Y DO POKEMON"""
    i=1
    while(i<=N):
        print("Tentativa",i,":")

        xt=int(input("Digite a coordenada x (inteiro >=0) do treinador: "))
        yt=0
        while (yt <= 0):
            yt=int(input("Digite a coordenada y (inteiro >=0) do pokemon: "))
        vy=int(input("Digite o componente y da velocidade de lançamento: "))
        vx=1
        if(tentativa(vx,vy,g,xt,yt)):
            return True
        i=i+1
    return False
    """":return: se retornar False, repetir o programa; se retornar True, o sistema foi concluído
                         com êxito com o resultado esperado, ou acabaram o número de tentativas do programa."""
if __name__=="__main__":
    n=0
    """QUERO FORÇAR QUE ELE DIGITE O NUMERO DE POKEBOLAS QUE SEJA MAIOR OU IGUAL A ZERO"""
    while(n<=0):
        n=int(input("Digite o numero N de pokebolas: "))

    g=int(input("Digite o valor da gravidade: "))
    xp=0
    while(xp<=0):
        xp=int(input("Digite a coordenada x (inteiro >=0) do pokemon: "))
    yp=0
    while(yp<=0):
        yp=int(input("Digite a coordenada y (inteiro >=0) do pokemon: "))
    if(captura(n,xp,yp,g)):
        print("Parabéns!!!!")

