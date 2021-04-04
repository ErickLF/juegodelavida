from simulacion import Simulacion

def main():
    screen_width = 480
    screen_height = 480
    gridsize = 20

    simulacion = Simulacion(gridsize,screen_height,screen_width)
    simulacion.run()

main()