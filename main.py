import dearpygui.dearpygui as dpg
import numpy as np

dpg.create_context()

def gaussElim(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                #if not null define λ
                lam = a [i,k]/a[k,k]
                #we calculate the new row of the matrix
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                #we update vector b
                b[i] = b[i] - lam*b[k]
                # backward substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b

def call_back_data() :
    matrik_1 = dpg.get_value("matrik_1")
    matrik_2 = dpg.get_value("matrik_2")
    matrik_3 = dpg.get_value("matrik_3")
    koefisien_1 =  dpg.get_value("koefisien_1")
    koefisien_2 =  dpg.get_value("koefisien_2")
    koefisien_3 =  dpg.get_value("koefisien_3")

    a = np.array([[matrik_1],[matrik_2],[matrik_3]])
    convert_a = [[float(x) for x in row[0].split(',')] for row in a]
    convert_matrik = np.array(convert_a)
    b = np.array([ koefisien_1, koefisien_2, koefisien_3 ])
    
    result = gaussElim(convert_matrik, b)

    print(convert_matrik)
    print(result)
    # print(result)
    with dpg.window(label="hasil Gauss"): 
        dpg.add_text(convert_matrik)    
        dpg.add_text(result)
        for i in range(len(result)):
            dpg.add_text(f"x{i+1} = {round(result[i])}")

def call_back_data_jordan() :
    matrik_jordan_1 = dpg.get_value("matrik_jordan_1")
    matrik_jordan_2 = dpg.get_value("matrik_jordan_2")
    matrik_jordan_3 = dpg.get_value("matrik_jordan_3")
    koefision_jordan_1 =  dpg.get_value("koefision_jordan_1")
    koefision_jordan_2 =  dpg.get_value("koefision_jordan_2")
    koefision_jordan_3 =  dpg.get_value("koefision_jordan_3")

    a = np.array([[matrik_jordan_1],[matrik_jordan_2],[matrik_jordan_3]])
    convert_a = [[float(x) for x in row[0].split(',')] for row in a]
    convert_matrik_jordan = np.array(convert_a)
    b = np.array([ koefision_jordan_1, koefision_jordan_2, koefision_jordan_3 ])
    
    result = gaussElim(convert_matrik_jordan, b)

    print(result)
    # print(result)
    with dpg.window(label="Hasil Gauss Jordan"): 
        dpg.add_text(convert_matrik_jordan)    
        dpg.add_text(result)
        for i in range(len(result)):
            dpg.add_text(f"x{i+1} = {round(result[i])}")

with dpg.window(label="Gauss", width=400, height=300):

    with dpg.table(resizable=True, policy=dpg.mvTable_SizingStretchProp):
        dpg.add_table_column(label = "Header 1")
        dpg.add_table_column(label = "Header 2")

        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_1", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefisien_1", width=100)
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_2", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefisien_2", width=100)
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_3", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefisien_3", width=100)
        
    dpg.add_button(label="Hitung", callback=call_back_data)

with dpg.window(label="Gauss Jordan", width=400, height=300):

    with dpg.table(resizable=True, policy=dpg.mvTable_SizingStretchProp):
        dpg.add_table_column(label = "Header 1")
        dpg.add_table_column(label = "Header 2")

        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_jordan_1", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefision_jordan_1", width=100)
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_jordan_2", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefision_jordan_2", width=100)
        with dpg.table_row():
            with dpg.table_cell():
                dpg.add_input_text(tag = "matrik_jordan_3", width=260)
            with dpg.table_cell():
                dpg.add_input_float(tag = "koefision_jordan_3", width=100)
        
    dpg.add_button(label="Hitung", callback=call_back_data_jordan)
    
    
dpg.create_viewport(title='Persamaan Linier Gauss & Gauss Jordan', width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()