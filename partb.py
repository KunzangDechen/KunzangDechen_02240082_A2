class PokemonBinder:
    def __init__(self):
        self.binder = []  
        self.MAX_POKEDEX = 1025
        self.CARDS_in_PAGE = 64

    def add_card(self, num):
        if num < 1 or num > self.MAX_POKEDEX:
            print("Number not in valid range.")
        elif num in self.binder:
            print("This card is already in the binder.")
        else:
            self.binder.append(num)
            self.binder.sort()

            index = self.binder.index(num)
            page = index // self.CARDS_in_PAGE + 1
            position_on_page = index % self.CARDS_in_PAGE
            row = (position_on_page // 8) + 1
            column = (position_on_page % 8) + 1

            print("Card added!")
            print("Page:", page)
            print("Row:", row)
            print("Column:", column)

    def view_binder(self):
        print("You have", len(self.binder), "cards in the binder.")
        print("Cards added so far:")
        print(self.binder)

    def reset_binder(self):
        confirm = input("Type Reset to clear all cards: ")
        if confirm == "Reset":
            self.binder = []
            print("Binder has been reset.")
        else:
            print("Reset canceled.")

    def exit_program(self):
        print("Exiting program. Total cards:", len(self.binder))
        if len(self.binder) == self.MAX_POKEDEX:
            print("You have caught them all!")

class binder_manager:
    def __init__(self):
        self.binder = PokemonBinder()

    def run(self):
        while True:
            print("\nPokemon Binder Menu")
            print("1. Add a Pokemon card")
            print("2. View binder")
            print("3. Reset binder")
            print("4. Exit")

            choice = input("Enter your choice (1 to 4): ")

            if choice == "1":
                number_input = input("Enter your Pokedex number (1 to 1025): ")
                if number_input.isdigit():
                    self.binder.add_card(int(number_input))  # ← fix: use self.binder
                else:
                    print("That is not a valid number.")
            elif choice == "2":
                self.binder.view_binder()  # ← fix: use self.binder
            elif choice == "3":
                self.binder.reset_binder()  # ← fix: use self.binder
            elif choice == "4":
                self.binder.exit_program() 
                break
            else:
                print("Please enter a valid option.")
