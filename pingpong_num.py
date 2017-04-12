# pinpong number

def pingpang(n, k = 7):
    p = []
    q = 0
    signal = 1
    for i in range(1,n+1):
        if signal == 1:
            q = q + 1
            p.append(q)
        elif signal == 0:
            q = q - 1
            p.append(q)
        if i%k == 0 or str(k) in str(i):
            signal = 1-signal
    print(p[-1])
