# Here are the functions that will be called in (MAIN)
# Source oil data display function is available here.
# Also, a review function for imported oil is available
# And also the function of reviewing exported and imported gold
# And also the calculation function of gold in grams
# And also a function related to the availability of program options

from resources import *
from colorama import init, Fore
from colorama import init, Fore
from rich.console import Console
from rich.table import Table

#----------------------------------[option 1]-------------------------------------------
def display_oil_exports():
    print(Fore.BLUE +"\n")
    table = Table(title="Oil Exports ⛽️", show_lines=True, header_style="bold white")

    table.add_column("#", justify="center", style="bold white")
    table.add_column("Export Date", justify="center", style="blue")
    table.add_column("Export Country", justify="center", style="green")
    table.add_column("Petroleum Type", justify="center", style="cyan")
    table.add_column("Oil Price", style="magenta")
    table.add_column("Currency Used", justify="center", style="orange4")
    table.add_column("Export Cost", justify="center", style="bright_green")

    for index, country in enumerate(export_countries):
        table.add_row(f"{index+1}", country.Export_date, country.Export_Country, country.petroleum_Type, f"{country.oil_price}", country.Currency_used, f"{country.Export_cost}")
       
    console = Console()
    console.print(table)

#-------------------------------------------[option 2]----------------------    

def display_oil_importers():
    print(Fore.BLUE +"\n")

    table = Table(title="Oil Importing Countries ♻️", show_lines=True, header_style="bold white")

    table.add_column("#", justify="center", style="bold white")
    table.add_column("Importing Country", justify="center", style="yellow3")
    table.add_column("Type", justify="center", style="blue")
    table.add_column("Possible Cost", justify="center", style="violet")
    table.add_column("Importing NIC", justify="center", style="cyan")

    for index, country in enumerate(oil_import_countries):
        table.add_row(f"{index+1}",country.Importing_Country, country.Type_imported_material, f"{country.Possible_cost}", country.Importing_NIC)

    console = Console()
    console.print(table)


#-------------------------------------[opation 3]-------------------------------------------    

def display_gold_importers():
    print(Fore.BLUE +"\n")

    table = Table(title="Gold Importing Countries ♻️", show_lines=True, header_style="bold white")
    table.add_column("#", justify="center", style="bold white")
    table.add_column("Importing Country", justify="center", style="yellow3")
    table.add_column("Type", justify="center", style="blue")
    table.add_column("Possible Cost", justify="center", style="violet")
    table.add_column("Importing NIC", justify="center", style="cyan")

    for index, country in enumerate(gold_import_countries):
        table.add_row(f"{index+1}",country.Importing_Country, country.Type_imported_material, f"{country.Possible_cost}", country.Importing_NIC)

    console = Console()
    console.print(table)

#----------------------------------------[opation4]---------------------------------------------    


def display_Gold_Sources():
    print(Fore.BLUE +"\n")

    table = Table(title="Gold Sources ⚜️", show_lines=True, header_style="bold white")
    
    table.add_column("#", justify="center", style="bold white")
    table.add_column("Type", justify="center", style="yellow3")
    table.add_column("Price", justify="center", style="blue")
    table.add_column("Currency Used", justify="center", style="violet")
    table.add_column("Gold City", justify="center", style="cyan")

    for index, gold_source in enumerate(gold_sources):
        table.add_row(f"{index+1}", f"{gold_source.Gold_type}", f"{gold_source.Gold_price}", gold_source.currency_used, gold_source.Gold_city)

    console = Console()
    console.print(table)

#----------------------------------------[opation 5]-------------------------------------------------------    

def calculate_gold_price(weight, carat):
    price_per_gram = {14: 135.88, 18: 174.7, 21: 203.82, 22: 213.52, 24: 232.94}

    if weight <= 0:
        print(Fore.BLUE + "Invalid weight. Weight must be greater than zero.")
    elif carat not in price_per_gram:
        print(Fore.BLUE + "Invalid carat. Carat options are 14, 18, 21, 22, 24.")
    else:
        price = price_per_gram[carat]
        total_price = price * weight

        print(
            Fore.GREEN
            + f"⚑ Gold Price for {weight:.2f} grams of {carat} carat gold → $ {total_price:.2f}"
        )

#-----------------------------------------[all opations]-----------------

def view_options():
    my_options = [
    "Display oil exports ⛽️",
    "Display oil importers ♻️",
    "Display gold importers ♻️",
    "Display gold sources ⚜️",
    "Calculate gold price ⚜️",
    "Display stocks 📈",
    "Show Oil Export Chart 📊",
    "Gold Prices by Type chart 📊",
    "Oil Company chart 🏢",
    "Supervisor Operations 👥",
    "Exit 🛑",
]
    for index, option in enumerate(my_options):
        print(Fore.YELLOW + f"{index + 1}. {option}")