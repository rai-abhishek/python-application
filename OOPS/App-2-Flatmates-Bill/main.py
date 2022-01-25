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
        return bill * 30 / self.stay_days


class PdfReport:
    """
    this class will create objects to generate PDF for bill period. It will contain
    the name of the person, bill period and individual contribution.
    """

    def __init__(self, filename):
        self.fileName = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass
