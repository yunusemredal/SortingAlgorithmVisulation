from tkinter import *
from tkinter import ttk
import random
from src.algorithms.bubbleSorti import bubbleSort
from src.algorithms.bubbleSorti import stopSorting
from src.algorithms.quickSort import quickSort
from src.algorithms.mergeSort import mergeSort
from src.algorithms.insertionSort import insertionSort
from src.algorithms.selectionSort import selectionSort
from src.graf.grafics import draw_bar_chart, draw_scatter_chart, draw_stem_chart
root = Tk()
root.title('SIRALAMA ALGORİTMALARI GÖRSELLEŞTİRİCİSİ')
root.geometry('1080x800+200+80')
root.config(bg='White')
data = []
sorting_stopped = False

"""
    Animasyonu durdurur veya başlatır.
    Bu fonksiyon animasyonun arka planda devam etmesine engel olmaz. sadece animasyonu basıldığı yerde durdurur.
    tekrar Stop butonuna basıldığında animasyon  arka plandaki kaldığı yerden devam eder. Durdurulduğu yerden değil .
    """


def toggleSorting():
    global sorting_stopped
    sorting_stopped = not sorting_stopped  # Algoritmanın devam etmesi için startAlgorithm() fonksiyonunu çağır
def stopAlgorithm():
    #Durdurma algoritmasını çağırır . Stop butonuna bağlıdır.
    toggleSorting()


"""
    Bu fonksiyon verilen veri kümesini ve renk dizisini kullanarak grafik çizer.
    Aynı zamanda animasyonu durdurmak için root.update() fonksiyonunu kullanır.
    root.update() fonksiyonu sayesinde güncellemere dikkat edilir. 
    canvas.delete('all') fonksiyonu sayesinde sadece animasyon paneli sıfırlanmış olur. 
    canvas boyutlarını bir nebze kısaltarak girilmiştir. Bunun nedeni taşmanın engellenmesidir. 
    plotType değişkeni ile hangi grafik türünün çizileceği belirlenir. Bu değişken varG değişkenine bağlıdır. 
    """
def drowData(data, colorArray, plotType):
    # Animasyon durdurulmuşsa fonksiyonu hemen sonlandır
    root.update()
    if sorting_stopped:
        return
    canvas.delete('all')  # clear the canvas
    canvas_height = 690
    canvas_width = 810

    x_width = canvas_width / (len(data) + 1)
    offset = 0.01
    spacing_bet_rect = 0.1
    normalized_data = [i / max(data) for i in data]

    if plotType == 'Bar':
        draw_bar_chart(normalized_data, colorArray, x_width, offset, spacing_bet_rect, canvas_height,canvas)
        
    elif plotType == 'Scatter':
        draw_scatter_chart(normalized_data, colorArray, canvas_height, canvas_width,canvas,data)
    
    elif plotType == 'Stem':
        draw_stem_chart(colorArray, canvas_height, canvas_width,canvas,data,normalized_data)

    root.update_idletasks()

def startAlgorithm():
    global data
    selected_algorithm = var.get()
    speed = int(speedScale.get())*100 
    """
    Algoritmalarının başlaması ve kendilerine özel karmaşıklık değerlerinin yazdırılması için kullanılır.
    Algoritmalar Radio buttona bağlıdır. Bu da selected_algorithm değişkenine bağlıdır. 
    eğer veri yoksa tekrar başa döndürülür.
    

    Tkinderda 1000 birim 1 saniye demektir. Skala 10 birime kadar olduğundan 100 ile çarpıyoruz.
    bu sayede 10 birimde 1 saniye  yavaşlatıyoruz.  10 birim belirlendiğinde 1000 karşılaştırmada 1000 saniye yavaşlama oluyor . 
    
    Data verilerimizi , drowData fonksiyonu ile çizdirdik. speed ile hızını ayarladık.
    Burada bahsedilen hız değişkenleri yavaşlatma amaçlı yazılmıştır. ComparisonLabel ile karşılaştırma sayısını yazdırdık.
    TimeLabel ile geçen süreyi yazdırdık. Root ile de ana pencereyi gönderdik.
    """
    if not data:
        return
    # Eğer veri yoksa başa sarmasını istiyoruz. 
    #bubble sort karmaşıklığı: O(n^2)
    if selected_algorithm == 1:
        buble_Label=Label(root, text='Bubble Sort Karmaşıklığı: O(n^2)', font=('times new roman', 12, 'italic bold'), 
                            width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
        buble_Label.place(x=610, y=750)
        root.update()
        bubbleSort(data, drowData,speed,comparisonLabel,timeLabel,root,varG)
        
    #Quick Sort Karmaşıklığı: O(n log n)
    elif selected_algorithm == 2:
        quick_label=Label(root, text='Quick Sort Karmaşıklığı: O(n log n)', font=('times new roman', 12, 'italic bold'),
                            width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
        quick_label.place(x=610, y=750)
        root.update()
        quickSort(data,0,len(data)-1,drowData,speed,root,comparisonLabel,varG)

    #Merge Sort Karmaşıklığı: O(n log n)
    elif selected_algorithm == 3:
        merge_sort_label = Label(root, text='Merge Sort Karmaşıklığı: O(n log n)', font=('times new roman', 12, 'italic bold'),
                            width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
        merge_sort_label.place(x=610, y=750)
        root.update()
        mergeSort(data,drowData,speed,root,timeLabel,comparisonLabel,varG)

    #Insertion Sort Karmaşıklığı: O(n^2)
    elif selected_algorithm == 4:
        insertion_sort_label = Label(root, text='Insertion Sort Karmaşıklığı: O(n^2)', font=('times new roman', 12, 'italic bold'),
                            width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
        insertion_sort_label.place(x=610, y=750)
        root.update()
        insertionSort(data, drowData,speed,root,timeLabel,comparisonLabel,varG)

    #Selection Sort Karmaşıklığı: O(n^2)
    elif selected_algorithm == 5:
        selection_sort_label = Label(root, text='Selection Sort Karmaşıklığı: O(n^2)', font=('times new roman', 12, 'italic bold'),
                            width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
        selection_sort_label.place(x=610, y=750)
        root.update()
        selectionSort(data, drowData,speed,root,timeLabel, comparisonLabel,varG)

    drowData(data,['green' for x in range(len(data))],varG.get())

"""
    Generate butonuna basıldığında çalışan fonksiyondur. Bu fonksiyon sayesinde verilerimizi görsel şekile bürünmesine imkan sağlıyoruz
    Bu fonksiyon rasgele oluşturduğu verileri drowData fonksiyonuna gönderiyor. gönderme sırasına göre dönen cevabı ekrana çiziyor.
"""
def Generate():
    global data
    if len(entrys.get()) != 0:
        data = []
        for x in entrys.get().split(','):
            data.append(int(x))
        drowData(data,['red'for x in range(len(data))],varG.get())
    else:
        """
        print("Selected Algorithm: " + selected_algorithm.get())
        miniValue = int(minValue.get())
        maxiValue = int(maxValue.get())
        sizeeValue = int(sizeValue.get())
        """
        minValue=0
        maxValue=200
        data = []
        for _ in range(int(sizeValue.get())):
                data.append(random.randrange(minValue, maxValue + 1))
        # data.append(random.randrange(int(miniValue.get()), int(maxiValue.get()) + 1))
        drowData(data,['red'for x in range(len(data))],varG.get())

def deleteAll():
    """
    Sıfırla butonuna basınca tüm ekrandaki bilgilerin çoğunu sıfırlamaktadır."""
    canvas.delete('all')
    data.clear()
    sizeValue.set(0)
    speedScale.set(0.0)
    comparisonLabel.config(text="Karşılaştırma sayısı: 0")
    timeLabel.config(text="Geçen süre: 0 saniye")



    

#Tanımlamalar ve yerleştirmeler
selected_algorithm = IntVar()
selected_graf = StringVar()
varG = StringVar()
varG.set('Bar')
var = IntVar()
var.set(1) 
#burada Radio butonlarımızı tanımlıyoruz. Bu butonlar arasında seçim yaparak hangi algoritmayı çalıştırmak istediğimizi belirliyoruz.

radio1 = Radiobutton(root, text="Bubble Sort",font=('times new roman',14,'italic'),background='white', variable=var, value=1)
radio2 = Radiobutton(root, text="Quick Sort",font=('times new roman',14,'italic'),background='white', variable=var, value=2)
radio3 = Radiobutton(root, text="Merge Sort",font=('times new roman',14,'italic'),background='white', variable=var, value=3)
radio4 = Radiobutton(root, text="Insertion Sort",font=('times new roman',14,'italic'),background='white', variable=var, value=4)
radio5 = Radiobutton(root, text="Selection Sort",font=('times new roman',14,'italic'),background='white', variable=var, value=5)
radio6 = Radiobutton(root, text="Sütun Grafik",font=('times new roman',14,'italic'),background='white', variable=varG, value='Bar')
radio7 = Radiobutton(root, text="Dağılım Grafik",font=('times new roman',14,'italic'),background='white', variable=varG, value='Scatter')
radio8 = Radiobutton(root, text="Kök Grafik",font=('times new roman',14,'italic'),background='white', variable=varG, value='Stem')


#Burada radio butonlarının konumlarını belirtiyoruz.
radio1.place(x=0, y=30)
radio2.place(x=0, y=60)
radio3.place(x=0, y=90)
radio4.place(x=0, y=120)
radio5.place(x=0, y=150)
radio6.place(x=0, y=215)
radio7.place(x=0, y=245)
radio8.place(x=0, y=275)

#Buttonlar
#Rastgele sayı üretme butonu Generate algoritmasını çağırır
random_generate= Button(root,text="Oluştur",bg='white',fg='black',
                        font=('times new roman',12,'italic bold'),
                        relief=SUNKEN,activebackground='white',
                        activeforeground='black',bd=5, width=10 ,
                        command=Generate)
random_generate.place(x=0,y=480)

#Sıfırlama butonu deleteAll algoritmasını çağırır
sıfırla=Button(root,text="Sıfırla",bg='white',fg='black',
                font=('times new roman',12,'italic bold'),
                relief=SUNKEN,activebackground='white',
                activeforeground='black',bd=5, width=10 ,
                command=deleteAll)
sıfırla.place(x=0,y=520)
#Başlatma butonu startAlgorithm algoritmasını çağırır
start=Button(root,text="Start",bg='white',fg='black',
                        font=('times new roman',12,'italic bold'),
                        relief=SUNKEN,activebackground='white',
                        activeforeground='black',bd=5, width=10 ,
                        command=startAlgorithm)
start.place(x=120,y=480)
#Durdurma butonu stopAlgorithm algoritmasını çağırır
stopButton=Button(root,text="Stop",bg='white',fg='black',
            font=('times new roman',12,'italic bold'),
            relief=SUNKEN,activebackground='white',
            activeforeground='black',bd=5, width=10 ,
            command=stopAlgorithm)
stopButton.place(x=120,y=520)

#Labellar
#Grafik başlığını yazdıran label
grafLabel= Label(root,text='Grafik:',font=('times new roman',16,'italic bold'),
                    width= 20,background='white',)#, fg='black',bg='white',relief=GROOVE,bd=5)
grafLabel.place(x=0,y=185)
#Algoritma başlığını yazdıran label
mainlabel = Label(root,text='Algoritma',background='white',
                    font=('times new roman',16,'italic bold'),
                    width= 20)
                    #fg='black',bg='white',relief=GROOVE,bd=5)
mainlabel.place(x=0,y=0)
#Boyut button başlığını yazdıran label
sizeValueLabel= Label(root,text='Boyut:',
                font=('times new roman',12,'italic bold'),background='white',
                width= 10,height=2, fg='black')
sizeValueLabel.place(x=0,y=380)
#hız button başlığını yazdıran label
speedValueLabel = Label(root, text='Hız:', 
                        font=('times new roman',12,'italic bold'),background='white',
                        width= 10,height=2, fg='black')
speedValueLabel.place(x=0, y=420)
#Karşılaştırma bilgilerinin sort algoritmalarından alınan değerlerle güncellenmesini sağlayan label 
comparisonLabel = Label(root, text="Karşılaştırma: 0",
                        font=('times new roman',12,'italic'),
                        width= 25,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
comparisonLabel.place(x=250, y=750)
#Zaman bilgilerinin  Sort algoritmalarından alınan değerlerle güncellenmesini sağlayan label 
timeLabel= Label(root,text=" ",
                        font=('times new roman',12,'italic'),
                        width= 25,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
timeLabel.place(x=430,y=750)
entrysLabel=Label(root, text='Sıralamak İstediğiniz Sayıları Giriniz: ',
                    font=('times new roman', 12, 'italic bold'), 
                    width= 30,height=2,bg='white', fg='black',relief=GROOVE,bd=1)
entrysLabel.place(x=0, y=310)


#Scale buttonları 
#Hız butonu 0 ile 10 arasında bir skala belirlendir. 
speedScale = Scale(root, from_=0.1, to=10.2, resolution=0.2, length=150, digits=2, orient=HORIZONTAL,
                   font=('times new roman', 14, 'italic'),
                   relief=GROOVE, bd=2,bg='white', width=10)
speedScale.place(x=100, y=420)
#boyut butonu 0 ile 100 arasında bir skala belirlendir. Bunun sebebi algoritmanın sunum esnasında verimli olarak çalışması 
sizeValue= Scale(root,from_=0,to=100 ,length=150,orient=HORIZONTAL,bg='white',
                    font=('times new roman',14,'italic'),resolution=1,
                    bd=2,width=10)
sizeValue.place(x=100,y=380)

entrys = Entry(root, font=('times new roman', 12), width=30,bg='#dddddd')
entrys.place(x=0, y=350)

#Grafik arayüzünün yeri 
canvas = Canvas(root, width=800, height=740, bg='White',relief=GROOVE, bd=5)
canvas.place(x=250,y=0)
"""
Kodun  minimum ve maksimum değerlerin kullanıcı tarafından belirlenmesi için yapılmıştır fakat pasife alınmıştır. 
"""
minValueLabel= Label(root,text='Min Değer:',
                        font=('times new roman',12,'italic bold'),background='white',
                        width= 10,height=2, fg='black')
minValue= Scale(root,from_=0,to=50,length=150,orient=HORIZONTAL,bg='white',
                    font=('times new roman',14,'italic'),resolution=1,
                    bd=2,width=10)
#minValueLabel.place(x=0,y=580)
#minValue.place(x=100,y=580)

maxValueLabel= Label(root,text='Max Değer:',
                        font=('times new roman',12,'italic bold'),background='white',
                        width= 10,height=2, fg='black')
maxValue= Scale(root,from_=0,to=200,length=150,orient=HORIZONTAL,bg='white',
                    font=('times new roman',14,'italic'),resolution=1,
                    bd=2,width=10)
#maxValue.place(x=100,y=650)
#maxValueLabel.place(x=0,y=650)

root.mainloop()