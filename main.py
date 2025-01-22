def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

ZOMBIE: Sprite = None
game.splash("MineZombie", "By Cao_Atrevido 😝 ")
tiles.set_current_tilemap(tilemap("""
    level
"""))
Cao_Atrevido = sprites.create(img("""
        f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f 
            4 4 4 4 4 4 4 4 4 4 4 4 4 4 
            4 1 1 1 1 4 4 4 4 1 1 1 1 4 
            4 1 1 1 1 4 4 4 4 1 1 1 1 4 
            4 1 1 f f 4 4 4 4 1 1 f f 4 
            4 1 1 f f 4 4 4 4 1 1 f f 4 
            4 4 4 4 4 4 4 4 4 4 4 4 4 4 
            4 4 1 1 4 4 4 4 4 4 1 1 4 4 
            4 4 1 1 4 4 4 4 4 4 1 1 4 4 
            4 4 1 1 1 1 1 1 1 1 1 1 4 4 
            4 4 1 1 1 1 1 1 1 1 1 1 4 4
    """),
    SpriteKind.player)
info.set_life(0)
controller.move_sprite(Cao_Atrevido, 100, 0)

def on_update_interval():
    global ZOMBIE
    ZOMBIE = sprites.create(assets.image("""
        ZZZOMBIE
    """), SpriteKind.player)
game.on_update_interval(2000, on_update_interval)

def on_forever():
    if info.life() == 0:
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                1,
                255,
                0,
                1291,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        game.set_game_over_message(False, "GAME OVER! TRY AGAIN!")
forever(on_forever)
