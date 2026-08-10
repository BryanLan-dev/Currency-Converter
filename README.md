# Currency Converter
<img width="304" height="341" alt="image" src="https://github.com/user-attachments/assets/0f8035fd-309e-4565-bf51-d688e97e4967" />

A simple desktop GUI app built with Python and Flet that converts amounts between currencies using live exchange rates.

## Features

- Clean, minimal desktop interface
- Live exchange rates pulled from a public API (no API key required)
- Convert between any currencies supported by the rate provider
- Input validation with inline error messages

## Requirements

- Python 3.12+
- `flet` (GUI framework)
- `requests` (for API calls)

## Setup

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd currency
   ```

2. **Install dependencies**
   ```bash
   py -m pip install flet requests
   ```

3. **Run it**
   ```bash
   py currency_converter.py
   ```

   The first run installs the Flet desktop runtime automatically (one-time setup).

## Usage

1. Enter an amount in the **Amount** field
2. Enter the currency you're converting **from** (e.g. `USD`)
3. Enter the currency you're converting **to** (e.g. `EUR`)
4. Click **Convert** to see the result

Currency codes are case-insensitive — the app automatically converts input to uppercase (e.g. `usd` -> `USD`).

## How It Works

The app fetches live exchange rates (relative to USD) from a free public API:

```python
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
```

To convert between two non-USD currencies, the amount is first normalized to USD, then converted to the target currency:

```python
usd_amount = amount / rates[from_currency]
converted = usd_amount * rates[to_currency]
```

The GUI is built with [Flet](https://flet.dev), which renders a native desktop window from Python code using Flutter under the hood.

## Notes

- Requires an internet connection to fetch live rates.
- If an invalid currency code is entered, the app displays a link to the list of supported currency codes.
- No API key needed - the exchange rate API used here is free and public.

## Future Improvements

- Cache exchange rates locally to reduce API calls
- Add a dropdown/autocomplete for currency selection instead of free text
- Display last-updated timestamp for the exchange rates
- Add support for historical exchange rate lookups
