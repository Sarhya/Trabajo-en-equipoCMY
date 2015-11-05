def buscar(N,dicc):
    de=N.split()
    for i in dicc:
        for j in de:
            if i==j:
                print i,dicc[i]

def simbolos (N,dicc):
    symbol=N.split()
    for i in dicci:
        elem={}
        resto={}
        b = i.split()
        resto['Nu. Atomico']=b[0]
        resto['Propiedades']=b[4:]
        elem[b[2]]=resto
        dicci[b[4]]=elem

def lines(pt-data1,N):
    dicc={}
	try:
        f = open(pt-data1.csv,"r")
 	    l = f.readlines()
	    for i in l:
            elem={}
	        resto={}
	        b = i.split()
	        resto['Nu. Atomico']=b[0]
	        resto['Propiedades']=b[4:]
            elem[b[3]]=resto
	        dicci[b[1]]=elem
	        #print dicc[N]
        for i in dicci:
            if i==dicci['nombre']:
                print i,dicc[i]

	except:
        return("error")
