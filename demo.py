import os
import pandas as pd


src = 'D:/Ku/2.0/2.4/duLieu'
objects = os.listdir(src)
files_file = [f for f in objects if os.path.isfile(os.path.join(src, f))]


def tinhSo(motTramSo):
    count = [int(0) for x in range(100)]
    mang = [x for x in range(100)]
    for y in range(100):
        count[y] = motTramSo.count(y)
    for a in range(100):
        for b in range(0, a):
            if count[a] < count[b]:
                haha = count[b]
                count[b] = count[a]
                count[a] = haha
                hehe = mang[b]
                mang[b] = mang[a]
                mang[a] = hehe
    top = sorted(mang[17:82])
    return top


tongtien = 0
ghi = open("lai.txt", 'w')
ghi.close()
for x in files_file:
    y = x.split(".")
    today = y[0]  # Tách lấy ngày đang xét
    # ----------------TÍNH TOÁN-----------------
    Date = x
    motTramSo = []
    mang = [x for x in range(100)]
    top = []  # lưu 35 phần tử ra nhiều nhất
    down = []  # lưu 65 phần tử ra ít nhất
    count = [int(0) for x in range(100)]
    danhSach = []
    ketQua = []
    nguoc = []
    cut = []

    time = 0.0
    maxx = 0
    timemax = 0
    minn = 0
    timemin = 0
    phut120 = 0
    phut280 = 0
    heSo = 1
    maxHeSo = 1
    timeHeSo = 0

    read = open(src + '/' + Date, 'r', encoding='utf-8')
    cut = read.readlines()
    read.close()
    dem = 0
    cut = [x.strip() for x in cut]  # xoá khoảng trắng, \n, \t ở trong list cut
    for x in cut:
        danhSach.append(int(x))
    tinhtien = 0
    ttngay = "ttNgay" + today
    # mở file ttngay...txt để ghi quá trình chơi
    ghittngay = open('D:/Ku/2.0/2.4/ketqua/' + ttngay + '.txt', 'w')

    for x in danhSach:
        dem += 1
        if dem <= 100:
            motTramSo.append(x)
        if dem > 100:
            so = tinhSo(motTramSo)
            ghittngay.write(str(so))
            ghittngay.write("\nSo tiep theo la: "+ str(x))
            motTramSo.pop(0)
            motTramSo.append(x)
            if heSo > 81:
                ghittngay.write("\nRefresh lai he so = 1")
                heSo = 1
            if so.count(x) > 0:
                tinhtien += 33 * heSo
                ketQua.append('0') 
                ghittngay.write("\nHe so la: " + str(heSo))
                heSo = 1
            else:
                tinhtien -= 65 * heSo
                ketQua.append('x')
                ghittngay.write("\nHe so la: " + str(heSo))
                heSo *= 3
            ghittngay.write("\nket qua: " + str(ketQua))
            ghittngay.write("\nTien lai: " + str(tinhtien))
            time += 90.0
            ghittngay.write("\nDa choi duoc: "+ str(time/60) + " phut" + "\n---------------------------------------------------\n")
        
        if tinhtien > maxx:
            maxx = tinhtien
            timemax = time / 60
        else:
            if tinhtien < minn:
                minn = tinhtien
                timemin = time / 60
        if (time / 60) == 120:
            phut120 = tinhtien
        if (time / 60) > 280:
            phut280 = tinhtien
            break

    ghittngay.close()

    # ghi ra file lai.txt
    tongtien += tinhtien
    ghi = open("lai.txt", 'a')
    ghi.write("\n______________________________________________________")
    ghi.write("\nTien lai: " + str(tinhtien))
    ghi.write("\nNgay: " + str(today))
    ghi.write("\nMax: " + str(maxx) + " Time: " + str(timemax) + " Phut")
    ghi.write("\nMin: " + str(minn) + " Time: " + str(timemin) + " Phut")
    ghi.write("\n120p: " + str(phut120) + "          280p: " + str(phut280))
    ghi.close()

ghi = open("lai.txt", 'a')
ghi.write("\n\nTong tien: " + str(tongtien))
ghi.close()
print("Dừng chương trình !!")
