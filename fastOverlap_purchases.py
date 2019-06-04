# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:28:56 2019

@author: Milan Dean
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

class ShopifyPurchaseOverlap(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Shopify Purchase Behavior')
        self.geometry('800x800')
        self.resizable(width=False, height=False)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Developing the dictionary that will contain future pages.
        self.frames = {}

        for F in (StartPage, PurchaseAnalysis):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    #Method used to raise each page to the front of the Frame.
    def show_frame(self, container):

        frame = self.frames[container]
        frame.tkraise()
  
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Welcome to the Monkedia Purchase Behavior Application!", font=('Verdana', 16))
        label.place(x=115, y=150)

        button = ttk.Button(self, text="Purchase Analysis",
                            command=lambda: controller.show_frame(PurchaseAnalysis))
        button.config(width=30)
        button.place(x=300, y=350)

class PurchaseAnalysis(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text="Purchase Analysis", font=('Verdana', 20))
        label1.place(x=275, y=150)

        button1 = ttk.Button(self, text="Back to Home", 
                             command=lambda: [controller.show_frame(StartPage), self.clear()])
        
        button1.place(x=20, y=750)
        
        button3 = ttk.Button(self, text='Browse First File', command=self.askopenfile_one)
        button3.config(width=30)
        button3.place(x=20, y=350)
        
        file_one_label = ttk.Entry(self, text='')
        file_one_label.config(width=50)
        
        button4 = ttk.Button(self, text='Browse Second File', command=self.askopenfile_two)
        button4.config(width=30)
        button4.place(x=20, y=400)
        
        button5 = ttk.Button(self, text='Calculate', command=self.cronch)
        button5.config(width=30)
        button5.place(x=300, y=600)
        
    def askopenfile_one(self):
        #Simply opens either a CSV or Excel file in the users directory and assigns to a variable.
        
        self.file = filedialog.askopenfilename(title = "Select file", 
                                               filetypes = (("CSV Files","*.csv"),("Excel Files", "*.xlsx")))
        
        #Creating label that shows the path directory and name of first file, so user knows file was imported.
        self.fileOne_label = ttk.Entry(self, text='')
        self.fileOne_label.config(width=50)
        self.fileOne_label.place(x=250, y=351)
        self.fileOne_label.delete(0, 'end')
        self.fileOne_label.insert(0, self.file)
        self.fileOne_label.config(state='disabled')
        
        if self.file:
            try:
                self.df_one = pd.read_csv(self.file)
            except:
                self.df_one = pd.read_excel(self.file)
                
    def askopenfile_two(self):
        #Simply opens either a CSV or Excel file in the users directory and assigns to a variable.
        
        self.file_two = filedialog.askopenfilename(title = "Select file", 
                                                   filetypes = (("CSV Files","*.csv"),("Excel Files", "*.xlsx")))
        
        #Creating label that shows the path directory and name of second file, so user knows file was imported.
        self.fileTwo_label = ttk.Entry(self, text='')
        self.fileTwo_label.config(width=50)
        self.fileTwo_label.place(x=250, y=401)
        self.fileTwo_label.delete(0, 'end')
        self.fileTwo_label.insert(0, self.file_two)
        self.fileTwo_label.config(state='disabled')
        
        if self.file_two:
            try:
                self.df_two = pd.read_csv(self.file_two)
            except:
                self.df_two = pd.read_excel(self.file)
                                   
    def cronch(self):
        """Function that creates a hashset in order to compare customer IDs in O(N) time, and assign that
        value to a variable, stored in a label."""
        
        try:
            set_df1 = set((self.df_one['customer_id']))
            set_df2 = set((self.df_two['customer_id']))
            
            result = set_df1.intersection(set_df2)
            percent = str((round((len(result)/len(self.df_one['customer_id']))*100, 2)))
            ans = 'Resulting purchase overlap: ' + percent + '%'
            
            self.resultLabel = ttk.Label(text=ans, font=('Calibri', 14))
            self.resultLabel.config(width=50)
            self.resultLabel.place(x=270, y=645)

        except:
            ans = 'Error: Please make sure correct files are properly formatted.'
            
            self.resultLabel = ttk.Label(text=ans, font=('Calibri', 14))
            self.resultLabel.config(width=50)
            self.resultLabel.place(x=175, y=645)
            self.resultLabel.after(2000, lambda: self.resultLabel.destroy())
            
    def clear(self):
        #Ensures the result is destroyed when called - used on button click before changing frames.
        self.resultLabel.destroy()
        
        
    def basket_askopenfile(self):
    #Simply opens either a CSV or Excel file in the users directory and assigns to a variable.
    
        self.file = filedialog.askopenfilename(title = "Select file", 
                                               filetypes = (("CSV Files","*.csv"),("Excel Files", "*.xlsx")))
        
        #Creating label that shows the path directory and name of first file, so user knows file was imported.
        self.fileOne_label = ttk.Entry(self, text='')
        self.fileOne_label.config(width=50)
        self.fileOne_label.place(x=240, y=400)
        self.fileOne_label.delete(0, 'end')
        self.fileOne_label.insert(0, self.file)
        self.fileOne_label.config(state='disabled')
        
        if self.file:
            try:
                self.df_one = pd.read_csv(self.file)
            except:
                self.df_one = pd.read_excel(self.file)

if __name__ == "__main__":
    
    app = ShopifyPurchaseOverlap()
    app.mainloop()
