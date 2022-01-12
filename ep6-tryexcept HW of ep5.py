#ep5 การบ้าน

#เฉลยการบ้าน EP.5
#สร้างแท็บแสดงผลจาก csv 
#ใส่ตาราง Treeview สำหรับแสดงผล

#messagebox เป็นการเด้งกล่อง popup ออกมา 

from tkinter import *
from tkinter import ttk, messagebox
import csv
#บันทึกเวลาตอนตอนเซฟด้วย โดยจาก datetime ให้ import datetime
from datetime import datetime

#ทำการ import csv เข้ามาเพื่อบันทึกข้อมูล
# ttk is theme of Tk (เป็นการทำให้สวยขึ้น)
GUI = Tk()
#ใส่ชื่อโปรแกรม
GUI.title('โปรแกรมบันทึกค่าใช้จ่ายและคำนวณค่าใช้จาย by bLalita')
GUI.geometry('600x650+20+20')

###################สร้าง menu bar ####################
#Menu()มาจาก import *
menubar = Menu(GUI) #สร้างmenuหลักที่ชื่อว่าmenubar
GUI.config(menu=menubar) #GUI.config()คำสั่งให้menuนี้ไปติดกับGUIหลัก
#ให้มีmenuเท่ากับmenubar Tabด้านบนคือmenubarให้โปรแกรมของเรา

#สร้าง add menu ลงไปเบนmenubar
#เพิ่ม File menu
#คำสั่ง tearoff=0 คือเพื่อไม่อยากให้ดึงคำสั่งออกมาหน้าต่างใหม่
filemenu = Menu(menubar,tearoff=0) #สร้าง filemanu เป็น object มาชุดหนี่ง เป็นก้อนสี่เหลี่ยม
menubar.add_cascade(label='File',menu=filemenu) #เราจะเอาตัวใน menubar จะทำการ add_cascade คือ add ตัว filemenu ที่เป็นobjectเข้าไปโดยใส่ชื่อ label ให้ว่าชื่อ File
#การ add command(คำสั่ง) ใน File menu
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

#เพิ่ม Help menu
#สร้างฟังก์ชั้น Help
def About():
	messagebox.showinfo('About','สวัสดีค่ะ โปรแกรมนี้เป็นโปรแกรมที่ช่วยบันทึกข้อมูลค่าใช้จ่าย\nหากใครสนใจบริจาคให้เพื่อนำไปพัฒนาโปรแกรมต่อ\nสามารถโอนมาได้ทาง เลขที่บัญชี:72002930300039 Kbank ')

helpmenu = Menu(menubar,tearoff=0) #สร้าง Helpmanu เป็น object มาชุดหนี่ง เป็นก้อนสี่เหลี่ยม
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)


#เพิ่ม Donate menu
donatemenu = Menu(menubar,tearoff=0) #สร้าง Helpmanu เป็น object มาชุดหนี่ง เป็นก้อนสี่เหลี่ยม
menubar.add_cascade(label='Donate',menu=donatemenu)



####################################################
#notebookมาจากตัว ttk 
#สร้าง Tab เอาNotebookไปใส่ในGUI
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.pack(fill=BOTH,expand=1)

#ใส่รูป icon บน Tab
#หาจาก https://iconarchive.com/?fbclid=IwAR0h7q5NTyMReN4iwUX4ggSu9fvh6H5RPBCrXuiez1lrcOvKKIb1mDX4Ah0
#เลือกโหลด 24 pixel
icon_t1 = PhotoImage(file='T1_wallet.png')  #.subsample(2) ใช้ย่อรูปภาพ ไม่แนะนำ ความใช้รูปภาพเต็ม
icon_t2 = PhotoImage(file='T2_list.png')

#วิธีแก้ขนาด Tab ให้เท่ากันทั้งข้อความที่สั้นและยาว
#จะใช้วิธี f-string (formatของstring) 
# {30} ตัวคอนโทลตัว space ว่าให้มีความยาวเท่าไหร่
#เครื่องหมายยกกำลัง '^' ทำให้ข้อความอยู่ที่ center


Tab.add(T1, text=f'{"ค่าใช้จ่าย": ^{30}}',image=icon_t1,compound='top') #compund เป็นการ control รูปภาพว่าอยากให้อยู่ด้านซ้ายleft ขวาright บนtop ล่างdown
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด": ^{30}}',image=icon_t2,compound='top')


#ย้าย F1 ไปใน T1
F1 = Frame(T1)
#F1.place(x=100,y=50)
#ไม่ขยายตามหน้าจอ
F1.pack() #ขยายตามหน้าจอแ

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร',
		'Sun':'อาทิตย์'}

def Save(event=None):
	
	expense = v_expense.get()
	#.get()เป็นการดึงมาจาก v_expense = StringVar()
	price = v_price.get()
	#.get()เป็นการดึงมาจาก v_price = StringVar()
	quantity = v_quantity.get()
	#.get()เป็นการดึงมาจาก v_amount = StringVar()
	

	#กรณีแก้ปัญหากรอกข้อมูลไม่ครบ มี 2 แบบ

	#แบบที่ 1
	if expense == '':
		messagebox.showwarning('Error','กรุญากรอกข้อมูลค่าใช้จ่าย')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')		
		return
		#return คือการไม่ทำต่อจบแค่นี้จะทำให้ไม่ saveค่า

	elif price == '':
		messagebox.showwarning('Error','กรุญากรอกราคา')
		return
	elif quantity == '':
		messagebox.showwarning('Error','กรุญากรอกจำนวน')
		return


	#คำสั่ง tryexcept ถ้าerror จะไม่ทำงาน
	#ต้องมีการเตือนว่ากรอกผิด จะใส่ pop up และคำว่า error

	try:
		total = int(price)*int(quantity)
		# total คือ รวมค่าใช้จ่ายทั้งหมด

		#ทำการบันทึกเวลาตอนตอนเซฟ
		dt = datetime.now() # current date and time
		date_time = dt.strftime("%m/%d/%Y, %H:%M:%S")
		today = dt.strftime('%a')
		d_time = days[today]+'-'+date_time

		print('รายการ: {} ราคา: {} บาท จำนวน: {} อัน'.format(expense,price,quantity))
		print('รวมค่าใช้จ่ายทั้งหมด: {} บาท วันและเวลาที่save: {}'.format(total,d_time))

		#ทำการแสดงผลลัพธ์ที่บันทึกไว้ลงข้างล่าง
		#\n ขึ้นบรรทัดใหม่
		text = 'รายการ: {} ราคา: {} บาท จำนวน: {} อัน รวมค่าใช้จ่ายทั้งหมด: {} บาท\n'.format(expense,price,quantity,total)
		text = text + 'วันและเวลาที่save: {}'.format(d_time)

		#ทำการแสดงผลลัพธ์
		v_result.set(text)

		#clear ข้อมูลเก่าจะ ใช้คำสั่ง .set('') เป็นการ set ให้เป็นคำๆนั้น 
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')


		#-------บันทึกข้อมูลลง csv----------

		#การเซฟลง csv แยกฟังก์ชันหรือรวมเลยก็ได้ ที่จะทำคือรวมไปเลย
		#utf-8 คือตัวที่สามารถทำให้พิมพ์ภาษาไทยได้
		with open('savedataHW.csv','a',encoding='utf-8',newline='') as f:
			# with open คือคำสั่งเปิดไฟล์แล้วปิดอัตโนมัติ

			#-------ฟังก์ชันสำหรับเขียน csv----------
			fw = csv.writer(f)# file writter เป็นการสร้างฟังก์ชันสำหรับเขียนข้อมูล
			data = [expense,price,quantity,total,d_time] #ข้อมูลที่ต้องการใส่
			fw.writerow(data) #เอาข้อมูลมาใส่เป็นแถวๆ

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		#เมื่อมีการกด save จะต้องมีการอัพเดตไฟล์ใหม่ด้วย
		update_table()
	except:
		print('ERROR')
		#messagebox มีหลายแบบ แบบที่ 1 คือ showerror() แบบที่ 2 คือ showwarning() แบบที่ 3 showinfo()
		
		#messagebox.showerror('Error','กรุญากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด') #ก่อน ,คือ อยู๋บนหัวกล่องข้อความ หลัง , คืออยู๋ในกล่องข้อความ
		messagebox.showwarning('Error','กรุญากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('Error','กรุญากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')


#วิธีการทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save)

#<Return> คือปุ่ม Enter

#เปลี่ยน font
#เอา ข้อความ ช่องกรอกข้อมูล ปุ่ม ไปใส่ใน F1
FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'


#---------Image-----------
#ใส่รูปภาพ
main_icon = PhotoImage(file='get-money.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack(pady=20)

#-------text1----------

L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
#ทำช่องกรอก
v_expense = StringVar()
#StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#----------------------


#-------text2----------

L = ttk.Label(F1,text='ราคา(บาท)',font=FONT1).pack()
#ทำช่องกรอก
v_price = StringVar()

E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#----------------------


#-------text3----------

L = ttk.Label(F1,text='จำนวน(อัน)',font=FONT1).pack()
#ทำช่องกรอก
v_quantity = StringVar()

E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#----------------------

icon_b1 = PhotoImage(file='b1_save.png')


B1 = ttk.Button(F1,text=f'{"Save": ^{30}}',image=icon_b1,compound='top',command=Save)
B1.pack(ipadx=25,ipady=5,pady=20)
#ipadx และ ipady คือ การขยายภายใน
#pady,padx คือระยะความห่างรอบนอก

v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green') #ถ้าใช้ ttk เปลี่ยนสีจะใช้ foreground
#ถ้าใช้ Label ธรรมดา เปลี่ยนสีจะใช้ fg ตามข้างล่าง
#result = Label(F1, textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=10)

##################TAB2##################

'''	วิธีอ่านไฟล์แบบเก่า ในภาษาอื่น
    f = open('savedataHW.csv',newline='',encoding='utf-8')
	fr = csv.reader(f)
	f.close()'''

#สร้างฟังก์ชันread csv ขึ้นมา 

#ไม่ต้องใส่โหมด'a','w'เพราะใช้กับโหมด writer เท่านั้น ใส่ newline เพราะอาจจะอ่านบรรทัดผิด
#utf-8 สำคัญมาก เพราะภาษาไทยต้องใส่ไม่อย่างนั้นอ่านไม่ได้
#as f คือ as ไฟล์ๆนึงแล้วตั้งค่าเป็นตัวแปร f ประมาณว่าให้เปิดcsvตัวนี้ขึ้นมาแล้วให้ตั้งชื่อเล่นว่าตัว f

#nest list เอาไว้แสดงผลในlistและในindexข้างในอีกที
		# print(data)
		# print(data[0])
		# print('------')
		# print(data[0][4])
		# ลองใช้ for loop ช่วย run
		# เลือกเจาะจงตัวทำได้ 2 แบบ
		# for d in data:
		# 	print(d[0])		
		# for a,b,c,d in data:
		# 	print(d)

#with open เพื่อป้องการลืม close ไฟล์
def read_csv():
	with open('savedataHW.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr) #แปลงให้อ่านออก โดยแปลง fr ให้เป็น list เพื่อให้อ่านออก
	return(data)
	#การส่งต่อใน python เรียกว่าการ return ข้อมูล
	#ต้อง return ค่า ถ้าต้องการนำค่าในlistไปใช้งานต่อ 
		
# การสร้าง table

L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['รายการ','ค่าใช้จ่าย','จำนวน','รวม','วัน-เวลา']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20) #columns=header บอกว่าตัวตารางมี header 5 รายการ show='headings' เป็นตัวทำให้ตารางของเราไม่มีการเป็นข้อย่อยๆลงมา
resulttable.pack()

#ใส่ header แบบใช้มือ ใช้ header[0] reference มากกว่าการเขียนใหม่
# for i in range(len(header)):
# 	resulttable.heading(header[i],text=header[i])

#****แบบไม่ต้องยุ่งยาก**** จำเป็นต้องมี
for h in header:
	resulttable.heading(h,text=h)

#ปรับความกว้างแต่ละ column
#จะทำการใช้ zip คู่กันได้เพื่อให้ header กับ ความกว้าง column มาใช้งานพร้อมกัน
headerwidth = [80,80,80,80,170] #หน่วยpixel
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)


#วิธีการหยอดข้อมูลลงใน table

#แบบธรรมดา
#ดึง resulttable ออกมาก่อน แล้วใส่ค่าลงในตาราง
#value จะเป็นชุดข้อมูลที่มีจำนวนเท่ากับ column
#end ใส่ตัวสุดท้ายล่างสุด , 0 จะใส่ตัวแรก

# resulttable.insert('','end',value=['น้ำ',30,5,150,'จันทร์'])
# resulttable.insert('','end',value=['นม',20,2,40,'อังคาร'])


#แบบใหม่

#วิธีการ insert data
#หลังจาก read จะต้อง update table
def update_table():
	#เมื่อทุกครั้งที่มีการ run ขึ้นมา จะทำการ delete ค่าก่อนที่จะมีการอัพเดต table
	#get_children() คือ รหัสพิเศษที่โปรแกรมตั้งขึ้นมาอัตโนมัติ  
	#แบบ for loop 
	# for c in resulttable.get_children():
	# 	resulttable.delete(c)

	#แบบ * เป็นการทำซ้ำบรรทัดนี้เป็นการสั่ง delete อัตโนมัติ
	resulttable.delete(*resulttable.get_children())
	#ดึง data มาก่อน
	data = read_csv() #เป็น list ซ้อน list
	for d in data:
		resulttable.insert('','0',value=d)
    #เมื่อมีการกด save จะต้องมีการอัพเดตไฟล์ใหม่ด้วย

update_table()



GUI.mainloop()
