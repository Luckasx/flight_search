import webbrowser
from datetime import datetime, timedelta


def search(from_air, to_air, when_depart, when_return, search_days=0):
    '''
    from_air (string): AIRPORT, 
    to_air (string) AIRPORT,
    when_depart (string)  date with YYYYMMDD format,
    when_return (string) date with YYYYMMDD format, 
    search_days (int) days forward to search
    '''
    MAX_DAYS = 3
    counter = 0

    date_depart = datetime.strptime(when_depart, '%Y%m%d')
    date_return = datetime.strptime(when_return, '%Y%m%d')

    while counter <= search_days and counter < MAX_DAYS:        

        temp_depart = date_depart+timedelta(days=counter)
        temp_return = date_return+timedelta(days=counter)

        depart_yymmdd = datetime.strftime(temp_depart, '%y%m%d')
        depart_yyyy_mm_dd = datetime.strftime(temp_depart, '%Y-%m-%d')
        depart_mm_dd_yyyy = datetime.strftime(temp_depart, '%d-%m-%Y')

        returning_yymmdd = datetime.strftime(temp_return, '%y%m%d')
        returning_yyyy_mm_dd = datetime.strftime(temp_return, '%Y-%m-%d')
        returning_mm_dd_yyyy = datetime.strftime(temp_return, '%d-%m-%Y')

        urls = [f'https://www.skyscanner.com.br/transporte/passagens-aereas/{from_air}/{to_air}/{depart_yymmdd}/{returning_yymmdd}/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1#/details/11562-2409181110--32269,-30727-1-11493-2409190700|11493-2410012150--30727,-32269-1-11562-2410021025/index/13',
                f"https://www.kayak.com.br/flights/{from_air}-{to_air}/{depart_yyyy_mm_dd}/{returning_yyyy_mm_dd}/2adults?sort=bestflight_a",
                f"https://www.zupper.com.br/resultados?type=roundTrip&adultQty=1&childrenQty=0&infantQty=0&onlyBusinessClass=false&slices=%5B%7B%22originAirport%22:%22{from_air}%22,%22destinationAirport%22:%22{to_air}%22,%22departureDate%22:%22{depart_yyyy_mm_dd}%22%7D,%7B%22destinationAirport%22:%22{from_air}%22,%22originAirport%22:%22{to_air}%22,%22departureDate%22:%22{returning_yyyy_mm_dd}%22%7D%5D",
                f"https://www.viajanet.com.br/shop/flights/results/roundtrip/{from_air}/{to_air}/{depart_yyyy_mm_dd}/{returning_yyyy_mm_dd}/1/0/0?from=SB&di=1&reSearch=true",
                f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br&tipo=DF&de={from_air}&para={to_air}&ida={depart_mm_dd_yyyy}&volta={returning_mm_dd_yyyy}&ADT=1&CHD=0&INF=0"]

        for url in urls:
            webbrowser.open(url)
            print(url)

        counter = counter + 1
