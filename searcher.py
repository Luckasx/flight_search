import webbrowser
from datetime import datetime, timedelta


def search(from_air, to_air, when_depart, when_return, search_days=0):

    counter = 0

    date_depart = datetime.strptime(when_depart, '%Y%m%d')
    date_return = datetime.strptime(when_return, '%Y%m%d')

    while counter <= search_days:        

        temp_depart = date_depart+timedelta(days=counter)
        temp_return = date_return+timedelta(days=counter)

        depart_yymmdd = datetime.strftime(temp_depart, '%y%m%d')
        depart_yyyy_mm_dd = datetime.strftime(temp_depart, '%Y-%m-%d')

        returning_yymmdd = datetime.strftime(temp_return, '%y%m%d')
        returning_yyyy_mm_dd = datetime.strftime(temp_return, '%Y-%m-%d')

        urls = [f'https://www.skyscanner.com.br/transporte/passagens-aereas/{from_air}/{to_air}/{depart_yymmdd}/{returning_yymmdd}/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1#/details/11562-2409181110--32269,-30727-1-11493-2409190700|11493-2410012150--30727,-32269-1-11562-2410021025/index/13',
                f"https://www.kayak.com.br/flights/{from_air}-{to_air}/{depart_yyyy_mm_dd}/{returning_yyyy_mm_dd}/2adults?sort=bestflight_a"]

        for url in urls:
            webbrowser.open(url)

        counter = counter + 1
