controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
})
let ZOMBIE : Sprite = null
game.splash("MineZombie", "By Cao_Atrevido 😝 ")
tiles.setCurrentTilemap(tilemap`
    level
`)
let Cao_Atrevido = sprites.create(img`
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
    `, SpriteKind.Player)
info.setLife(0)
controller.moveSprite(Cao_Atrevido, 100, 0)
game.onUpdateInterval(2000, function on_update_interval() {
    
    ZOMBIE = sprites.create(assets.image`
        ZZZOMBIE
    `, SpriteKind.Player)
})
forever(function on_forever() {
    if (info.life() == 0) {
        music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 0, 1291, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        game.setGameOverMessage(false, "GAME OVER! TRY AGAIN!")
    }
    
})
