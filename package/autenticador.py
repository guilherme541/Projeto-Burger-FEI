

def autenticação(c):
    try:
        with open("./%s.txt" %c, "r", encoding='utf-8') as dados:
            v = dados.read().split(';')
            if v[1] == c:
                dados.close()
                return True
    except:
            return False