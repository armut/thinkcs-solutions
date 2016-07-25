class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs & 60


    def add_time(t1, t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()

    def __gt__(self, other):
        return self.after(time2)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def between(self, t1, t2):
        if self.to_seconds() >= t1 and self.to_seconds() < t2:
            return True
        return False
