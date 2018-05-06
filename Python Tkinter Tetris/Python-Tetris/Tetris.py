import tkinter as t
import time
import math as ma
import random
r = t.Tk()
r.geometry("600x720")
r.title("Tetris-v2")
cl = ["#ffffff", "#333333"]
r["bg"] = cl[0]
ls, mp, rn = list, map, range
pd, m, q, pg, qg = [], [], [], [], []
g, ng, pn, uf, uc, sp, tn = 0, 0, 0, 0, 0, 2, 0
a = "all"
bb = t.Canvas(r, width=364, height=664, highlightthickness=0, bg=cl[0])
nx = t.Canvas(r, width=146, height=62, highlightthickness=0, bg=cl[0])
nx.place(x=415, y=50)
tt = t.Label(r, width=15, height=16, bg=cl[0], font=("", 14))
tt.place(x=406, y=115)
t.Frame(r, bg="#ffaaaa", width=10).pack(fill="y", side="left")
img = list(map(lambda i: t.PhotoImage(
    file="./pic/"+i+".gif"), list("ABCIOTJLSZ")))


def bs(e):
    global pd, m, g, q, x, y, pn, pg, sp, tn, qg, nx, ng, lp, sc
    tn = 0

    def rq(n): return ls(mp(lambda i: [
        i % 4-1, -int(i > 3)], list(map(int, str([3, 56, 5, 4, 6, 306, 45][n]+1200)))))
    if e < 1:
        lp = 0
        sc = 0
    if e < 2:
        if pn % 7 == 0 or e < 0:
            pn = 0
            pg = qg
            qg = random.sample(ls(rn(7)), 7)
            pg += [qg[0]]
        g = pg[pn]
        if e > -1:
            ng = pg[pn+1]
            nq = rq(ng)
            lp += 1
        pn += int(e > -1)
    bb.delete(a)
    nx.delete(a)
    q = rq(g)
    for i in rn(4):
        if e < 0:
            m += [t.Canvas(bb, width=32, height=31, highlightthickness=0)]
        m[i].delete(a)
        m[i].create_image(16, 16, image=img[g+3])
        if -1 < e < 2:
            nx.create_image(nq[i][0]*30+70-int(ng < 2)*15,
                            nq[i][1]*30+46, image=img[ng+3])
    for i in rn(22):
        if e < 1:
            pd += [[]]
        for l in rn(12):
            if e < 1:
                pd[i] += [int(i % 21 < 1 or l % 11 < 1)]
            if e > 1:
                pd[i][l] = int(pd[i][l] > 0)
            bb.create_image(l*30+17, i*30+17, image=img[pd[i][l]])
    tt.config(text="[ NEXT ]"+"\n"*5+"Loop : "+str(lp)+"\n\nScore : " +
              str(sc)+"\n"*4+"Python-Tetris v2\n2018/5/6\n\nCreated by\nTellurium")
    x = 5
    y = 58-sp


def spd(e):
    global sp, x, pd, ts, q, g, y, uf, tn
    n = str(e)[7:8]
    if e.num == 2:
        sp = (sp+26) % 52
        return
    else:
        if n == "R":
            return
        ed = int(e.delta < 0)
        if n == "h" and (g+1) % 6 < 2:
            tn = (tn+ed*2-1) % 4
            if tn > 1:
                tn = tn % 2
                ed = -ed+1
        n4 = y
        if n4 % 30 > 20:
            n4 = ma.floor(n4/30)*30
        n3 = int(n4 % 30 < 1)
        for i in rn(2):
            for l in q:
                if n == "P":
                    if pd[ts+l[1]+n3][x+l[0]+e.num-2] > 0:
                        return
                else:
                    n2 = ed*2-1
                    if pd[ts+l[0]*n2+n3][x+l[1]*(-n2)] > 0:
                        return
            ts = ma.ceil(n4/30)
            n3 -= uf
    if n == "P":
        x += e.num-2
    elif g != 1:
        for i in rn(4):
            q[i][ed] *= -1
            q[i] = q[i][::-1]


bb.place(x=30, y=20)
bs(-1)


def loop():
    global ts, y, x, uf, uc, pd, q, m, pn, sp, lp, sc
    pd = []
    bs(0)
    sb.config(state="disabled")
    while 1:
        ts = ma.floor((y-1)/30)
        if y % 30 > 29-sp or y < 60 or uf > 0:
            if any(ls(mp(lambda i: pd[ts+i[1]+2][x+i[0]] > 0, q))):
                uf = 1
                if y < 61:
                    bs(2)
                    sb.config(state="normal")
                    pn = 0
                    ml(sp+2)
                    break
            else:
                uf = 0
                uc = 0
        uc += uf
        if uc > 30:
            uf = 0
            for i in rn(4):
                pd[ts+q[i][1]+1][x+q[i][0]] = g+3
            sz = 0
            for i in ls(mp(lambda i: int(all(i))*pd.index(i), pd[2:21])):
                if i > 0:
                    pd[2:i+1] = pd[1:i]
                    pd[1] = [1]+[0]*10+[1]
                    sz += 1
            for l in rn(sz):
                sc += [40, 60, 200, 900][l]
            uc = 0
            tn = 0
            bs(1)
        y += sp*int(uf < 1)+((ts+1)*30-y)*uf
        time.sleep(0.03)
        try:
            for i in ["<Button>", "<ButtonRelease>", "<MouseWheel>"]:
                r.bind(i, spd)
        except:
            exit()
        ml(1)
        r.update()


def ml(e):
    global q
    for i in rn(4):
        m[i].place(x=q[i][0]*30+x*30+1, y=q[i][1]*30+y+e)


sb = t.Button(r, width=6, height=1, font=("", 20), text="START",
              borderwidth=0, bg=cl[0], fg=cl[1], command=loop)
sb.place(x=440, y=500)
r.mainloop()
exit()
