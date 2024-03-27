# Отношение


define maxlove = 100

# Foyr
define relationship_foyr = 50

# alice
define relationship_alice = 50

# miriam
define relationship_miriam = 50

# Хаулис
define relationship_howlis = 50


# Общие
# авторитет
define authority = 50


# персонажи
default persistent.AddAllAchieve = []


init python:
    allAchievements = {
        "Новичок":"achievements/achiva1.png", # При первом запуске
        "Мистер Фойр":"cards/foir_card.png",
        "Элис":"cards/alice_card.png",
        "Хаулис":"cards/howlis_card.png",
        "Мириам":"cards/miriam_card.png",

    }

    imageAchive = None
    maxCountAchive = 10
    # persistent.AddAllAchieve = []
    # тест, не сохроняет, можно по кд получать

    # Функция для добавления достижения
    def AddAchieve(achieve, message, title):
        if not achieve in persistent.AddAllAchieve:
            persistent.AddAllAchieve.append(achieve)
            imageAchive = allAchievements[achieve]
            renpy.show_screen("notifyAchieve", message, achieve, imageAchive)

    # Авторитет переменная
    persistent.authority = 0
     # Функция для добавления авторитета
    def AddAuthority(authority, message):
        persistent.authority += authority
        renpy.show_screen("notifyAuthority", message, authority)
