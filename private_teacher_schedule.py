# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:15:43 2019

@author: Suat
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:06:52 2019

@author: Suat
"""

import calendar
import datetime
import sys
import sqlite3 as sq #For tables and database

con = sq.connect('Gym.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called

if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk


 
class Calendar:
    def __init__(self, parent, values):
        self.values = values
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        actualday = datetime.date.today().day
        self.wid = []
        self.day_selected = actualday
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''
         
        self.setup(self.year, self.month)
         
    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            #w.destroy()
            self.wid.remove(w)
     
    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)
 
    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1
         
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)
        
         
    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name
         
        #data
        self.values['day_selected'] = day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]
         
        self.clear()
        self.setup(self.year, self.month)
         
    def setup(self, y, m):
        left = tk.Button(self.parent, text='<', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=1)
         
        header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)
         
        right = tk.Button(self.parent, text='>', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5)
         
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num)
         
        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    #print(calendar.day_name[day])
                    b = tk.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
#                    b = tk.Button(self.parent, width=1, text=day)
                    #bu butona basıldıgında giris ekranları acılsın
                    self.wid.append(b)
                    b.grid(row=w, column=d)
                     
        sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)
         
        ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)
         
    def kill_and_save(self):
        self.parent.destroy()
 
 
if __name__ == '__main__':
 
    class Control:
        def __init__(self, parent):
            self.parent = parent
            self.choose_btn = tk.Button(self.parent, text='Choose')
#            self.choose_btn = tk.Button(self.parent, text='Choose',command=self.popup)
            self.show_btn = tk.Button(self.parent, text='Show Selected')
            self.choose_btn.grid(row=9, column=0)
            self.show_btn.grid(row=9, column=10)
            
            self.data = {}
#            child = tk.Toplevel()
            cal = Calendar(parent, self.data)
#        def popup(self):
#            child = tk.Toplevel()
#            cal = Calendar(child, self.data)
             
            self.price = tk.StringVar(self.parent)
            self.houR = tk.StringVar(self.parent)


            #Entry for 'input' in GUI
            self.ucreT = tk.Entry(self.parent, textvariable=self.price)
            self.ucreT.grid(row=8,column=9)

            #Entry for 'input' in GUI
            self.saaT = tk.Entry(self.parent, textvariable=self.houR)
            self.saaT.grid(row=8,column=10)
            
            #Labels for entries
            self.L1 = tk.Label(self.parent, text = "Price", font=("arial", 14))
            self.L2 = tk.Label(self.parent, text = "Hour", font=("arial",14))
            self.L1.grid(row=7, column=9)
            self.L2.grid(row=7, column=10)
            
            #delete later this is trial for accessing date
            self.L3 = tk.Label(self.parent, text='{}'.format(cal.day_selected), font=("arial",14))
            self.L3.grid(row=15, column=15)
            print(cal.day_selected)
        #absorb func to isolate the text entered in the entry boxes and submit to database
        def absorb():
                print("You have submitted a record")
                
                c.execute('CREATE TABLE IF NOT EXISTS ' +comp.get()+ ' (Datestamp TEXT, MaxWeight INTEGER, Reps INTEGER)') #SQL syntax
                
                date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #Date in format from 'import datetime'
        
                c.execute('INSERT INTO ' +comp.get()+ ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',
                          (date, weight.get(), reps.get())) #Insert record into database.
                con.commit()
        
        
        def print_selected_date(self):
            print(self.data)
             
 
    root = tk.Tk()
    root.title("Hi")
    app = Control(root)
    root.mainloop()