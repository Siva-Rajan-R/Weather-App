import flet as ft

def Create_Weather_Card(width,temp,city,haze,humidity):
    return  ft.Container(
            height=200,
            padding=ft.padding.all(20),
            border_radius=30,
            width=width,
            margin=ft.margin.all(10),
            gradient=ft.LinearGradient([ft.Colors.BLUE_100,ft.Colors.PINK_200,ft.Colors.OUTLINE_VARIANT]),
            content=ft.Row(
                controls=[
                    ft.Column(
                        [
                            ft.Text(temp,size=50,color=ft.Colors.BLACK),
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.HOUSE_OUTLINED,color="black"),
                                    ft.Text(city ,color="black",size=15,weight=ft.FontWeight.W_800)
                                ],
                                
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.CLOUD_QUEUE_OUTLINED,color="black"),
                                    ft.Text(haze,color="black",size=15,weight=ft.FontWeight.W_800)
                                ],
                                
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.WATER_DROP_OUTLINED,color="black"),
                                    ft.Text(humidity,color="black",size=15,weight=ft.FontWeight.W_800)
                                ],
                                
                            ),
                        ],
                        
                    ),
                    ft.Row(
                        [
                            ft.Image(src='https://mir-s3-cdn-cf.behance.net/project_modules/disp/0dafe246152113.58497778c03e5.gif')
                            
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.END
                    )
                    
                ]
            )

        )

class BottomContainerResponsiveRow(ft.ResponsiveRow):
    def __init__(self,icon_1,icon_color_1,icon_1_text,icon_2,icon_color_2,icon_2_text):
        super().__init__()
        self.controls=[
            ft.Column(
                col=6,
                controls=[
                    ft.Divider(opacity=0,height=5),
                    ft.Icon(
                        name=icon_1,
                        size=60,
                        color=icon_color_1
                    ),
                    ft.Text(icon_1_text,size=23,weight=ft.FontWeight.W_800,text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                col=6,
                controls=[
                    ft.Divider(opacity=0,height=5),
                    ft.Icon(
                        name=icon_2,
                        size=60,
                        color=icon_color_2
                    ),
                    ft.Text(icon_2_text,size=23,weight=ft.FontWeight.W_800,text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
        self.alignment=ft.MainAxisAlignment.SPACE_EVENLY

