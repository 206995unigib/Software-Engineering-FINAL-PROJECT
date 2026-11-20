# validation.py - checks the data the user types. Returns True if it's fine, or the error message.
# KIS: just simple ifs and one try/except.
# Planned functions:
#   validate_vehicle(...) -> validates the whole form before add_vehicle


def validate_vehicle(plate, year, price, km):

    try:
        plate = plate.strip()
        if plate == "":     
            return "Plate cannot be empty"
        

        intyear = int(year) #intyear = the parameter value converted to an integer, if it fails, error...
        
        if not (intyear >= 1930 and intyear <= 2026):
            return "Year must be between 1930 & 2026"

        pricefloat = float(price)
        if not (pricefloat >= 0 and pricefloat <= 10000000):
            return "Price must be between 0 & 10000000"
        
        floatkms = float(km)
        if not (floatkms >= 0 and floatkms <= 500000):
            return "Kms must be between 0 and 500000"
    
    except ValueError:
        return "Year, price and KMs must be numbers"

    return True


