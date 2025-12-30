import pgzrun

alien = Actor('alien', (10, 50))

def draw():
    screen.clear()
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()

pgzrun.go()