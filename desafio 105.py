def notas(* n, sit=False):
    r={}
    r['total']=len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['situação']='BOA'
        elif r['media']>=5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r
#principal
resp=notas(5.5,4,8)
print(resp)