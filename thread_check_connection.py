#!/usr/bin/python

import sys
import threading
from time import sleep


class ConnectionSample:
    """
    Connection sample class.

    The class has connect and disconnect methods that have
    to be filled with your own code.
    ConnectionSample launches a threaded method to check
    your connection meanning a function satisfy_condition,
    wich you have to provide the code.
    The checker runs every SHORT_CHECK time. But, after 
    the MAX_DISCONNECTION is reached, the checker pass to 
    a low frequence, checking the connection every 
    LONG_CHECK.
    You have to provide your code for what doing after a 
    disconnection. Maybe, a reconnect method?
    """
    # Constants
    SHORT_CHECK = 1
    LONG_CHECH = 4
    MAX_DISCONNECTIONS = 2

    def __init__(self) -> None:
        """
        Default constructor
        """
        # Initialize private vars
        self._con = False
        self._stop = False
        self._long_check = False
        self._errors_count = 0

        # Creating and launching check connection thread
        print("Initializing con")
        thread_func = threading.Thread(target=self._check_connection)
        print("Starting thread ...")
        thread_func.start()

    def connect(self) -> None:
        """
        Sample method for performing a connection
        """
        # TODO: Paste your connection code here
        self._con = True

    def disconnect(self) -> None:
        """
        Sample method for performing a disconnection
        """
        # TODO: Paste your disconnection code here
        self._con = False

    def _check_connection(self) -> None:
        """
        Threaded method to check the connection
        """
        print("Thread started!")
        # Do while does not have a stop request
        while(not self._stop):
            # If not connected
            if not self._satisfy_condition():
                print("Disconnected!")
                # Increment errors count
                self._errors_count += 1
                # If errors count if greater than maximum disconnection do:
                if self._errors_count > self.MAX_DISCONNECTIONS:
                    # Change sleep time to be slower and does not overrun cpu
                    self._long_check = True

                # TODO: Do what you want when disconnected.
                # Maybe, try to reconnect?
            else:
                print("Connected!")
                # Reset errors count to zero
                self._errors_count = 0
                # Change sleep time to be faster while connected
                self._long_check = False

            # Initialize sleep time
            sleep_time = self.LONG_CHECH if self._long_check else self.SHORT_CHECK
            print(f"Checking every {sleep_time} secs")
            sleep(sleep_time)

        print("Thread stopped")

    @property
    def stop(self) -> bool:
        """
        Sample getter property for stop var
        """
        return self._stop

    @stop.setter
    def stop(self, value) -> None:
        """
        Sample setter property for stop var
        """
        self._stop = value

    def _satisfy_condition(self) -> bool:
        """
        Function to check connection condition
        Return True for a connected status.
        Otherwise, return False.
        """
        # TODO: Paste your condition code here
        return self._con


def main():
    """
    Main function
    """
    con = ConnectionSample()
    sleep(10)
    con.connect()
    sleep(10)
    con.disconnect()
    sleep(4)
    con.stop = True
    sleep(10)
    sys.exit(0)


# Calling main function
if __name__ == "__main__":
    main()
