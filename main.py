import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import Tk
import pandas as pd



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.geometry("900x900")  # set the root dimensions
        self.title("Convert svg to png")
        # tells the root to not let the widgets inside it determine its size.
        self.pack_propagate(False)
        self.resizable(0, 0)  # makes the root window fixed in size.

        self.file_frame = tk.LabelFrame(self, text="Open File")

        self.file_frame.place(height=180, width=900)
                # Buttons
        self.label_email =tk.Label(self.file_frame,text="Email")
        self.label_email.place(rely=0.25, relx=0.1,height=30)

        self.email_entry= tk.Entry(self.file_frame)
        self.email_entry.place(rely=0.25, relx=0.2,height=30,width=160)

        self.label_password =tk.Label(self.file_frame,text="Password")
        self.label_password.place(rely=0.60, relx=0.1,height=30)

        self.password_entry= tk.Entry(self.file_frame)
        self.password_entry.place(rely=0.60, relx=0.2,height=30,width=160)
        self.button1 = tk.Button(
            self.file_frame, text="Import CSV File",command=lambda: self.File_dialog())
        self.button1.place(rely=0.85, relx=0.50)

        self.button2 = tk.Button(
            self.file_frame, text="Start", command=lambda: self.start_func())
        self.button2.place(rely=0.85, relx=0.30)
        #Result
        self.Result_button =tk.Button(self.file_frame,text="Result",command=lambda: self.result_func())
        self.Result_button.place(rely=0.85, relx=0.80)

        # Total per day
        self.label_Total_per_day =tk.Label(self.file_frame,text="Total per day")
        self.label_Total_per_day.place(rely=0.0, relx=0.70,height=30) 
        self.Total_per_day_entry= tk.Entry(self.file_frame)
        self.Total_per_day_entry.place(rely=0.0, relx=0.8,width=160,height=30)
        #Time between
        self.label_Time_between =tk.Label(self.file_frame,text="Time between")
        self.label_Time_between.place(rely=0.3, relx=0.70,height=30) 
        self.Time_between_entry= tk.Entry(self.file_frame)
        self.Time_between_entry.place(rely=0.3, relx=0.8,width=160,height=30)
       
       #Start at
        self.label_Start_at =tk.Label(self.file_frame,text="Start at")
        self.label_Start_at.place(rely=0.6, relx=0.70,height=30) 
        self.Start_at_entry= tk.Entry(self.file_frame)
        self.Start_at_entry.place(rely=0.6, relx=0.8,width=160,height=30)     


        # The file/file path text
        self.label_file = ttk.Label(self.file_frame, text="No File Selected")
        self.label_file.place(rely=0, relx=0)
    #     # Frame for TreeView
        self.frame1 = tk.LabelFrame(self)
        self.frame1.place(height=650, width=680, rely=0.20, relx=0)

    #     # Frame for open file dialog
        self.frame2 = tk.LabelFrame(self)
        self.frame2.place(height=650, width=220, rely=0.20, relx=0.75)

        self.tv2 = ttk.Treeview(self.frame2)
    #     # set the height and width of the widget to 100% of its container (frame1).
        self.tv2.place(relheight=1, relwidth=1)

        # command means update the yaxis view of the widget
        self.treescroll1y = tk.Scrollbar(
            self.frame2, orient="vertical", command=self.tv2.yview)
        # command means update the xaxis view of the widget
        self.treescroll1x = tk.Scrollbar(
            self.frame2, orient="horizontal", command=self.tv2.xview)
        # assign the scrollbars to the Treeview Widget
        self.tv2.configure(xscrollcommand=self.treescroll1x.set,
                           yscrollcommand=self.treescroll1y.set)
        # make the scrollbar 
        self.treescroll1x.pack(side="bottom", fill="x")
        # make the scrollbar 
        self.treescroll1y.pack(side="right", fill="y")



    #     # Treeview Widget
        self.tv1 = ttk.Treeview(self.frame1)
        # set the height and width of the widget to 100% of its container (frame1).
        self.tv1.place(relheight=1, relwidth=1)
        self.tv1["column"] = ["title","image_url","link","description"]
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            # let the column heading = column name
            self.tv1.heading(column, text=column)
        self.tv1.bind("<Double-1>", self.OnDoubleClick)

        # command means update the yaxis view of the widget
        self.treescrolly = tk.Scrollbar(
            self.frame1, orient="vertical", command=self.tv1.yview)
        # command means update the xaxis view of the widget
        self.treescrollx = tk.Scrollbar(
            self.frame1, orient="horizontal", command=self.tv1.xview)
    #     # assign the scrollbars to the Treeview Widget
        self.tv1.configure(xscrollcommand=self.treescrollx.set,
                           yscrollcommand=self.treescrolly.set)
    #     # make the scrollbar fill the x axis of the Treeview widget
        self.treescrollx.pack(side="bottom", fill="x")
    #     # make the scrollbar fill the y axis of the Treeview widget
        self.treescrolly.pack(side="right", fill="y")

    def result_func(self):
        print("--------result-------------")

    def start_func(self):
        print("--------start-------------")

    def File_dialog(self):
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("csv files", "*.csv"), ("All Files", "*.*")))
        self.label_file["text"] = filename
        self.Load_excel_data()
        return None

    def Load_excel_data(self):
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = self.label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)
            df = df[["title","image_url","link","description"]]
        except KeyError:
            tk.messagebox.showerror(
                "Information", "The format file you have chosen is invalid")
            return None
        except ValueError:
            tk.messagebox.showerror(
                "Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror(
                "Information", f"No such file as {file_path}")
            return None
        
        self.clear_data()


        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.tv1.insert("", "end", values=row)
        return None
    def OnDoubleClick(self, event):
        item_1 = self.tv1.selection()[0]
        # for i in item:

        tk.messagebox.showinfo(title='info',message=str(self.tv1.item(item_1,"values")[0]))
        # print("you clicked on", self.tv1.item(item_1,"values")[0])
    def clear_data(self):
        self.tv1.delete(*self.tv1.get_children())
        return None


root = Root()
root.mainloop()
