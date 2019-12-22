
import numpy as np
import copy
from tkinter import *
import time
import os

class Mapa:
    def __init__(self, celdas):
        self.celdas = celdas
    
    def tamanoEjeX(self):
        return len(self.celdas[0]) #Número de celdas del primer array de celdas (Solo eje X)
    
    def tamanoEjeY(self):
        return len(self.celdas) #Número de arrays del primer array de celdas (eje Y)
    
    def tipoCelda(self, f, c):
        return self.celdas[f][c] #te devuelve el valor de una celda
    
#def suma(estado): # valor de las celdas escogidas en los estados
#    return mapaEjemplo.tipoCelda(estado[0], estado[1])    

#Mapa a seguir con los pesos de cada casilla.
mapaEjemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                     [1, 1, 1, 2, 2, 3, 2, 2, 1, 1],
                     [1, 1, 1, 2, 3, 3, 3, 2, 1, 1],
                     [1, 1, 1, 2, 2, 3, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

#mapaEjemplo = Mapa([[0, 0, 0, 0],
#                     [0, 0, 0, 0],
#                     [1, 1, 1, 0],
#                     [3, 1, 1, 0],
#                     [3, 1, 1, 0],
#                     [1, 1, 1, 0]])
class Env():
    
    def __init__(self):
        self.height = mapaEjemplo.tamanoEjeY(); #Altura del mapa
        self.width = mapaEjemplo.tamanoEjeX(); #Anchura del mapa
        self.posX = 0; #cambiar a posInicial
        self.posY = 5; #cambiar a posInicial
        self.endX = 9; #cambiar a posFinal
        self.endY = 0; #cambiar a posFinal
        self.actions = [0, 1, 2, 3];  #Tipos de acciones
        self.stateCount = self.height*self.width; #Numero de celdas
        self.actionCount = len(self.actions);


    def reset(self):#Tras acabar un epoch, vuelve a la posición inicial
        self.posX = 0; #cambiar a posInicial
        self.posY = 5; #cambiar a posInicial
        self.done = False;
        return 0, 0, False;

    # Acciones
    def step(self, action):
        if action==0: # Moverse a la izquierda 
            self.posX = self.posX-1 if ((self.posX>0) and (mapaEjemplo.tipoCelda(self.posY, self.posX - 1) != 0)) else self.posX;
        if action==1: # Moverse a la derecha
            self.posX = self.posX+1 if ((self.posX<self.width-1) and (mapaEjemplo.tipoCelda(self.posY, self.posX + 1) != 0)) else self.posX;
        if action==2: # Moverse hacia arriba
            self.posY = self.posY-1 if ((self.posY>0) and (mapaEjemplo.tipoCelda(self.posY-1, self.posX) != 0)) else self.posY;
        if action==3: # Moverse hacia abajo
            self.posY = self.posY+1 if ((self.posY<self.height-1) and (mapaEjemplo.tipoCelda(self.posY+1, self.posX) != 0)) else self.posY;

        done = self.posX==self.endX and self.posY==self.endY; #Si La posición actual es la del final, entonces done es true
        nextState = self.width*self.posY + self.posX;
        reward = 1 if done else 0;
        return nextState, reward, done; #Si ha llegado al final, otorga recompensa

    # Devuelve una acción aleatoria
    def randomAction(self):
        return np.random.choice(self.actions);

    # Imprime el mapa por consola. Recorre el mapa entero, al llegar a una celda, imprime su valor, si es la posición actual
    # imprime "R", si es la posición final imprime "Q"
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.posY==i and self.posX==j:
                    print("R", end='');
                elif self.endY==i and self.endX==j:
                    print("Q", end='');
                else:
                    print(mapaEjemplo.tipoCelda(i, j), end='');
            print("");
    
    def grid(self, root):           # Función del GUI para la mejora

        for i in range(self.height):
                for j in range(self.width):                 # Recorremos el mapa
                    if self.posY==i and self.posX==j:
                        label = Label(root, text="R", bg="white", height=2, width=2, relief="raised")   
                        label.grid(row=i, column=j)         # Dibujamos el agente
                    elif self.endY==i and self.endX==j:
                        label = Label(root, text="Q", bg="black", fg="white", height=2, width=2, relief="raised")   
                        label.grid(row=i, column=j)         # Dibujamos el final
                    elif mapaEjemplo.tipoCelda(i, j)==1:
                        label = Label(root, bg="yellow", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)         # Por aquí vamos coloreando los 
                    elif mapaEjemplo.tipoCelda(i, j)==2:    # distintos tipos de casillas
                        label = Label(root, bg="green", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)         
                    elif mapaEjemplo.tipoCelda(i, j)==3:
                        label = Label(root, bg="brown", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)
                    elif mapaEjemplo.tipoCelda(i, j)==0:
                        label = Label(root, bg="blue", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)
            
         

    def gridAct(self, root):                # Con esta función vamos actualizando el GUI
                                            # Para ahorrar tiempo no le pasamos las casillas
        for i in range(self.height):        # de agua o destino, ya que nunca cambian
                for j in range(self.width):
                    if self.posY==i and self.posX==j:
                        label = Label(root, text="R", bg="white", height=2, width=2, relief="raised")   
                        label.grid(row=i, column=j)
                    elif self.endY==i and self.endX==j:
                        label = Label(root, text="Q", bg="black", fg="white", height=2, width=2, relief="raised")   
                        label.grid(row=i, column=j)
                    elif mapaEjemplo.tipoCelda(i, j)==1:
                        label = Label(root, bg="yellow", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)
                    elif mapaEjemplo.tipoCelda(i, j)==2:
                        label = Label(root, bg="green", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)
                    elif mapaEjemplo.tipoCelda(i, j)==3:
                        label = Label(root, bg="brown", height=2, width=2, relief="raised")
                        label.grid(row=i, column=j)


# Creamos la ventana principal 
root = Tk()                 
# Crea el environment
env = Env()

# QTable : contiene todos los q-valores para todas las parejas (estado,acción)
qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

# Parámetros, Epochs es el número de iteraciones que vamos a permitir al algoritmo para alcanzar el estado óptimo.
#Cuanto más alto epsilon más acciones aleatorias
#Cuanto más alto el decay, más rápido bajará el epsilon tras cada iteración y antes dejarán de hacerse la mayoría de acciones aleatorias
#Gamma afecta a la ecuación de Belmman y a la creación de la Qtable
epochs = 50
gamma = 0.1
epsilon = 0.08
decay = 0.1

# Llamamos a la función para crear el mapa en la GUI
env.grid(root)

# Entrenamiento
minSteps = 5000 #Variable auxiliar para obtener el número menor de pasos
for i in range(epochs):
    state, reward, done = env.reset()
    steps = 0
    

    while not done: 
     #   os.system('clear')
        #print("epoch #", i+1, "/", epochs) #------------------------------ Descomenta para ver progreso de epoch
        #env.render() #------------------------------------------------------ Descomenta para ver el mapa cada vez
        time.sleep(0.05)
        
        # Actualizamos la GUI
        env.gridAct(root)
        root.update()

        # cuenta los pesos de las casillas por las que pasa
        steps += mapaEjemplo.tipoCelda(env.posY, env.posX)
        
        # Probabilidad de hacer movimiento aleatorio para descubrir otros caminos
        if np.random.uniform() < epsilon:
            action = env.randomAction()
        # Si no se mueve de forma aleatoria, va hacia la casilla que tiene en la Qtable que lo acerca más a la recompensa (greedy)
        else:
            action = qtable[state].index(max(qtable[state]))

        # Hace una acción
        next_state, reward, done = env.step(action)

        # Actualiza la Qtable con la ecuación de Bellman usando gamma 
        qtable[state][action] = reward + gamma * max(qtable[next_state])

        # Pasa al siguiente estado
        state = next_state
    # Se actualiza Epsilon multiplicandose por el decay y restándose al Epsilon actual, haciendo que con cada iteración se hagan menos
    #acciones aleatorias
    epsilon -= decay*epsilon

    print("\nCompletado en", steps, "pasos".format(steps))
    time.sleep(0.8)
    #Si ha descubierto un camino más óptimo al anterior óptimo, guarda la suma de los pesos.
    if steps < minSteps:
        minSteps = steps
root.mainloop()
print("\nValor camino mínimo hallado: ", minSteps)