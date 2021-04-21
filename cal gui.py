from tkinter import *
from tkinter import ttk
import calendar

class Cal_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("My Calendar")
        self.root.geometry("600x300+300+100")
        self.root.config(bg="black")

        title=Label(self.root,text='Calendar'.upper(),bd=10,relief=GROOVE,font=("times new roman",20,'bold'),bg="#073475",fg="white")
        title.pack(side=TOP,fill=X)

        #==========Variable==============
        self.month_var = StringVar()
        self.year_var = StringVar()
        self.text = "" 
        self.sp = 6

        #==========Input Frame===========
        input_frame = Frame(self.root,bd=4,relief=RIDGE,bg='#074033')
        input_frame.place(x=5,y=60,width=200,height=235)


        month_lbl =  Label(input_frame,text="Select Month",bg='#074033',fg="white",font=("times new roman ",14,"bold"))
        month_lbl.grid(row=0,column=0,pady=10,padx=22,sticky='w')
        combo_month = ttk.Combobox(input_frame,width=15,font=("times new roman",12,'bold'),textvariable=self.month_var,state="readonly")
        combo_month['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        combo_month.grid(row=1,column=0,pady=5,padx=22,sticky='w')

        year_lbl =  Label(input_frame,text="Select Year",bg='#074033',fg="white",font=("times new roman ",14,"bold"))
        year_lbl.grid(row=2,column=0,pady=10,padx=22,sticky='w')
        combo_year = ttk.Combobox(input_frame,width=15,font=("times new roman",12,'bold'),textvariable=self.year_var,state="readonly")
        combo_year['values']=[str(i) for i in range(1900,2101)]
        combo_year.grid(row=3,column=0,pady=5,padx=22,sticky='w')

        show_btn = Button(input_frame,text="Show",width=5,bg="yellow",command=self.show).grid(row=4,column=0,padx=16,pady=10)

        #===========Calendar Frame=======
        cal_frame = Frame(self.root,bd=4,relief=RIDGE,bg='#074093')
        cal_frame.place(x=210,y=60,width=385,height=235)

        cal_title = Label(cal_frame,text="Show Calendar",font="arial 15 bold",bd=7,relief=GROOVE,bg='#074033',fg="white").pack(fill=X)
        scrol_y = Scrollbar(cal_frame,orient=VERTICAL)
        self.textarea = Text(cal_frame,yscrollcommand=scrol_y.set,state="normal",font="12")
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        self.month_var.set('May')
        self.year_var.set('2020')
        self.show()
    
    def _month_cal(self,year,month):
        self.cal = calendar.monthcalendar(year,month)
        self.text = ""
        for i in self.cal:
            for j in i:
                if j!=0:
                    if j<10:
                        self.text += "  "+str(j)+" "*self.sp
                    else:
                        self.text += str(j)+" "*self.sp
                else:
                    self.text += "    "+" "*self.sp
            self.text += "\n"
        return self.text

    def _print_mid(self,txt,length):
        l = length - len(str(txt))
        l2 = l//2
        text = " "*(l-l2+5)+str(txt)+" "*l2
        return text

    def show(self):
        self.textarea.delete('1.0',END)
        year = int(self.year_var.get())
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        months_index = [i for i in range(1,13)]
        weeks = ['Monday','Tuesday', 'wednesday','Thursday','Friday','Saturday','Sunday']
        weeks_index = [i for i in range(0,7)]
        weeks_dict = dict(zip(weeks_index,weeks))
        months_dict = dict(zip(months,months_index))
        month = int(months_dict[self.month_var.get()])
        self.week = (" "*self.sp).join('Mo Tu We Th Fr Sa Su'.split())
        self.textarea.insert(END,self._print_mid(self.month_var.get()+" "+self.year_var.get(),len(self.week))+"\n")
        self.textarea.insert(END,self.week+"\n")
        text = self._month_cal(year,month)
        self.textarea.insert(END,text)
        today = calendar.datetime.datetime.weekday(calendar.datetime.date(int(calendar.datetime.datetime.now().strftime("%y")),int(calendar.datetime.datetime.now().strftime("%m")),int(calendar.datetime.datetime.now().strftime("%d"))))
        today_name = weeks_dict[today]
        self.textarea.insert(END,"="*26)
        self.textarea.insert(END,"\nToday : "+calendar.datetime.datetime.now().strftime("%d-%m-%y")+", "+today_name)

        


if __name__ == "__main__":
    root = Tk()
    ob=Cal_gui(root)
    root.mainloop()