"""
    字典推导式
"""

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
