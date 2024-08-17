from flet import Container, Column, FilledButton,Row, Text, View,LinearGradient, alignment, colors, MainAxisAlignment

def __view__():

    return View(
        "/index",
        controls=[
            Column([
                Container(
                   margin=0,
                   width=800,
                   height=450,
                   alignment=alignment.center,
                   gradient=LinearGradient(
                              begin=alignment.top_center,
                              end=alignment.bottom_center,
                              colors=[colors.BLUE, colors.YELLOW],
                    ),
                   content=Row([
                       FilledButton(text="Sale Generator", 
                                    on_click=lambda e: e.page.go("/sale_gen")
                                    ),
                       FilledButton(text="Excel formatter",
                                    on_click=lambda e: e.page.go("/excel")),
                   ], alignment=MainAxisAlignment.CENTER)
                )
            ])
        ]
    )