class Roundtrip:

    adult_rate = 37550.0
    child_rate = (1 / 3) * adult_rate

    def __init__(self):

        self.adult_price = 0
        self.child_price = 0
        self.total_price = 0
        self.total_price_tax = 0
        self.final_price = 0

        self.adult_passangers = 0
        self.child_passangers = 0

        self.__menu()

    def get_input(self):

        self.adult_passangers = int(
            input("Enter the number of ADULT passangers travelling: ")
        )
        self.child_passangers = int(
            input("Enter the number of CHILD passangers travelling: ")
        )

        self.calc_price()

    def calc_price(self):

        self.adult_price = int(self.adult_passangers * Roundtrip.adult_rate)
        self.child_price = int(self.child_passangers * Roundtrip.child_rate)

        self.display_price()

    def __menu(self):
        user_choice = input(
            """
Welcome to the round trip calculator from Mumbai to Dubai.
Please go through the following instructions and choose youe choice:

1. Press 1 to calculate price.
2. Press 2 to quit.
"""
        )
        if user_choice == "1":
            self.get_input()
        elif user_choice == "2":
            print("Have a great day!!!!")
        else:
            print("Invalid Input.")

    def display_price(self):

        self.total_price = self.adult_price + self.child_price
        print("The total price will be {}.".format(self.total_price))

        self.service_tax()

    def service_tax(self):

        temp1 = (7 / 100) * self.total_price
        self.total_price_tax = int(self.total_price + temp1)
        print(
            "The total price with serivce tax will be {}.".format(self.total_price_tax)
        )

        self.final_price_met()

    def final_price_met(self):

        temp2 = (10 / 100) * self.total_price_tax
        self.final_price = self.total_price_tax - temp2
        print("The final price is Rs. {}.".format(round(self.final_price)))


object_1 = Roundtrip()
