import xlsxwriter
import datetimer

max_col = 6

"""
Create excel file with array data
Analize column 'Fecha'date value
if date value has more than 7 days make red the cell
"""

#Pass arr as raw data and name of the file, also some extra data.
def createExcel(arr, name, surplusUSD):
  
    #Define columns
    columns = ["Legajo", "Part number", "Part name", "Cantidad", "Fecha", "Cost $USD"]
    
    #Define filename
    fileName ='excel/'+name+'.xlsx' 

    
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet('Surplus')
    worksheet.set_column('A:F', 20) 
    rows_str = str(len(arr)+1)
    
    # Create a list of column headers, to use in add_table().
    column_settings = [{'header': column} for column in columns]

    
    # Add a table to the worksheet.
    worksheet.add_table('A1:F' + rows_str, {'data': arr, 'columns': column_settings})
    

    cell_format_red = workbook.add_format({'bold':True, 'font_color': 'white'})
    cell_format_red.set_bg_color('red')


    
    #i = fila x= current value[array 1d]
    for i, x in enumerate(arr):     
        #print("evaluating: ind(",i,", 4) ", x[4])  
        if datetimer.passedSevenDays(x[4]):    
            #print("writing on : (",i,",4)")        
            worksheet.write(i+1 , 4, x[4], cell_format_red )
            
          

    #adding extra information about surplus
    cell= [(len(arr)+4), 0]
    cell_format = workbook.add_format({'bold':True, 'font_color': 'red', 'font_size':20})
    worksheet.write(cell[0],cell[1], surplusUSD + ' máx tolerable 7 days: $250', cell_format )
    worksheet.set_row(cell[0], 25) 

    worksheet.row_col_headers
    


    #workbook.set_custom_property('Date completed',   date.today)
    workbook.read_only_recommended()
    workbook.close()
   
    
   
