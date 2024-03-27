label scane_6:
    # Если пришла смерть:
    "В зале внезапно стало будто бы раза в два темнее. Списав подобное на опьянение, Рей не стал придавать особого значения происходящему."
    "Но из транса его вывел лис."

    show foyr neytral anim with dissolve:
        zoom .35 xalign .5 yalign .99
    foyr "Ты только посмотри кто здесь…"
    "Лицо мужчины было через чур серьёзным. Обернувшись, паренёк увидел даму в чёрном. От неё веяло холодом, а аура внушала страх."
    "Таких ли называют смертью?"
    "Поток мурашек пробежался по телу, а рука, держащая стакан, предательски задрожала. Незнакомка же, осмотревшись, заняла столик в дальнем углу."
    foyr "Слушай, я, пожалуй, пойду. Дел много… Да и… сам придумай мне отговорку."
    "С этими словами мистер Фойр удалился. Растерянный человек не находил себе места среди демонов, а тут ещё и это…"

    "Заметив волнение в стороне бара, леди взглянула парню прямо в глаза."

    menu:
        "Не отрывать взгляд":
            jump scane_6_don_eyes
        "Отвернуться":
            jump scane_6_turn_away
        "Уйти":
            jump scane_6_to_leave



    return

label scane_6_don_eyes:
    # Если выбрали не отрывать взгляд (+5 Хаулис):
    hide foyr neytral anim with dissolve

    show screen lovemeter_howlis with dissolve
    pause .3
    $ relationship_howlis += 5

    "Смотря в глубокие серые глаза девушки, Рей будто попал в сети её обаяния. Холодный образ стал притягательным, а пугающая аура будто исчезла."

    hide screen lovemeter_howlis with dissolve

    '''
    Сделав глубокий вдох, парень направился к незнакомке. Та была явно удивлена, но старалась не показывать этого.

    Подойдя к столику, юноша спросил разрешения сесть. Получив одобрительный кивок, Рей занял место напротив леди смерти.
    '''
    show howlis surprise anim with dissolve:
        zoom .35 xalign .5 yalign .99
    stranger_howlis "Не боишься меня?"
    rey "Мы не знакомы, ничего плохого я вам не сделал, так что…"
    stranger_howlis "Какие глупые рассуждения. Такие как я могут убить не за что."
    stranger_howlis "Всё ещё считаешь, что ты в безопасности?"
    rey "Тут много свидетелей… И к тому же…"
    stranger_howlis "Ну вот, рассуждаешь прямо как глупые людишки!"
    $ AddAchieve("Хаулис", "Новое знакомство", "foir")
    howlis "В любом случае, с моей стороны будет невежливо оставаться безымянной. Хаулис."
    rey "Рей."
    howlis "Зачем подошёл ко мне?"
    rey "Не вы ли обратили на меня взгляд первой?"
    howlis "Так и было, не скрою."
    "Повисло неловкое молчание. Прямолинейность девушки сбивала с толку. Рей вновь взглянул на Хаулис. "
    "Она была столь холодна и безэмоциональна, что казалось, будто разговор не суждено продолжиться."
    howlis "Скажи, кто же ты? Просто смельчак или же дурачок?"
    rey "Как грубо."
    howlis "Просто честно. Со мной обычно не знакомятся, а обходят стороной."
    rey "Всё таки не каждый день видишь смерть…"
    show howlis displacement anim with dissolve:
        zoom .35 xalign .5 yalign .99
    howlis "И то верно. И всё же, скажи… Неужели таким как я суждено быть одним? Одиночество ведь страшнее смерти."

    "Словно сболтнув чего-то лишнего, девушка отвела взгляд. "
    "Рей слегка опешил от столь странной темы для обсуждения, однако решил немного приободрить леди смерть."

    rey "Каждый вправе найти себе друга или любимого человека. {w}Раса – лишь формальность, которая мешает наслаждаться всеми благами."
    rey "Но это не наказание, а лишь установки, которые всё же не могут помешать стать счастливым."
    "Встав из-за стола, Хаулис обошла парня со спины и, приобняв за плечи, прошептала на ухо…"
    howlis "Спасибо."
    "Медленно отстранившись, девушка взяла в баре бутылку вина и покинула заведение."
    "Потеряв дар речи, парень понял, что лучше пойти домой. Такой странный вечер выдался, сил больше не осталось."

    jump next_scane_6
    return


label scane_6_turn_away:
    # Если выбрали отвернуться :
    hide foyr neytral anim with dissolve

    "Почувствовав на спине холодок, юноша невольно уставился в пол. Ему было неловко от внимания смерти. "
    "Холодное прикосновение на плече. Рей резко обернулся. За его спиной стояла та самая девушка."

    show howlis surprise anim with dissolve:
        zoom .35 xalign .5 yalign .99

    stranger_howlis "Прошу прощения, если напугала."
    rey "Ах, да… Ничего…"
    "Рей был напуган. Но старался держаться уверенно. Леди же элегантно приземлилась на соседний стул, где ещё минуту назад выпивал лис."
    stranger_howlis "Мне бокал красного вина 1903 года."
    "Бармен исполнил заказ смерти, а юноша всё не мог понять, что же ем предпринять."
    rey "Меня зовут Рей, а вас?"
    howlis "Хаулис."
    "Разговора не последовало. Неприступная, безэмоциональная – такие ассоциации были у юноши с этой девушкой."
    "Пробыв в молчаливой компании ещё с пол часа, Рей покинул бар, направившись в сторону дома."
    jump next_scane_6
    return

label scane_6_to_leave:
    # Если выбрали уйти (- 5 Хаулис):
    show screen lovemeter_howlis with dissolve
    pause .3
    $ relationship_howlis -= 5

    "Резко подскочив, Рей направился к выход вслед за лисом."

    hide screen lovemeter_howlis with dissolve

    '''
    Бросив краткий взгляд в сторон смерти, он заметил отчаяние и невыносимую печаль в её взгляде.

    Отводя дурные мысли, парень направился к дому.
    '''
    jump next_scane_6
    return

label next_scane_6:
    jump scane_7
    return