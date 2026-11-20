# validation.py - checks the data the user types. Raises ValueError if something is wrong.
# Planned functions:
#   validate_vehicle(...) -> validates the whole form before add_vehicle


def validate_vehicle(plate, year, price, km):

    try:
        plate = plate.strip()
        if plate == "":     
            return "Plate cannot be empty"
        

        intyear = int(year) #intyear = al valor del parametro convertido en entero, si falla, error...
        
        if not (intyear >= 1930 and intyear <= 2026):
            return "Year must be between 1930 & 2026"

        pricefloat = float(price)
        if not (pricefloat >= 0 and pricefloat <= 1000000):
            return "Price must be between 0 & 100000"
        
        floatkms = float(km)
        if not (floatkms >= 0 and floatkms <= 500000):
            return "Kms must be between 0 and 500000"
    
    except ValueError:
        return "Year, price and KMs must be numbers"

    return True


