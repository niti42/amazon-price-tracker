# Automated Amazon Tracker

This project tracks the price of an Amazon product and sends an email alert when the price drops below a specified target price. If you runthis code periodically, it will scrape the current price of the product from its Amazon page and compare it with the target price (price at which you want to buy).

## Prerequisites

- Python 3.x
- Requests library for making HTTP requests
- BeautifulSoup library for parsing HTML
- Dotenv library for managing environment variables
- An email-sending function (provided in `notifications.py`)

## Installation

1. **Clone this repository to your local machine**.
2. **Install the required dependencies using pip**:

   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

3. **Set up your environment variables**:

   Create a `.env` file in the root directory of your project and add your email credentials:

   ```env
   my_email=your_email@example.com
   password=your_email_password
   ```

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Input the product URL**:

   The script will prompt you to input the Amazon product URL you want to track.

3. **Set your target price**:

   The script compares the current price with the target price set in the code (`target_price = 300`).

4. **Receive email alerts**:

   If the current price drops below the target price, you will receive an email alert.
