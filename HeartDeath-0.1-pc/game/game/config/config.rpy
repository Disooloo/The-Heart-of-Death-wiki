# Тряска
init:
    define vpunch3 = Move((0, 10), (0, -10), .05, bounce=True, repeat=True, delay=.275*.5)
    define hpunch3 = Move((15, 0), (-15, 0), .05, bounce=True, repeat=True, delay=.275*.5)




# image
image main_menu1 = "main_menu.png"
image main_menu2 = "main_menu1.png"
image main_menu_active = "main_menu_active.png"
image main_menu_heart = "interface/main_meny/heart.png"

# bg
image bg fon_pereulok_noch = "bg/fon_pereulok_noch.png"
image bg fon_ofis_krasnyj = "bg/fon_ofis_krasnyj.png"
image bg fon_pereulok_mesto_prestplenia_1 = "bg/fon_pereulok_mesto_prestplenia_1.png"
image bg fon_bar_krasnyj = "bg/fon_bar_krasnyj.png"
image bg fon_kvartira_noch = "bg/fon_kvartira_noch.png"
image bg telek_fon = "bg/telek_fon.png"
image bg foto_pereulk_mesto_prestuplenia = "bg/foto_pereulk_mesto_prestuplenia.png"



# Анимация частиц в main_menu
image chastichka_1_1 = SnowBlossom("interface/main_meny/partikl_001.png", count=60, yspeed=(-20, 20), xspeed=(100, 140), border=1, start=0, fast=False)
image chastichka_1_2 = SnowBlossom("interface/main_meny/partikl_001.png", count=40, yspeed=(-20, 20), xspeed=(120, 150), border=1, start=0, fast=False)
image chastichka_2 = SnowBlossom("interface/main_meny/partikl_002.png", count=300, yspeed=(-20, 20), xspeed=(50, 90), border=1, start=0, fast=False)


# Выборы пролог
# первый выбор Кровавый бал (1) Небесный лайм (2) Чёрная смерть (3)
define future_choice_drinking1 = None
# выбор - Проститутка - Бармен - Ди-джей
define occupation_choice = None

# ------------------------------Вампир (Элис) -------------------------------
# напиток для элис знакомство 1
define drink_for_alice_acquaintance_1 = None
# ------------------------------/Вампир (Элис) -------------------------------

# ------------------------------Эльф (Мириам)-------------------------------
# Действие Подойти, Помахать рукой, Отвернуться
define prolongation_miriam_action_1 = None

# ------------------------------/Эльф (Мириам)-------------------------------


# Анимация появления света с серцем
image main_menu_heart:
    "main_menu1.png" with dissolve
    pause 5
    "main_menu_active.png" with dissolve
    pause 9
    repeat
