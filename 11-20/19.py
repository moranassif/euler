class date:

    months = {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}

    def __init__(self, day, month, year, week_day):
        self.day = day
        self.month = month
        self.year = year
        self.week_day = week_day

    def inc_date(self):
        days_in_month = self.months[self.month]
        # Check leap
        if self.day == self.months[2] and self.month == 2 and self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            days_in_month += 1
        self.day += 1
        if self.day > days_in_month:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        self.week_day += 1
        self.week_day %= 7

    def check_sunday(self):
        return self.day == 1 and self.week_day == 0

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __str__(self):
        return "Day: {} Month: {} Year: {} Week day: {}".format(self.day, self.month, self.year, self.week_day)


d = date(1, 1, 1900, 1)
start = date(1, 1, 1901, 8)
limit = date(31, 12, 2000, 8)

sundays = 0
before = True
while d != limit:
    if d == start:
        before = False
    if d.check_sunday() and not before:
        sundays += 1
    d.inc_date()

print("sundays: {}".format(sundays))