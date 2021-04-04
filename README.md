# Juego de la vida
Este es una simulación del juego de la vida realizado en Python

Se trata de un juego de cero jugadores, lo que quiere decir que su evolución está determinada por el estado inicial y no necesita ninguna entrada de datos posterior. El "tablero de juego" es una malla plana formada por cuadrados (las "células") que se extiende por el infinito en todas las direcciones. Por tanto, cada célula tiene 8 células "vecinas", que son las que están próximas a ella, incluidas las diagonales. Las células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y "apagadas"). El estado de las células evoluciona a lo largo de unidades de tiempo discretas (se podría decir que por turnos). El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente. Todas las células se actualizan simultáneamente en cada turno, siguiendo estas reglas:

Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").

Para mayor información [aquí](https://es.wikipedia.org/wiki/Juego_de_la_vida#El_juego)

Para poder instalar y ejecutar el juego debera de instalar las librerias de:
* numpy
* pygame

Donde numpy nos ayudara con el manejo del tablero de las celulas y pygame nos ayudara a poder visualizar nuestro programa graficamente.

Bastara con crear nuestro entorno virtual y ejecutar el comando: pip install -r requirements.txt