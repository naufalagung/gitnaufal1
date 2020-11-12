#NAUFAL AGUNG

#SOAL 1 HASHTAG
# x = input('masukan kalimat: ')      #pertama kita buat dulu metode dimana kita bisa input kata yg kita mau
# def hashtag(x):
#     if len(x)>=140:                 #kemudian buat conditional pertama. kalau saya, saya mulai dari conditional penolakan dulu, yakni jika karakter lebih dari 140 char, maka keluar False
#         print('FALSE')
#     elif len(x)>=1 or len(x)<140:   #kemudian, buat conditional kedua, yakni kondisi yang diharapkannya
#         y = x.title()               #disini saya menggunakan method title yang berfungsi untuk mengkapitalkan awalan setiap kata. semisal ada kalimat nama saya naufal, maka outputnya itu Nama Saya Naufal
#         z = y.split()               #setelahnya, saya split. tujuannya adalah karena output yg diinginkan itu antar kata ga ada spasinya. 
#         r = ''.join(z)              #agar terwujudnya output yg diinginkan, saya gunakan join dengan spasi berupa tidak adanya spasi
#         print('"#'+r+'"')
#     elif len(x)<=0:                 #yg empty string belum kak
#         print('FALSE')
#     return
# hashtag(x)

# pertama kita buat kode yang bisa memasukan input yang kita mau
# x = input('masukan kalimat: ')
# if len(x)>=140:
#     print('FALSE')
# elif len(x)>=1 or len(x)<140:
#     y = x.title()
#     z = y.split()
#     r = ''.join(z)
#     print('"#'+r+'"')
# elif len(x)<=0:
#     print('FALSE')






#SOAL 2 CREATE_PHONE_NUMBER
# def create_phone_number(x):       #pertama kita buat dulu nama fungsi yang diinginkan. pada soal namanya sesuai berikut
#     list1 = x[0:3]                #kemudian, karena output yang diinginkan itu menurut saya merupakan pembagian dari 3 list, makanya dibuat 3 list baru yang berisikan sesuai dengan index dari output yang diinginkan. pada kasus disoal, index dari outputnya sesuai dengan apa yang telah tertulis di kode
#     list2 = x[3:6]
#     list3 = x[6:]
#     str1 = list(map(str, list1))  #kemudian, kita ubah list tersebut menjadi sebuah string dengan fungsi map. tujuan utama fungsi map adalah mengubah list menjadi string
#     str2 = list(map(str, list2))
#     str3 = list(map(str, list3))
#     return '"('+''.join(str1)+') '+''.join(str2)+'-'+''.join(str3)+'"' #terakhir, kita gabung semuanya dengan fungsi join. 

# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))







#SOAL 3 SORT_ODD_EVEN
list1=[5, 3, 2, 8, 1, 4]
#output yang diinginkan [1, 3, 8, 4, 5, 2]

def fungsi1(list1):             # pertama buat beberapa fungsi kosong yang akan dijadikan sebagai tempat menampung hasil
    genap1 = []                 # list yang berisikan angka2 ganjil
    ganjil1 = []                # list yang berisikan angka2 genap
    maxgenap1 = []              # list yang berisikan angka genap dengan urutan dari terbesar ke terkecil
    minganjil1 = []             # list yang berisikan angka ganjil dengan urutan dari terkecil ke terbesar
    hasil1      = []

#misahin angka genap dan ganjil
    for i in list1:
        if i%2==0:              # ketika elemen di dalam list dibagi 2 dan tidak bersisa, maka akan dimasukan ke dalam list genap1
            genap1.append(i)
        elif i%2!=0:            # ketika elemen di dalam list dibagi 2 dan bersisa, maka akan dimasukan ke dalam list ganjil1
            ganjil1.append(i)

#sort genap1 dari max ke min
    for i in range(len(genap1)):
        maxg = max(genap1)
        maxgenap1.append(maxg)
        genap1.remove(maxg)


#sort ganjil1 dari min ke max
    for i in range(len(ganjil1)):
        ming = min(ganjil1)
        minganjil1.append(ming)
        ganjil1.remove(ming)

#gabung list maximum dengan list minimum sesuai yang output diinginkan
    for i in range(len(list1)):
        if i%2==0:
            hasil1.append(maxgenap1[0])
            maxgenap1.pop(0)
        elif i%2!=0:
            hasil1.append(minganjil1[0])
            minganjil1.pop(0)

    return hasil1

print(fungsi1(list1))












#SOAL 4 HOLLOW TRIANGLE
#            coloumn
#         (1)(2)(3)(4)(5) 
#    r (1) -  -  #  -  -
#    0 (2) -  #  -  #  -
#    w (3) #  #  #  #  #

# for row in range(1,4): #pertama kita buat segitia dengan mengasumsikan nilainya tetap dulu. dalam hal ini, saya mencoba dengan menginput value dari row / hollowTriangle sebesar 3. jadi kita tulisnya 1,4, karena range itu akan ngerange dari nilai awal hinga akhir-1 
#     for col in range (1,6): #kemudian, kita buat repetisi ke kanannya mau seberapa banyak. dalam kasus ini, pada setiap row, repetisinya sebanyak 5 kali (termasuk spasi). berarti kita tulisnya 1,6, karena range itu akan ngerange dari nilai awal hinga akhir-1 
#         if row==3 or row+col==4 or col-row==2: #kemudian kita analisis conditionalnya seperti apa. pertama kita lihat dimana aja bintang itu kita inginkan berada: (1) pada row ketiga, kita ingin ada semua bintang. hal ini juga bisa kita tuangkan dalam bentuk kode sebagai row==3 (ketika berada pada row 3, maka print semua bintang). kemudian, kita menggunakan 'or' agar ketika salah satu conditional terpenuhi, maka kode dapat berjalan. (2) kemudian, kita ingin menggambarkan bintang pada sisi diagonal. untuk itu, kita lihat posisi diagonal pertama (yang di kiri). kalau kita lihat, value dari bintang yang ada pada row 1 dibagian kiri itu = 4 (dari 3+1). begitu pula pada row 2, total valuenya juga 2(2+2). begitu pula pada row 3 (1+3). (3)conditional terakhir adalah, kita lakukan hal yg sama seperti conditional yg kedua, namun, pada kali ini kita kurangin angka antara coloumn dengan row. pada row 1, bintangnya berada pada value 3-1=2. pada row kedua, nilai bintangnya adalah 4-2=2. pada row ketiga, nilai bintangnya adalah 5-3=2. oleh karenanya, kita tulis col-row=2
#             print('*', end=' ') #kemudian kita tulis fungsi print dari bintangnya
#         else:
#             print(' ', end=' ') #jika kemudian fungsi ini me-looping pada value yg tidak sesuai dengan value conditional if, maka yg akan di print adalah spasi kosong
#     print()

# #selesai tahap 1. kemudian, kita ingin ubah agar bisa di input angkanya, sehingga:

# n=int(input('masukan jumlah row: ')) #pertama kita jadiin n sebagai nilai input
# for row in range(1,n+1): #kemudian, kalau kita lihat dari fungsi diatas, nilai 4 itu merupakan nilai 3+1 (row+1). oleh karenanya, kita tulis n+1
#     for col in range(1,n*2): #kemudian, kita mengacu lagi pada fungsi diatas. dengan nilai n=3, maka coloumn itu =6. artinya, 6= 2*3. oleh karenanya, kita subtitusi 3 dengan n, akan menjadi 2*n
#         if row==n or row+col==n+1 or col-row==n-1: #sama halnya dengna yang sebelumnya, kita buat angka yang diatas itu terdiri dari elemen 3. pada akhirnya, kita akan mengetahui bahwa angka 4 merupakan pertambahan dari 3+1, dan angka 2 merupakan pengurangan dari 3-1. oleh karenanya, kita tulis n+1 dan n-1 pada kode 
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# #kalau di soal spasinya dimnta diganti jadi underscore, maka kodenya akan menjadi:
# n=int(input('masukan jumlah row: ')) 
# for row in range(1,n+1): 
#     for col in range(1,n*2): 
#         if row==n or row+col==n+1 or col-row==n-1: 
#             print('*', end='')
#         else:
#             print('_', end='')
#     print()
