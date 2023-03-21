import json

from datetime import datetime

from chalice import Chalice

app = Chalice(app_name='DayServer')

@app.route('/day')
def day_info():  # put application's code here
    now = datetime.now()
    # now = datetime.strptime(f'12-25-2022', '%m-%d-%Y')
    day_of_year = now.timetuple().tm_yday
    year = now.year
    month = now.month
    day = now.day
    print( year )
    christmas_day_of_year = datetime.strptime(f'12-25-{year}', '%m-%d-%Y').timetuple().tm_yday
    if day_of_year > christmas_day_of_year:
        christmas_date = datetime.strptime( f'12-25-{year + 1}', '%m-%d-%Y' )
        new_now = datetime.strptime( f'{month}-{day}-{year}', '%m-%d-%Y' )
        days_to_Christmas = (christmas_date - new_now).days
    else:
        days_to_Christmas = christmas_day_of_year - day_of_year
    days_to_hanukkah = 352 - day_of_year
    dayInfo = {'day_of_year':day_of_year, 'days_to_christmas':days_to_Christmas, 'days_to_hanukkah':days_to_hanukkah}
    return json.dumps(dayInfo)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
