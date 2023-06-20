class NationalPark:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name

    def trips(self, new_trip=None):
        from classes.trip import Trip

        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)

        return self._trips

    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor

        if (
            new_visitor
            and isinstance(new_visitor, Visitor)
            and new_visitor not in self._visitors
        ):
            self._visitors.append(new_visitor)

        return self._visitors

    def total_visits(self):
        from classes.trip import Trip

        return len(
            [trip.national_park for trip in Trip.all if trip.national_park == self]
        )

    def best_visitor(self):
        from classes.trip import Trip

        list_of_visitors = [
            trip.visitor for trip in Trip.all if trip.national_park == self
        ]
        return max(list_of_visitors, key=list_of_visitors.count)
