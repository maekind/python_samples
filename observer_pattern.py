#!/usr/bin/python

""" Contains classes for implementing Observer pattern """

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque
# More info in deque here:
# https://docs.python.org/3/library/collections.html#collections.deque
from time import sleep
from typing import List
import threading
import logging

__package__ = "python_and_pizzas"
__authors__ = "Marco Espinosa"
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Marco Espinosa"
__email__ = "hi@marcoespinosa.es"
__status__ = "Development"



# Abstract clases to implement the pattern

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def cooked(self, subject: Observable) -> None:
        """
        Receive update from subject.
        The pattern call this function "update", but to make
        ir more inclusive with the sample, I called it "cooked" ;)
        """
        pass


class Observable(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

# Sample clases to use the pattern

# In this sample, the Pizzaman creates some pizzas.
# Then, he cooks them into the StoneOven. The StaoneOven
# has a limited capacity, so the PizzaMan observes for
# a finished pizza.
# Futhermore, he can put more other pizzas to cook.


class Pizza:
    """
    This class modelize a basic pizza
    """

    def __init__(self, name) -> None:
        """
        Default constructor
        """
        # Initialize the pizza"s name
        self._name = name
        # Initialize a list of ingredients
        self._ingredients = []

    def add_ingredient(self, ingredient):
        """
        Method to add ingredients to the ingredients list
        """
        self._ingredients.append(ingredient)

    @property
    def name(self):
        """
        name property getter
        """
        return self._name


class PizzaMan(Observer):
    """
    This class implements the observer object.
    """

    def __init__(self, name) -> None:
        # Calling Observer constructor
        super().__init__()

        # Initialize variables
        self._pizzas = deque([])
        self._oven = None

        # Set pizzaman's name
        self._name = name

        # Pending pizzas
        self._pending_pizzas = deque([])

        # Set logger name
        self._log = logging.getLogger(self._name)

    def cooked(self, pizza, owner):
        """
        This method is called by the StoneOven
        when a pizza is cooked.
        """
        if owner is self._name:
            # Remove pizza from pending pizzas list
            self._pending_pizzas.remove(pizza)
            self._log.info(
                f"Pizza {pizza.name} is ready to deliver!")

    def use(self, oven):
        """
        This method attachs de PizzaMan itself (Observer) to the
        object oven (Observable) to be notified when a pizzas is cooked.
        """
        self._log.info(f"Request to use the oven. (Attach to the Observable object)")
        self._oven = oven
        self._oven.attach(self)
        sleep(1)
        
    def clean_oven(self):
        """
        This method is called when the PizzaMan
        is not going to cook more pizzas.
        It detachs the pizzaman (Observer) from the oven (Observable),
        so the pizzaman is no longer receiving notifications from the 
        oven.
        """
        if self._oven:
            self._log.info(f"I'm no longer using the oven (Detach from the Observable object)")
            self._oven.detach(self)
            sleep(1)
        
    def prepare(self, pizza):
        """
        This method prepares a pizza an put it into
        the queue to be cooked.
        """
        self._log.info(f"Preparing a pizza {pizza.name} ...")
        # Sleep to simulate some preparation time :)
        sleep(2)
        # Add pizza to the pending pizzas list
        self._pending_pizzas.append(pizza)
        # Introduce the pizza into the oven for cooking
        self._oven.cook(pizza, self._name)
        self._log.info(f"The pizza {pizza.name} is ready to cook.")

    @property
    def name(self):
        """
        name property getter
        """
        return self._name

    @property
    def pending_pizzas(self):
        """
        pending_pizzas property getter
        """
        return self._pending_pizzas


class Oven(Observable):
    """
    This class implements the observable object.
    """

    def __init__(self, name, capacity, cooking_time) -> None:
        """
        Default constructor
        """
        # Calling Observable constructor
        super().__init__()

        # Set name
        self._name = name
        # Maximum capacity of the oven
        self._capacity = capacity
        # Pizza cooking time
        self._cooking_time = cooking_time
        # List of pizzas cooking
        self._pizzas_cooking = deque([])
        # List of pizzas cooking
        self._pizzas_prepared = deque([])
        # List of pizzamans that use the oven
        self._pizza_mans: List[Observer] = []
        # lock for safety acces to variables from threads
        self._lock = threading.Lock()
        # Set logger name
        self._log = logging.getLogger(self._name)

        # Turns on oven
        self._cook = True
        thread_func = threading.Thread(target=self._turn_on)
        thread_func.start()

    def cook(self, pizza, owner):
        """
        Method to tell the oven that a pizza is ready to cook
        """
        with self._lock:
            self._pizzas_prepared.append((pizza, owner))

    def attach(self, pizzaman: Observer):
        """
        Method to attach observers
        """
        self._log.info(f"{pizzaman.name} is allowed to use the oven (Attached to the Observable object)")
        # Add pizzaman to the observers list to be notified
        self._pizza_mans.append(pizzaman)

    def detach(self, pizzaman: Observer):
        """
        Removes attached observer
        """
        # Removes the pizzaman from the list of observers. So
        # he won't be no longer notified
        self._pizza_mans.remove(pizzaman)

    def notify(self, pizza, owner):
        """
        Function to notify observers of data changes
        """
        # Notify all pizzamans that a pizza is ready to deliver
        for pizzaman in self._pizza_mans:
            pizzaman.cooked(pizza, owner)

    def _turn_on(self):
        """
        Method to cook pizzas. This method runs in an independant thread,
        so while the oven was on, it cooks pizzas without exceed its capacity.
        If the capacity is reached, it will wait until a pizza was ready to 
        deliver.
        """
        cooking = []
        pizza = None

        # Execut forever until turn off action was received
        while(self._cook):
            # Check for number pizzas cooking, to not exceed its capacity
            if self._capacity > len(self._pizzas_cooking):
                # If there are pizzas waiting for cooking:
                if self._pizzas_prepared:
                    with self._lock:
                        # Take a pizza for cooking
                        pizza, owner = self._pizzas_prepared.popleft()
                        # Adds pizza into the pizzas cooking list
                        self._pizzas_cooking.append(pizza)
                    # Create and launch a pizza threaded cook.
                    cook_pizza = threading.Thread(
                        target=self._cook_pizza, args=(pizza, owner,))
                    # Add cooking thread to a list of running threads (or pizzas cooking)
                    cooking.append(cook_pizza)
                    cook_pizza.start()
                    # Print how many pizzas are in the oven
                    if len(self._pizzas_cooking) < 2:
                        self._log.info(
                            f"There is {len(self._pizzas_cooking)} pizza cooking.")
                    elif len(self._pizzas_cooking) > 1:
                        self._log.info(
                            f"There are {len(self._pizzas_cooking)} pizzas cooking.")

        # If turn off action is recived, wait for all pending pizzas to be cooked
        for index, pizza_cooking in enumerate(cooking):
            # Wait for pizza ...
            pizza_cooking.join()

    def _cook_pizza(self, pizza, owner):
        """
        Cooks a pizza and notify the Pizzaman when its done
        """
        self._log.info(f"Pizza {pizza.name} from {owner} is in the oven.")
        # Simulate pizza's cooking time
        sleep(self._cooking_time)
        with self._lock:
            # Remove pizza from pizzas cooking list. It is ready!
            self._pizzas_cooking.remove(pizza)
        # Notify all pizzaman observing the oven
        self.notify(pizza, owner)

    def turn_off(self):
        """
        Method to turn off the oven
        This method sends a stop action to the method that is cooking
        """
        # We cannot stop the oven if there are pizzas cooking yet!
        if self._pizzas_cooking:
            self._log.error(
                f"Cannot stop oven. There are {len(self._pizzas_cooking)} pizzas cooking.")
            return False

        # Set cook to False, to say the oven that has to stop. Refers to
        # the turns_on method
        self._cook = False

        return True

    @property
    def pizzas_cooking(self):
        """
        pizzas_cooking property getter
        """
        return self._pizzas_cooking

def configure_logger():
    """
    Method to configure logging
    """
    logargs = {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'}
    
    logargs["level"] = "INFO"
        
    logging.basicConfig(**logargs)

def main():
    """
    Main function
    """
    
    # Configure logger properties
    configure_logger()

    # Create a oven of capacity for 2 pizzas
    # that takes 10 seconds to cook each one.
    oven = Oven("Stone Oven", 2, 10)

    # Creates two pizzaman
    pizzaman1 = PizzaMan("Marco")
    pizzaman2 = PizzaMan("Giuseppe")

    # Pizzamans request to use the oven
    pizzaman1.use(oven)
    pizzaman2.use(oven)

    # Marco prepare a pizza
    margarita = Pizza("Margarita")
    margarita.add_ingredient("Tomato")
    margarita.add_ingredient("Mozzarella")

    pizzaman1.prepare(margarita)

    # Giuseppe prepare a pizza
    proschiutto = Pizza("Proschiuto")
    proschiutto.add_ingredient("Tomato")
    proschiutto.add_ingredient("Mozzarella")
    proschiutto.add_ingredient("Proschiutto")

    pizzaman2.prepare(proschiutto)

    # Marco prepare a pizza
    tuna = Pizza("Tuna")
    tuna.add_ingredient("Tomato")
    tuna.add_ingredient("Mozzarella")
    tuna.add_ingredient("Tuna")
    tuna.add_ingredient("Black olives")

    pizzaman1.prepare(tuna)

    # Marco prepare a pizza
    salami = Pizza("Salami")
    salami.add_ingredient("Tomato")
    salami.add_ingredient("Mozzarella")
    salami.add_ingredient("Salami")

    pizzaman1.prepare(salami)

    # Giuseppe prepare a pizza
    quattro_stagioni = Pizza("Quattro stagioni")
    quattro_stagioni.add_ingredient("Tomato")
    quattro_stagioni.add_ingredient("Mozzarella")
    quattro_stagioni.add_ingredient("Mushrooms")
    quattro_stagioni.add_ingredient("Artichokes")
    quattro_stagioni.add_ingredient("Black olives")

    pizzaman2.prepare(quattro_stagioni)

    # Wait while there are pizzas cooking into the oven
    while(pizzaman1.pending_pizzas or pizzaman2.pending_pizzas):
        sleep(1)

    # Turn off oven when all pizzas ready
    while not oven.turn_off():
        sleep(5)

    # Clean oven
    pizzaman1.clean_oven()
    pizzaman2.clean_oven()


if __name__ == "__main__":
    main()
