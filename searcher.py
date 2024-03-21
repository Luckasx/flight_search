import webbrowser
from datetime import datetime


def search(from_air, to_air, when_depart, when_return):

        depart_yymmdd = datetime.strftime(when_depart, '%y%m%d')
        depart_yyyy_mm_dd = datetime.strftime(when_depart, '%Y-%m-%d')

        returning_yymmdd = datetime.strftime(when_return, '%y%m%d')
        returning_yyyy_mm_dd = datetime.strftime(when_return, '%Y-%m-%d')

        urls = [f'https://www.skyscanner.com.br/transporte/passagens-aereas/{from_air}/{to_air}/{depart_yymmdd}/{returning_yymmdd}/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1#/details/11562-2409181110--32269,-30727-1-11493-2409190700|11493-2410012150--30727,-32269-1-11562-2410021025/index/13',
                f"https://www.kayak.com.br/flights/{from_air}-{to_air}/{depart_yyyy_mm_dd}/{returning_yyyy_mm_dd}/2adults?sort=bestflight_a"]


        for url in urls:
                webbrowser.open(url)


