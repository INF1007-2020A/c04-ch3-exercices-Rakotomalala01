#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    b=a**(1/2)
    return b


def square(a: float) -> float:
    b=a**2
    return b


def average(a: float, b: float, c: float) -> float:

    return (a+b+c)/3




def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    radians degs=angle_degs*math.pi/180
    radians mins=angle_mins*math.pi/(10800)
    radians sec=angle_secs*math.pi/(648000)
    return radians degs+radians mins+radians sec




def to_degrees(angle_rads: float) -> tuple:
    return angle_rads*math.pi/180


def to_celsius(temperature: float) -> float:
    return temperature


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
