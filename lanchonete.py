class lanchonete:
    def __init__(self,item1,item2,item3):
        self.item1=item1
        self.item2=item2
        self.item3=item3
    def pedidos(self):
        return print("O seu pedido foi",self.item1,"um",self.item2,"e um",self.item3)

seupedido=str(input("Qual o seu pedido?"))
seupedido2=str(input("algo mais?"))
pededido3=str(input("Mais alguma coisa?"))
l=lanchonete(seupedido,seupedido2,pededido3)
l.pedidos()