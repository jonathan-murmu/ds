from .observer_abc import AbsObserver

class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_ticket = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f'current open tickets: {self.open_tickets}')
        print(f'closed tickets: {self.new_tickets}')
        print(f'new tickets: {self.closed_tickets}')

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)