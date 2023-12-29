# Chan Siang Hao Sean, 213178U, IT2852, BF2201

from tabulate import tabulate
from validate_email import validate_email
import re
import json
from game import *


class Car:
    def __init__(self, car_engine_no, car_brand, car_type, mileage, reg_year):
        self.__car_engine_no = car_engine_no
        self.car_brand = car_brand
        self.__type = car_type
        self.mileage = mileage
        self.__reg_year = reg_year

    def __str__(self):
        return f"\nCar Engine No: {self.__car_engine_no}\nCar Brand: {self.car_brand}\nType: {self.__type}\nMileage: {self.mileage}\nReg Year: {self.__reg_year}\n"

    def get_car_engine_no(self):
        return self.__car_engine_no

    def set_car_engine_no(self, car_engine_no):
        self.__car_engine_no = car_engine_no

    def get_car_brand(self):
        return self.car_brand

    def set_car_brand(self, car_brand):
        self.car_brand = car_brand

    def get_type(self):
        return self.__type

    def set_type(self, car_type):
        self.__type = car_type

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_reg_year(self):
        return self.__reg_year

    def set_reg_year(self, reg_year):
        self.__reg_year = reg_year

    @staticmethod
    def search_car_by_engine_no(cars):
        car_engine_no = input("\033[96mEnter the car engine number to search for:\033[0m ")
        found_cars = [car for car in cars if car.get_car_engine_no() == car_engine_no]
        return found_cars

    @staticmethod
    def radix_sort(cars, category, order):
        def counting_sort(cars, get_category_value):
            n = len(cars)
            output = [None] * n

            max_category = max(get_category_value(car) for car in cars)
            count = [0] * (max_category + 1)

            for car in cars:
                index = get_category_value(car)
                count[index] += 1

            for i in range(1, max_category + 1):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                car = cars[i]
                index = get_category_value(car)
                output[count[index] - 1] = car
                count[index] -= 1
                i -= 1

            for i in range(n):
                cars[i] = output[i]

        def get_category_value_engine_no(car):
            return int(car.get_car_engine_no()[exp]) if exp < len(car.get_car_engine_no()) else 0

        def get_category_value_brand(car):
            return ord(car.get_car_brand()[exp]) if exp < len(car.get_car_brand()) else 0

        def get_category_value_type(car):
            return ord(car.get_type()[exp]) if exp < len(car.get_type()) else 0

        def get_category_value_mileage(car):
            return car.get_mileage() // (10 ** exp) % 10

        def get_category_value_reg_year(car):
            return car.get_reg_year() // (10 ** exp) % 10

        def get_category():
            valid_categories = ["1", "2", "3", "4", "5"]
            if str(category) not in valid_categories:
                print("\033[91mInvalid category. Please try again\033[0m")
                return get_category_value_engine_no
            if category == "1":
                return get_category_value_engine_no
            elif category == "2":
                return get_category_value_brand
            elif category == "3":
                return get_category_value_type
            elif category == "4":
                return get_category_value_mileage
            elif category == "5":
                return get_category_value_reg_year

        max_length = max(len(car.get_car_engine_no()) for car in cars)
        get_category_value = get_category()
        for exp in range(max_length - 1, -1, -1):
            counting_sort(cars, get_category_value)

        if order == "1":
            sorted_cars = cars
        elif order == "2":
            sorted_cars = cars[::-1]
        else:
            raise ValueError("Invalid order. Please choose '1' (asc) or '2' (desc).")

        table = []
        for car in sorted_cars:
            row = [car.get_car_engine_no(), car.get_car_brand(), car.get_type(), car.get_mileage(), car.get_reg_year()]
            table.append(row)

        headers = ["Engine No.", "Brand", "Type", "Mileage", "Registration Year"]
        print("\033[92mSorted cars:\033[0m")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def input_car_details():
    while True:
        try:
            car_engine_no = input("\033[96mEnter the car engine number (or '!' to cancel):\033[0m ")
            if car_engine_no == "!":
                confirm = input("\033[93mAre you sure you want to cancel entering car details? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEntering car details canceled.\033[0m")
                    return None
            elif not 9 <= len(car_engine_no) <= 17:
                raise ValueError("\033[91mPlease enter a valid car engine number between 9 to 17 characters.\033[0m")
            elif any(car.get_car_engine_no() == car_engine_no for car in cars):
                raise ValueError("\033[91mEngine number already exists. Please enter a unique engine number.\033[0m")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            car_brand = input("\033[96mEnter the car brand (or '!' to cancel):\033[0m ")
            if car_brand == "!":
                confirm = input("\033[93mAre you sure you want to cancel entering car details? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEntering car details canceled.\033[0m")
                    return None
            elif not car_brand.isalpha():
                raise ValueError("\033[91mCar brand must be an alphabetic string.\033[0m")
            elif len(car_brand) < 3 or len(car_brand) > 10:
                raise ValueError("\033[91mCar brand must be between 3 and 10 characters long.\033[0m")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            car_type = input("\033[96mEnter the car type (or '!' to cancel):\033[0m ")
            if car_type == "!":
                confirm = input("\033[93mAre you sure you want to cancel entering car details? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEntering car details canceled.\033[0m")
                    return None
            elif not car_type.isalpha():
                raise ValueError("\033[91mCar type must be an alphabetic string.\033[0m")
            elif len(car_type) < 3 or len(car_type) > 15:
                raise ValueError("\033[91mCar type must be between 3 and 15 characters long.\033[0m")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            car_mileage = input("\033[96mEnter the car mileage (or '!' to cancel):\033[0m ")
            if car_mileage == "!":
                confirm = input("\033[93mAre you sure you want to cancel entering car details? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEntering car details canceled.\033[0m")
                    return None
            else:
                car_mileage = int(car_mileage)
                if 0 < car_mileage < 10001:
                    break
                else:
                    raise ValueError(
                        "\033[91mPlease enter a valid car mileage (an integer between 1 and 10000).\033[0m")
        except ValueError as e:
            print(e)

    while True:
        try:
            car_reg_year = input("\033[96mEnter the car registration year (or '!' to cancel):\033[0m ")
            if car_reg_year == "!":
                confirm = input("\033[93mAre you sure you want to cancel entering car details? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEntering car details canceled.\033[0m")
                    return None
            else:
                car_reg_year = int(car_reg_year)
                if 1990 <= car_reg_year <= 2023:
                    break
                else:
                    raise ValueError(
                        "\033[91mPlease enter a valid car registration year (between 1990 and 2023).\033[0m")
        except ValueError as e:
            print(e)

    return Car(car_engine_no, car_brand.capitalize(), car_type, car_mileage, car_reg_year)


def bubble_sort(cars):
    for i in range(len(cars) - 1):
        for j in range(len(cars) - i - 1):
            if cars[j].car_brand > cars[j + 1].car_brand:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]

    return cars


def insertion_sort(cars):
    for i in range(1, len(cars)):
        current_value = cars[i]
        current_index = i

        while current_index > 0 and cars[current_index - 1].car_mileage < current_value.mileage:
            cars[current_index] = cars[current_index - 1]
            current_index -= 1

        cars[current_index] = current_value

    return cars


def edit_car_details(car):
    while True:
        try:
            car_brand = input("\033[93mEnter the car brand (or '!' to cancel):\033[0m ")
            if car_brand == "!":
                confirm = input("\033[93mAre you sure you want to cancel editing? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEditing canceled.\033[0m")
                    return
            elif not car_brand.isalpha():
                raise ValueError("\033[91mCar brand must be an alphabetic string.\033[0m")
            elif len(car_brand) < 3 or len(car_brand) > 10:
                raise ValueError("\033[91mCar brand must be between 3 and 10 characters long.\033[0m")
            car.set_car_brand(car_brand)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            car_type = input("\033[93mEnter the car type (or '!' to cancel):\033[0m ")
            if car_type == "!":
                confirm = input("\033[93mAre you sure you want to cancel editing? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEditing canceled.\033[0m")
                    return
            elif not car_type.isalpha():
                raise ValueError("\033[91mCar type must be an alphabetic string.\033[0m")
            elif len(car_type) < 3 or len(car_type) > 15:
                raise ValueError("\033[91mCar type must be between 3 and 15 characters long.\033[0m")
            car.set_type(car_type)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            car_mileage = input("\033[93mEnter the car mileage (or '!' to cancel):\033[0m ")
            if car_mileage == "!":
                confirm = input("\033[93mAre you sure you want to cancel editing? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEditing canceled.\033[0m")
                    return
            else:
                car_mileage = int(car_mileage)
                if 0 < car_mileage < 10001:
                    car.set_mileage(car_mileage)
                    break
                else:
                    raise ValueError(
                        "\033[91mPlease enter a valid car mileage (an integer between 1 and 10000).\033[0m")
        except ValueError as e:
            print(e)

    while True:
        try:
            car_reg_year = input("\033[93mEnter the car registration year (or '!' to cancel):\033[0m ")
            if car_reg_year == "!":
                confirm = input("\033[93mAre you sure you want to cancel editing? (yes/no): \033[0m")
                if confirm.lower() == "yes":
                    print("\033[91mEditing canceled.\033[0m")
                    return
            else:
                car_reg_year = int(car_reg_year)
                if 1990 <= car_reg_year <= 2023:
                    car.set_reg_year(car_reg_year)
                    break
                else:
                    raise ValueError(
                        "\033[91mPlease enter a valid car registration year (between 1990 and 2023).\033[0m")
        except ValueError as e:
            print(e)

    print("\033[92mCar details updated successfully!\033[0m")


def delete_car_by_engine_no(cars):
    car_engine_no = input("\033[96mEnter the car engine number to delete:\033[0m ")
    found_cars = [car for car in cars if car.get_car_engine_no() == car_engine_no]
    if found_cars:
        print("\033[92mMatching cars found:\033[0m")
        for car in found_cars:
            print(car)

        confirm_delete = input("\033[96mAre you sure you want to delete these cars? (yes/no):\033[0m ")
        if confirm_delete.lower() == "yes":
            cars = [car for car in cars if car not in found_cars]
            print("\033[92mCars deleted successfully!\033[0m")
        else:
            print("\033[91mDeletion canceled.\033[0m")
    else:
        print("\033[91mNo cars found with the provided engine number.\033[0m")
    return cars


def filter_cars_by_category(cars):
    print("\033[93mSelect a category to filter by:\033[0m")
    print("\033[96m1. Car Engine Number\033[0m")
    print("\033[96m2. Car Brand\033[0m")
    print("\033[96m3. Car Type\033[0m")
    print("\033[96m4. Mileage\033[0m")
    print("\033[96m5. Registration Year\033[0m")
    print("\033[91m6. Exit\033[0m")

    try:
        choice = input("\033[93mEnter your choice: \033[0m")
    except EOFError:
        print("\033[91mEnd of file reached.\033[0m")
        return

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("\033[91mPlease enter a valid choice.\033[0m")
        return

    category = None
    found_cars = []

    if choice == "1":
        category = "\033[91mcar engine number\033[0m"
        search_term = input("\033[93mEnter the car engine number to filter by: \033[0m")
        found_cars = [car for car in cars if car.get_car_engine_no() == search_term]
    elif choice == "2":
        category = "\033[91mcar brand\033[0m"
        search_term = input("\033[93mEnter the car brand to filter by: \033[0m")
        found_cars = [car for car in cars if car.get_car_brand() == search_term]
    elif choice == "3":
        category = "\033[91mcar type\033[0m"
        search_term = input("\033[93mEnter the car type to filter by: \033[0m")
        found_cars = [car for car in cars if car.get_type() == search_term]
    elif choice == "4":
        category = "\033[91mmileage\033[0m"
        search_term = input("\033[93mEnter the car mileage to filter by: \033[0m")
        found_cars = [car for car in cars if car.get_mileage() == int(search_term)]
    elif choice == "5":
        category = "\033[91mregistration year\033[0m"
        search_term = input("\033[93mEnter the car registration year to filter by: \033[0m")
        found_cars = [car for car in cars if car.get_reg_year() == int(search_term)]
    elif choice == "6":
        return

    if found_cars:
        print(f"\n\033[93mMatching cars found based on {category}:\033[0m")
        table = [[car.get_car_engine_no(), car.get_car_brand(), car.get_type(), car.get_mileage(), car.get_reg_year()]
                 for car in found_cars]
        headers = ["Engine No.", "Brand", "Type", "Mileage", "Registration Year"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))
    else:
        print(f"\n\033[91mNo cars found based on {category}.\033[0m")


def selection_sort_by_type(cars):
    n = len(cars)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if cars[j].get_type() < cars[min_index].get_type():
                min_index = j
        cars[i], cars[min_index] = cars[min_index], cars[i]

    return cars


def merge_sort_by_year_engine_no(cars):
    if len(cars) <= 1:
        return cars

    mid = len(cars) // 2
    left_half = cars[:mid]
    right_half = cars[mid:]

    left_sorted = merge_sort_by_year_engine_no(left_half)
    right_sorted = merge_sort_by_year_engine_no(right_half)

    merged = merge(left_sorted, right_sorted)

    return merged


def cocktail_sort_by_id(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i].customer.customer_id > arr[i + 1].customer.customer_id:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if arr[i].customer.customer_id > arr[i + 1].customer.customer_id:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].get_reg_year() < right[right_index].get_reg_year():
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index].get_reg_year() > right[right_index].get_reg_year():
            merged.append(right[right_index])
            right_index += 1
        else:
            if left[left_index].get_car_engine_no() < right[right_index].get_car_engine_no():
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


class Queue:
    def __init__(self):
        self.requests = []
        self.customers = {}

    def add_request(self, request):
        self.requests.append(request)
        self.customers[request.customer.customer_id] = request.customer

    def get_num_requests(self):
        return len(self.requests)

    def process_next_request(self):
        if self.requests:
            processed_request = self.requests.pop(0)
            del self.customers[processed_request.customer.customer_id]
            return processed_request
        else:
            return None

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id, None)

    def search_requests(self, search_term):
        results = []
        for request in self.requests:
            if search_term.lower() in request.customer.customer_id.lower() \
                    or search_term.lower() in request.customer.customer_name.lower() \
                    or search_term.lower() in request.customer.customer_email.lower() \
                    or search_term.lower() in request.request.lower():
                results.append(request)
        return results


class InputValidator:
    @staticmethod
    def validate_customer_id(customer_id):
        return re.match(r'^\d{4}[A-Za-z]$', customer_id)

    @staticmethod
    def validate_customer_name(customer_name):
        return re.match(r'^[A-Za-z\s]+$', customer_name)

    @staticmethod
    def validate_customer_email(customer_email):
        return validate_email(customer_email)

    @staticmethod
    def validate_customer_points(customer_points):
        return re.match(r'^[1-9]\d{0,3}$|^10000$', customer_points)

    @staticmethod
    def validate_menu_choice(choice, menu_options):
        return choice in [str(i) for i in range(1, menu_options + 1)] or choice == '!'


class DataManager:
    @staticmethod
    def save_data(queue):
        data = []
        for request in queue.requests:
            data.append({
                'customer_id': request.customer.customer_id,
                'customer_name': request.customer.customer_name,
                'customer_email': request.customer.customer_email,
                'customer_points': request.customer.customer_points,
                'request': request.request,
            })
        with open('data.json', 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_data(queue):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)

            for item in data:
                customer = Customer(item['customer_id'], item['customer_name'], item['customer_email'],
                                    item['customer_points'])
                customer_request = CustomerRequest(customer, item['request'])
                queue.add_request(customer_request)

        except FileNotFoundError:
            print("\033[91mData file not found, starting with an empty database.\033[0m")
        except json.JSONDecodeError:
            print("\033[91mData file is corrupted, starting with an empty database.\033[0m")
        except KeyError:
            print("\033[91mData file is missing some required fields, starting with an empty database.\033[0m")
        except Exception:
            print(
                "\033[91mAn unexpected error occurred while loading data: {e}, starting with an empty database.\033[0m")


class Customer:
    def __init__(self, customer_id, customer_name, customer_email, customer_points):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_points = customer_points


def delete_customer(queue):
    while True:
        headers = ["No.", "Customer ID", "Customer Name", "Customer Email", "Customer Points", "Request"]
        data = [
            [i + 1, request.customer.customer_id, request.customer.customer_name, request.customer.customer_email,
             request.customer.customer_points, request.request]
            for i, request in enumerate(queue.requests)
        ]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        customer_num = input(
            "\033[96mEnter the number of the customer you want to delete (\033[0m\033[91mor type '!' to cancel\033[0m\033[96m): \033[0m")
        if customer_num == '!':
            print("\033[91mDeletion canceled.\033[0m")
            break
        else:
            try:
                customer_num = int(customer_num)
                if 0 < customer_num <= len(queue.requests):
                    deleted_request = queue.requests.pop(customer_num - 1)

                    # Check if there are any remaining requests for this customer
                    remaining_requests = [request for request in queue.requests if
                                          request.customer.customer_id == deleted_request.customer.customer_id]

                    # If there are no remaining requests, delete the customer
                    if not remaining_requests:
                        del queue.customers[deleted_request.customer.customer_id]

                    print("\033[92mCustomer deleted successfully.\033[0m")
                    break
                else:
                    print("\033[91mInvalid number. Please enter a number from the list.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a number.\033[0m")


class CustomerRequest:
    def __init__(self, customer, request):
        self.customer = customer
        self.request = request


def display_cars(cars):
    table = []
    for i, car in enumerate(cars, start=1):
        table.append([
            i,
            car.get_car_engine_no(),
            car.get_car_brand(),
            car.get_type(),
            car.get_mileage(),
            car.get_reg_year()
        ])

    headers = ["Car No", "Engine No", "Brand", "Type", "Mileage", "Reg Year"]
    print(tabulate(table, headers, tablefmt="fancy_grid"))


def customer_management_menu(queue):
    while True:
        print("\nCustomer Management Menu:")
        menu_options = [
            ["1", "\033[95mManually Add Customer\033[0m"],
            ["2", "\033[95mCocktail Sort by Customer ID\033[0m"],
            ["3", "\033[95mView Entire Database\033[0m"],
            ["4", "\033[95mDelete Customer\033[0m"],
            ["5", "\033[91mBack to Main Menu\033[0m"],
        ]
        table = tabulate(menu_options, headers=["Choice", "Option"], tablefmt="heavy_grid")
        print(table)

        choice = None
        while choice not in ['1', '2', '3', '4', '5']:
            choice = input("\033[96mEnter your choice (1-5): \033[0m")
            if choice not in ['1', '2', '3', '4', '5']:
                print("\033[91mInvalid choice. Please try again.\033[0m")

        if choice == '1':
            while True:
                customer_id = input(
                    "\033[96mEnter Customer ID (\033[0m\033[91mor type '!' to cancel\033[0m\033[96m):\033[0m")
                if customer_id == '!':
                    print("\033[91mRequest creation canceled.\033[0m")
                    break
                elif len(customer_id) > 5 or not re.match(r'^\d{4}[A-Za-z]$', customer_id):
                    print(
                        "\033[91mInvalid customer ID. Please enter an alphanumeric ID with 4 digits and 1 alphabetic character.\033[0m")
                else:
                    if queue.get_customer_by_id(customer_id):
                        print("\033[91mThis Customer ID already exists. Please enter a unique ID.\033[0m")
                        continue
                    customer_name = None
                    while customer_name is None or not re.match(r'^[A-Za-z\s]+$', customer_name):
                        customer_name = input(
                            "\033[96mEnter Customer Name (\033[0m\033[91mor type '!' to cancel\033[0m\033[96m): \033[0m")
                        if customer_name == '!':
                            print("\033[91mRequest creation canceled.\033[0m")
                            break
                        elif not re.match(r'^[A-Za-z\s]+$', customer_name):
                            print(
                                "\033[91mInvalid customer name. Please enter alphabetic characters and spaces only.\033[0m")
                        else:
                            customer_email = None
                            while customer_email is None or not re.match(
                                    r'^[\w.-]+@(gmail\.com|yahoo\.com|nyp\.edu\.sg)$', customer_email):
                                customer_email = input(
                                    "\033[96mEnter Customer Email (\033[0m\033[91mor type '!' to cancel\033[0m\033[96m): \033[0m")
                                if customer_email == '!':
                                    print("\033[91mRequest creation canceled.\033[0m")
                                    break
                                elif not re.match(r'^[\w.-]+@(gmail\.com|yahoo\.com|nyp\.edu\.sg)$', customer_email):
                                    print(
                                        "\033[91mInvalid email format. Please enter a valid email address.\033[0m")
                                else:
                                    customer_points = None
                                    while customer_points is None or not re.match(r'^[1-9]\d{0,3}$|^10000$',
                                                                                  customer_points):
                                        customer_points = input(
                                            "\033[96mEnter Customer Points (\033[0m\033[91mor type '!' to cancel\033[0m\033[96m): \033[0m")
                                        if customer_points == '!':
                                            print("Request creation canceled.")
                                            break
                                        elif not re.match(r'^[1-9]\d{0,3}$|^10000$', customer_points):
                                            print(
                                                "\033[91mInvalid points. Please enter a number from 1 to 10000.\033[0m")
                                        else:
                                            existing_customer = None
                                            for req in queue.requests:
                                                if req.customer.customer_id == customer_id:
                                                    existing_customer = req.customer
                                                    break
                                            if existing_customer is not None:
                                                print("\033[92mCustomer already exists.\033[0m")
                                                new_request = input(
                                                    "\033[96mEnter the new request for the customer: \033[0m")
                                                new_customer_request = CustomerRequest(
                                                    existing_customer,
                                                    new_request
                                                )
                                                queue.add_request(new_customer_request)
                                                print("\033[92mNew request added for the existing customer.\033[0m")
                                            else:
                                                customer = Customer(
                                                    customer_id, customer_name, customer_email, customer_points
                                                )
                                                request = input("\033[96mEnter your request: \033[0m")
                                                customer_request = CustomerRequest(customer, request)
                                                queue.add_request(customer_request)
                                                print("\033[92mNew customer and request added successfully.\033[0m")
                                            break
                                    break
                            break
                    break

        elif choice == '2':
            headers = ["No.", "Customer ID", "Customer Name", "Customer Email", "Customer Points", "Request"]
            data = [
                [i + 1, request.customer.customer_id, request.customer.customer_name, request.customer.customer_email,
                 request.customer.customer_points, request.request]
                for i, request in enumerate(queue.requests)
            ]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

            cocktail_sort_by_id(queue.requests)
            print("\033[92mCustomer requests sorted using Cocktail Sort by Customer ID.\033[0m")

        elif choice == '3':
            headers = ["No.", "Customer ID", "Customer Name", "Customer Email", "Customer Points", "Request"]
            data = [
                [i + 1, request.customer.customer_id, request.customer.customer_name, request.customer.customer_email,
                 request.customer.customer_points, request.request]
                for i, request in enumerate(queue.requests)
            ]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        elif choice == '4':
            delete_customer(queue)

        elif choice == '5':
            break


def main_menu():
    queue = Queue()
    DataManager.load_data(queue)

    if queue.get_num_requests() == 0:
        sample_requests = [
            ("1234A", "John Doe", "john.doe@example.com", "500", "Need assistance with product return."),
            ("5678B", "Jane Smith", "jane.smith@example.com", "2500", "Inquire about upcoming promotions."),
            ("9876C", "David Johnson", "david.johnson@example.com", "8000", "Report an issue with online payment."),
            ("4321D", "Sarah Anderson", "sarah.anderson@example.com", "1500",
             "Request a refund for a defective product."),
            ("2468E", "Michael Brown", "michael.brown@example.com", "3000", "Update shipping address for an order.")
        ]

        for request in sample_requests:
            customer = Customer(*request[:4])
            customer_request = CustomerRequest(customer, request[4])
            queue.add_request(customer_request)

    while True:
        print("\nManage Customer Request Menu:")
        menu_options = [
            ["1", "\033[95mAdd Request for Existing Customer\033[0m"],
            ["2", "\033[95mView Number of Requests\033[0m"],
            ["3", "\033[95mProcess Next Request\033[0m"],
            ["4", "\033[95mSearch for customers request (Linear Search)\033[0m"],
            ["5", "\033[95mAccess Customer Management\033[0m"],
            ["6", "\033[91mExit\033[0m"],
        ]
        table = tabulate(menu_options, headers=["Choice", "Option"], tablefmt="heavy_grid")
        print(table)

        try:
            choice = input("\033[96mEnter your choice (1-6) \033[91m(Press '!' to exit)\033[96m: \033[0m")
        except EOFError:
            print("\033[91mEnd of file reached.\033[0m")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("\033[91mPlease enter a valid choice.\033[0m")
            continue

        if choice == '!':
            DataManager.save_data(queue)
            break

        if choice == '1':
            while True:
                customer_id = input(
                    "\033[96mEnter Customer ID of existing customer \033[91m(Press '!' to exit)\033[96m: \033[0m")
                if customer_id == '!':
                    break
                if not InputValidator.validate_customer_id(customer_id):
                    print(
                        "\033[91mInvalid ID. Please enter an alphanumeric ID with 4 digits and 1 alphabetic character.\033[0m")
                    continue

                existing_customer = queue.get_customer_by_id(customer_id)
                if existing_customer:
                    new_request = input(
                        "\033[96mEnter the new request for the customer \033[91m(Press '!' to exit)\033[96m: \033[0m")
                    if new_request == '!':
                        break

                    new_customer_request = CustomerRequest(existing_customer, new_request)
                    queue.add_request(new_customer_request)
                    print("\033[92mNew request added for the existing customer.\033[0m")
                    break
                else:
                    print("\033[91mCustomer ID not found.\033[0m")

        elif choice == '2':
            num_requests = queue.get_num_requests()
            print("\033[96mNumber of customer requests in the queue:\033[0m", num_requests)

        elif choice == '3':
            processed_request = queue.process_next_request()
            if processed_request is not None:
                headers = ["Field", "Value"]
                data = [
                    ["Customer Name", processed_request.customer.customer_name],
                    ["Request", processed_request.request]
                ]
                table = tabulate(data, headers=headers, tablefmt="heavy_grid")
                print("\033[96mProcessing customer request:\n\033[0m")
                print(table)
                print("\033[96m\nRemaining customer requests in the queue:\033[0m", queue.get_num_requests())
            else:
                print("\033[91mNo customer requests in the queue.\033[0m")

        elif choice == '4':
            search_term = input("\033[96mEnter a search term \033[91m(Press '!' to exit)\033[96m: \033[0m")
            if search_term == '!':
                break
            if len(search_term) == 0:
                print("\033[91mSearch term cannot be empty.\033[0m")
                continue

            search_results = queue.search_requests(search_term)
            if search_results:
                headers = ["Customer ID", "Customer Name", "Customer Email", "Customer Points", "Request"]
                data = [
                    [request.customer.customer_id, request.customer.customer_name, request.customer.customer_email,
                     request.customer.customer_points, request.request]
                    for request in search_results
                ]
                table = tabulate(data, headers=headers, tablefmt="fancy_grid")
                print("\033[92mSearch results:\033[0m")
                print(table)
            else:
                print("\033[91mNo requests found matching that search term.\033[0m")

        elif choice == '5':
            customer_management_menu(queue)

        elif choice == '6':
            DataManager.save_data(queue)
            break


cars = []

car_1 = Car("123456789", "Toyota", "Corolla", 10000, 2015)
car_2 = Car("987654321", "Toyota", "Civic", 2000, 2010)
car_3 = Car("543210987", "Nissan", "Altima", 3000, 2015)
car_4 = Car("321098765", "Mazda", "Corolla", 4000, 2000)
car_5 = Car("109876543", "Subaru", "Impreza", 5000, 1995)
car_6 = Car("123123213", "Subaru", "Volvo", 4000, 2015)
cars.extend([car_1, car_2, car_3, car_4, car_5, car_6])

error_encountered = False

header = """\033[96m 
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ███████ ██ ███    ██  ██████   ██████  █████  ██████  
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██      ██ ████   ██ ██       ██      ██   ██ ██   ██ 
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ███████ ██ ██ ██  ██ ██   ███ ██      ███████ ██████  
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██          ██ ██ ██  ██ ██ ██    ██ ██      ██   ██ ██   ██ 
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ███████ ██ ██   ████  ██████   ██████ ██   ██ ██   ██\033[0m"""

menu_options = [
    ["  1", "\033[95mDisplay all cars\033[0m"],
    ["  2", "\033[95mAdd a new car\033[0m"],
    ["  3", "\033[95mSort cars by brand (Ascending Order) (Bubble Sort)\033[0m"],
    ["  4", "\033[95mSort cars by mileage (Descending Order) (Insertion Sort)\033[0m"],
    ["  5", "\033[95mSort Cars by Category (Ascending/Descending) (Radix Sort)\033[0m"],
    ["  6", "\033[95mSort Cars by Type (Ascending Order) (Selection Sort)\033[0m"],
    ["  7",
     "\033[95mSort Cars by Registration year first, then car engine number (Ascending Order) (Merge Sort)\033[0m"],
    ["  8", "\033[95mSearch Car by Engine number\033[0m"],
    ["  9", "\033[95mFilter cars by category\033[0m"],
    ["  10", "\033[95mDelete a car\033[0m"],
    ["  11", "\033[95mEdit a car's details\033[0m"],
    ["  12", "\033[95mManage Customer Requests\033[0m"],
    ["  13", "\033[91mExit\033[0m"],
]

print(header)

while True:
    print("\n\033[1mWhat would you like to do?\033[0m")
    table = tabulate(menu_options, headers=["Choice", "Option"], tablefmt="heavy_grid", stralign="left")
    print(table)

    try:
        choice = input("\033[97mEnter your choice: \033[0m")
    except EOFError:
        print("\033[91mEnd of file reached.\033[0m")
        break

    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
        print("\033[91mPlease enter a valid choice.\033[0m")
        continue

    if choice == "1":
        print("\n\033[1mHere is a list of all cars:\033[0m")
        display_cars(cars)
    elif choice == "2":
        new_car = input_car_details()
        cars.append(new_car)
        print("\033[92mCar added successfully!\033[0m")
    elif choice == "3":
        cars = bubble_sort(cars)
        print("\033[92mCars sorted by brand using bubble sort:\033[0m")
        display_cars(cars)
    elif choice == "4":
        cars = insertion_sort(cars)
        print("\033[92mCars sorted by mileage using insertion sort:\033[0m")
        display_cars(cars)
    elif choice == "5":
        valid_categories = ["1", "2", "3", "4", "5"]
        valid_orders = ["1", "2"]

        category = ""
        while category not in valid_categories:
            print("\033[96mAvailable categories to sort by:\033[0m")
            print("\033[94m1. Engine No.")
            print("2. Brand")
            print("3. Type")
            print("4. Mileage")
            print("5. Registration Year\033[0m")
            category = input("\033[96mEnter the category to sort by (1-5): \033[0m")

            if category not in valid_categories:
                print("\033[91mInvalid category. Please choose a valid category.\033[0m")

        order = ""
        while order not in valid_orders:
            print("\033[96mAvailable sorting orders:")
            print("1. Ascending")
            print("2. Descending\033[0m")
            order_input = input("\033[96mEnter the order to sort (1-2): \033[0m")

            if order_input in valid_orders:
                order = order_input
            else:
                print("\033[91mInvalid order. Please choose a valid order.\033[0m")

        Car.radix_sort(cars, category, order)
        category_name = {
            "1": "Engine No.",
            "2": "Brand",
            "3": "Type",
            "4": "Mileage",
            "5": "Registration Year"
        }
        order_name = {
            "1": "ascending",
            "2": "descending",
        }
        print(f"\033[96mCars have been sorted via {category_name[category]} and {order_name[order]} order!\033[0m")
    elif choice == "6":
        selection_sort_by_type(cars)
        display_cars(cars)
    elif choice == "7":
        sorted_cars = merge_sort_by_year_engine_no(cars)
        display_cars(sorted_cars)
    elif choice == "8":
        found_cars = Car.search_car_by_engine_no(cars)
        if found_cars:
            print("\033[1mMatching car found:\033[0m")
            display_cars(found_cars)
        else:
            print("\033[91mNo cars found with the provided engine number.\033[0m")
    elif choice == "9":
        display_cars(cars)
        filter_cars_by_category(cars)
    elif choice == "10":
        cars = delete_car_by_engine_no(cars)
    elif choice == "11":
        car_engine_no = input("\033[96mEnter the car engine number to edit: \033[0m")
        found_cars = [car for car in cars if car.get_car_engine_no() == car_engine_no]
        if found_cars:
            print("\033[92mMatching car found:\033[0m")
            display_cars(found_cars)
            confirm_edit = input("\033[96mAre you sure you want to edit this car? (yes/no): \033[0m")
            if confirm_edit.lower() == "yes":
                for car in found_cars:
                    edit_car_details(car)
        else:
            print("\033[91mInvalid Car engine number, Try again\033[0m")
    elif choice == "12":
        main_menu()
    elif choice == "13":
        print("\n\033[91mExiting car management system...\033[0m")
        break
    else:
        print("\n\033[91mInvalid choice! Please try again.\033[0m")
