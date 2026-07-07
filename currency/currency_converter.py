import flet as ft
import requests

# Public API that returns live exchange rates relative to USD.
# No API key required.
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(amount, from_currency, to_currency):
     """
    Convert `amount` from `from_currency` to `to_currency` using
    live exchange rates fetched from the API.
    """

    # Fetch the latest rates (all relative to USD as the base currency)
    data = requests.get(API_URL).json()
    rates = data["rates"]

    # Make sure both currency codes are actually supported by the API
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("https://www.exchangerate-api.com/dpcs/supported-currencies")
        
    # Step 1: normalize the input amount to USD
    usd_amount = amount / rates[from_currency]

    # Step 2: convert from USD to the target currency
    converted = usd_amount * rates[to_currency]
    
    return converted

def main(page: ft.Page):
    # Basic window setup
    page.title = "Currency Converter"
    page.window.width = 320
    page.window.height = 380
    page.padding = 20

    # Input field for the amount to convert (defaults to 1)
    amount_input = ft.TextField(label="Amount",
                                value="1", width=280)
    
    # Input field for the source currency code (defaults to USD)
    from_input = ft.TextField(label="From currency",
                                value="USD", width=280)
    
    # Input field for the target currency code (defaults to EUR)
    to_input = ft.TextField(label="To currency",
                                value="EUR", width=280)
    
    # Text element used to display the conversion result or errors
    result_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    
    def convert_click(e):
        try:
            # Parse the amount as a float (raises ValueError if invalid)
            amount = float(amount_input.value)
           
            # Normalize currency codes to uppercase (e.g. "usd" -> "USD")
            from_currency = from_input.value.upper()
            to_currency = to_input.value.upper()

            # Perform the actual conversion via the API
            result = convert_currency(amount, from_currency, to_currency)
            
            # Display the formatted result
            result_text.value = f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}" 

        except Exception as ex:
            # Catch invalid input, bad currency codes, network errors, etc.
            result_text.value = f"Error: {ex}"

        # Refresh the page so the updated result_text is shown
        page.update()

    # Build the page layout: title, inputs, convert button, and result
    page.add(
        ft.Column(
            controls=[
                ft.Text("Currency Converter", size=24,
                        weight=ft.FontWeight.BOLD),
                amount_input,
                from_input,
                to_input,
                ft.Button(content=ft.Text("Convert"), 
                                  on_click=convert_click, 
                                  width=280),
                result_text,
            ],
            spacing=15,
        )
    )
# Launch the Flet app, calling main() once the window session starts
ft.run(main)
