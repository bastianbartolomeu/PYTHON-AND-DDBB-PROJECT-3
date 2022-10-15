import requests
import pymongo
import json

class MP3:

    def apis_gob(self):
        response = requests.get("https://apis.digital.gob.cl/fl/feriados/2020", headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            })
        return response

    def api_to_database(self):
        api = self.apis_gob()
        rej = json.loads(api.text)
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        mybbdd = cl['FERIADOS2020']
        colec = mybbdd['Chile']
        colec.insert_many(rej)
                
    
    def conexion(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        print('')
        print(cl)
        print(db)
        print(col)
        

    def todos_los_feriados(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        cont = 0
        print('')
        print('=============== TODOS LOS FERIADOS =========================')
        print('')
        for i in col.find({}):
            cont +=1 
            print(cont,' |El dia de ',i['nombre'],' es un feriado tipo ', i['tipo'],' y se celebra el ',i['fecha'])
        print('====== EXISTEN UN TOTAL DE ', cont,' FERIADOS EN LA API ====== ')

    def feriados_civiles(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        cont = 0
        print('')
        print('=============== TODOS LOS FERIADOS CIVILES =========================')
        print('')
        for i in col.find({"tipo":"Civil"}):
            cont +=1 
            print(cont,' |El dia de ',i['nombre'],' es un feriado tipo ', i['tipo'],' y se celebra el ',i['fecha'])
        print(' ')
        print('====== EXISTEN ',cont, ' Feriados civiles ======')

    def feriados_irrenunciable(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        cont = 0
        print('')
        print('=============== TODOS LOS FERIADOS IRRENUNCIABLE =========================')
        print('')
        for i in col.find({"irrenunciable":"1"}):
            cont +=1 
            print(cont,' |El dia de ',i['nombre'],' es un feriado tipo ', i['tipo'],' y se celebra el ',i['fecha'])
        print('====== EXISTEN ', cont,' FERIADOS IRRENUNCIABLE ======')
    
    
    def texto_santo(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        cont = 0
        print('')
        print('=============== TODOS LOS FERIADOS DEL CON TEXTO SANTO =========================')
        print('')
        for i in col.find({"nombre":{'$regex': 'Santo'}}):
            cont +=1 
            print(cont,' |El dia de ',i['nombre'],' es un feriado tipo ', i['tipo'],' y se celebra el ',i['fecha'])
        print('====== EXISTEN  ', cont,' FERIADOS CON LA PALABRA SANTO ======')


    def leyes_plebiscito(self):
        cl = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cl['FERIADOS2020']
        col = db['Chile']
        cont = 0
        print('')
        print('=============== Leyes relacionadas con el Plebiscito de Abril =========================')
        print('LAS LEYES RELACIONADAS CON EL PLEBISCITO SON : ')
        print(' ')
        feriado = col.find_one({"nombre":"Plebiscito Constitucional"})
        for i in feriado['leyes']:
            cont +=1 
            print(cont, '| ',i['nombre'],' en ',i['url'])
        print('====== EXISTEN', cont,' LEYES RELACIONADAS CON EL PLEBISCITO ======')
        



#mp3 = MP3()
#mp3.conexion()
#mp3.apis_gob()
#mp3.api_to_database()
#mp3.api_to_database()
#mp3.todos_los_feriados()
#mp3.feriados_civiles()
#mp3.feriados_irrenunciable()
#mp3.texto_santo()
#mp3.texto_santo()











