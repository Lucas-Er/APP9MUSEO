import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "Orange"
    page.window_width = 1200
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 300
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)

    #audios de lenguajes
    fortran = ft.Audio(src="fortran.mp3", volume=1, balance=0)
    page.overlay.append(fortran)
    
    cobol = ft.Audio(src="cobol.mp3",volume=1,balance=0)
    page.overlay.append(cobol)
    
    pascal = ft.Audio(src="pascal_lenguaje.mp3", volume=1,balance=0)
    page.overlay.append(pascal)
    
    c = ft.Audio(src="c.mp3",volume=1, balance=0)
    page.overlay.append(c)
    
    html = ft.Audio(src="html.mp3",volume=1,balance=0)
    page.overlay.append(html)
    
    python = ft.Audio(src="python.mp3",volume=1,balance=0)
    page.overlay.append(python)
    
    sql = ft.Audio(src="sql.mp3",volume=1,balance=0)
    page.overlay.append(sql)
    
    php = ft.Audio(src="php.mp3",volume=1,balance=0)
    page.overlay.append(php)
    
    java = ft.Audio(src="java.mp3",volume=1,balance=0)
    page.overlay.append(java)
    
    js = ft.Audio(src="ttsmaker-file-2024-11-4-19-0-25.mp3",volume=1,balance=0)
    page.overlay.append(js)
    
    perl = ft.Audio(src="perl.mp3",volume=1,balance=0)
    page.overlay.append(perl)
    
    swift = ft.Audio(src="swift.mp3",volume=1,balance=0)
    page.overlay.append(swift)

    #Audios de las redes sociales

    redes = ft.Audio(src="redes.sociales.portada.audio.mp3.mp3",volume=1,balance=0)
    page.overlay.append(redes)
    
    facebook =ft.Audio(src="RS-Audio-FB.mp3",volume=1,balance=0)
    page.overlay.append(facebook)

    tiktok = ft.Audio(src="RS-Audio-TK.mp3",volume=1,balance=0)
    page.overlay.append(tiktok)

    twitter = ft.Audio(src="RS-Audio-twitter.mp3",volume=1,balance=0)
    page.overlay.append(twitter)

    youtube = ft.Audio(src="RS-Audio-You tube.mp3",volume=1,balance=0)
    page.overlay.append(youtube)

    snapchat = ft.Audio(src="RS-Audio-Snapchat.mp3",volume=1,balance=0)
    page.overlay.append(snapchat)

    whatsapp = ft.Audio(src="RS-Audio-Wsp.mp3",volume=1,balance=0)
    page.overlay.append(whatsapp)

    wechat = ft.Audio(src="RS-Audio-We Chat.mp3",volume=1,balance=0)
    page.overlay.append(wechat)

    pinterest = ft.Audio(src="RS-Audio-Pinterest.mp3",volume=1,balance=0)
    page.overlay.append(pinterest)

    tinder = ft.Audio(src="RS-Audio-Tinder.mp3",volume=1,balance=0)
    page.overlay.append(tinder)

    telegram = ft.Audio(src="RS-Audio-Telegram.mp3",volume=1,balance=0)
    page.overlay.append(telegram)

    #Audio de la informatica durante la pandemia
    
    informatica = ft.Audio(src="LIDLP.Audio.intro.mp3",volume=1,balance=0)
    page.overlay.append(informatica)

    googlemeet = ft.Audio(src="LIDLP.audioGoogleMeet.mp3",volume=1,balance=0)
    page.overlay.append(googlemeet)

    microsoft = ft.Audio(src="LIDLP.audioMcrosoftTeams.mp3",volume=1,balance=0)
    page.overlay.append(microsoft)

    disney = ft.Audio(src="LIDLP.audioDisney.mp3",volume=1,balance=0)
    page.overlay.append(disney)

    zoom = ft.Audio(src="LIDLP.audioZoom.mp3",volume=1,balance=2)
    page.overlay.append(zoom)

    prime = ft.Audio(src="LIDLP.audioAmazonPrimeVideo.mp3",volume=1,balance=0)
    page.overlay.append(prime)
    
    tt = ft.Audio(src="LIDLP.audioTikTok.mp3",volume=1,balance=0)
    page.overlay.append(tt)

    discord = ft.Audio(src="LIDLP.audioDiscord.mp3",volume=1,balance=0)
    page.overlay.append(discord)

    classroom = ft.Audio(src="LIDLP.audioGoogleClassroom.mp3",volume=1,balance=0)
    page.overlay.append(classroom)

    #Audios de las nuevas tecnologias

    tecno = ft.Audio(src="LNT.Audio.mp3",volume=1,balance=0)
    page.overlay.append(tecno)



    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        fortran.pause()
        cobol.pause()
        pascal.pause()
        c.pause()
        html.pause()
        python.pause()
        sql.pause()
        php.pause()
        java.pause()
        js.pause()
        perl.pause()
        swift.pause()

        redes.pause()
        facebook.pause()
        tiktok.pause()
        twitter.pause()
        youtube.pause()
        snapchat.pause()
        whatsapp.pause()
        wechat.pause()
        pinterest.pause()
        tinder.pause()
        telegram.pause()

        googlemeet.pause()
        microsoft.pause()
        informatica.pause()
        disney.pause()
        zoom.pause()
        prime.pause()
        tt.pause()
        discord.pause()
        classroom.pause()

        tecno.pause()
        


    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
    
    def play_fortran(e):
        StopAll()
        fortran.play()
    
    def play_cobol(e):
        StopAll()
        cobol.play()
        
    def play_pascal2(e):
        StopAll()
        pascal.play()
    
    def play_c(e):
        StopAll()
        c.play()
    
    def play_html(e):
        StopAll()
        html.play()
    
    def play_python(e):
        StopAll()
        python.play()
    
    def play_sql(e):
        StopAll()
        sql.play()
    
    def play_php(e):
        StopAll()
        php.play()
    
    def play_java(e):
        StopAll()
        java.play()
    
    def play_js(e):
        StopAll()
        js.play()
    
    def play_perl(e):
        StopAll()
        perl.play()
    
    def play_swift(e):
        StopAll()
        swift.play()

    def play_redes(e):
        StopAll()
        redes.play()

    def play_facebook(e):
        StopAll()
        facebook.play()

    def play_tiktok(e):
        StopAll()
        tiktok.play()

    def play_twitter(e):
        StopAll()
        twitter.play()

    def play_youtube(e):
        StopAll()
        youtube.play()

    def play_snapchat(e):
        StopAll()
        snapchat.play()

    def play_whatsapp(e):
        StopAll()
        whatsapp.play()

    def play_wechat(e):
        StopAll()
        wechat.play()

    def play_pinterest(e):
        StopAll()
        pinterest.play()

    def play_tinder(e):
        StopAll()
        tinder.play()

    def play_telegram(e):
        StopAll()
        telegram.play()

    def play_googlemeet(e):
        StopAll()
        googlemeet.play()

    def play_microsoft(e):
        StopAll()
        microsoft.play()
        
    def play_informatica(e):
        StopAll()
        informatica.play()

    def play_disney(e):
        StopAll()
        disney.play()

    def play_zoom(e):
        StopAll()
        zoom.play()

    def play_prime(e):
        StopAll()
        prime.play()

    def play_tt(e):
        StopAll()
        tt.play()

    def play_discord(e):
        StopAll()
        discord.play()

    def play_classroom(e):
        StopAll()
        classroom.play()

    def play_tecno(e):
        StopAll()
        tecno.play()
    


    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)   
    # Botones Tipos de lenguaje btn = ElevatedButton(content=ft.Image(src="",width=img_width,height=img_height, border_radius=border_radius, semantics_label="""))
    btn21 = ElevatedButton(content=ft.Image(src="fortran.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="Fortran"), on_click=play_fortran)
    btn22 = ElevatedButton(content=ft.Image(src="cobol.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="cobol"), on_click=play_cobol)
    btn23 = ElevatedButton(content=ft.Image(src="pascal.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="pascal"), on_click=play_pascal2)
    btn24 = ElevatedButton(content=ft.Image(src="c.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="C"),on_click=play_c)
    
    btn25 = ElevatedButton(content=ft.Image(src="html.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="html"),on_click=play_html)
    btn26 = ElevatedButton(content=ft.Image(src="python.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="python"),on_click=play_python)
    btn27 = ElevatedButton(content=ft.Image(src="sql.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="sql"),on_click=play_sql)
    btn28 = ElevatedButton(content=ft.Image(src="php.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="php"),on_click=play_php)
    
    btn29 = ElevatedButton(content=ft.Image(src="java.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="java"),on_click=play_java)
    btn30 = ElevatedButton(content=ft.Image(src="javascrip.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="javascrip"),on_click=play_js)
    btn31 = ElevatedButton(content=ft.Image(src="perl.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="perl"),on_click=play_perl)
    btn32 = ElevatedButton(content=ft.Image(src="swift.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="swift"),on_click=play_swift)
    
    #Botones Las Redes sociales

    btn33 = ElevatedButton(content=ft.Image(src="redes.sociales.portada.jpeg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="redes"),on_click=play_redes)
    btn34 =ElevatedButton(content=ft.Image(src="RS-Imagen-FB.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="facebook"),on_click=play_facebook)
    btn35 = ElevatedButton(content=ft.Image(src="RS-Imagen-TK.png",width=img_width,height=img_width,border_radius=border_radius,semantics_label="tiktok"),on_click=play_tiktok)
    btn36 = ElevatedButton(content=ft.Image(src="RS-Imagen-twitter2.jpeg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="twitter"),on_click=play_twitter)
    btn37 = ElevatedButton(content=ft.Image(src="RS-Imagen-Youtube.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="youtube"),on_click=play_youtube)
    btn38 = ElevatedButton(content=ft.Image(src="RS-Audio-Snapchat.jpg",width=img_width,height=img_width,border_radius=border_radius,semantics_label="snapchat"),on_click=play_snapchat)
    btn39 = ElevatedButton(content=ft.Image(src="RS-Imagen-Wsp.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="whatsapp"),on_click=play_whatsapp) 
    btn40 = ElevatedButton(content=ft.Image(src="RS-Imagen-WeChat.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="wechat"),on_click=play_wechat)
    btn41 = ElevatedButton(content=ft.Image(src="RS-Imagen-Pinterest.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="pinterest"),on_click=play_pinterest)
    btn42 = ElevatedButton(content=ft.Image(src="RS-Imagen-tinder.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tinder"),on_click=play_tinder)
    btn43 = ElevatedButton(content=ft.Image(src="RS-Imagen-Telegram.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="telegram"),on_click=play_telegram)
   
   
   
    #Botones La informatica durante la pandemia de covid 19
    
    btn44 = ElevatedButton(content=ft.Image(src="introlidlp..jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="informatica"),on_click=play_informatica)
    btn45 = ElevatedButton(content=ft.Image(src="LIDPL.imagenGoogleMeet.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="googlemeet"),on_click=play_googlemeet)
    btn46 = ElevatedButton(content=ft.Image(src="LIDLP.microsoft.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="microsoft"),on_click=play_microsoft)
    btn47 = ElevatedButton(content=ft.Image(src="LIDLP.imagenDisney.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="disney"),on_click=play_disney)
    btn48 = ElevatedButton(content=ft.Image(src="LIDLP.imagenZoom.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="zoom"),on_click=play_zoom)
    btn49 = ElevatedButton(content=ft.Image(src="LIDLP.imagenAmazonPrimeVideo.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="prime"),on_click=play_prime)
    btn50 = ElevatedButton(content=ft.Image(src="LIDLP.imagenTikTok.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tt"),on_click=play_tt)
    btn51 = ElevatedButton(content=ft.Image(src="LIDLP.imagenDiscord.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="discord"),on_click=play_discord)
    btn52 = ElevatedButton(content=ft.Image(src="LIDLP.imagenGoogleClassroom.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="classroom"),on_click=play_classroom)
   
   
    #botones Las nuevas tecnologias 

    btn53 = ElevatedButton(content=ft.Image(src="LNT.Imagen.jpg",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tecno"),on_click=play_tecno)
    



    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]),                                    
                                    ft.ElevatedButton(
                                        "la evolucion de los lenguajes de programacion",
                                        on_click=lambda _: [StopAll(), page.go('/lenguajes'),]),
                                    ft.ElevatedButton(
                                        'Las Redes Sociales',
                                        on_click=lambda _: [StopAll(), page.go('/redes')]),
                                    ft.ElevatedButton(
                                        'la informatica durante la pandemia de covid-19',
                                        on_click=lambda _: [StopAll(), page.go('/pandemia')]),
                                    ft.ElevatedButton(
                                        'las nuevas tecnologias',
                                        on_click=lambda _: [StopAll(), page.go('/nuevas')]),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la evolucion de los lenguajes de informatica"',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                    alignment="center",
                                    controls=[btn5, btn6, btn7,btn8]  
                                    ),
                                    ft.Row(
                                    alignment="center",
                                        controls=[btn9, btn10, btn11,btn12] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn13,btn14,btn15,btn16] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn17,btn18,btn19,btn20] 
                                    ),
                                    ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las redes sociales"',
                                        on_click=lambda _: page.go('/redes')
                                    ),
                                    ft.Text("Los lenguajes de programación han evolucionado a lo largo de la historia, aquí te presentamos algunos de los más importantes:",color="white", size=15),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn21,btn22,btn23,btn24]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn25,btn26,btn27,btn28]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn29,btn30,btn31,btn32]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de las redes sociales
        elif page.route == '/redes':
            page.views.append(
                View(
                    "/redes",
                    controls=[
                        AppBar(
                            title=ft.Text("Las redes sociales"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la informatica durante la pandemia"',
                                        on_click=lambda _: page.go('/pandemia')
                                    #agregar botones aqui de las redes sociales
                                    ),
                                    ft.Text("Aqui se mostraran algunas de las principales redes sociales:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn33]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn34,btn35,btn36,btn37]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn38,btn39,btn40]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn41,btn42,btn43]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #viata de la informatica durante la pandemia
        elif page.route == '/pandemia':
            page.views.append(
                View(
                    "/pandemia",
                    controls=[
                        AppBar(
                            title=ft.Text("la informatica durante la pandemia de covid-19"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las nuevas tecnologias"',
                                        on_click=lambda _: page.go('/nuevas')
                                    ),
                                    ft.Text("Aqui se mostraran algunas plataformas que fueron fundamentales para el pereodo de la pamdemia:"),
                                
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn44]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn45,btn46,btn47]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn48,btn49,btn50]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn51,btn52]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #viata de la las nuevas tecnologias
        elif page.route == '/nuevas':
            page.views.append(
                View(
                    "/nuevas",
                    controls=[
                        AppBar(
                            title=ft.Text("las nuevas tecnologias"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Text("A continuacion se mostrara un audio breve sobre las nuevas tecnologias:"),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn53]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")
