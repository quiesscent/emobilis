# convertery

def celsius(temp):
        pass


def fahrenheit(temp):
        pass


def kelvin(temp):
        pass


while True:
    temperature = input("Enter temperature: ")

    if isinstance(temperature, str):
        print("Temperature {temperature can not be a string")

    conversion = input("Enter Unit to convert: ")

    if conversion == 'Celcius':

        conv = celsius(temperature)

    if conversion == 'fahrenheit':

        conv = fahrenheit(temperature)

    else:

        conv = kelvin(temperature)
