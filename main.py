# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi #The loadUi function is used to load the design we have made with Qt designer with .ui extension on line 18.

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)  # NavigationToolBar2QT from the Matplotlib module is imported to be able to operate on the graph


from urllib.request import urlopen



url = "https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")



#Rearranging the html file and table
table_start_index = html.find("var geneldurumjson =") + len("var geneldurumjson =")
table_end_index = html.find("}];//]]>")
table = html[table_start_index : table_end_index]
table = table.replace('.12.' , ' Dec ')
table = table.replace('.11.' , ' Nov ')
table = table.replace('.10.' , ' Oct ')
table = table.replace('.09.' , ' Sep ')
table = table.replace('.08.' , ' Aug ')
table = table.replace('.07.' , ' Jul ')
table = table.replace('.06.' , ' Jun ')
table = table.replace('.05.' , ' May ')
table = table.replace('.04.' , ' Apr ')
table = table.replace('.03.' , ' Mar ')
table = table.replace('.02.' , ' Feb ')
table = table.replace('.01.' , ' Jan ')
table = table.replace('.' , '')


#Daily Cases
daily_case_list = []
daily_list_December2022 = [] 
daily_list_November2022 = [] 
daily_list_October2022 = [] 
daily_list_September2022 = [] 
daily_list_August2022 = [] 
daily_list_July2022 = [] 
daily_list_June2022 = [] 
daily_list_May2022 = [] 
daily_list_April2022 = [] 
daily_list_March2022 = [] 
daily_list_February2022 = [] 
daily_list_January2022 = [] 
daily_list_December2021 = [] 
daily_list_November2021 = [] 
daily_list_October2021 = [] 
daily_list_September2021= [] 
daily_list_August2021 = [] 
daily_list_July2021 = [] 
daily_list_June2021 = [] 
daily_list_May2021 = [] 
daily_list_April2021 = [] 
daily_list_March2021 = [] 
daily_list_February2021 = [] 
daily_list_January2021 = []
daily_list_December2020 = []



#Dates
date_list = []
date_list_December2022 = [] 
date_list_November2022 = [] 
date_list_October2022 = [] 
date_list_September2022 = [] 
date_list_August2022 = [] 
date_list_July2022 = [] 
date_list_June2022 = [] 
date_list_May2022 = [] 
date_list_April2022 = [] 
date_list_March2022 = [] 
date_list_February2022 = [] 
date_list_January2022 = [] 
date_list_December2021 = [] 
date_list_November2021 = [] 
date_list_October2021 = [] 
date_list_September2021= [] 
date_list_August2021 = [] 
date_list_July2021 = [] 
date_list_June2021 = [] 
date_list_May2021 = [] 
date_list_April2021 = [] 
date_list_March2021 = [] 
date_list_February2021 = [] 
date_list_January2021 = []
date_list_December2020 = [] 
date_2022 = '2022'
date_2021 = '2021'
date_2020 = '2020'
date_jan = 'Jan'
date_feb = 'Feb'
date_mar = 'Mar'
date_apr = 'Apr'
date_may = 'May'
date_jun = 'Jun'
date_jul = 'Jul'
date_aug = 'Aug'
date_sep = 'Sep'
date_oct = 'Oct'
date_nov = 'Nov'
date_dec = 'Dec'



#Dictionaries
dic = {}
dic_jan2022 = {}
dic_feb2022 = {}
dic_mar2022 = {}
dic_apr2022 = {}
dic_may2022 = {}
dic_jun2022 = {}
dic_jul2022 = {}
dic_aug2022 = {}
dic_sep2022 = {}
dic_oct2022 = {}
dic_nov2022 = {}
dic_dec2022 = {}
dic_jan2021 = {}
dic_feb2021 = {}
dic_mar2021 = {}
dic_apr2021 = {}
dic_may2021 = {}
dic_jun2021 = {}
dic_jul2021 = {}
dic_aug2021 = {}
dic_sep2021 = {}
dic_oct2021 = {}
dic_nov2021 = {}
dic_dec2021 = {}
dic_dec2020 = {}



#Total Cases by Months
total_jan2022 = 0 
total_feb2022 = 0 
total_mar2022 = 0 
total_apr2022 = 0 
total_may2022 = 0 
total_jun2022 = 0 
total_jul2022 = 0 
total_aug2022 = 0 
total_sep2022 = 0 
total_oct2022 = 0 
total_nov2022 = 0 
total_dec2022 = 0
total_jan2021 = 0 
total_feb2021 = 0 
total_mar2021 = 0 
total_apr2021 = 0 
total_may2021 = 0 
total_jun2021 = 0 
total_jul2021 = 0 
total_aug2021 = 0 
total_sep2021 = 0 
total_oct2021 = 0 
total_nov2021 = 0 
total_dec2021 = 0
total_dec2020 = 0 

#Total Cases Annual by Month





date = 'start loop' #loop starter 
while  date != '01 Dec 2020': #loop for months
    date_start_index = table.find("tarih") + len("tarih") + 3
    date_end_index = table.find("gunluk_test") - 3
    date = table[date_start_index : date_end_index]
    date_list.append(date)
    daily_case_start_index = table.find("gunluk_vaka") + len("gunluk_vaka") + 3
    daily_case_end_index = table.find("gunluk_hasta") - 3
    daily_case = int(table[daily_case_start_index : daily_case_end_index])
    daily_case_list.append(daily_case)
    table = table.replace('tarih' , '' , 1)
    table = table.replace('gunluk_test' , '' , 1)
    table = table.replace('gunluk_vaka' , '' , 1)
    table = table.replace('gunluk_hasta' , '' , 1)
    if date_2022 in date:
        if date_jan in date:
            date_list_January2022.append(date)
            daily_list_January2022.append(daily_case)
            dic_jan2022 = dict(zip(date_list_January2022,daily_list_January2022))
            total_jan2022 += daily_case
        elif date_feb in date:
            date_list_February2022.append(date)
            daily_list_February2022.append(daily_case)
            dic_feb2022 = dict(zip(date_list_February2022,daily_list_February2022))
            total_feb2022 += daily_case
        elif date_mar in date:
            date_list_March2022.append(date)
            daily_list_March2022.append(daily_case)
            dic_mar2022 = dict(zip(date_list_March2022,daily_list_March2022))
            total_mar2022 += daily_case
        elif date_apr in date:
            date_list_April2022.append(date)
            daily_list_April2022.append(daily_case)
            dic_apr2022 = dict(zip(date_list_April2022,daily_list_April2022))
            total_apr2022 += daily_case
        elif date_may in date:
            date_list_May2022.append(date)
            daily_list_May2022.append(daily_case)
            dic_may2022 = dict(zip(date_list_May2022,daily_list_May2022))
            total_may2022 += daily_case
        elif date_jun in date:
            date_list_June2022.append(date)
            daily_list_June2022.append(daily_case)
            dic_jun2022 = dict(zip(date_list_June2022,daily_list_June2022))
            total_jun2022 += daily_case
        elif date_jul in date:
            date_list_July2022.append(date)
            daily_list_July2022.append(daily_case)
            dic_jul2022 = dict(zip(date_list_July2022,daily_list_July2022))
            total_jul2022 += daily_case
        elif date_aug in date:
            date_list_August2022.append(date)
            daily_list_August2022.append(daily_case)
            dic_aug2022 = dict(zip(date_list_August2022,daily_list_August2022))
            total_aug2022 += daily_case
        elif date_sep in date:
            date_list_September2022.append(date)
            daily_list_September2022.append(daily_case)
            dic_sep2022 = dict(zip(date_list_September2022,daily_list_September2022))
            total_sep2022 += daily_case
        elif date_oct in date:
            date_list_October2022.append(date)
            daily_list_October2022.append(daily_case)
            dic_oct2022 = dict(zip(date_list_October2022,daily_list_October2022))
            total_oct2022 += daily_case
        elif date_nov in date:
            date_list_November2022.append(date)
            daily_list_November2022.append(daily_case)
            dic_nov2022 = dict(zip(date_list_November2022,daily_list_November2022))
            total_nov2022 += daily_case
        elif date_dec in date:
            date_list_December2022.append(date)
            daily_list_December2022.append(daily_case)
            dic_dec2022 = dict(zip(date_list_December2022,daily_list_December2022))
            total_dec2022 += daily_case
    if date_2021 in date:
        if date_jan in date:
            date_list_January2021.append(date)
            daily_list_January2021.append(daily_case)
            dic_jan2021 = dict(zip(date_list_January2021,daily_list_January2021))
            total_jan2021 += daily_case
        elif date_feb in date:
            date_list_February2021.append(date)
            daily_list_February2021.append(daily_case)
            dic_feb2021 = dict(zip(date_list_February2021,daily_list_February2021))
            total_feb2021 += daily_case
        elif date_mar in date:
            date_list_March2021.append(date)
            daily_list_March2021.append(daily_case)
            dic_mar2021 = dict(zip(date_list_March2021,daily_list_March2021))
            total_mar2021 += daily_case
        elif date_apr in date:
            date_list_April2021.append(date)
            daily_list_April2021.append(daily_case)
            dic_apr2021 = dict(zip(date_list_April2021,daily_list_April2021))
            total_apr2021 += daily_case
        elif date_may in date:
            date_list_May2021.append(date)
            daily_list_May2021.append(daily_case)
            dic_may2021 = dict(zip(date_list_May2021,daily_list_May2021))
            total_may2021 += daily_case
        elif date_jun in date:
            date_list_June2021.append(date)
            daily_list_June2021.append(daily_case)
            dic_jun2021 = dict(zip(date_list_June2021,daily_list_June2021))
            total_jun2021 += daily_case
        elif date_jul in date:
            date_list_July2021.append(date)
            daily_list_July2021.append(daily_case)
            dic_jul2021 = dict(zip(date_list_July2021,daily_list_July2021))
            total_jul2021 += daily_case
        elif date_aug in date:
            date_list_August2021.append(date)
            daily_list_August2021.append(daily_case)
            dic_aug2021 = dict(zip(date_list_August2021,daily_list_August2021))
            total_aug2021 += daily_case
        elif date_sep in date:
            date_list_September2021.append(date)
            daily_list_September2021.append(daily_case)
            dic_sep2021 = dict(zip(date_list_September2021,daily_list_September2021))
            total_sep2021 += daily_case
        elif date_oct in date:
            date_list_October2021.append(date)
            daily_list_October2021.append(daily_case)
            dic_oct2021 = dict(zip(date_list_October2021,daily_list_October2021))
            total_oct2021 += daily_case
        elif date_nov in date:
            date_list_November2021.append(date)
            daily_list_November2021.append(daily_case)
            dic_nov2021 = dict(zip(date_list_November2021,daily_list_November2021))
            total_nov2021 += daily_case
        elif date_dec in date:
            date_list_December2021.append(date)
            daily_list_December2021.append(daily_case)
            dic_dec2021 = dict(zip(date_list_December2021,daily_list_December2021))
            total_dec2021 += daily_case
    if date_2020 in date:
        if date_dec in date:
            date_list_December2020.append(date)
            daily_list_December2020.append(daily_case)
            dic_dec2020 = dict(zip(date_list_December2020,daily_list_December2020))
            total_dec2020 += daily_case        



dic = dict(zip(date_list,daily_case_list))

daily_case_list_reversed = []
daily_case_list_reversed = daily_case_list
daily_case_list_reversed.reverse()#haftalık vakalar için ters çevirdim





#print(total_dec2020)#bir aydaki toplam vaka sayısı
#print(dic_dec2020)#bir aydaki günler ve o günlere karşılık gelen vaka sayıları
#print(daily_list_December2020)#bir aydaki vaka sayıları(ayın son gününden ilk gününe doğru)
#print(date_list_December2020)#bir aydaki günler(ayın son gününden ilk gününe doğru)
#print(dic)#tüm günler ve o günlere karşılık gelen vaka sayıları
#print(date_list)#tüm günler(sondan başa doğru)
#print(daily_case_list)#tüm vaka sayıları(sondan başa doğru)



weeks2021 = [] #2021 deki haftalar
weeks2022 = [] #2022 deki haftalar
weekly_dates = [] #haftalarin tarih araliklari
weekly_case_list = [] 
weekly_case_list0 = [] # son 21 hafta
dic_2021_weekly = dict()
dic_2022_weekly = dict()



table_start_index = html.find("var haftalikdurumjson =") + len("var haftalikdurumjson =")
table_end_index = html.find("}];//]]>")
table = html[table_start_index : table_end_index]
table = table.replace('.' , '')

while  date != '30 Mayıs - 05 Haziran 2022': #loop for weeks
    date_start_index = table.find("tarih") + len("tarih") + 3
    date_end_index = table.find("test_sayisi") - 3
    
    date = table[date_start_index : date_end_index]
    
    weekly_dates.append(date)
    weekly_case_start_index = table.find("\"vaka_sayisi\"") + len("\"vaka_sayisi\"") + 2
    weekly_case_end_index = table.find("\"hasta_sayisi\"") - 2
    weekly_case = int(table[weekly_case_start_index :  weekly_case_end_index])
    weekly_case_list0.append(weekly_case)
    table = table.replace('tarih' , '' , 1)
    table = table.replace('test_sayisi' , '' , 1)
    table = table.replace('\"vaka_sayisi\"' , '' , 1)
    table = table.replace('\"hasta_sayisi\"' , '' , 1)

weekly_case_list0.reverse() #son 21 haftayı ters cevirdik.
weekly_case_list.extend(weekly_case_list0) # listeleri birlestirdik 74 + 21





for i in range(31,len(daily_case_list_reversed), 7):
    weekly_case_list.append(sum(daily_case_list_reversed[i : i+7])) #30Aralik 2020'yi almadan toplam 74 hafta

for i in range(95):
    if i<52:
        weeks2021.append(str(i+1) + ". week")
    else:
        weeks2022.append(str(i-51) +". week")

total_2021 = [total_jan2021, total_feb2021, total_mar2021, total_apr2021, total_may2021, total_jun2021, total_jul2021, total_aug2021, total_sep2021, total_oct2021,total_nov2021,total_dec2021]
months = ['jan' ,'feb','mar','apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct','nov', 'dec']

total_2022 = [total_jan2021, total_feb2021, total_mar2021, total_apr2021, total_may2021]
months_ = ['jan' ,'feb','mar','apr', 'may']

dic_2021_weekly = dict(zip(weeks2021, weekly_case_list[:52]))
dic_2022_weekly = dict(zip(weeks2022, weekly_case_list[52:]))


date_list.reverse()


# 1. week
#        [{"tarih":"31 Ekim - 13 Kasım 2022","test_sayisi":""
#       "vaka_sayisi":"28.808","hasta_sayisi":"" 
    
     
class MatplotlibWidget(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui",self)

        self.setWindowTitle("PyQt5 & Matplotlib Homework GUI")   # give name GUI window

        self.pushButton_2021_generate_daily.clicked.connect(self.update_graph_2021_daily) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.

        self.pushButton_2021_generate_weekly.clicked.connect(self.update_graph_2021_weekly) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.
        
        self.pushButton_2021_generate_montly.clicked.connect(self.update_graph_2021_monthly) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.
        
        self.pushButton_2022_generate_daily.clicked.connect(self.update_graph_2022_daily) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.

        self.pushButton_2022_generate_weekly.clicked.connect(self.update_graph_2022_weekly) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.
        
        self.pushButton_2022_generate_monthly.clicked.connect(self.update_graph_2022_monthly) # connect the update_graph function (slot) to the clicked signal of the button we defined in Qt Designer.
        
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph_2021_daily(self):
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(date_list[31:396],daily_case_list[31:396])
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Daily in Turkey')
        self.MplWidget.canvas.draw()
        
        
    def update_graph_2021_weekly(self):
        
      

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(weeks2021,weekly_case_list[:52])
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Weekly in Turkey')
        self.MplWidget.canvas.draw()
     
    def update_graph_2021_monthly(self):
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(months,total_2021)
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Monthly in Turkey')
        self.MplWidget.canvas.draw()
    
    def update_graph_2022_daily(self):
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(date_list[397:547],daily_case_list[397:547])
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Daily in Turkey')
        self.MplWidget.canvas.draw()
        
        
    def update_graph_2022_weekly(self):
        
      

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(weeks2022,weekly_case_list[53:96])
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Weekly in Turkey')
        self.MplWidget.canvas.draw()
     
    def update_graph_2022_monthly(self):
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(months_,total_2022)
        self.MplWidget.canvas.axes.set_title('Total Coronavirus Cases Monthly in Turkey')
        self.MplWidget.canvas.draw()

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
