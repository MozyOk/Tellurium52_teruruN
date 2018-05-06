import tkinter as tk
import time
import random as rd
g=0.1#GameSpeed
tkr=tk.Tk()
bpt=[];trs=[];im=[];img=[];but=None
zy=1;zx=5;rn=0;df=0;sco=0;tm=0;dief=0
bt=rd.randrange(0,7);ts=rd.randrange(0,7);ovf=1;scp=[40,60,200,900]
cb=["m","b","w","f","r","y","g","a","p","h","o"]
l=[0,0];a=[-1,0];b=[1,0];c=[0,1];d=[-1,1];e=[1,1]
tc=[l,a,b,c],[l,a,b,d],[l,a,b,e],[l,a,b,[2,0]],[l,a,c,d],[l,a,c,e],[l,b,c,d]
def awake():
    global grid,tkr,but
    for bdc in range(0,22):
        bpt.insert(bdc,[])
        for bpc in range(0,12):
            bpt[bdc].insert(bpc,int(bpc<1 or bpc>10 or bdc==21)+int(bdc==0)*2)
    tkr.geometry("600x700")
    tkr.title("Python-Tetris")
    tkr.bind("<Key>",kp)
    but=tk.Button(tkr,text="---START---",command=go)
    but.place(x=440,y=450)
def loop():
    global but
    grid = tk.Canvas(tkr,width = 400,height = 700)
    grid.place(x=25, y=5)
    g2=tk.Canvas(tkr,width=200,height=200)
    g2.place(x=430,y=50)
    lb=tk.Label(tkr,text="Next\n\n\nScore : "+str(sco)+"\n\nTime : "+str(tm)+"\n\n\nPythonTetris v1.1\nCreated by Tellurium\n18/3/9\n\n\n[A]Left  Right[D]\n[S]Turbo\n\n[Q][W]Turn")
    lb.place(x=420,y=160)
    for gx in range(0,12):
        for gy in range(0,22):
            n=bpt[gy][gx]
            gmg=img[n%12+int(n>11)*4]
            grid.create_image(10+gx*30,10+gy*30,image = gmg,anchor = tk.NW)
    if ovf==0:
        for i in range(0,4):
            cn=tc[bt][i];cy=cn[1];cx=cn[0]
            g2.create_image(32+cx*30,30+cy*30,image=img[bt+4],anchor=tk.NW)
        but.config(state="disabled")
    tkr.update()
def kp(e):
    global zy,ovf;q=0;w=0;a=0
    if ovf==1:return
    if e.char=="a":w-=1
    if e.char=="d":w+=1
    if e.char=="q" and zy>2:a+=1
    if e.char=="w" and zy>2:a-=1
    if e.char=="s":q=1
    point(q,w,a)
def point(e,ee,f):
    global zy,zx,ts,rn,df,nt,dief
    zx+=ee;brn=rn
    if ts!=4:rn+=f
    if rn>3-int(ts==3)*2:rn=0
    if rn<0:rn=3-int(ts==3)*2
    for ii in range(0,2):
        for i in range(0,4):
            cn=tc[ts][i];sy=cn[1];sx=cn[0]
            for t in range(0,rn):
                ps=sy;sy=sx;sx=-ps
            cy=sy+zy;cx=sx+zx
            mp=bpt[cy][cx]
            if zy<3 and bpt[cy][5+sx]!=0 and bpt[cy][5+sx]<11:
                dief=1
            if dief==0:
                if ee!=0 and mp!=0 and mp<8:
                    zx-=ee
                    return
                if mp!=0 and mp<12 and ii==0:
                    if f!=0:rn=brn;return
                    if ee!=0:zx-=ee;return
                    df+=1
                    if df==2:
                        over();zy=1;zx=5;rn=0;df=0
                    return
                if ii==1:
                    if i==0:clean(0)
                    bpt[cy][cx]=ts+12
            elif ii==1:
                bpt[1+sy][5+sx]=ts+12
    zy+=e
def over():
    global ts,bt
    clean(ts+4)
    ts=bt
    bt=rd.randrange(0,7)
    if bt==ts:bt=rd.randrange(0,7)
def clean(e):
    global sco,df
    sp=0
    for ii in range(0,20):
        n=0
        for i in range(0,10):
            o=bpt[ii+1][i+1]
            if o==3:
                for t in range(0,ii):
                    bpt[ii+1-t][i+1]=bpt[ii-t][i+1]
                bpt[1][i+1]=0
                if i==9:sp+=1
            if o>11:
                bpt[ii+1][i+1]=e
            if o>3:
                n+=1
            if n==10 and df!=0:
               for t in range(0,10):
                  bpt[ii+1][t+1]=3
    for tt in range(0,sp):
        sco+=scp[tt]
def go():
    global ovf,tm,sco,zy,zx
    ovf=0;zy=1;zx=5;tm=0;sco=0
    awake()
    main()
def die():
    global ovf
    for ii in range(0,20):
        for i in range(0,10):
            if bpt[ii+1][i+1]>0 and bpt[ii+1][i+1]<11:bpt[ii+1][i+1]=3
    ovf=1;but.config(state="normal");loop()
nt=2
for c in range(0,11):
    img.insert(c,tk.PhotoImage(file ="./pic(OLD)/"+cb[c]+".gif"))
awake()
def main():
    global ovf,tm,dief
    loop()
    while ovf==0:
        nt=0;tm+=1
        point(1,0,0)
        if dief==1:dief=0;nt=0;die()
        while nt<3:
            nt+=1;time.sleep(g);loop()
while True:
    main()
