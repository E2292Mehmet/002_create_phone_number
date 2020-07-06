# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

def create_phone_number(p):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])