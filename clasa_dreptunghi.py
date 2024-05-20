"""
Implementeaza clasa Dreptunghi:
- atribute: lungime, lățime, culoare
- constructor pentru toate atributele
- metode:
    - descrie()
    - aria()
    - perimetrul()
    - schimbă_culoarea(noua_culoare):
        - această metodă nu returneaza nimic.
        - Ea va lua ca parametru o noua culoare si va suprascrie atributul self.culoare.
        - Poti verifica schimbarea culorii prin apelarea metodei descrie().
"""
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return (f'Dreptunghiul are o lungime de {self.lungime}, latime de {self.latime} si este {self.culoare}.')

    def aria(self):
        return (f'Aria dreptunghiului este: {self.lungime * self.latime}')

    def perimetrul(self):
        return (f'Perimetrul dreptunghiului este: {(2 * self.lungime) + (2 * self.latime)}')

    def schimba_culoarea(self, noua_culoare):
        print(f'Culoarea {self.culoare} a devenit {noua_culoare}.')

dreptunghi1 = Dreptunghi(5, 4, 'alb')
dreptunghi2 = Dreptunghi(10, 5, 'verde')


print(dreptunghi1.descriere())
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())
print(dreptunghi1.schimba_culoarea('mov'))

print("---" * 15)

print(dreptunghi2.descriere())
print(dreptunghi2.aria())
print(dreptunghi2.perimetrul())
print(dreptunghi2.schimba_culoarea('albastru'))