from PIL import Image, ImageDraw, ImageFont
import random
from random import randint

players = [
    'niko',
    'vaiber',
    'Dead',
    'Federico',
    'Slend',
    'dro9',
    'spaceuk',
    'lord'
]
score = [0,0]

frames = []
font = ImageFont.truetype("arial.ttf",15)
font2 = ImageFont.truetype("arial.ttf",30)
# get an image
def redgoal(s1,s2):
    global frames
    with Image.open("C:/Users/av.malandin/Desktop/code/icebig.png").convert("RGBA") as base:
        sc = str(s1)+' - '+str(s2)
    
        global puck
        puck = 0
        draw = ImageDraw.Draw(base)
        draw.text((1,1),sc,font = font2, fill="yellow")
        draw.ellipse((105,300,135,330), fill=(255,0,0), outline=(0,0,0))
        draw.text((105,285),players[3],font=font,fill="black")
        draw.ellipse((1102,300,1132,330), fill=(0,0,255), outline=(0,0,0))
        draw.text((1102,285),players[7],font=font,fill="black")

        def playerA(i):
            global puck
            x1 = randint(100,1137)
            y1 = randint(20, 595)
            draw.ellipse((x1,y1,x1+30,y1+30), fill=(255,0,0), outline=(0,0,0))
            draw.text((x1,y1-15),players[i],font=font,fill="black")
            if puck==0:
                puck = 1
                p1 = randint(-1,1)
                if p1>0: p1=p1+19+15
                elif p1<0: p1=p1-19+15
                elif p1==0: p1=p1+15+19

                p2 = randint(-1,1)
                if p2>0: p2=p2+19+15
                elif p2<0: p2=p2-19+15
                elif p2==0: p2=p2+15+19

                draw.line((x1+p1+6,y1+p2+6,1140,randint(300,335)),fill="yellow",width=3)
                draw.ellipse((x1+p1,y1+p2,x1+p1+15,y1+p2+15), fill=(0,0,0), outline=(0,0,0))
        def playerB(i):
            x1 = randint(100,1137)
            y1 = randint(20, 595)
            draw.ellipse((x1,y1,x1+30,y1+30), fill=(0,0,255), outline=(0,0,0))
            draw.text((x1,y1-15),players[i],font=font,fill="black")
        
        for i in range(3):
            playerA(i)
        for i in range(4,7):
            playerB(i)
        
    frames.append(base)

def bluegoal(s1,s2):
    global frames
    with Image.open("C:/Users/av.malandin/Desktop/code/icebig.png").convert("RGBA") as base:
        sc = str(s1)+' - '+str(s2)

        global puck
        puck = 0
        draw = ImageDraw.Draw(base)
        draw.text((1,1),sc,font = font2, fill="yellow")
        draw.ellipse((105,300,135,330), fill=(255,0,0), outline=(0,0,0))
        draw.text((105,285),players[3],font=font,fill="black")
        draw.ellipse((1102,300,1132,330), fill=(0,0,255), outline=(0,0,0))
        draw.text((1102,285),players[7],font=font,fill="black")
        def playerA(i):
            global puck
            x1 = randint(100,1137)
            y1 = randint(20, 595)
            draw.ellipse((x1,y1,x1+30,y1+30), fill=(255,0,0), outline=(0,0,0))
            draw.text((x1,y1-15),players[i],font=font,fill="black")

        def playerB(i):
            global puck
            x1 = randint(100,1137)
            y1 = randint(20, 595)
            draw.ellipse((x1,y1,x1+30,y1+30), fill=(0,0,255), outline=(0,0,0))
            draw.text((x1,y1-15),players[i],font=font,fill="black")
            if puck==0:
                puck = 1
                p1 = randint(-1,1)
                if p1>0: p1=p1+19+15
                elif p1<0: p1=p1-19+15
                elif p1==0: p1=p1+15+19

                p2 = randint(-1,1)
                if p2>0: p2=p2+19+15
                elif p2<0: p2=p2-19+15
                elif p2==0: p2=p2+15+19

                draw.line((x1+p1+6,y1+p2+6,90,randint(300,335)),fill="yellow",width=3)
                draw.ellipse((x1+p1,y1+p2,x1+p1+15,y1+p2+15), fill=(0,0,0), outline=(0,0,0))
                
        
        for i in range(3):
            playerA(i)
        for i in range(4,7):
            playerB(i)

    frames.append(base)

for i in range(randint(3,13)):
    if randint(0,1)==0:
        score[0]+=1
        redgoal(score[0],score[1])

    else:
        score[1]+=1
        bluegoal(score[0],score[1])
        

frames[0].save('C:/Users/av.malandin/Desktop/code/montage.gif',
    save_all = True,
    append_images= frames[1:],
    optimize = True,
    duration = 2000,
    loop = 0
)

