# Trabajo-en-equipoCMY
#Carpeta en donde subiremos los trabajos


def buscar(N,dicc):
    de=N.split()
    for i in dicc:
        for j in de:
            if i==j:
                print i,dicc[i]

def lines():
    dicci={}
    try:
        f = open('elementos.csv',"r")
        l = f.readlines()
        for i in l:
            elem={}
            resto={}
            b = i.split()
            resto['Nu. Atomico']=b[0]
            resto['Propiedades']=b[4:]
            elem[b[3]]=resto
            dicci[b[1]]=elem
        return dicci
    except:
        return("error")


b = raw_input('Escribe una serie de simbolos de elementos ')
buscar(b,lines())
