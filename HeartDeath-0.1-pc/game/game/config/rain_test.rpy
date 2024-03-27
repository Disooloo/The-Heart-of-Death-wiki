init python:
    # объявление картинок и псевдонимов
    images_auto()

    # плавность появления дождя и звуклв
    rain_t = 0


    # функции громыхания для внедрения в картинки
    def s_play(snd, trans, st, at):
        splay(snd, volume=0.1)  # Уменьшаем громкость

    def s_rain(trans, st, at):
        sfxplay("rain", fadein=rain_t, volume=0.1)  # Уменьшаем громкость

    # остановка шума дождя
    def s_rain_off(trans, st, at):
        sfxstop(fadeout=rain_t)


    # функции громыхания для внедрения в картинки
    def s_play(snd, trans, st, at):
        splay(snd)

    def s_rain(trans, st, at):
        sfxplay("rain", fadein=rain_t)

    # остановка шума дождя
    def s_rain_off(trans, st, at):
        sfxstop(fadeout=rain_t)

init:
    # анимация дождя (прозрачность можно менять)
    image rain ani = Ani("rain ", 4, .1, zoom=3, alpha=.1)

    # дождь с затемнением
    image rain:
        contains:
            "#014b"
            xysize(1920, 1080) alpha 0.5  # Пример затемнения с полупрозрачным темным цветом
        contains:
            "rain ani"
        on show:
            function s_rain
        on hide:
            function s_rain_off

    # анимация молнии
    image light ani = Ani("lightning ", 3, .05, True, True)

    $ t1, t2, t3 = rndf(8, 15), rndf(12, 20), rndf(15, 25)
    $ t11, t22, t33 = rndf(2, 4), rndf(5, 7), rndf(7, 10)
    $ xz = (1, -1)

    # мерцание молнии
    transform l_flash(t, tt):
        anchor (.5, .0)
        xzoom xz[rnd(1)]
        alpha 0
        tt
        alpha 1
        .1
        alpha 0
        .1
        alpha 1
        .1
        alpha 0
        t - tt - .3
        repeat

    # мерцающие молнии
    image light1 = At("light ani", l_flash(t1, t11))
    image light2 = At("light ani", l_flash(t2, t22))
    image light3 = At("light ani", l_flash(t3, t33))

    # синхронные с молниями вспышки
    image light_1 = At(At("#fff8", l_flash(t1, t11)), align(.5, .5))
    image light_2 = At(At("#fff6", l_flash(t2, t22)), align(.5, .5))
    image light_3 = At(At("#fff4", l_flash(t3, t33)), align(.5, .5))

    # картинка со вспышками, молниями и со звуком грома
    image thunder:
        contains:
            "light_1"
            t1
            repeat
        contains:
            "light1"
            align(rndf(.0, 1.), .0)
            t11
            function renpy.curry(s_play)("thunder1")
            t1 - t11
            repeat
        contains:
            "light_2"
            t2
            repeat
        contains:
            "light2"
            align(rndf(.0, 1.), .0)
            t22
            function renpy.curry(s_play)("thunder2")
            t2 - t22
            repeat
        contains:
            "light_3"
            t3
            repeat
        contains:
            "light3"
            align(rndf(.0, 1.), .0)
            t33
            function renpy.curry(s_play)("thunder3")
            t3 - t33
            repeat

# Убираем изображения молний
image light_1:
    pass

image light1:
    pass

image light_2:
    pass

image light2:
    pass

image light_3:
    pass

image light3:
    pass
