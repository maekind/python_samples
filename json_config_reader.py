#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This sample uses the file json_sample.json located into the data folder """

import json
from os import path

__authors__ = 'Marco Espinosa'
__license__ = 'MIT License'
__version__ = '1.0'
__maintainer__ = 'Marco Espinosa'
__email__ = 'hi@marcoespinosa.es'
__status__ = 'Development'


class ConfigReaderException(Exception):
    """
    This is a custom exception for our ConfigReader class
    that heritages from Exception base class.
    """


class ConfigReader:
    """
    This class provides an interface to read
    a configuration file in json format
    """

    def __init__(self, config_file) -> None:
        """
        Default constructor
        """
        # Set configuration file
        self._config = None
        self._config_file = config_file

        # Initialize vars
        self._content = None

        # Load configuration file content
        self._load_config()

    def _load_config(self) -> None:
        """
        Method to load configuration file
        """
        try:
            # Opening configuration file for reading
            with open(self._config_file, 'r') as file_:
                self._content = json.loads(file_.read())

            print("Configuration file loaded successfully!")

        except Exception as error:
            # Raise custom exception
            raise ConfigReaderException(
                f"{self._config}: cannot load configuration: {error}")

    def get_parameter(self, parameter, default=None):
        """
        Return the configuration option in the given path.
        If it is not found, the default value is returned.
        """
        opt = self._content
        try:
            for i in parameter:
                opt = opt[i]
        except KeyError:
            opt = default

        return opt

    def print_config_parameters(self) -> None:
        """
        Pretty print for the parameters in the configuration file
        """
        print("")
        print("Configuration file content")
        print("=====================================")
        print(json.dumps(self._content, indent=4, sort_keys=True))


def main():
    """
    Main function
    """
    # Load configuration file
    config_reader = ConfigReader(path.join("data", "json_sample.json"))

    # Get some string parameter
    param_value = config_reader.get_parameter(["section 1", "param 1"])
    # Print the parameter value and its type
    print(
        f"Section 1->param 1 value: {param_value} (Type:{type(param_value)})")

    # Get some float parameter
    param_value = config_reader.get_parameter(["section 2", "param 4"])
    # Print the parameter value and its type
    print(
        f"Section 2->param 4 value: {param_value} (Type:{type(param_value)})")

    # Get some dictionary parameter
    param_value = config_reader.get_parameter(["section 3", "my dict"])
    # Print the parameter value and its type
    print(
        f"Section 3->my dict value: {param_value} (Type:{type(param_value)})")

    # Get some non-existent parameter with default value
    param_value = config_reader.get_parameter(
        ["section 10", "non-existent"], default="This parameter does not exists!")
    # Print the parameter value and its type
    print(
        f"Non-existent parameter value: {param_value} (Type:{type(param_value)})")

    # Pretty json print of all parameters in configuration file
    config_reader.print_config_parameters()


if __name__ == "__main__":
    main()
