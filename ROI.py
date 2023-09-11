'''Everything works except for my ROI method option.  
It always returns 0%..'''
class ROI:
    def __init__(self):
        self.rental_income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_investment = 0
        
        
# =============================================================================================
    def driver(self):
        while True:
            driver_choice = input("\n*---<ROI CALCULATOR MENU>---*\nHello! What would you like to calculate: [I]ncome / [E]xpenses / [C]ash Flow / [T]otal Investment / or [R]OI calculation? ").lower()

            if driver_choice in ('i','income'):
                self.add_monthly_income()

            elif driver_choice in ('e','expenses'):
                self.add_expenses()

            elif driver_choice in ('c','cash','cash flow'):
                self.add_monthly_income()
                self.add_expenses()
                self.get_cash_flow()

            elif driver_choice in ('t','total','total investment'):               
                self.calculate_total_investment()

            elif driver_choice in ('r','roi','return','return on investment'): 
                self.calculate_total_investment()              
                self.roi_calculator()

            else:
                print("Please enter a valid input.")

            return_to_user = input("Would you like to return to the Calculator Menu? [C]ontinue / [Q]uit: ")
            if return_to_user in ('q','quit'):
                print("...quiting ROI calculator. Have a nice day!\n")
                break
            elif return_to_user not in ('c','continue'):
                print("Invalid input, try again.")

# =============================================================================================
    def user_input(self, ask_user):
        while True:
            try:
                good_input = float(input(ask_user))
                break
            except ValueError:
                print("Invalid input. Please enter a number amount, EX: 200")

        return good_input

# =============================================================================================
    def add_monthly_income(self):
        rental_income = self.user_input("\nWhat is your monthly rental income? ")
        laundry = self.user_input("How much is your laundry per month? ")
        storage = self.user_input("How much is your storage per month? ")
        misc = self.user_input("Do you have any miscellaneous income? ")

        self.total_monthly_income = rental_income + laundry + storage + misc

        print(f"Total monthly income is: ${self.total_monthly_income}\n")

        return self.total_monthly_income
   
# =============================================================================================
    def add_expenses(self):
        tax = self.user_input("\nWhat do you pay on taxes? ")
        insurance = self.user_input("What does your insurance cost? ")
        utilities = self.user_input("How much do you pay on utilities? ")
        hoa = self.user_input("How much are you paying for HOA? Enter 0 if you dont have an HOA: ")
        lawn_care = self.user_input("How much do you pay for lawn service? ")
        vacancy = self.user_input("How much for vacancy? ")
        repairs = self.user_input("How much are you paying on repairs? ")
        cap_expentiures = self.user_input("How much for capital expenditures? ")
        prop_management = self.user_input("How much is your property management? ")
        mortgage = self.user_input("Finally, what is your mortgage? ")

        self.total_monthly_expenses = (tax + insurance + utilities + hoa + lawn_care + vacancy + 
                                    repairs + cap_expentiures + prop_management + mortgage)

        print(f"Total monthly expenses are: ${self.total_monthly_expenses}\n")

        return self.total_monthly_expenses    

# =============================================================================================
    def get_cash_flow(self):
        cash_flow = self.total_monthly_income - self.total_monthly_expenses
        self.cash_flow = cash_flow
        print(f"Monthly income of (${self.total_monthly_income}) - Monthly expenses of (${self.total_monthly_expenses}) =\nTotal monthly cash flow is (${self.cash_flow})\n")

        return cash_flow
        
# =============================================================================================    
    def calculate_total_investment(self):
        down_payment = self.user_input("\nWhat is your down payment? ")
        closing_costs = self.user_input("What are the closing costs? ")
        rehab_budget = self.user_input("What is the rehab budget? ")
        roi_misc = self.user_input("Do you have any miscellaneous fees? ")

        self.total_investment = (down_payment + closing_costs + rehab_budget + roi_misc)
    

        print(f"Total investment: ${self.total_investment}\n")

        return self.total_investment

# =============================================================================================        
    def roi_calculator(self):
        # self.add_monthly_income()
        # self.add_expenses()
        # self.calculate_total_investment()
        annual_cash_flow = (self.cash_flow * 12)
        # print(annual_cash_flow)
        cash_on_cash_roi = (annual_cash_flow / self.total_investment) * 100
        
        print(f"Your Return on Investment is {cash_on_cash_roi:.2%}")

        return cash_on_cash_roi
        

my_rental = ROI()
my_rental.driver()