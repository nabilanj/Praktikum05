#Tugas Praktikum 05
print ("Program Input Nilai")

Data = {}
while True :
    print ("")
    A = input ("[ (A)dd, (E)dit, (D)elete, (S)earch, (L)ist, (Q)uit ] : ")
    if A.lower() == 'q' :
        break
    elif A.lower() == 'l' :
        if Data != {}  :
            print ()
            print ("                     DAFTAR NILAI MAHASISWA                       ")
            print ("==================================================================")
            print ("| NO |     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
            print ("==================================================================")
            i = 0
            for x in Data.items() :
                i+= 1
                print ("| {6:2} |  {0:10s} | {1:9} | {2:5d} | {3:3d} | {4:3d} |{5:12.2f} |"\
                       .format (x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print ("==================================================================")
        else :
            print ("                     DAFTAR NILAI MAHASISWA                       ")
            print ("==================================================================")
            print ("| NO |     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
            print ("==================================================================")
            print ("|                   TIDAK ADA DATA MAHASISWA                     |")
            print ("==================================================================")

        
                   
    elif A.lower () == 'a' :
        print (" TAMBAHKAN DATA ")
        NAMA = input (" Masukkan Nama        : ")
        NIM = input (" Masukkan NIM         : ")
        TUGAS = int(input (" Masukkan Nilai Tugas : "))
        UTS = int(input (" Masukkan Nilai UTS   : "))
        UAS = int(input (" Masukkan Nilai UAS   : "))
        AKHIR = float((TUGAS)*30/100 + (UTS)*35/100 + (UAS)*35/100)
        Data[NAMA] = NIM, TUGAS, UTS, UAS, AKHIR
    elif A.lower () == 'e' :
        print (" Edit Data")
        NAMA = input (" Masukkan Nama        : ")
        if NAMA in Data.keys() :
            NIM = input (" Masukkan NIM         : ")
            TUGAS = int(input (" Masukkan Nilai Tugas : "))
            UTS = int(input (" Masukkan Nilai UTS   : "))
            UAS = int(input (" Masukkan Nilai UAS   : "))
            AKHIR = float((TUGAS)*30/100 + (UTS)*35/100 + (UAS)*35/100)
            Data[NAMA] = NIM, TUGAS, UTS, UAS, AKHIR
        else :
            print (" DATA {0} TIDAK ADA ".format(NAMA))
    elif A.lower () == 's' :
        print (" Search Data ")
        NAMA = input (" Masukkan Nama        : ")
        if NAMA in Data.keys() :
            print ("=============================================================")
            print ("|     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
            print ("=============================================================")
            print ("|  {0:10s} | {1:9} | {2:5d} | {3:3d} | {4:3d} |{5:12.2f} |"\
                   .format(NAMA, NIM, TUGAS, UTS, UAS, AKHIR))
            print ("=============================================================")
        else :
            print(" DATA {0} TIDAK ADA ".format(NAMA))
    
    elif A.lower () == 'd' :  
        print (" Hapus Data")
        NAMA = input (" Masukkan Nama        : ")
        if NAMA in Data.keys () :
            del Data[NAMA]
        else :
            print(" DATA {0} TIDAK ADA ".format(NAMA))
    else :
        print (" Pilihlah Menu Yang Tersedia.......")
        
    
