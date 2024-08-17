from flet import app, Page, MainAxisAlignment, colors
from pages.home import __view__ as landing_page
from pages.sale_gen import __view__ as sale_gen
from pages.Excel_formatter import __view__ as excel_formatter

def main(page:Page):
    # page
    page.title="Name it later"
    page.window.height=450
    page.window.width=800
    page.window.frameless=False
    page.window.min_height= 450
    page.window.max_height= 450
    page.window.min_width=800
    page.window.max_width=800
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.padding=0
    # routes and functions releated to them
    index=landing_page()
    sale=sale_gen()
    excel_format=excel_formatter()
    
    def route_change(routes):
        page.views.clear()
        page.views.append(index)
        if page.route == "/sale_gen":
            page.views.append(sale)
            page.bgcolor="#0F0F0F"
        elif page.route == "/excel":
            page.views.append(excel_format)
        elif page.route == "/index":
            page.views.append(index)
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)
    
    # page roue config
    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)
    page.views.append(index)
    page.update()

if __name__=="__main__":
    app(target=main)