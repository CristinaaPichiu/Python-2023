from csv_validate.Read import read_csv
from csv_validate.Validate import CSVValidator


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_not_empty(value):
    return bool(value)

def condition_genre(value):
    return bool(value is not None and len(value) >= 5)




# Define user-defined rules
rules = {
    'Title': is_not_empty,
    'Author': is_not_empty,
    'Genre': is_not_empty,
    'Year': is_integer,
    'Genre': condition_genre
}

# Provide the CSV file path
csv_file_path = 'csv_validate/data.csv'

# Read CSV data
csv_data = read_csv(csv_file_path)

# Initialize CSVValidator with rules
validator = CSVValidator(rules)

# Validate CSV data
validation_errors = validator.validate(csv_data)

# Display validation errors, if any
if validation_errors:
    for error in validation_errors:
        print(error)
else:
    print("CSV validation successful.")
