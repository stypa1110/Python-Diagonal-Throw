#-*- coding: utf-8 -*-
'''
Created on 08-10-2014

@author: Michał Stypczyński
'''

import pylab
import math

kat=int(input("Podaj kąt rzutu (w stopniach): "))             #Zaczytuje z klawiatury kąt rzutu (raw_input zwraca string)
predkosc=float(input("Podaj predkość początkową (w m/s): "))  #Zaczytuje z klawiatury prędkość początkową

alfa=math.radians(kat)   #Funkcja radians zamienia wartość kąta z stopni na radiany
V0=predkosc              #Prędkość początkową w [m/s]
Vy=V0*math.sin(alfa)     #Wylicza prędkość początkową względem osi y
Vx=V0*math.cos(alfa)     #Wylicza prędkość początkową względem osi x
g=9.81                   #Przyspieszenie ziemskie w [m/s^2]
t=0.0                    #Ustawiamy czas na 0.0 [s]

s=[]                     #Tworzenie pustej listy gdzie będziemy przechowywać odleglości[m]
h=[]                     #Tworzenie pustej listy gdzie będziemy przechowywać wysokości [m]

def wysokosc(t):        #Funkcja wylicza wysokość dla danej wartosci czasu
    return (Vy*t)-((g*t*t)/2)
def odleglosc(t):       #Funkcja wylicza odleglość dla danej wartosci czasu
    return Vx*t

while wysokosc(t) >= 0: #Petla licząca wysokość i odległość obiektu co 0.01[s]
    h.append(wysokosc(t))
    s.append(odleglosc(t))
    t += 0.01

pylab.plot(s,h)                     #Tworzy wykres dla podanych wartosci plot(x,y)
pylab.xlim(0,(s[-1]+1))             #Ustawia w jakim zakresie ma być pokazywany wykres na osi x
pylab.ylim(0,(max(h)+1))            #Ustawia w jakim zakresie ma być pokazywany wykres na osi y
pylab.xlabel(u'Odległość [m]')      #ustawia etykiete dla osi x
pylab.ylabel(u'wysokość [m]')       #Ustawia etykiete dla osi y
pylab.title(u'Rzut ukośny')         #Ustawia tytuł wykresu
pylab.grid(True)                    #Pokazuje dodatkowe linie poziomie i pionowe na wykresie
pylab.show()                        #Pokazuje wykres
print ('Czas', t , '[s]')            #Wypisuje w konsoli czas lotu obiektu
print ('Wysokość', max(h), '[m]')     #Wypisuje w konsoli maksymalna wysokość jaką uzyskał obiekt
print ('Odległość', s[-1], '[m]')     #Wypisuje w konsoli odległość na jaką obiekt doleciał
