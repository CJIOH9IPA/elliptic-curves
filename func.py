#Алгоритм Евклида
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
#Обратное мультипликативное
def mulinv(b, p):
    g, x, y = egcd(b, p)
    if g == 1:
        return (x % p)
def sumPoint(x1, y1, x2, y2):
    a = -1
    b = 1
    p = 751
    if (x1 == x2) and (y1 == y2):
        num = (3 * x1 * x1 + a)
        den = 2 * y1
        lmd = (num * mulinv(den, p)) % p
        print('(3x1^2+a/2y1)mod p = ',num,'/',den,'mod', p,' = ',lmd)
        print('lambda = ', lmd)
        x3 = (lmd * lmd - x1 - x1)
        if x3 < 0:
            x3 = (p - abs(x3)) % p
        else:
            x3 = x3 % p
        print('x3 = (lambda^2 - x1 - x2)mod p = (',lmd,'*',lmd,'-',x1,'-',x2,')mod ',p,'=', x3)
        y3 = (lmd * (x1 - x3) - y1)
        if y3 < 0:
            y3 = (p - abs(y3)) % p
        else:
            y3 = y3 % p
        print('y3 = (lambda*(x1 - x3) - y1)mod p = (',lmd,'*(',x1,'-',x3,') -',y1,')mod ', p, '=', y3)
        return (x3, y3)
    else:
        num = y2 - y1
        den = x2 - x1
        if (num < 0) and (den < 0):
            num = abs(num)
            den = abs(den)                
        else:
            if (num < 0) or (den < 0):                
                num = (p - abs(num)) % p
                den = abs(den)
            else:
                num = num % p            
        lmd = (num * mulinv(den, p)) % p
        print('(y2 - y1/x2 - x1)mod p = ',num,'/',den,'mod', p,' = ',lmd)
        print('lambda = ', lmd)
        x3 = (lmd * lmd - x1 - x2) % p
        print('x3 = (lambda^2 - x1 - x2)mod p = (',lmd,'*',lmd,'-',x1,'-',x2,')mod ',p,'=', x3)
        y3 = (lmd * (x1 - x3) - y1)
        if y3 < 0:
            y3 = (p - abs(y3)) % p
        else:
            y3 = y3 % p
        print('y3 = (lambda*(x1 - x3) - y1)mod p = (',lmd,'*(',x1,'-',x3,') -',y1,')mod ', p, '=', y3)
        return (x3, y3)
#Инверсия точки
def invPoint(x, y):
    p = 751
    y = p-y
    return (x, y)    
def multPoint(x, y, n):
    x1 = x
    y1 = y
    x2 = x
    y2 = y
    while n > 1:
        print(123 - n,')')
        x2, y2 = sumPoint(x1, y1, x2, y2)
        n -= 1
    #print('Точка kPb = (', x2, ',', y2, ')')
    return(x2, y2)
def encrypt():
    i = 0
    lw = 9
    #Массив точек, кодирующих  буквы
    let = [[247, 234, 243, 238, 240, 229, 238, 236, 237],
           [266, 587, 87, 576, 309, 151, 576, 39, 297],
           ['т','е','р','н','о','в','н','и','к']]
    #Массив k
    k = [8, 14, 17, 17, 2, 10, 8, 2, 2]
    while i < lw:
        #G
        xg = 0
        yg = 1
        #OK
        xk = 188
        yk = 93
        xg, yg = multPoint(xg, yg, k[i])
        xk, yk = multPoint(xk, yk, k[i])
        #print('xk, yk',xk,yk)
        #print('koord letter',let[0][i], let[1][i])
        xk, yk = sumPoint(let[0][i], let[1][i], xk, yk)
        print('Код. букву "', let[2][i], '" с коорд.(', let[0][i], ',', let[1][i], ') Cm = {(', xg, ',', yg, ')', ', (', xk, ',', yk, ')}')
        i += 1
def decrypt():
    i = 0
    lw = 11
    pnt = [[377, 425, 188, 179, 568, 568, 377, 188, 489, 16, 425],
             [456, 663, 93, 275, 355, 355, 456, 93, 468, 416, 663],
             [367, 715, 279, 128, 515, 482, 206, 300, 362, 69, 218],
             [360, 398, 353, 79, 67, 230, 645, 455, 446, 510, 601]]
    nb = 44
    while i < lw:
        x, y = multPoint(pnt[0][i], pnt[1][i], nb)
        x, y = invPoint(x, y)
        x, y = sumPoint(pnt[2][i], pnt[3][i], x, y)
        print('Расшифрованная точка = (',x,',', y,')')
        i += 1   
def genSign():
    p  = 751
    n = 13
    x = 416
    y = 55
    e = 6
    d = 12
    k = 7
    #kG
    x, y = multPoint(x, y, k)
    r = x % n
    z = mulinv(k, n)
    s = (z * (e + d * r)) % n
    print ('Цифровая подпись равна (', r, ',', s, ')')
def checkSign():
    e = 8
    p = 751
    n = 13
    xg = 562
    yg = 89
    arr = [[135, 11],
           [82, 10]]
    if (arr[0][1] >= 1) and (arr[0][1] <= n - 1) and (arr[1][1] >= 1) and(arr[1][1] <= n - 1):
        v = mulinv(arr[1][1], n)
        print('v =',v)
        u1 = (e * v) % n
        print('u1 =',u1)
        u2 = (arr[0][1] * v) % n
        print('u2 =',u2)
        x1, y1 = multPoint(xg, yg, u1)
        x2, y2 = multPoint(arr[0][0], arr[1][0], u2) 
        x, y = sumPoint(x1, y1, x2, y2)
        print ('Точка Х =',x, y)
        if (x % n) == arr[0][1]:
            print('Подпись действительная')
        else:
            print('Подпись фальшивая')
    else:
        print('Подпись фальшивая')

a, b = multPoint(49,568,122)
print('n*P = 122*(49, 568) = (',a,',',b,')')
##print ('nb * kG = 45 * (377, 456) = (',a,',',b,')')
#a, b = invPoint(70,556)
#print ('- R = (',a,',',b,')')
#a, b = sumPoint(33,355,70,195)
#print('2P + 3Q - R = (',a,',',b,')')
#encrypt()
#difPoint(301, 734, 157, 55)
#a, b =sumPoint(301, 734, 175, 559)
#print (a,b)
#x1 = 66
#y1 = 552
#k = 3
#x2 = 406
#y2 = 397
#x2, y2 = multPoint(x2,y2,k)
#x, y = sumPoint(x1,y1,x2,y2)
#print(x,y)
#decrypt()
#genSign()
#checkSign()
