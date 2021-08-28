'''Niet! W Pythonie przeciążanie funkcji nie bangla. Dla osób które nie wiedzą czym jest przeciążanie -
chodzi o możliwość posiadania kilku funkcji o takiej samej nazwie, a różniących się tylko ilością
(ewentualnie typem) parametrów. W innych językach programowania w takiej sytuacji to która metoda
zostałaby wywołana zależałoby od podanych do niej parametrów. W Pythonie jest to zrobione zupełnie
inaczej. Przeciążanie nie działa, każda kolejna funkcja o tej samej nazwie przesłania jej poprzednie
wystąpienie. Sprawdźmy to w praktyce:'''

# class Witacz:
#     def powitaj(self):
#         print("No siemka!")
#     def powitaj(self,kogo):
#         print("No siemka {}!".format(kogo))
# w=Witacz()
# w.powitaj()

'''i dla odmiany: '''
class Witacz:
    def powitaj(self,kogo):
        print("No siemka {}!".format(kogo))
    def powitaj(self):
        print("No siemka!")
w=Witacz()
w.powitaj()