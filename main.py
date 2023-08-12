# Here are implemented functions, classes, and calls
# And some libraries that have been used.

import matplotlib.pyplot as plt
from funcation import *
from resources import *
from colorama import init, Fore
import rich, os
from rich.text import Text
from rich.panel import Panel
os.system("cls" if os.name == "nt" else "clear")

# _____________________________________________________________________
rich.print(Panel(Text(" 📉 WELCOME TO THE OIL & GOLD STOCK MARKET 📉 ", justify="center")))
print(Fore.BLUE+ """\n \t \t \t \tThis program aims to monitor the current prices and changes in the oil and gold markets in real time and continuously
                                                You can follow price fluctuations and market trends and predict future changes.  
                                     This enhances your chances of making informed investment decisions and making outstanding profits.""")
print("\n")
print(Fore.WHITE + "⤵︎")
# ______________________________________________________________________
view_options()
while True:
    choice = input(Fore.RED + "☞ Enter your choice [ All ] → ")

    if choice == "1":
        display_oil_exports()
    elif choice == "2":
        display_oil_importers()
    elif choice == "3":
        display_gold_importers()
    elif choice == "4":
        display_Gold_Sources()
    # ______________________________________________________________________
    elif choice == "5":
        while True:
            print(Fore.WHITE + "\n--- GOLD ACCOUNT : ----\n ")
            print(Fore.BLACK +"◈ You can calculate the gram of GOLD you want, you must specify the karat \n")
            try:
                weight = float(input(Fore.BLUE + "● Enter the weight in grams: "))
                carat = int(
                    input(
                        Fore.BLUE
                        + "● Enter the carat : \n☉  14 \n☉  18 \n☉  21 \n☉  22 \n☉  24 \n☞  "
                    )
                )
                calculate_gold_price(weight, carat)

                exit_choice = input(
                    Fore.RED + "◢ Do you want to exit  of this option ? (Y/N): "
                )
                if exit_choice.lower() == "y":
                    break
            except ValueError:
                print(
                    Fore.RED + "🛑 Invalid input. Please enter a valid weight and carat."
                )
    # _______________________________________________________________________
    elif choice == "6":
        stocks = stock_prices
        print(Fore.WHITE + "\n --- Stocks : ---- \n")
        print(Fore.BLACK + "◈ Here, you can pick the firm and the type of stock  you want, and determine the total number of stocks you desire .")
        print(Fore.BLACK + "◈ Example : Aramco → Crude Oil - Company: Aramco |Type of oil Stock : Crude oil  \n")
        for stock, price in stocks.items():
            print(Fore.BLUE + f"{stock}: $ {price}")
        stock_type = input(Fore.WHITE + " \n● Enter the stock type: ")
        stock_company = input(Fore.WHITE + "● Enter the stock company: ")

        stock_company_with_type = f"{stock_company} {stock_type}"

        stock_price = stocks.get(stock_company_with_type, 0)
        stock_count = int(input("● Enter the number of stocks: "))
        stock_price *= stock_count
        stocks[stock_company_with_type] = stock_price
        print(
            Fore.GREEN
            + f"⚑ Total price for {stock_count} stocks of {stock_company} → $ {stock_price}"
        )
    # ______________________________________________________________________
    elif choice == "7":
        show_oil_export_chart()
    elif choice == "8":
        Gold_Source()
    # ______________________________________________________________________
    elif choice == "9":
        oil_company_data = oil_stock_prices(stock_prices)
        input("☞ Press - Enter - to choose another option . ")
    # ______________________________________________________________________

    elif choice == "10":
        # ------------------[ supervisor login ]----------------------

        print(Fore.WHITE + "-- Supervisor Login --")
        username = input(Fore.BLUE + "● username> ")
        password = input(Fore.BLUE + "● password> ")
        if (
            username == "Basma"
            and password == "1234"
            or username == "Ahmed"
            and password == "12345"
        ):
            print(Fore.GREEN + "⚑ Login successful.")
            print(Fore.WHITE + "\n-- Supervisor Operations --")
            print(Fore.BLUE + "● choose Product (Oil / Gold):")
            print("1. Gold ⚜️")
            print("2. Oil  ⛽️")
            product = int(input(Fore.WHITE + "→ "))

            # ------------------------[ Gold Operations ]-------------------
            if product == 1:
                print(Fore.WHITE + "---[ supervisor Operations(Gold) ]---")
                print(Fore.BLUE + "1. Add Gold Source")
                print("2. Modify Gold Source")
                print("3. Delete Gold Source")
                print("4. Add Gold Import")
                print("5. Modify Gold Import")
                print("6. Delete Gold Import")
                gold_option = int(input(Fore.WHITE + "→ "))
                # ------------------------[ Gold Source ]-------------------
                if gold_option == 1:  # add to gold sources
                    print(Fore.WHITE + "-- Add Gold Source :--")
                    gold_type = input(Fore.BLUE + "● Enter the gold type: ")
                    gold_price = float(input("● Enter the gold price: "))
                    currency_used = input("● Enter the currency used: ")
                    gold_city = input("● Enter the gold city: ")
                    gold_item = GoldSource(
                        gold_type, gold_price, currency_used, gold_city
                    )
                    gold_sources.append(gold_item)
                    print(Fore.GREEN + "⚑ Gold Source added successfully.")

                elif gold_option == 2:  # Modify Gold Source
                    print(Fore.WHITE + "--- Modify Gold Source :---")
                    print(Fore.BLUE + "● Enter the gold type to modify:")
                    gold_type = input(Fore.WHITE + " → ")
                 
                    if gold_type in [gold_item.Gold_type for gold_item in gold_sources]:
                        gold_item.Gold_type = input("● Enter the gold type: ")
                        gold_item.Gold_price = float(
                            input("● Enter the gold price: ")
                        )
                        gold_item.currency_used = input(
                            "● Enter the currency used: "
                        )
                        gold_item.Gold_city = input("● Enter the gold city: ")
                        print(Fore.GREEN + "⚑ Gold Source modified successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Gold Source not found.")

                elif gold_option == 3:  # Delete Gold Source
                    print(Fore.WHITE + " --- Delete Gold Source :---")
                    print(Fore.BLUE + "● Enter the gold type to delete:")
                    gold_type = input(Fore.WHITE + "→  ")

                    if gold_type in [gold_item.Gold_type for gold_item in gold_sources]:
                        gold_sources.remove(gold_item)
                        print(Fore.GREEN + "⚑ Gold Source deleted successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Gold Source not found.")

                # ------------------------------------[ Gold Import ]--------------------------------

                elif gold_option == 4:  # Added Gold Import
                    print(Fore.WHITE + "-- Add Gold Import :--")
                    importing_country = input(
                        Fore.BLUE + "● Enter the importing country: "
                    )
                    possible_cost = float(input("● Enter the possible cost: "))
                    importing_NIC = input("● Enter the importing NIC: ")
                    type_imported_material = input(
                        "● Enter the type of imported material: "
                    )
                    import_country = ImportingCountries(
                        importing_country,
                        "Gold",
                        possible_cost,
                        importing_NIC,
                        type_imported_material,
                    )
                    gold_import_countries.append(import_country)
                    print(Fore.GREEN + "⚑ Gold Import added successfully.")

                elif gold_option == 5:  # Modify Gold Import
                    print(Fore.WHITE + "-- Modify Gold Import :--")
                    print(Fore.BLUE + "● Enter the importing country to modify : ")
                    importing_country = input(Fore.WHITE + "→  ")
                    if importing_country in [import_country.Importing_Country for import_country in gold_import_countries]:
                        import_country.Importing_Country = input(
                            "● Enter the importing country: "
                        )
                        import_country.Imported_need = input(
                            "● Enter the imported need: "
                        )
                        import_country.Possible_cost = float(
                            input("● Enter the possible cost: ")
                        )
                        import_country.Importing_NIC = input(
                            "● Enter the importing NIC: "
                        )
                        import_country.Type_imported_material = input(
                            "● Enter the type of imported material: "
                        )
                        print(Fore.GREEN + "⚑ Gold Import modified successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Gold Import not found.")

                elif gold_option == 6:  # Delete Gold Import
                    print(Fore.WHITE + "-- Delete Gold Import :--")
                    print(Fore.BLUE + "● Enter the importing country to delete:")
                    importing_country = input(Fore.WHITE + "→ ")
                    if importing_country in [import_country.Importing_Country for import_country in gold_import_countries]:
                        gold_import_countries.remove(import_country)
                        print(Fore.GREEN + "⚑ Gold Import deleted successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Gold Import not found.")
                else:
                    print("◢ Invalid option.")

            # -----------------------------[ Oil Operations ]---------------------------
            elif product == 2:
                print(Fore.WHITE + "---[ supervisor Operations(Oil) ]---")
                print(Fore.BLUE + "1. Add Oil Export")
                print("2. Modify Oil Export")
                print("3. Delete Oil Export")
                print("4. Add Oil Import")
                print("5. Modify Oil Import")
                print("6. Delete Oil Import")
                oil_option = int(input(Fore.WHITE + "→ "))

                # ------------------------------[ Oil Export ]-------------------------------------

                if oil_option == 1:  # Added Oil Export
                    print(Fore.WHITE + "-- Add Oil Export :--")
                    petroleum_Type = input(Fore.BLUE + "● Enter the petroleum type: ")
                    oil_price = float(input("● Enter the oil price: "))
                    Export_date = input("● Enter the export date: ")
                    Export_Country = input("● Enter the export country: ")
                    Currency_used = input("● Enter the currency used: ")
                    Export_cost = float(input("● Enter the export cost: "))
                    export_country = ExportingCountries(
                        petroleum_Type,
                        oil_price,
                        Export_date,
                        Export_Country,
                        Currency_used,
                        Export_cost,
                    )
                    export_countries.append(export_country)
                    print(Fore.GREEN + "⚑ Oil Export added successfully.")

                elif oil_option == 2:  # Modify Oil Export
                    print(Fore.WHITE + "-- Modify Oil Export :--")
                    print(Fore.BLUE + "● Enter the export country to modify :")
                    Export_Country = input(Fore.WHITE + "→ ")

                    this_exporting_countries = [export_country.Export_Country for export_country in export_countries]

                    if Export_Country in this_exporting_countries:
                        selected_export_country = export_countries[this_exporting_countries.index(Export_Country)]
                        selected_export_country.petroleum_Type = input(
                            Fore.BLUE + "● Enter the petroleum type: "
                        )
                        selected_export_country.oil_price = float(
                            input("● Enter the oil price: ")
                        )
                        selected_export_country.Export_date = input(
                            "● Enter the export date: "
                        )
                        selected_export_country.Export_Country = input(
                            "● Enter the export country: "
                        )
                        selected_export_country.Currency_used = input(
                            "● Enter the currency used: "
                        )
                        selected_export_country.Export_cost = float(
                            input("● Enter the export cost: ")
                        )
                        print(Fore.GREEN + "⚑ Oil Export modified successfully.")
                        
                        
                    else:
                        print(Fore.RED + "🛑 Oil Export not found.")
                    
                elif oil_option == 3:  # Delete Oil Export
                    print(Fore.WHITE + "-- Delete Oil Export :--")
                    print(Fore.BLUE + "● Enter the export country to delete:")
                    Export_Country = input(Fore.WHITE + "→ ")

                    this_exporting_countries = [export_country.Export_Country for export_country in export_countries]

                    if Export_Country in this_exporting_countries:
                        selected_export_country = export_countries[this_exporting_countries.index(Export_Country)]
                        
                        export_countries.remove(selected_export_country)
                        print(Fore.GREEN + "⚑ Oil Export deleted successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Oil Export not found.")

                # ------------------------------------[ Oil Import ]----------------------------------------------------

                elif oil_option == 4:  # Added oil import
                    print(Fore.WHITE + "-- Add Oil Import :--")
                    importing_country = input(
                        Fore.BLUE + "● Enter the importing country: "
                    )
                    possible_cost = float(input("● Enter the possible cost: "))
                    importing_NIC = input("● Enter the importing NIC: ")
                    type_imported_material = input(
                        "● Enter the type of imported material: "
                    )
                    import_country = ImportingCountries(
                        importing_country,
                        "Oil",
                        possible_cost,
                        importing_NIC,
                        type_imported_material,
                    )
                    oil_import_countries.append(import_country)
                    print(Fore.GREEN + "⚑ Oil Import added successfully.")

                elif oil_option == 5:  # modify oil import
                    print(Fore.WHITE + "-- Modify Oil Import :--")
                    print(Fore.BLUE + "● Enter the importing country to modify:")
                    importing_country = input(Fore.WHITE + "→ ")

                    this_importing_countries = [import_country.Importing_Country for import_country in oil_import_countries]

                    if importing_country in this_importing_countries:
                        selected_import_country = oil_import_countries[this_importing_countries.index(importing_country)]
                        selected_import_country.Importing_Country = input(
                            Fore.BLUE + "● Enter the importing country: "
                        )
                        selected_import_country.Possible_cost = float(
                            input("● Enter the possible cost: ")
                        )
                        selected_import_country.Importing_NIC = input(
                            "● Enter the importing NIC: "
                        )
                        selected_import_country.Type_imported_material = input(
                            "● Enter the type of imported material: "
                        )
                        print(Fore.GREEN + "⚑ Oil Import modified successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Oil Import not found.")

                elif oil_option == 6:  # delete oil import
                    print(Fore.WHITE + "-- Delete Oil Import :--")
                    print(Fore.BLUE + "● Enter the importing country to delete:")
                    importing_country = input(Fore.WHITE + "→ ")

                    this_importing_countries = [import_country.Importing_Country for import_country in oil_import_countries]

                    if importing_country in this_importing_countries:

                        selected_import_country = oil_import_countries[this_importing_countries.index(importing_country)]

                        oil_import_countries.remove(selected_import_country)
                        print(Fore.GREEN + "⚑ Oil Import deleted successfully.")
                        
                    else:
                        print(Fore.RED + "🛑 Oil Import not found.")
                else:
                    print("◢ Invalid option.")
        else:
            print(Fore.RED + "🛑 Login failed.")
    # _____________________________________________________________________________________________________________________
    elif choice == "11":
        print(
            Fore.GREEN
            + "\n ---[Thank you for using our software We look forward to serving you again ☻]---"
        )
        break
    else:
        view_options()
        print(
            Fore.RED
            + "🛑 This option is not available - choose from the options available to you "
        )
