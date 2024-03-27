
screen lovemeter_alice:
    vbar:
        xsize 60
        ysize 400
        xalign 0.95
        yalign 0.3
        # Привязываем значение полоски к переменной love_jacky, а максимальное значение - к maxlove. При изменении переменной полоска будет плавно изменяться за 1 секунду (delay).
        value AnimatedValue(value=relationship_alice, range=maxlove, delay=1.0)
        # Указываем картинки для полной и пустой полоски
        bottom_bar Frame("gui/bar/bottom.png",10,10)
        top_bar Frame("gui/bar/top.png",10,10)
screen lovemeter_miriam:
    vbar:
        xsize 60
        ysize 400
        xalign 0.95
        yalign 0.3
        # Привязываем значение полоски к переменной love_jacky, а максимальное значение - к maxlove. При изменении переменной полоска будет плавно изменяться за 1 секунду (delay).
        value AnimatedValue(value=relationship_miriam, range=maxlove, delay=1.0)
        # Указываем картинки для полной и пустой полоски
        bottom_bar Frame("gui/bar/bottom.png",10,10)
        top_bar Frame("gui/bar/top.png",10,10)
screen lovemeter_howlis:
    vbar:
        xsize 60
        ysize 400
        xalign 0.95
        yalign 0.3
        # Привязываем значение полоски к переменной love_jacky, а максимальное значение - к maxlove. При изменении переменной полоска будет плавно изменяться за 1 секунду (delay).
        value AnimatedValue(value=relationship_howlis, range=maxlove, delay=1.0)
        # Указываем картинки для полной и пустой полоски
        bottom_bar Frame("gui/bar/bottom.png",10,10)
        top_bar Frame("gui/bar/top.png",10,10)

# показать аторитет в углу экрана
screen authority_screen:
    frame:
        padding(20,10)
        xalign 0.0
        yalign 1.0
        xoffset 10
        yoffset -10
        text "Aft: [persistent.authority]" size 18 color "#FFFFFF"

screen notifyAuthority(message, amount):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "{size=+10}[amount]{/size}\n[message!tq]"
    timer 3.25 action Hide('notifyAuthority')



# финал пролог, выбор из Мириам, Хаулис , Элис
screen prolog_final_choice:
    modal True

    # zorder 100
    frame:
        xalign 0.5
        xsize 1920
        background Frame("black")


        text "{size=+10}Выберите героиню{/size}" xalign .5 ypos 100



    imagebutton:
        xalign 0 ypos 200
        xsize 450 ysize 450
        idle "sp/final_prolog/howlis_prolog_final_ilde.png"
        hover "sp/final_prolog/howlis_prolog_final_hover.png"
        action Hide("prolog_final_choice"), Jump("scane_7_general_continuation_prologue_next")

    imagebutton:
        xalign .45 ypos 200
        xsize 450 ysize 450
        idle "sp/final_prolog/miriam_prolog_final_ilde.png"
        hover "sp/final_prolog/miriam_prolog_final_hover.png"
        action Hide("prolog_final_choice"), Jump("scane_7_general_continuation_prologue_next")

    imagebutton:
        xalign .95 ypos 200
        xsize 450 ysize 450
        idle "sp/final_prolog/alice_prolog_final_ilde.png"
        hover "sp/final_prolog/alice_prolog_final_hover.png"
        action Hide("prolog_final_choice"), Jump("scane_7_general_continuation_prologue_next")
