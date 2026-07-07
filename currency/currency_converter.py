import flet as ft
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_currency(amount, from_currency, to_currency):
    data = requests.get(API_URL).json()
    rates = data["rates"]
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("https://www.exchangerate-api.com/dpcs/supported-currencies")
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return converted

def main(page: ft.Page):
    page.title = "Currency Converter"
    page.window.width = 320
    page.window.height = 380
    page.padding = 20

    amount_input = ft.TextField(label="Amount",
                                value="1", width=280)
    
    from_input = ft.TextField(label="From currency",
                                value="USD", width=280)
    
    to_input = ft.TextField(label="To currency",
                                value="EUR", width=280)
    
    result_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    
    def convert_click(e):
        try:
            amount = float(amount_input.value)
            
            from_currency = from_input.value.upper()
            
            to_currency = to_input.value.upper()
            
            result = convert_currency(amount, from_currency, to_currency)
            
            result_text.value = f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}" 

        except Exception as ex:
            result_text.value = f"Error: {ex}"
        page.update()

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

ft.run(main)