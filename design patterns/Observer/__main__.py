from .kpis import KPIs

from .currentkpis import CurrentKPIs
from .forecast import ForecastKPIs


with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25,10,5)
        kpis.set_kpis(5,20,15)
        kpis.set_kpis(2,54,25)

print('detaching...')
# kpis.detach(currentKPIs)
kpis.set_kpis(100, 200,200)