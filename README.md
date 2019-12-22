Como ver� en la carpeta, hemos adjuntado dos archivos
uno de ellos tiene formato ".ipynb", que se abre con un 
notebook, por ejemplo "jupyter", y otro archivo
".py" que se puede abrir con cualquier IDE de python.
Nosotros probamos el trabajo usando jupyter notebook
y Visual Studio Code.
La principal diferencia entre ambos archivos es que el archivo
".ipynb" no incluye la mejora, que consiste en un visualizador gr�fico.
Mientras que el archivo ".py" si que la incluye, ya que en Visual studio 
se aprecia bastante mejor.

Procedemos a detallar el c�digo del archivo .py, 
que contiene la mejora.

La estructura del c�digo es la siguiente.

Se empieza creando la clase mapa, con m�todos que
devuelven el tama�o del mapa tanto en el eje X
como en el eje Y. Adem�s de un m�todo llamado 
"tipoCelda" que devuelve el valor de una celda al 
darle los valores X e Y de la coordenada del mapa.

Luego definimos el mapa en un Array de dos dimensiones 
donde la posici�n (0,0) se encuentra en la esquina superior izquierda.
Los n�meros de dentro del mapa equivalen a las siguientes casillas:
0=agua
1=llanura
2=bosque
3=monta�a

Para resolver el ejemplo hemos considerado que cruzar dos 
llanuras equivale a cruzar un bosque, y cruzar 3 llanuras 
equivale a una monta�a. Estos valores pueden modificarse
pero nunca debe modificarse que el agua es igual a 0, o el agente 
podr� atravesarla.

M�s abajo hemos definido el  __init__ del entorno, con atributos comentados en
el propio c�digo. Lo m�s relevante son los atributos "posX", "posY"
"endX" y "endY", que respectivamente son, las coordenadas del eje (x,y)
del punto inicial del agente y las coordenadas del destino.

Luego est� la funci�n reset, donde se ponen las coordenadas a las que vuelve
el agente tras una iteraci�n. Para el funcionamiento correcto debe ser igual a
"posX" y "posY".

Debajo tenemos las acciones, que mueven el agente en una de las cuatro direcciones
cardinales. Pero antes de moverse, comprueba que en la casilla  a la que se dirige no haya
agua o se salga del mapa.

La siguiente funci�n es randomAction, que escoge una acci�n aleatoria.

Luego est� render, que se dedica a imprimir el mapa por consola, en la posici�n
del agente imprime una R y en la del destino una Q.

Luego est� el Grid, esto forma parte de la mejora gr�fica.

Comenzamos dibujando todas las casillas del mapa, eligiendo color seg�n su n�mero en el array,
tambi�n la posici�n dl destino y del agente.

luego est� la funci�n gridAct, que permite que se vaya actualizando el mapa con cada paso del algoritmo.

Ahora entramos en el algoritmo en s�.
Generamos una Q-table que contiene todas las parejas (estado,acci�n)

luego los par�metros principales:
Epoch es el n�mero de iteraciones
gamma es el factor de descuento, afecta a la ecuaci�n de Bellman y la
creaci�n de la Q-table.
Epsilon es un valor entre 0 y 1, cuanto m�s alto, m�s acciones aleatorias toma
el algoritmo.
Decay tambi�n est� entre 0 y 1, cuanto m�s alto, antes deja el algoritmo de tomar
acciones aleatorias.

tras esto creamos el mapa en la interfaz gr�fica.
establecemos una variable auxiliar para acabar contando el n�mero de pasos m�nimo 
que consigue el algoritmo.

Luego procedemos a abrir un bucle for que se repite el n�mero de veces que haya en la 
variable Epoch.

Y ahora entramos en un bucle while del que no se sale hasta que el agente llegue al destino.

dentro de este while se llama a la actualizaci�n del mapa con cada iteraci�n, se cuenta el valor
de la casilla actual y se suma al n�mero de pasos, se c�lcula la probabilidad de hacer un movimiento
aleatorio o de seguir la Q-table, se realiza una acci�n, se actualiza la Q-table, se reduce Epsilon y se vuelve a empezar.

Tras todas las iteraciones del bucle for que se repet�a "Epoch veces",
se imprime por consola el n�mero m�nimo de pasos descubierto por el algoritmo. 