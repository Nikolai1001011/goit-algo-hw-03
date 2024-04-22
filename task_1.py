from datetime import datetime

def get_days_from_today(date):
    try:
      # Convert a date string in the format 'YYYY-MM-DD' to a datetime object
        given_date = datetime.strptime(date, '%Y-%m-%d')
         # Getting the current date
        current_date = datetime.today()
        # Calculate the difference between the current date and the specified date
        delta = current_date - given_date
        # Return the difference in days as an integer
        return delta.days
    except ValueError:
        # Handling an invalid input format exception
        return "Неправильний формат дати. Використайте формат 'РРРР-ММ-ДД'."

#example
print(get_days_from_today("2006-11-11"))  # 6372