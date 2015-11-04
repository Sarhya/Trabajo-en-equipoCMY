# Trabajo-en-equipoCMY
#Carpeta en donde subiremos los trabajos


def lines(nombreArchivo,N):
    dicc={}
    try:
        f = open(nombreArchivo,"r")
        l = f.readlines()
        for i in l:
            elem={}
            resto={}
            b = i.split()
            resto['Nu. Atomico']=b[0]
            resto['Propiedades']=b[4:]
            resto['nombre']=b[3]
            dicc[b[1]]=resto
        #print dicc[N]
        for i in dicc:
                if j==dicc['nombre']:
                    print i,dicc[i]

    except:
        return("error")
