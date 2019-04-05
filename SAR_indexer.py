import json
# cada doc: {'article': ' ','url' 'date' 'keywords' 'id': '', 'summary': '', 'title':''}, {'article'...
diccionariDocs = {}
postingListTerms = {} #cada termino: lista de id de las noticias en que aparece

for doc in folder:
    with open(doc) as file:
        data = json.load(file)
        #asignar id al document -> hash accesible por docid
        #guardar doc en diccionari de docs

    for article in data:
        #NEWID asignar id nuevo a cada noticia(article) -> tupla(docid, pos)
        text = data[article].split()
        text = text.lower()
        for simb in text:
            if simb in lletres or simb in nums:
                postingListTerms[simb] = postingListTerms.get(simb,0) + newId
                #funciona(?) o va sumant totes les noves id's????


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
