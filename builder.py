"""Holds building methods for displaying weather data and forecasts."""
from __future__ import annotations
import requests
from abc import ABC, abstractmethod
from typing import Any

API_KEY = '83e37e184dcc4d32527456121bcf5df1'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = 'Kyiv'
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
print(response)


class weather_info(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def get_coord(self) -> None:
        pass

    @abstractmethod
    def get_wind(self) -> None:
        pass

    @abstractmethod
    def get_base(self) -> None:
        pass


class concretebuilderweather(weather_info):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Weather()

    @property
    def product(self) -> Weather:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def get_coord(self) -> None:
        self._product.add(f"{response['coord']}")

    def get_wind(self) -> None:
        self._product.add(f"{response['wind']}")

    def get_base(self) -> None:
        self._product.add(f"{response['base']}")


class Weather():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    builder = concretebuilderweather()

    print("Standard basic product: ")
    builder.get_coord()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    builder.get_coord()
    builder.get_wind()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.get_coord()
    builder.get_wind()
    builder.get_base()
    builder.product.list_parts()
