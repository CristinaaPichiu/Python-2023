class CSVValidator:

    def __init__(self, rules):
        self.rules = rules

    def validate(self, data):
        errors = []
        for row_number, row in enumerate(data, start=1):
            for field, rule_func in self.rules.items():
                if field not in row:
                    errors.append(f"Row {row_number}: Missing value for field '{field}'.")
                elif not rule_func(row[field]):
                    errors.append(f"Row {row_number}: Validation failed for field '{field}'.")
        return errors
