# Here is a class indicating the source oil.
# There is a class indicating the source gold.
# Also, a class that contains countries that import oil and gold.
# It is also a function that indicates companies with stock of oil and its prices.


import matplotlib.pyplot as plt
from colorama import init, Fore


# ----------------------[ Oil Exporting ]---------------------------
class ExportingCountries:
    def __init__(
        self,
        petroleum_Type,
        oil_price: int,
        Export_date,
        Export_Country,
        Currency_used,
        Export_cost: int,
    ):
        self.petroleum_Type = petroleum_Type
        self.oil_price = oil_price
        self.Export_date = Export_date
        self.Export_Country = Export_Country
        self.Currency_used = Currency_used
        self.Export_cost = Export_cost

    def print_info(self):
        print(Fore.BLUE + "- Petroleum Type:", self.petroleum_Type, "⛽️")
        print("- Oil Price:", self.oil_price, "")
        print("- Export Date:", self.Export_date)
        print("- Export Country:", self.Export_Country)
        print("- Currency Used:", self.Currency_used)
        print("- Export Cost:", self.Export_cost)


export_country1 = ExportingCountries(
    "Crude Oil", 94.32, "1938", "Kingdom Saudi Arabia ", "SAR", 50_000
)
export_country2 = ExportingCountries(
    "Brent Crude oil ", 86.39, "1977", "United Kingdom", "USD", 10_000
)
export_country3 = ExportingCountries(
    "WTI Crude Oil", 83.64, "1930", " US State of Texas ", "USD", 11_000
)
export_country4 = ExportingCountries(
    "Heavy Crude Oil", 82.39, "1932", "Venezuela", "VEF", 18_000
)
export_country5 = ExportingCountries(
    "North Sea Crude ", 99.9, "1980", "North Pole", "USD", 90_000
)
export_country6 = ExportingCountries(
    "Russian Urals Crude", 70.9, "1900", "Russian", "RUB", 80_000
)
export_country7 = ExportingCountries(
    "Libyan crude ", 98.4, "1900", "Russian", "RUB", 60_000
)

export_countries = [
    export_country1,
    export_country2,
    export_country3,
    export_country4,
    export_country5,
    export_country6,
    export_country7,
]
petroleum_types = [country.petroleum_Type for country in export_countries]
export_costs = [country.Export_cost for country in export_countries]

# _________________________[ Chart ]___________________________


def show_oil_export_chart():
    plt.bar(petroleum_types, export_costs)
    plt.xlabel("Petroleum Type")
    plt.ylabel("Export Cost")
    plt.title("Export Costs by Petroleum Type")
    plt.xticks(rotation=45)
    plt.show()


# --------------------------[ Gold Source ]----------------------------------
class GoldSource:
    def __init__(self, Gold_type, Gold_price, currency_used, Gold_City):
        self.Gold_type = Gold_type
        self.Gold_price = Gold_price
        self.currency_used = currency_used
        self.Gold_city = Gold_City

    def print_info(self):
        print(Fore.BLUE + "- Gold Type:", self.Gold_type, "⚜️")
        print("- Gold Price:", self.Gold_price)
        print("- Currency Used:", self.currency_used)
        print("- Gold City:", self.Gold_city)


gold_item1 = GoldSource("24K", 3000, "RMB", "China")
gold_item2 = GoldSource("22K", 2500, "GHS", "Ghana")
gold_item3 = GoldSource("21K", 2000, "GBP", "London")
gold_item4 = GoldSource("18K", 1500, "ZAR", "South Africa")
gold_item5 = GoldSource("14K", 1000, "RUB", "Russian")
gold_item6 = GoldSource("10K", 800, "UZS", "Uzbakistan")
gold_item7 = GoldSource("24K", 3500, "CAD", "Canada")


gold_sources = [
    gold_item1,
    gold_item2,
    gold_item3,
    gold_item4,
    gold_item5,
    gold_item4,
    gold_item5,
    gold_item6,
    gold_item7,
]
gold_types = [item.Gold_type for item in gold_sources]
gold_prices = [item.Gold_price for item in gold_sources]

# _________________________[ Chart ]___________________________


def Gold_Source():
    plt.bar(gold_types, gold_prices)
    plt.xlabel("Gold Type")
    plt.ylabel("Gold Price")
    plt.title("Gold Prices by Type")
    plt.xticks(rotation=45)
    plt.show()


# ----------------------------[ Importing (GOLD / OIL)]-----------------------------------------


class ImportingCountries(ExportingCountries, GoldSource):
    def __init__(
        self,
        Importing_Country,
        Imported_need,
        Possible_cost: int,
        Importing_NIC,
        Type_imported_material,
    ):
        ExportingCountries.__init__(
            self,
            petroleum_Type=None,
            oil_price=None,
            Export_date=None,
            Export_Country=None,
            Currency_used=None,
            Export_cost=None,
        )
        GoldSource.__init__(
            self, Gold_type=None, Gold_price=None, currency_used=None, Gold_City=None
        )
        self.Importing_Country = Importing_Country
        self.Imported_need = Imported_need
        self.Type_imported_material = Type_imported_material
        self.Importing_NIC = Importing_NIC
        self.Possible_cost = Possible_cost

    def print_info(self):
        print(Fore.BLUE + "- Import Country:", self.Importing_Country, "♻️")
        print("- Imported Need:", self.Imported_need)
        print("- Possible Cost:", self.Possible_cost)
        print("- Importing NIC:", self.Importing_NIC)
        print("- Type of Imported Material:", self.Type_imported_material)


import_country1 = ImportingCountries(
    "United State", "Oil", 1000.9, "Kingdom Saudi Arabia", "Crude Oil"
)
import_country2 = ImportingCountries(
    "China", "Oil", 10_000, "United Kingdom", "Brent Crude oil"
)
import_country3 = ImportingCountries(
    "India", "Oil", 100_0000, "Venezuelan", "Heavy Crude Oil"
)
import_country4 = ImportingCountries(
    "France", "Oil ", 30_0000, "Russian", "Urals Crude"
)
import_country5 = ImportingCountries(
    "Switzrland", "Gold ", 60_0000, "South Africa", "24K"
)
import_country6 = ImportingCountries(
    "United Arab Emirates", "Gold ", 90_0000, "Uzbakistan", "24K"
)
import_country7 = ImportingCountries("Italy", "Gold ", 70_000, "Ghana", "22K")
import_country8 = ImportingCountries("Russian", "Gold ", 120_0000, "China", "18K")


oil_import_countries = [
    import_country1,
    import_country2,
    import_country3,
    import_country4,
]
gold_import_countries = [
    import_country5,
    import_country6,
    import_country7,
    import_country8,
]

# -------------------------------------[ STOCK - COMPANIES ]----------------------------------------------------------

stock_prices = {
    "Aramco Crude Oil": 100.70,
    "Chevron Brent": 80.67,
    "Marathon Petroleum WIT": 85.465,
    "CIED Heavy Crude Oil": 83.342,
    "SHELL Heavy Crude Oil": 80.456,
    "ExxonMobil Crude Oil": 90.345,
    "Resneft Heavy Crude Oil": 97.45,
    "TOTAL Brent": 96.095,
}


# _________________________[ Chart ]___________________________
def oil_stock_prices(stock_prices):
    companies = list(stock_prices.keys())
    prices = list(stock_prices.values())
    plt.bar(companies, prices)
    plt.xlabel("Company")
    plt.ylabel("Stock Price")
    plt.title("Oil Companies ")
    plt.xticks(rotation=45)
    plt.show()