# Greetings, instructions
print('Zdravstvuyte! This is "Obsolete Russian units of measurement" converter.')
print('Meet with russian native linear measures such as vershok, pyad, lokot, arshin, sazhen, versta and poprishche!')
print('But no need for worry: you can actually start with the good ol metre ;)')
print('Plus every calculation would be accompanied by metric conversion.')


# converting functions: rus_convert to convert between rus units and metric_convert to convert the result to metres

def rus_convert(value, unit_in, unit_out):
    rus_dict = {'metre': 2.136, 'vershok': 48, 'pyad': 12, 'lokot': 6, 'arshin': 3, 'sazhen': 1, 'versta': 0.002,
                'poprishche': 0.0001}
    return value * rus_dict[unit_out] / rus_dict[unit_in]


def metric_convert(value, unit_in):
    to_meter_dict = {'metre': 2.136, 'vershok': 48, 'pyad': 12, 'lokot': 6, 'arshin': 3, 'sazhen': 1, 'versta': 0.002,
                     'poprishche': 0.0001}
    return value * to_meter_dict['metre'] / to_meter_dict[unit_in]


# Dictionary for units checking

are_units_there = {'metre': 2.136, 'vershok': 48, 'pyad': 12, 'lokot': 6, 'arshin': 3, 'sazhen': 1, 'versta': 0.002,
                   'poprishche': 0.0001}

# Data input
original_amount = input('Please, enter the amount of input value: ')
if str.isdigit(original_amount):
    original_amount = float(original_amount)
    from_unit = input('and the input unit itself: ')
    if from_unit in are_units_there:
        to_unit = input('Now, enter the unit you want your value to be converted to: ')
        if to_unit in are_units_there:

            # Calculations
            rus_result = rus_convert(float(original_amount), str(from_unit), str(to_unit))
            metric_result = metric_convert(float(rus_result), str(to_unit))

            # Result output
            print('Your answer is', round(float(rus_result), 2), str(to_unit))
            print('which is the same as', round(metric_result, 2), 'metres')
        else:
            print('Unfortunately there is no such unit this converter knows of. Please choose one from the intro')
    else:
        print('Unfortunately there is no such unit this converter knows of. Please choose one from the intro')
else:
    print('Your amount is invalid. Please enter a number')
