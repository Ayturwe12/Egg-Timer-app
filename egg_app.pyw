from tkinter import *
from PIL import ImageTk,Image
import pygame
import os




root = Tk()
root.geometry("400x400")
root.title("Yumurta Sayacı")

base = os.path.dirname(os.path.abspath(__file__))

icon=os.path.join(base, "yumurta.ico")
root.iconbitmap(icon)

image_path =  os.path.join(base, "background.png")
image = Image.open(image_path)
image = image.resize((400,400))
bg_image = ImageTk.PhotoImage(image)


bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def stop_music():
    pygame.mixer.music.stop()
def durdur():
    global dur
    dur=True
    stop_music()
def resetle():
    global yeniden
    yeniden=True
    stop_music()


dur=False #süre döngüsünü durdurmak için bir değişken
yeniden=False


pygame.mixer.init()
music1=os.path.join(base, "tiktacsound.mp3")
pygame.mixer.music.load(music1)



def countdown(second):


    global l,dur,yeniden,sure

    min = second // 60
    sec = second % 60
    min_sabit=sure//60
    sec_sabit=sure%60
    try:
        l.config(text=f"{min}:{sec}")
        b.config(state=NORMAL,text="süreyi resetle",command=lambda:resetle())
        b1.config(state=NORMAL,text="durdur", command=lambda:durdur())


        if not dur and not yeniden :
            pygame.mixer.music.play(-1)
            if min!=0 or sec!=0:
                after = root.after(1000, countdown, second - 1)
            else:
                stop_music()

                pygame.mixer.init()
                music2 = os.path.join(base, "timeisfinishedsound.mp3")
                pygame.mixer.music.load(music2)
                pygame.mixer.music.play(-1)



                stop_button=Button(root,text="alarmı kapat",command=lambda:stop_music(),font=("Tahoma", 10, "bold"),
                    bg="#FF4500", fg="black", relief="ridge", cursor="hand2")
                stop_button.place(x=105,y=300,width=200)




        else:
            if dur :
                l.config(text=f"{min}:{sec+1}")
                b.config(state=DISABLED)
                b1.config(text="devam et", command=lambda:countdown(second))
                dur=False
            if yeniden:

                l.config(text=f"{min_sabit}:{sec_sabit}")
                b.config(text="süreyi başlat", command=lambda: countdown(sure))
                b1.config(state=DISABLED)
                yeniden=False

    except:
        return











def button1_clicked(x):
    global l,b,b1,saniye,sure
    delete_all()
    stop_music()
    if x=="start":
        frame_creator()
    else:
        l = Label(root,
                   fg="black", bg="orange", font=("Impact", 15), borderwidth=1, relief="solid")
        l.place(x=180, y=260)

        b= Button(root, text="Süreyi başlat", font=("Tahoma", 10, "bold"),
                    bg="orange", fg="black", relief="ridge", cursor="hand2")
        b.place(x=240, y=260)
        b1 = Button(root, text=" Durdur",state=DISABLED, font=("Tahoma", 10, "bold"),
                    bg="orange", fg="black", relief="ridge", cursor="hand2")
        b1.place(x=100, y=260)

        b_back = Button(root, command=lambda: button1_clicked("start"), text="<--", relief="groove", cursor="exchange",
                        borderwidth=0,
                        background="#DAA520", fg="black")
        b_back.place(x=350, y=50)

        if x == "1":
            img_lbl_1 = Label(root, image=img_1)
            img_lbl_1.place(x=140, y=80)

            l1 = Label(root, text="Rafadan yumurta için gereken süre: ",
                      fg="black", bg="orange", font=("Impact", 15), borderwidth=1, relief="solid")
            l1.place(x=70, y=210)

            l.config(text="04:00")
            sure=240
            b.config(command=lambda: countdown(240))
        elif x == "2":
            img_lbl_2 = Label(root, image=img_2)
            img_lbl_2.place(x=140, y=80)

            l1 = Label(root, text="Az pişmiş yumurta için gereken süre: ",
                      fg="black", bg="orange", font=("Impact", 15), borderwidth=1, relief="solid")
            l1.place(x=55, y=210)

            l.config(text="06:00")
            sure=360
            b.config(command=lambda: countdown(360))
        elif x == "3":
            img_lbl_3 = Label(root, image=img_3)
            img_lbl_3.place(x=140, y=80)

            l1 = Label(root, text="Normal yumurta için gereken süre: ",
                      fg="black", bg="orange", font=("Impact", 15), borderwidth=1, relief="solid")
            l1.place(x=70, y=210)

            l.config(text="09:00")
            sure=540
            b.config(command=lambda: countdown(540))

        elif x == "4":
            img_lbl_4 = Label(root, image=img_4)
            img_lbl_4.place(x=140, y=80)

            l1 = Label(root, text="Çok pişmiş yumurta için gereken süre: ",
                      fg="black", bg="orange", font=("Impact", 15), borderwidth=1, relief="solid")
            l1.place(x=55, y=210)

            l.config(text="12:00")
            sure=720
            b.config(command=lambda: countdown(720))



def delete_all():
    global bg_label,bg_image,image
    for i in root.winfo_children():
        if i != bg_label :
            i.destroy()



def frame_creator():
    global img_1, img_2, img_3, img_4  # Fotoğrafların kaybolmasını önlemek için global
    global img_lbl_1, img_lbl_2, img_lbl_3, img_lbl_4,b_back

    img1 =  os.path.join(base, "rafadan.png")
    img2 =os.path.join(base, "azpismis.png")
    img3 = os.path.join(base, "normal.png")
    img4 = os.path.join(base, "cokpismis.png")

    img1_ = Image.open(img1)
    img2_ = Image.open(img2)
    img3_ = Image.open(img3)
    img4_ = Image.open(img4)

    img_1 = ImageTk.PhotoImage(img1_)
    img_2 = ImageTk.PhotoImage(img2_)
    img_3 = ImageTk.PhotoImage(img3_)
    img_4 = ImageTk.PhotoImage(img4_)

    img_lbl_1 = Label(root, image=img_1)
    img_lbl_1.place(x=60, y=80)

    img_lbl_2 = Label(root, image=img_2)
    img_lbl_2.place(x=220, y=80)

    img_lbl_3 = Label(root, image=img_3)
    img_lbl_3.place(x=60, y=230)

    img_lbl_4 = Label(root, image=img_4)
    img_lbl_4.place(x=220, y=230)

    #butonları ekledim
    b1 = Button(root, text="Rafadan(4dk)", command=lambda:button1_clicked("1"),font=("Tahoma", 10, "bold"),
                bg="orange", fg="black", relief="ridge",cursor="hand2")

    b1.place(x=70, y=203)

    b2 = Button(root, text="Az pişmiş(6dk)", command=lambda: button1_clicked("2"),font=("Tahoma", 10, "bold"),
                bg="orange", fg="black", relief="ridge",cursor="hand2")
    b2.place(x=230, y=203)

    b3 = Button(root, text="Normal(9dk)", command=lambda: button1_clicked("3"),font=("Tahoma", 10, "bold"),
                bg="orange", fg="black", relief="ridge",cursor="hand2")
    b3.place(x=70, y=355)

    b4 = Button(root, text="Çok Pişmiş(12dk)", command=lambda: button1_clicked("4"),font=("Tahoma", 10, "bold"),
                bg="orange", fg="black", relief="ridge",cursor="hand2")
    b4.place(x=230, y=355)

    b_back = Button(root,command=lambda:ana_ekran(), text="<--", relief="groove", cursor="exchange", borderwidth=0,
                    background="#DAA520", fg="black")
    b_back.place(x=350, y=50)

    l=Label(root,text="Lütfen yumurta tercihinizi yapın: ",
            fg="black",bg="orange",font=("Impact",15),borderwidth=1,relief="solid")
    l.place(x=75,y=20)

def ana_ekran():

    delete_all()
    w1=Label(root, text=" Yumurta Sayacı ",font=("Impact",20,"bold"),bg="orange",borderwidth=1,relief="solid")
    w1.place(x=110,y=100)

    b1=Button(root,text="Başlat",font=("Tahoma",20,"bold"),cursor="mouse",bg="orange red",command=lambda:button1_clicked("start"))
    b1.place(x=150,y=200)

    madeby=Label(root,text='Made By "Ahmet Güler"',font=("courier new",8,"italic"),fg="grey",bg="#E9967A")
    madeby.place(x=230,y=360)








ana_ekran()
root.mainloop()