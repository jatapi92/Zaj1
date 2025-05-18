from Zaj1.Zaj3 import geompy

kwadrat1 = geompy.figury2d.Kwadrat(3)
prostokat1 = geompy.figury2d.Prostokat(3, 4)
kolo1 = geompy.figury2d.Kolo(5)

print(kwadrat1.pole, kwadrat1.obwod, sep='|')
print(prostokat1.pole, prostokat1.obwod, sep='|')
print(kolo1.pole, kolo1.obwod, sep='|')

szescian1 = geompy.figury3d.Szescian(3)
prostopadloscian1 = geompy.figury3d.Prostopadloscian(3, 4, 5)
kula1 = geompy.figury3d.Kula(5)

print(szescian1.pole, szescian1.objetosc, sep='|')
print(prostopadloscian1.pole, prostopadloscian1.objetosc, sep='|')
print(kula1.pole, kula1.objetosc, sep='|')

