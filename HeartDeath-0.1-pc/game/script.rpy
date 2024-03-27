label start:
    jump scene_start
    return

# Заставка
label splashscreen:
    scene black
    pause(0.5)
    $ renpy.movie_cutscene("video/screensaver.ogg")
    pause(0.5)
    scene black with fade
