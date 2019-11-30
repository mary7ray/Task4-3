# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70



    def __add_distance(self, killometry):
        self.odometr += killometry
        return self.odometr

    def __subtract_fuel(self, liters):
        self.fuel -= liters

    def drive(self, killometry):
        liters = killometry / 10
        if liters <= self.fuel:
            self.__add_distance(killometry)
            print('Let’s drive!')
        elif self.fuel == 0:
            self.__subtract_fuel(liters)
            print('Need more fuel, please, fill more!')

    def __str(self):
        print(f'Car {self.model} {self.year} {self.fuel} {self.odometr}')


# car1 = Car('USA', 'Tesla Model S', 2010)
# print(car1.model)
# print(car1.year)
# car1.drive(300)

car2 = Car('FRA','Pejo S6', 2009)
print(car2.model)
print(car2.year)
car2.drive(300)

print(car2.fuel)

# print(car2.str())