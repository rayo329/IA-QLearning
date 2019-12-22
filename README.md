Como verá en la carpeta, hemos adjuntado dos archivos
uno de ellos tiene formato ".ipynb", que se abre con un 
notebook, por ejemplo "jupyter", y otro archivo
".py" que se puede abrir con cualquier IDE de python.
Nosotros probamos el trabajo usando jupyter notebook
y Visual Studio Code.
La principal diferencia entre ambos archivos es que el archivo
".ipynb" no incluye la mejora, que consiste en un visualizador gráfico.
Mientras que el archivo ".py" si que la incluye, ya que en Visual studio 
se aprecia bastante mejor.

Procedemos a detallar el código del archivo .py, 
que contiene la mejora.

La estructura del código es la siguiente.

Se empieza creando la clase mapa, con métodos que
devuelven el tamaño del mapa tanto en el eje X
como en el eje Y. Además de un método llamado 
"tipoCelda" que devuelve el valor de una celda al 
darle los valores X e Y de la coordenada del mapa.

Luego definimos el mapa en un Array de dos dimensiones 
donde la posición (0,0) se encuentra en la esquina superior izquierda.
Los números de dentro del mapa equivalen a las siguientes casillas:
0=agua
1=llanura
2=bosque
3=montaña

Para resolver el ejemplo hemos considerado que cruzar dos 
llanuras equivale a cruzar un bosque, y cruzar 3 llanuras 
equivale a una montaña. Estos valores pueden modificarse
pero nunca debe modificarse que el agua es igual a 0, o el agente 
podrá atravesarla.

Más abajo hemos definido el  __init__ del entorno, con atributos comentados en
el propio código. Lo más relevante son los atributos "posX", "posY"
"endX" y "endY", que respectivamente son, las coordenadas del eje (x,y)
del punto inicial del agente y las coordenadas del destino.

Luego está la función reset, donde se ponen las coordenadas a las que vuelve
el agente tras una iteración. Para el funcionamiento correcto debe ser igual a
"posX" y "posY".

Debajo tenemos las acciones, que mueven el agente en una de las cuatro direcciones
cardinales. Pero antes de moverse, comprueba que en la casilla  a la que se dirige no haya
agua o se salga del mapa.

La siguiente función es randomAction, que escoge una acción aleatoria.

Luego está render, que se dedica a imprimir el mapa por consola, en la posición
del agente imprime una R y en la del destino una Q.

Luego está el Grid, esto forma parte de la mejora gráfica.

Comenzamos dibujando todas las casillas del mapa, eligiendo color según su número en el array,
también la posición dl destino y del agente.

luego está la función gridAct, que permite que se vaya actualizando el mapa con cada paso del algoritmo.

Ahora entramos en el algoritmo en sí.
Generamos una Q-table que contiene todas las parejas (estado,acción)

luego los parámetros principales:
Epoch es el número de iteraciones
gamma es el factor de descuento, afecta a la ecuación de Bellman y la
creación de la Q-table.
Epsilon es un valor entre 0 y 1, cuanto más alto, más acciones aleatorias toma
el algoritmo.
Decay también está entre 0 y 1, cuanto más alto, antes deja el algoritmo de tomar
acciones aleatorias.

tras esto creamos el mapa en la interfaz gráfica.
establecemos una variable auxiliar para acabar contando el número de pasos mínimo 
que consigue el algoritmo.

Luego procedemos a abrir un bucle for que se repite el número de veces que haya en la 
variable Epoch.

Y ahora entramos en un bucle while del que no se sale hasta que el agente llegue al destino.

dentro de este while se llama a la actualización del mapa con cada iteración, se cuenta el valor
de la casilla actual y se suma al número de pasos, se cálcula la probabilidad de hacer un movimiento
aleatorio o de seguir la Q-table, se realiza una acción, se actualiza la Q-table, se reduce Epsilon y se vuelve a empezar.

Tras todas las iteraciones del bucle for que se repetía "Epoch veces",
se imprime por consola el número mínimo de pasos descubierto por el algoritmo. 