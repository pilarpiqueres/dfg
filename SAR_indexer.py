import json
import pickle
import re
import sys
# cada doc: {'article': ' ','url' 'date' 'keywords' 'id': '', 'summary': '', 'title':''}, {'article'...
diccionariDocs = {}
diccionariArticles = {}
postingListTerms = {} #cada termino: lista de id de las noticias en que aparece
docid = 0
artid = 0

#guardar un objecte(índex) en un fitxer
def save_object(object, file_name):
    with open(file_name, 'wb') as fh:
        pickle.dump(object, fh)

clean_re = re.compile('\W+') #sustituye cosas no alfanumericas por espacios
def clean_text(text):
    return clean_re.sub(' ', text)

        
def indexer(folder,fitxerGuardat):    
        
    for doc in folder:
        #asignar id al document -> hash accesible por docid
        #guardar doc en diccionari de docs 
        with open(doc) as file:
            data = json.load(file)

        diccionariDocs[docid] = data.name #no sé si funciona cert així la inserció en diccionaris
        docid = docid + 1

        pos = 0   #posició de cada article dins de cada doc

        for article in data:
            #NEWID asignar id nuevo a cada noticia(article) -> tupla(docid, pos)
            tupla = [docid, pos]
            pos = pos + 1

            diccionariArticles[artid] = tupla
            artid = artid + 1

            text = text.lower()
            text = clean_text(text)
            text = data[article].split()
            for simb in text:
                #if simb in lletres or simb in nums:
                postingListTerms[simb] = postingListTerms.get(simb,'no')
                if postingListTerms[simb] == 'no' :
                    postingListTerms[simb] = postingListTerms.get(simb) + (artid,)
                else postingListTerms[simb] != 'no':
                    if artid not in postingListTerms[simb]:
                        postingListTerms[simb] = postingListTerms.get(simb) + (artid,)

    
    objecte = [diccionariDocs, diccionariArticles, postingListTerms]
    save_object(objecte, fitxerGuardat)               
        

    '''El fichero invertido puede ser una tabla hash implementada como un diccionario de
    python, indexado por término y que haga referencia a una lista con los newid
    asociados a ese término.'''

    '''La mejor forma de guardar los datos de los índices en disco es utilizar la librería pickle
    que permite guardar un objeto python en disco. Si quieres guardar más de un objeto,
    puedes hacer una tupla con ellos, (obj1, obj2, …, objn), y guardar la tupla. Consulta la
    práctica del mono infinito.'''
    #Toda la información necesaria para el recuperador de noticias se guardará en un único
    #fichero en disco.


'''Aceptará dos argumentos de entrada: el primero el directorio donde está la colección
de noticias y el segundo el nombre del fichero donde se guardará el índice.'''
if "_name_" == main:
    if len(sys.argv) < 3:
        syntax()
    colNot = sys.argv[1]
    savIndx = sys.argv[2]
  #  indexer(colNot, savIndx)
