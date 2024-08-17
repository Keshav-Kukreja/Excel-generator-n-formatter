import flet as ft
import datetime
import random
import pandas as pd

col_list=["Series","Date", "Master", "Amount", "Item", "Sale Type"]
voucher_list=[]
# style
focused_color=ft.colors.RED
bgcolor="#FF9B50"
btn_color="#E25E3E"
textfield_color="#232D3F"
    
dd = ft.Dropdown(
        label="Tax",
        focused_border_color=focused_color,
        width=100,
        height=45,
        filled=True,
        bgcolor=textfield_color,
        content_padding=0,
        color=ft.colors.RED,
        alignment=ft.alignment.center,
        options=[
            ft.dropdown.Option("3%"),
            ft.dropdown.Option("5%"),
            ft.dropdown.Option("12%"),
            ft.dropdown.Option("18%"),
            ft.dropdown.Option("28%"),
        ],
    )

item_type = ft.Dropdown(
        label="Sale Type",
        focused_border_color=focused_color,
        width=200,
        filled=True,
        bgcolor=textfield_color,
        color=ft.colors.BLUE,
        options=[
            ft.dropdown.Option("L/GST-TaxIncl."),
            ft.dropdown.Option("Local-TaxIncl."),
            ft.dropdown.Option("I/GST-TaxIncl."),
            ft.dropdown.Option("Center-TaxIncl."),
            ft.dropdown.Option("L/GST-ItemWise"),
            ft.dropdown.Option("Local-ItemWise"),
            ft.dropdown.Option("I/GST-ItemWise"),
            ft.dropdown.Option("Center-ItemWise"),
        ],
    )

Date_start= ft.TextField(
        label="DD/MM/YYYY",
        filled=True, 
        bgcolor=textfield_color,
        color=ft.colors.WHITE,
        focused_border_color=focused_color
        )
Date_end= ft.TextField(
        label="DD/MM/YYYY", 
        filled=True, 
        bgcolor=textfield_color,
        color=ft.colors.WHITE,
        focused_border_color=focused_color
        )
    
to=ft.Text("To", color=ft.colors.WHITE)
    
Amt_start= ft.TextField(
        label="Start",
        filled=True, 
        bgcolor=textfield_color,
        color=ft.colors.WHITE,
        focused_border_color=focused_color)
    
Amt_end= ft.TextField(
        label="End",
        filled=True, 
        bgcolor=textfield_color,
        color=ft.colors.WHITE,
        focused_border_color=focused_color)

total_amt = ft.TextField(
        label="Total Amount",
        filled=True, 
        bgcolor=textfield_color,
        color=ft.colors.WHITE,
        focused_border_color=focused_color)
    
def create_df(voucher_list,col):
      df = pd.DataFrame(voucher_list, columns=col)
      df_sorted = df.sort_values(by=['Date'], ascending=[True])
      df_sorted.to_excel("sale.xlsx",index=False)
    

def log(e):
        voucher_list.clear()
        i=0
        try :
            while i<int(total_amt.value):
                    start_date=Date_start.value.split("/")
                    start_date=list(map(int, start_date))
                    end_date=Date_end.value.split("/")
                    end_date=list(map(int, end_date))
                    start_date = datetime.date(int(start_date[2]), start_date[1], start_date[0])
                    end_date = datetime.date(end_date[2], end_date[1], end_date[0])
                    delta = end_date - start_date
                    random_days = random.randrange(delta.days + 1)
                    random_date = start_date + datetime.timedelta(days=random_days)
                    random_amt = random.randint(int(Amt_start.value),int(Amt_end.value))
                    date = random_date.strftime('%m-%d-%Y')
                    nested_list=["Main",date, "cash", random_amt, dd.value, item_type.value]
                    voucher_list.append(nested_list)
                    i+=random_amt
            else: 
                    create_df(voucher_list,col_list)
                    dlg = ft.AlertDialog(
                    title=ft.Text("Excel generated successfully")
                    )
                    e.page.dialog = dlg
                    dlg.open = True
                    e.page.update()
        except:
            dlg = ft.AlertDialog(
                title=ft.Text("Input Error")
                )
            e.page.dialog = dlg
            dlg.open = True
            e.page.update()
            print("input error")
        
gen_btn = ft.ElevatedButton(text="Generate Excel", 
                                bgcolor=btn_color,
                                color=ft.colors.WHITE,
                                icon = ft.icons.SAVE,
                                width=300,
                                height=50,
                                on_click=log)

Back_btn = ft.ElevatedButton(text="Back", 
                                bgcolor=ft.colors.WHITE,
                                color=ft.colors.BLACK,
                                icon = ft.icons.KEYBOARD_ARROW_LEFT,
                                width=300,
                                height=50,
                                on_click=lambda e: e.page.go("/index"))


def __view__():
    return ft.View(
        "/sale_gen",
        controls=[
        ft.Container(
        width=800,
        height=450,
        alignment=ft.alignment.center,
                   gradient=ft.LinearGradient(
                              begin=ft.alignment.top_center,
                              end=ft.alignment.bottom_center,
                              colors=[ft.colors.BLACK87, ft.colors.GREY_400],
                    ),
        content=ft.Column(
            [   
                ft.Column(
                [
                  ft.Row([ft.Text("Date",size=20, color=ft.colors.WHITE)],alignment=ft.MainAxisAlignment.CENTER),
                  ft.Row(
                  [
                   Date_start,
                   to,
                   Date_end,
                  ],alignment=ft.MainAxisAlignment.CENTER,)
                ],alignment=ft.MainAxisAlignment.CENTER),
               
               ft.Column(
                [
                  ft.Row([ft.Text("Amount", size=20, color=ft.colors.WHITE)],alignment=ft.MainAxisAlignment.CENTER),
                  ft.Row(
                  [
                   Amt_start,
                   Amt_end,
                  ],alignment=ft.MainAxisAlignment.CENTER,)
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text("Other Info", size=20, color=ft.colors.WHITE)],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([total_amt,dd,item_type],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([gen_btn, Back_btn],alignment=ft.MainAxisAlignment.CENTER)
            ]
        )
    )
            ]
    )
