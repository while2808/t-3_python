try :
    d={'user':'1234'}
    c=int(input())
    if c==1 :
        u=input()
        p=input()
        if u in d.keys():
            if p in d.values():
                print('login')
            else :
                raise Exception("pass not match")
        else :
            raise Exception(" u name not match")
    elif c==2 :
        u=input()
        p=input()
        p1=input()
        if p==p1 :
            d[u]=p
            print(d[u])
        else :
            raise Exception("pass and con pass not match")
    else :
        raise Exception("invalid choice")
except Exception as e :
    print(e)