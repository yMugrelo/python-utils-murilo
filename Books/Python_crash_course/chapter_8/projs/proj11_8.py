def make_car(manufacturer, model, **kwargs):
    car_info = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
    }
    for key, value in kwargs.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
