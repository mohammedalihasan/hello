# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import arcpy
arcpy.env.workspace = "F:/layer"
fc="asd.shp"

def button_callback():
    arcpy.MakeFeatureLayer_management(fc,"table_output")
    query1 = " Data__Land LIKE 'سكني'"
    H1=arcpy.SelectLayerByAttribute_management("table_output", "NEW_SELECTION",query1)
    total=arcpy.GetCount_management(H1)
    tot=float(total.getOutput(0))
    print ("total number is"+str(tot))

    query2 = " area >=120 AND area <=4200 "+" AND Data__Land LIKE 'سكني'"
    H2=arcpy.SelectLayerByAttribute_management("table_output", "NEW_SELECTION",query2)
    C=arcpy.GetCount_management(H2)
    selected_numbers=float(C.getOutput(0))
    print(selected_numbers)
    n=float(selected_numbers/tot)
    print(int(n*100))
    tkMessageBox.showinfo( "Message Box name", str(int(n*100))+"%")


def start_prog():
    
    window = Tkinter.Tk()

    ##Creates the window from the imported Tkinter module
    window.geometry("600x400")
    ##Creates the size of the window
    window.title("Test :)")

    B = Tkinter.Button(window, text ="Hello", command = button_callback)

    B.pack()
    window.mainloop()


start_prog()


    
