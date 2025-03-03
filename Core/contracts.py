#договоренность между двуями сторонами, что должно прходить в ответе
USER_DATA_SHEME = {
    'type':'object',
    #характеристики
    'properties':{
        'id':{'type':'number'},
        'email':{'type':'string'},
        'first_name':{'type':'string'},
        'last_name':{'type':'string'},
        'avatar':{'type':'string'}
    },
    #Обязательные параметры
    'requierd':['id', 'email','first_name','last_name', 'avatar']
}
