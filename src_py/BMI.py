def BMI():
    """To calculate your body index
    """
    weight_float = float(input('Please type up your weight(kg): '))
    height_float = float(input('Now please type up your height(cm): '))
    height = height_float / 100
    body_mass_index = weight_float / (height ** 2)
    BMI_ = str(body_mass_index)
    print('\nThank you very much!\n\nYour Body Mass Index is: ' + BMI_)
    return BMI()
BMI()

import doctest
doctest.testmod()