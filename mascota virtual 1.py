def hambre(cart):
    if cart[1]<10:
        cart[1]=cart[1]+1       
    if cart[4] > 0:
        cart[4]=cart[4]-1
        if cart[4]==0:
            print("Su mascota esta muy sucia")
    menu(cart)
def sueño(cart):
    if cart[2]<10:
        cart[2]=cart[2]+1
    if cart[1]>0:
        cart[1]=cart[1]-1
        if cart[1]==0:
            print("Su mascota tiene mucha hambre")
    menu(cart)
def divercion(cart):
    if cart[3]<10:
        cart[3]=cart[3]+1
    if cart[1]>0:
        cart[1]=cart[1]-1
        if cart[1]==0:
            print("Su mascota tiene mucha hambre")
    if cart[2]>0:
        cart[2]=cart[2]-1
        if cart[2]==0:
            print("Su mascota tiene mucho sueño")
    if cart[4]>0: 
        cart[4]=cart[4]-1
        if cart[4]==0:
            print("Su mascosa esta muy sucia")
    menu(cart)
def limpieza(cart):
    if cart[4]<10:
        cart[4]=cart[4]+1
    if cart[2]>0:
        cart[2]=cart[2]-1
    menu(cart)

def dibujar(cart):
    
    BH = ""
    BS = ""
    BD = ""
    Bs = ""
    x = cart[1]
    for i in range (x):
        BH = BH + "|"
    x = cart[2]    
    for i in range (cart[2]):
        BS = BS+'|'
    x = cart[3]    
    for i in range (cart[3]):
        BD = BD+'|'
    x = cart[4]
    for i in range (cart[4]):
        Bs = Bs+'|'            

    print("Hambre ",BH)
    print("Sueño  ",BS)
    print("Diver  ",BD)
    print("Baño   ",Bs)

def menu(cart):
    
    x=6
    dibujar(cart)
    while(x != 0):
        print("[1] alimentar mascota","[2] Dormir mascota","[3] Jugar mascota","[4] Bañar mascota","[0] Salir")
        
        x=int(input())
        if x==0:
            break
        if x==1:
            hambre(cart)
        if x==2:
            sueño(cart)
        if x==3:
            divercion(cart)        
        if x==4:
            limpieza(cart)
        if x==" ":
            x=6   
            




cart=[0,10,10,10,10]
menu(cart)
