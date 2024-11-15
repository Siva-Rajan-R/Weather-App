from flet import AlertDialog,Icon,FontWeight,TextAlign,Colors,TextButton,Icons,Text,MainAxisAlignment

def Get_Current_Location(geo,page):
    
    getting_permission=geo.request_permission()
    page.update()

    if getting_permission.name in ['UNABLE_TO_DETERMINE','DENIED','DENIED_FOREVER']:
        page.dialog=AlertDialog(
                                modal=False,
                                bgcolor=Colors.INDIGO_50,
                                title=Icon(Icons.LOCATION_ON,color='red'),
                                content=Text('Location Permission Is Needed!',size=18,weight=FontWeight.W_700,text_align=TextAlign.CENTER,color='black'),
                                actions=[
                                    TextButton('Open Permission Setting',on_click=lambda e:geo.open_app_settings())
                                ],
                                open=True,
                                actions_alignment=MainAxisAlignment.CENTER
                            )
    page.update()
    location=geo.get_current_position()
    geo.update()
    return {'lat':location.latitude,'lon':location.longitude}