# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CRoss,12.7.20,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        ___str__(self): returns product name and price formatted correctly and as a string
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CRoss,12.5.2020,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name="", product_price=0):
        self.product_name = product_name
        self.product_price = product_price

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Name cannot be numbers")

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if isinstance(value, float) == True:
            self.__product_price = value
        else:
            raise Exception("Prices must be numbers.")

    # Methods
    def __str__(self):
        return self.product_name + ",$" + "%.2f" % self.product_price


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CRoss,12.5.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_objects):
        """ Reads data from .txt file and translates to list of objects

        :param file_name: name of file you want to read from
        :param list_of_objects: list of objects you want to add file data to

        :return: list_of_objects
        """
        # clear out current list if applicable
        try:
            list_of_objects.clear()
            # open file in read mode
            file = open(file_name, "r")
            # iterate over file, remove newline character
            # split on comma and initialize each row into a new instance of Person object
            for line in file:
                line.strip()
                file_product, file_price = line.split(",$")
                row_object = Product(file_product, float(file_price))
                list_of_objects.append(row_object)
            file.close()
            return list_of_objects
        except FileNotFoundError:
            print("File not found! No items loaded.")

    def write_data_to_file(file_name, list_of_objects):
        """Write data to file from list of objects
        :param file_name: name of file you want to write to
        :param list_of_objects: list of objects you want to write from

        :return: nothing

        """
        file = open(file_name, "w")
        for item in list_of_objects:
            file.write(f"{item}\n")
        file.close()

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Manages user input and program output

    methods:
        print_menu_tasks:
        input_menu_choice:
        show_current_data(list_of_objects): --> print list of objects
        input_new_item:

    changelog:
        CRoss,12.5.20,Added new methods
    """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a new item
            2) Save Data to File        
            3) Reload Data from File
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return int(choice)

    @staticmethod
    def show_current_data(list_of_objects):
        """Show curret data in list

        :return: none
        """
        for item in list_of_objects:
            print(item)

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_item():
        """ Get user input for new item and price

        :return: string, string
        """
        try:
            user_item = input("Please input item: ")
            while user_item.isnumeric():
                print("Please enter valid name. Must not be numbers.")
                user_item = input("Please input name: ")
            user_price = input("Please input price: ")
            user_price = float(user_price)

        except Exception:
            print("Please enter valid price. Must be numbers.")
            # user_price = float(input("Please input price: "))

        return Product(user_item, user_price)


# Exceptions  -------------------------------------------- #

class InvalidChoice(Exception):
    def __str__(self):
        return "Please choose option 1, 2, 3, or 4"


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into list of objects
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while True:
    try:
        # show user menu of options
        IO.print_menu_tasks()

        # get users choice and assign to variable intChoice
        intChoice = IO.input_menu_choice()

        if intChoice == 1:
            # get new item and price from user
            # strItem, fltPrice = IO.input_new_item()
            newItem = IO.input_new_item()
            # initialize new instance of Product object w/ user data
            # newItem = Product(strItem, fltPrice)
            # add new object to current list
            lstOfProductObjects.append(newItem)
            # show current list to user
            print("Item added! Current data is:")
            IO.show_current_data(lstOfProductObjects)
        elif intChoice == 2:
            # call file processor function to write data to file
            FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            # show status to user
            print("Items saved!")
        elif intChoice == 3:
            # call file processor function to read data from the file
            FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
            # show current data
            IO.show_current_data(lstOfProductObjects)
        elif intChoice == 4:
            # exit program
            break
        else:
            raise InvalidChoice()

    except ValueError as e:
        print(f"Built-in Python error message is:\n{e}")
    except Exception as e:
        print(f"Error! Built-in Python error message is:\n{e}")
        print(e)