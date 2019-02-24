from .helper import Helper

def row_colour(date):
    date = Helper().convert_date_to_datetime(date)

    if not date or not date.date() or date.date() > date.now().date():
        return '#0000FF'
    elif date.date() == date.now().date():
        return '#00802B'

    return '#FF0000'