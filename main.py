import flet as ft
from fetchlocation import Get_Current_Location
from fetchweather import Get_Weather_Details
from buildweatherui import Create_Weather_Card,BottomContainerResponsiveRow
import datetime

def main(page:ft.Page):
    page.theme_mode=ft.ThemeMode.DARK
    geo=ft.Geolocator()
    weather_list=ft.Ref[ft.ListView]()
    bottom_weather_container=ft.Ref[ft.Container]()

    def convert_utc_to_time(utc_time):
        print(utc_time)
        a=datetime.datetime.fromtimestamp(utc_time, datetime.timezone.utc)
        #for indian timezone in 12hrs format
        b=datetime.timedelta(seconds=19800)
        c= a + b
        return c.strftime("%I:%M:%S %p")



    def get_current_location_weather(e):
        #°
        page.views[1].floating_action_button.content=ft.ProgressRing(color='black')
        page.update()
        response=Get_Current_Location(geo,page)
        weather=Get_Weather_Details(response['lat'],response['lon'])
        print(weather)
        if weather:
            temp_in_celcius=f"{weather['main']['temp']-273.15:.2f}°C"
            weather_list.current.controls.insert(
                0,
                Create_Weather_Card(page.width,temp_in_celcius,weather['name'],weather['weather'][0]['main'],f"Humidity {weather['main']['humidity']}%")
            )
            page.views[1].floating_action_button.visible=False
            sunset=convert_utc_to_time(weather['sys']['sunset'])
            sunrise=convert_utc_to_time(weather['sys']['sunrise'])
            bottom_weather_container.current.content.controls.extend(
                [
                    BottomContainerResponsiveRow(ft.Icons.SUNNY,ft.Colors.AMBER_500,f"Sunrise at\n{sunrise}",ft.Icons.SUNNY_SNOWING,ft.Colors.AMBER_300,f"Sunset at\n{sunset}"),
                    BottomContainerResponsiveRow(ft.Icons.REMOVE_RED_EYE,ft.Colors.GREEN_ACCENT,f"Visibility\n{weather['visibility']/1000} km",ft.Icons.WIND_POWER,ft.Colors.CYAN,f"Wind\n{weather['wind']['speed']*3.6} Km/Hr")
                ]
            )
            bottom_weather_container.current.visible=True
            weather_list.current.visible=True
            page.views[1].controls.pop(1)
        page.update()

        
        
    def pg_1():
        return ft.View(
            controls=[
            
                ft.SafeArea(
                    ft.Container(
                        width=page.width,
                        padding=20,
                        gradient=ft.LinearGradient([ft.Colors.PURPLE_500,ft.Colors.TRANSPARENT,ft.Colors.PINK]),
                        border_radius=50,
                        
                        content=ft.Column([
                            ft.Text(value="WEATHER FORCASTING",weight=ft.FontWeight.W_900,size=20,text_align=ft.TextAlign.CENTER)
                        ],horizontal_alignment="center")
                    )
                ),
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                value='Please Find Your Location To Access The Weather Information By Clicking Below Icon',
                                text_align=ft.TextAlign.LEFT,
                                color='white',
                                size=30,
                                weight=ft.FontWeight.W_700
                            ),
                            shadow=ft.BoxShadow(0,5,'white',blur_style=ft.ShadowBlurStyle.OUTER),
                            border_radius=30,
                            alignment=ft.Alignment(0,0),
                            margin=ft.margin.all(10),
                            padding=ft.padding.all(20)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    width=page.width
                ),
                ft.ListView(
                    ref=weather_list,
                    expand=True,
                    height=page.height,
                    visible=False,
                    controls=[
                        ft.Container(
                            ref=bottom_weather_container,
                            content=ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=page.width,
                            expand=True,
                            border_radius=30,
                            margin=ft.margin.all(10),
                            padding=ft.padding.all(20),
                            gradient=ft.LinearGradient([ft.Colors.BLUE_500,ft.Colors.PINK_200,ft.Colors.OUTLINE_VARIANT]),
                            visible=False,
                            alignment=ft.Alignment(0,0)
                        )
                    ]
                )

                
            ],
            floating_action_button=ft.FloatingActionButton(icon=ft.Icons.MY_LOCATION,on_click=get_current_location_weather,bgcolor=ft.Colors.BLUE_50,foreground_color=ft.Colors.BLACK),
            
            
       )
    
    page.views.append(
        pg_1()
    )
    page.overlay.extend([geo])
    page.update()
    
        
ft.app(target=main)