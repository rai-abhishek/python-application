from calendar import monthrange


class Bill:
    """
    this class will create objects for bill. The bill will be defined on bill
    period and amount paid
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmates:
    """
    this class will create objects for flatmates person and will calculate the contribution
    """

    def __init__(self, name, stay_days):
        self.name = name
        self.stay_days = stay_days

    def pay(self, bill):
        days = Calculations.get_days_in_month(bill)
        return round(bill.amount * (self.stay_days / days), 2)


class PdfReport:
    """
    this class will create objects to generate PDF for bill period. It will contain
    the name of the person, bill period and individual contribution.
    """

    def __init__(self, filename):
        self.fileName = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


class Calculations:

    @staticmethod
    def month_to_num(string):
        """static function to calculate convert month abbreviation to month numbers"""
        return {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
        }[string]

    @staticmethod
    def get_days_in_month(string):
        num_month = int(Calculations.month_to_num(string.period.split()[0]))
        year = int(string.period.split()[1])
        num_days = monthrange(year, num_month)[1]
        return num_days


testbill = Bill(120, "March 2022")
obj1 = Flatmates('Abhishek', 20)
obj2 = Flatmates('Rakhee', 25)

print("each share", obj1.name, obj1.pay(testbill), obj2.name, obj2.pay(testbill))
