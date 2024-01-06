def token(usuario,contraseña):
    acceso = json.loads(requests.post('https://api.invertironline.com/token',data={
        "username":usuario,
        "password":contraseña,
        "grant_type":"password"
    }).text)
    return acceso
    
def refreshtoken():
    pass