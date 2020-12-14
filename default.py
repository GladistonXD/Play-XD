# -*- coding: utf-8 -*-
import urllib, urlparse, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, hashlib, re, urllib2, htmlentitydefs
import ftplib
from random import randrange
#import re
#import ssl
import requests
import codecs
from six.moves.html_parser import HTMLParser
#import urlresolver
#from bs4 import BeautifulSoup
Versao = "21.12.00"

AddonID = 'plugin.video.GladistonXD'
Addon = xbmcaddon.Addon(AddonID)
AddonName = Addon.getAddonInfo("name")
icon = Addon.getAddonInfo('icon')

addonDir = Addon.getAddonInfo('path').decode("utf-8")
iconsDir = os.path.join(addonDir, "resources", "images")

addonfolder = Addon.getAddonInfo('path')
cachefolder   = addonfolder + '/resources/'
libDir = os.path.join(addonDir, 'resources', 'lib')
sys.path.insert(0, libDir)
import common
addon_data_dir = xbmc.translatePath(Addon.getAddonInfo("profile")).decode("utf-8")
cacheDir = os.path.join(addon_data_dir, "cache")
if not os.path.exists(cacheDir):
	os.makedirs(cacheDir)

cadulto = Addon.getSetting("cadulto")
cPage = Addon.getSetting("cPage") # dublado redecanais
cPageleg = Addon.getSetting("cPageleg")
cPagenac = Addon.getSetting("cPagenac")
cPagelan = Addon.getSetting("cPagelan")
cPageflix = Addon.getSetting("cPageflix")
cPageser = Addon.getSetting("cPageser")
cPageani = Addon.getSetting("cPageani")
cPagedes = Addon.getSetting("cPagedes")
cPagefo1 = Addon.getSetting("cPagefo1")
cPageMMf = Addon.getSetting("cPageMMf")
cPageGOf = Addon.getSetting("cPageGOf")
cPageFlf = Addon.getSetting("cPageFlf")
cPageQlf = Addon.getSetting("cPageQlf")
cPageBIZ = Addon.getSetting("cPageBIZ")
cPageMEG = Addon.getSetting("cPageMEG")
cPageFHD = Addon.getSetting("cPageFHD")
cPageVZ = Addon.getSetting("cPageVZ")

cPageserQF = Addon.getSetting("cPageserQF")
cPageserSF = Addon.getSetting("cPageserSF")
cPageserVZ = Addon.getSetting("cPageserVZ")
cEPG = Addon.getSetting("cEPG")
cOrdFO = "date" if Addon.getSetting("cOrdFO")=="0" else "title"
cOrdRCF = "date" if Addon.getSetting("cOrdRCF")=="0" else "title"
cOrdRCS = "date" if Addon.getSetting("cOrdRCS")=="0" else "title"
cOrdNCF = Addon.getSetting("cOrdNCF")
cOrdNCS = Addon.getSetting("cOrdNCS")

cPlayD = Addon.getSetting("cPlayD") #play

Cat = Addon.getSetting("Cat")
Catfo = Addon.getSetting("Catfo")
CatMM = Addon.getSetting("CatMM")
CatGO = Addon.getSetting("CatGO")
CatFl = Addon.getSetting("CatFl")
CatBB = Addon.getSetting("CatBB")
CatQ1 = Addon.getSetting("CatQ1")
CatMG = Addon.getSetting("CatMG")
CatHD = Addon.getSetting("CatHD")
CatVZ = Addon.getSetting("CatVZ")


cSIPTV = Addon.getSetting("cSIPTV")

Clista0=[ "Lançamentos",  "Acao", "Faroeste", "Animacao", "Aventura", "Comedia", "Drama", "Fantasia", "Ficcao-cientifica", "Romance", "Suspense", "Terror"]
Clista1=["[COLOR blue][B]Lançamentos[/COLOR][/B]",  "[COLOR blue][B]Ação[/COLOR][/B]", "[COLOR blue][B]Faroeste[/COLOR][/B]", "[COLOR blue][B]Animação[/COLOR][/B]", "[COLOR blue][B]Aventura[/COLOR][/B]", "[COLOR blue][B]Comedia[/COLOR][/B]", "[COLOR blue][B]Drama[/COLOR][/B]", "[COLOR blue][B]Fantasia[/COLOR][/B]", "[COLOR blue][B]Ficção-ciêntifica[/COLOR][/B]", "[COLOR blue][B]Romance[/COLOR][/B]", "[COLOR blue][B]Suspense[/COLOR][/B]", "[COLOR blue][B]Terror[/COLOR][/B]"]
Clista2=["Sem filtro (Mostrar Todos)",  "Acao", "Faroeste", "Animacao", "Aventura", "Comedia", "Drama", "Fantasia", "Ficcao-cientifica", "Romance", "Suspense", "Terror"]
Clistafo0=[ "0",                        "48",         "3",    "7",        "8",        "5",       "4",      "14",                "16",      "15",       "11"]
Clistafo1=["Sem filtro (Mostrar Todos)","Lançamentos","Ação", "Animação", "Aventura", "Comédia", "Drama",  "Ficção-Científica", "Romance", "Suspense", "Terror"]
ClistaMM0=["ultimos","category/lancamentos","category/acao","category/animacao","category/aventura","category/comedia","category/drama","category/fantasia","category/ficcao-cientifica","category/guerra","category/policial","category/romance","category/suspense","category/terror"]
ClistaMM1=["[COLOR red][B]Ultimos Adicionados[/COLOR][/B]","[COLOR red][B]Lançamentos[/COLOR][/B]","[COLOR red][B]Ação[/COLOR][/B]","[COLOR red][B]Animação[/COLOR][/B]","[COLOR red][B]Aventura[/COLOR][/B]","[COLOR red][B]Comédia[/COLOR][/B]","[COLOR red][B]Drama[/COLOR][/B]","[COLOR red][B]Fantasia[/COLOR][/B]","[COLOR red][B]F. Científica[/COLOR][/B]","[COLOR red][B]Guerra[/COLOR][/B]","[COLOR red][B]Policial[/COLOR][/B]","[COLOR red][B]Romance[/COLOR][/B]","[COLOR red][B]Suspense[/COLOR][/B]","[COLOR red][B]Terror[/COLOR][/B]"]
ClistaGO0=["",                                                                  "ano-lancamento/2020",                    "ano-lancamento/2019",            "category/acao",                      "category/animacao",                "category/aventura",                                        "category/comedia",              "category/drama",                                     "category/fantasia",           "category/ficcao-cientifica",                                       "category/documentario",                        "category/faroeste",                               "category/romance",                              "category/suspense",                                        "category/terror", ]
ClistaGO1=["[COLOR deepskyblue][B]Mostrar Todos[/COLOR][/B]",    "[COLOR yellow][B]Lançamentos 2020[/COLOR][/B]", "[COLOR slategray][B]2019[/COLOR][/B]",      "[COLOR red][B]Ação[/COLOR][/B]", "[COLOR lime][B]Animação[/COLOR][/B]", "[COLOR darkorchid][B]Aventura[/COLOR][/B]", "[COLOR hotpink][B]Comédia[/COLOR][/B]",       "[COLOR springgreen][B]Drama[/COLOR][/B]", "[COLOR salmon][B]Fantasia[/COLOR][/B]", "[COLOR paleturquoise][B]Ficção-Científica[/COLOR][/B]","[COLOR crimson][B]Documentário[/COLOR][/B]","[COLOR darkorange][B]Faroeste[/COLOR][/B]","[COLOR deepskyblue][B]Romance[/COLOR][/B]", "[COLOR darkorchid][B]Suspense[/COLOR][/B]",             "[COLOR lightgreen][B]Terror[/COLOR][/B]"]
ClistaFl0=["filmes", "0", "genero/acao", "genero/animacao", "genero/aventura", "genero/comedia", "genero/drama", "genero/ficcao", "genero/romance", "genero/suspense", "genero/terror"]
ClistaFl1=["[COLOR yellow][B]Mostrar Todos[/COLOR][/B]", "[COLOR yellow][B]Lançamentos[/COLOR][/B]", "[COLOR yellow][B]Ação[/COLOR][/B]", "[COLOR yellow][B]Animação[/COLOR][/B]", "[COLOR yellow][B]Aventura[/COLOR][/B]", "[COLOR yellow][B]Comedia[/COLOR][/B]", "[COLOR yellow][B]Drama[/COLOR][/B]", "[COLOR yellow][B]Ficção Ciêntifica[/COLOR][/B]", "[COLOR yellow][B]Romance[/COLOR][/B]", "[COLOR yellow][B]Suspense[/COLOR][/B]", "[COLOR yellow][B]Terror[/COLOR][/B]"]
ClistaQUE10=["lancamentoss",                                               "acao",                            "animacao",                                "aventura",                             "comedia",                               "faroeste",                           "documentario",                       "fantasia",                       "drama",                                "ficcao-cientifica",                           "romance",                                                 "historia",                               "misterio",                           "suspense",                                "musica",                                 "terror",                             "thriller"]
ClistaQUE11=["[COLOR yellow][B]Lançamentos[/COLOR][/B]", "[COLOR yellow][B]Ação[/COLOR][/B]", "[COLOR yellow][B]Animação[/COLOR][/B]", "[COLOR yellow][B]Aventura[/COLOR][/B]",  "[COLOR yellow][B]Comedia[/COLOR][/B]",  "[COLOR yellow][B]Faroeste[/COLOR][/B]","[COLOR yellow][B]Documentário[/COLOR][/B]", "[COLOR yellow][B]Fantasia[/COLOR][/B]", "[COLOR yellow][B]Drama[/COLOR][/B]","[COLOR yellow][B]Ficção Ciêntifica[/COLOR][/B]", "[COLOR yellow][B]Romance[/COLOR][/B]",    "[COLOR yellow][B]História[/COLOR][/B]",  "[COLOR yellow][B]Mistério[/COLOR][/B]", "[COLOR yellow][B]Suspense[/COLOR][/B]", "[COLOR yellow][B]Música[/COLOR][/B]",    "[COLOR yellow][B]Terror[/COLOR][/B]", "[COLOR yellow][B]Thriller[/COLOR][/B]"]
ClistaBIZ10=["0", "acao",                                               "animacao",                                  "comedia",                               "faroeste",                           "policial",                        "fantasia",                                     "drama",                                "ficcao-cientifica",                           "romance",                                                 "documentario",                               "misterio",                           "suspense",                                     "nacionais",                                     "terror"]
ClistaBIZ11=["[COLOR yellow][B]Lançamentos[/COLOR][/B]" , "[COLOR yellow][B]Ação[/COLOR][/B]", "[COLOR yellow][B]Animação[/COLOR][/B]",     "[COLOR yellow][B]Comedia[/COLOR][/B]",  "[COLOR yellow][B]Faroeste[/COLOR][/B]","[COLOR yellow][B]Policial[/COLOR][/B]", "[COLOR yellow][B]Fantasia[/COLOR][/B]", "[COLOR yellow][B]Drama[/COLOR][/B]","[COLOR yellow][B]Ficção Ciêntifica[/COLOR][/B]", "[COLOR yellow][B]Romance[/COLOR][/B]",                       "[COLOR yellow][B]Documentário[/COLOR][/B]",  "[COLOR yellow][B]Mistério[/COLOR][/B]", "[COLOR yellow][B]Suspense[/COLOR][/B]","[COLOR yellow][B]Nacionais[/COLOR][/B]",       "[COLOR yellow][B]Terror[/COLOR][/B]"]
ClistaMEG10=["assistir-filmes-lancamentos-2020-online",                    "assistir-filmes-de-acao-online",             "assistir-filmes-de-animacao",                 "assistir-filmes-de-comedia-online",                      "faroeste",                                   "fantasia",                        "assistir-filmes-drama-online-dublado-legendado",                        "assistir-filmes-ficcao-cientifica-online",                           "assistir-filmes-de-romance-online-dublado-legendado",                                                 "documentario",                               "misterio",                           "suspense",                                     "assistir-filmes-de-terror-online-dublado-legendado"]
ClistaMEG11=["[COLOR yellow][B]Lançamentos[/COLOR][/B]",                   "[COLOR yellow][B]Ação[/COLOR][/B]",     "[COLOR yellow][B]Animação[/COLOR][/B]",          "[COLOR yellow][B]Comedia[/COLOR][/B]",  "[COLOR yellow][B]Faroeste[/COLOR][/B]",            "[COLOR yellow][B]Fantasia[/COLOR][/B]",               "[COLOR yellow][B]Drama[/COLOR][/B]",                             "[COLOR yellow][B]Ficção Ciêntifica[/COLOR][/B]",                             "[COLOR yellow][B]Romance[/COLOR][/B]",                                           "[COLOR yellow][B]Documentário[/COLOR][/B]",  "[COLOR yellow][B]Mistério[/COLOR][/B]", "[COLOR yellow][B]Suspense[/COLOR][/B]",    "[COLOR yellow][B]Terror[/COLOR][/B]"]
ClistaFHD10=["release-year/2020",                                                        "genero/acao",                       "genero/animacao",                           "genero/comedia",                      "genero/faroeste",                                   "genero/fantasia",                                    "genero/drama",                                                         "genero/ficcao",                                                                 "genero/romance",                                                                "genero/documentario",                               "genero/musical",                           "genero/suspense",                                     "genero/terror"]
ClistaFHD11=["[COLOR yellow][B]Lançamentos[/COLOR][/B]",                   "[COLOR yellow][B]Ação[/COLOR][/B]",     "[COLOR yellow][B]Animação[/COLOR][/B]",          "[COLOR yellow][B]Comedia[/COLOR][/B]",  "[COLOR yellow][B]Faroeste[/COLOR][/B]",            "[COLOR yellow][B]Fantasia[/COLOR][/B]",               "[COLOR yellow][B]Drama[/COLOR][/B]",                             "[COLOR yellow][B]Ficção Ciêntifica[/COLOR][/B]",                             "[COLOR yellow][B]Romance[/COLOR][/B]",                                           "[COLOR yellow][B]Documentário[/COLOR][/B]",  "[COLOR yellow][B]Mistério[/COLOR][/B]",          "[COLOR yellow][B]Suspense[/COLOR][/B]",                       "[COLOR yellow][B]Terror[/COLOR][/B]"]
ClistaVZ10=["0",   "all",                                                        "acao",                       "animacao",                           "comedia",                      "faroeste",                                   "fantasia",                                    "drama",                                                         "romance",                                                                "documentario",                               "musical",                           "suspense",                                     "terror"]
ClistaVZ11=["[COLOR yellow][B]Lançamentos[/COLOR][/B]", "[COLOR yellow][B]2020[/COLOR][/B]",                   "[COLOR yellow][B]Ação[/COLOR][/B]",     "[COLOR yellow][B]Animação[/COLOR][/B]",          "[COLOR yellow][B]Comedia[/COLOR][/B]",  "[COLOR yellow][B]Faroeste[/COLOR][/B]",            "[COLOR yellow][B]Fantasia[/COLOR][/B]",               "[COLOR yellow][B]Drama[/COLOR][/B]",                             "[COLOR yellow][B]Romance[/COLOR][/B]",                                           "[COLOR yellow][B]Documentário[/COLOR][/B]",  "[COLOR yellow][B]Mistério[/COLOR][/B]",          "[COLOR yellow][B]Suspense[/COLOR][/B]",                       "[COLOR yellow][B]Terror[/COLOR][/B]"]
def setViewS():
	xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
	xbmc.executebuiltin("Container.SetViewMode(50)")
def setViewM():
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(50)")
	
favfilmesFile = os.path.join(addon_data_dir, 'favoritesf.txt')
favseriesFile = os.path.join(addon_data_dir, 'favoritess.txt')
historicFile = os.path.join(addon_data_dir, 'historic.txt')

	
makeGroups = "true"
URLP="http://cubeplay.000webhostapp.com/"
#URLP="http://localhost:8080/"
URLNC=URLP+"cloud/v2/nc/"
URLFO=URLP+"fo/"

#proxy = "http://localhost:8080/index.php?q="
proxy = ""

protocol="http://"
protocol2="http://"
reference="https://canaisgratis.info/"
reference2="|verifypeer=false"
#reference2="|verifypeer=false&referer=https://redecanais.se/"
#reference2="|referer=https://redecanais.se/"
#reference2=""
#reference3="|Referer=https://canaisgratis.eu/&verifypeer=false&User-Agent=Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30"
reference3="|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
RC="redecanais.cloud/"
RC2="https://redecanais.cloud/"
RC3="https://redecanaistv.com/"
RC4="https://topflix.tv/"
	
def getLocaleString(id):
	return Addon.getLocalizedString(id).encode('utf-8')

def Categories(): #70
	#AddDir("[B]!{0}: {1}[/B] - {2} ".format(getLocaleString(30036), getLocaleString(30037) if makeGroups else getLocaleString(30038) , getLocaleString(30039)), "setting" ,50 ,os.path.join(iconsDir, "setting.png"), isFolder=False)
	#AddDir("[COLOR white][B][Canais de TV1][/B][/COLOR]" , "", 100, "http://oi68.tinypic.com/116jn69.jpg", "http://oi68.tinypic.com/116jn69.jpg")
	AddDir("[COLOR white][B]Canais de TV[/B][/COLOR]" , "", 108, "https://uploaddeimagens.com.br/images/002/440/396/original/TV.jpg", "https://uploaddeimagens.com.br/images/002/440/396/original/TV.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR white][B]Canais de TV opção 2[/B][/COLOR]" , "", -1, "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR white][B]Radio TV[/B][/COLOR]" , "", 106, "https://uploaddeimagens.com.br/images/002/527/445/original/Radio-tv-black.png", "https://uploaddeimagens.com.br/images/002/527/445/original/Radio-tv-black.png", info='[COLOR][/COLOR]')
	AddDir("[B][COLOR white]Filmes[/COLOR][/B]", "" , -2,"https://uploaddeimagens.com.br/images/002/376/272/original/TONY.jpg", "https://uploaddeimagens.com.br/images/002/376/272/original/TONY.jpg", isFolder=True, info='[COLOR][/COLOR]')
	AddDir("[COLOR white][B]Séries[/B][/COLOR]" , "", -3, "https://uploaddeimagens.com.br/images/002/376/145/original/Novo_3.jpg", "https://uploaddeimagens.com.br/images/002/376/145/original/Novo_3.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR green][B]Histórico Filmes[/B][/COLOR]", "" ,305 , "https://cdn2.iconfinder.com/data/icons/business-office-icons/256/To-do_List-512.png", "https://cdn2.iconfinder.com/data/icons/business-office-icons/256/To-do_List-512.png", info='[COLOR][/COLOR]')
	AddDir("[COLOR crimson][B]Pesquisa[/B][/COLOR]" , "", 160, "https://uploaddeimagens.com.br/images/002/376/135/original/941129_stock-photo-illustration-of-a-magnifying-glass.jpg", "https://uploaddeimagens.com.br/images/002/376/135/original/941129_stock-photo-illustration-of-a-magnifying-glass.jpg", "https://azure.microsoft.com/svghandler/search/?width=400&height=315", "https://azure.microsoft.com/svghandler/search/?width=400&height=315", info="Pesquisa em todo o Addon por palavra-chave")
	AddDir("[B][COLOR orange]Checar Atualizações[/COLOR][/B]", "" , 200,"https://uploaddeimagens.com.br/images/002/376/161/original/Update.jpg", "https://uploaddeimagens.com.br/images/002/376/161/original/Update.jpg", isFolder=False, info="Checar se há atualizações\n\nAs atualizações normalmente são automáticas\nUse esse recurso caso não esteja recebendo automaticamente\r\nVersão atual: "+Versao)
# --------------  Menu
def MCanais(): #-1
    AddDir("[COLOR yellow][B]Opção 1  [COLOR lightskyblue][B](REDE CANAIS)[/B][/COLOR]" , "", 102, "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", info='[COLOR][/COLOR]')
    AddDir("[COLOR yellow][B]Opção 2  [COLOR lightskyblue][B](MAX)[/B][/COLOR]"  , "", 111, "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", info='[COLOR][/COLOR]')
    AddDir("[COLOR yellow][B]Opção 3  [COLOR lightskyblue][B](TOP2)[/B][/COLOR]", "", 104, "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", info='[COLOR][/COLOR]')
    #AddDir("[COLOR yellow][B]Opção 4[/B][/COLOR]" , "", 107, "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", "https://uploaddeimagens.com.br/images/002/595/851/original/CanaisTV55.jpg", info='[COLOR][/COLOR]')
def MFilmes(): #-2
	#AddDir("[COLOR white][B][Filmes Dublado/Legendado][/B][/COLOR]" , cPage, 220, "https://walter.trakt.tv/images/movies/000/222/254/fanarts/thumb/401d5f083e.jpg", "https://walter.trakt.tv/images/movies/000/222/254/fanarts/thumb/401d5f083e.jpg", background="cPage")
	#AddDir("[B][COLOR cyan]Filmes Lançamentos MMFilmes[/COLOR][/B]", "config" , 184,"https://walter.trakt.tv/images/movies/000/191/797/fanarts/thumb/6049212229.jpg", "https://walter.trakt.tv/images/movies/000/191/797/fanarts/thumb/6049212229.jpg", isFolder=True, info='[COLOR][/COLOR]')
	AddDir("[B][COLOR cyan]Filmes MMFilmes[/COLOR][/B]", "config" , 180,"https://uploaddeimagens.com.br/images/002/376/272/original/TONY.jpg", "https://uploaddeimagens.com.br/images/002/376/272/original/TONY.jpg", isFolder=True, info='[COLOR][/COLOR]')
	#AddDir("[COLOR maroon][B]Filmes Lançamentos Topflix.tv[/B][/COLOR]" , "config", 310, "https://walter.trakt.tv/images/movies/000/219/436/fanarts/thumb/0ff039faa5.jpg", "https://walter.trakt.tv/images/movies/000/219/436/fanarts/thumb/0ff039faa5.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR maroon][B]Filmes Topflix.tv[/B][/COLOR]" , "config", 210, "https://uploaddeimagens.com.br/images/002/588/199/original/tomb.jpg", "https://uploaddeimagens.com.br/images/002/588/199/original/tomb.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR yellow][B]Filmes NetCine[/B][/COLOR]" , "", 71, "https://uploaddeimagens.com.br/images/002/376/273/original/THORR.jpg", "https://uploaddeimagens.com.br/images/002/376/273/original/THORR.jpg", info='[COLOR][/COLOR]')
	#AddDir("[COLOR palevioletred][B]Filmes VerFilmesHD[/B][/COLOR]" , "", 530, "https://uploaddeimagens.com.br/images/002/376/273/original/THORR.jpg", "https://uploaddeimagens.com.br/images/002/376/273/original/THORR.jpg", info='[COLOR][/COLOR]')
	#AddDir("[COLOR deepskyblue][B]Filmes Lançamentos Assistir.biz[/B][/COLOR]" , "", 517, "https://uploaddeimagens.com.br/images/002/644/779/original/Sarta2.jpg", "https://uploaddeimagens.com.br/images/002/644/779/original/Sarta2.jpg", info='[COLOR][/COLOR]')
	AddDir("[COLOR deepskyblue][B]Filmes Assistir.biz[/B][/COLOR]" , "", 514, "https://uploaddeimagens.com.br/images/002/644/778/original/STAR.png", "https://uploaddeimagens.com.br/images/002/644/778/original/STAR.png", info='[COLOR][/COLOR]')
	AddDir("[COLOR mediumpurple][B]Filmes Vizer.tv[/B][/COLOR]" , "", 600, "https://uploaddeimagens.com.br/images/002/711/818/full/django.jpg", "https://uploaddeimagens.com.br/images/002/711/818/full/django.jpg", info='[COLOR][/COLOR]')
	#AddDir("[COLOR springgreen][B]Filmes QuerofilmesHD[/B][/COLOR]" , "config", 510, "https://uploaddeimagens.com.br/images/002/640/063/original/Vin.png", "https://uploaddeimagens.com.br/images/002/640/063/original/Vin.png", info='[COLOR][/COLOR]')
	#AddDir("[COLOR blue][B]Filmes Lançamentos RedeCanais[/B][/COLOR]" , cPage, 221, "https://walter.trakt.tv/images/movies/000/222/216/fanarts/thumb/6f9bb1a733.jpg", "https://walter.trakt.tv/images/movies/000/222/216/fanarts/thumb/6f9bb1a733.jpg", background="cPage", info='[COLOR][/COLOR]')
	AddDir("[COLOR blue][B]Filmes Dublado RedeCanais[/B][/COLOR]" , cPage, 90, "https://uploaddeimagens.com.br/images/002/376/274/original/ROCKKAAS.jpg", "https://uploaddeimagens.com.br/images/002/376/274/original/ROCKKAAS.jpg", background="cPage", info='[COLOR][/COLOR]')
	AddDir("[COLOR blue][B]Filmes Legendado RedeCanais[/B][/COLOR]" , cPageleg, 91, "https://walter.trakt.tv/images/movies/000/181/313/fanarts/thumb/cc9226edfe.jpg", "https://walter.trakt.tv/images/movies/000/181/313/fanarts/thumb/cc9226edfe.jpg", background="cPageleg", info='[COLOR][/COLOR]')
	AddDir("[COLOR blue][B]Filmes Nacional RedeCanais[/B][/COLOR]" , cPagenac, 92, "http://cdn.cinepop.com.br/2016/11/minhamaeeumapeca2_2-750x380.jpg", "http://cdn.cinepop.com.br/2016/11/minhamaeeumapeca2_2-750x380.jpg", background="cPagenac", info='[COLOR][/COLOR]')
	#AddDir("[COLOR purple][B]Filmes FilmesOnline[/B][/COLOR]" , "", 170, "https://uploaddeimagens.com.br/images/002/428/080/original/ROBOZIm.jpg", "https://uploaddeimagens.com.br/images/002/428/080/original/ROBOZIm.jpg")
	AddDir("[COLOR lightgreen][B]Filmes Superflix[/B][/COLOR]" , "", 411, "https://uploaddeimagens.com.br/images/002/428/080/original/ROBOZIm.jpg", "https://uploaddeimagens.com.br/images/002/428/080/original/ROBOZIm.jpg", info='[COLOR][/COLOR]')
	setViewM()
def MSeries(): #-3
	AddDir("[COLOR yellow][B]Séries NetCine[/B][/COLOR]" , "", 60, "https://walter.trakt.tv/images/shows/000/098/898/fanarts/thumb/bca6f8bc3c.jpg", "https://walter.trakt.tv/images/shows/000/098/898/fanarts/thumb/bca6f8bc3c.jpg")
	AddDir("[COLOR blue][B]Séries RedeCanais[/B][/COLOR]" , cPageser, 130, "https://walter.trakt.tv/images/shows/000/001/393/fanarts/thumb/fc68b3b649.jpg", "https://walter.trakt.tv/images/shows/000/001/393/fanarts/thumb/fc68b3b649.jpg", background="cPageser", info='[COLOR][/COLOR]')
	AddDir("[COLOR blue][B]Animes RedeCanais[/B][/COLOR]" , cPageser, 140, "https://walter.trakt.tv/images/shows/000/098/580/fanarts/thumb/d48b65c8a1.jpg", "https://walter.trakt.tv/images/shows/000/098/580/fanarts/thumb/d48b65c8a1.jpg", background="cPageser", info='[COLOR][/COLOR]')
	AddDir("[COLOR blue][B]Desenhos RedeCanais[/B][/COLOR]" , cPageani, 150, "https://walter.trakt.tv/images/shows/000/069/829/fanarts/thumb/f0d18d4e1d.jpg", "https://walter.trakt.tv/images/shows/000/069/829/fanarts/thumb/f0d18d4e1d.jpg", background="cPageser", info='[COLOR][/COLOR]')
	AddDir("[B][COLOR cyan]Séries MMFilmes[/COLOR][/B]", "config" , 190,"https://walter.trakt.tv/images/shows/000/037/522/fanarts/thumb/6ecdb75c1c.jpg", "https://walter.trakt.tv/images/shows/000/037/522/fanarts/thumb/6ecdb75c1c.jpg", isFolder=True, info='[COLOR][/COLOR]')
	AddDir("[B][COLOR lightgreen]Séries Superflix[/COLOR][/B]", "config" , 401,"https://walter.trakt.tv/images/shows/000/037/522/fanarts/thumb/6ecdb75c1c.jpg", "https://walter.trakt.tv/images/shows/000/037/522/fanarts/thumb/6ecdb75c1c.jpg", isFolder=True, info='[COLOR][/COLOR]')
	#AddDir("[B][COLOR springgreen]Séries QueroFilmesHD[/COLOR][/B]", "config" , 430,"https://cdn.mensagenscomamor.com/content/images/p000024904.jpg?v=2", "https://cdn.mensagenscomamor.com/content/images/p000024904.jpg?v=2", isFolder=True, info='[COLOR][/COLOR]')
	AddDir("[B][COLOR mediumpurple]Séries Vizer.tv[/COLOR][/B]", "config" , 450,"https://cdn.mensagenscomamor.com/content/images/p000024904.jpg?v=2", "https://cdn.mensagenscomamor.com/content/images/p000024904.jpg?v=2", isFolder=True, info='[COLOR][/COLOR]')
	setViewM()
######################
def SerieMenuBZ(): # 450
	pagina = "0" if not cPageserVZ else cPageserVZ
	if int(pagina) > 0:
		AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageserVZ")
	y= int(pagina)*1
	for x in range(0, 1):
		try:
			y +=0
			link = common.OpenURL("https://vizer.tv/includes/ajax/ajaxPagination.php?categoriesListSeries=all&anime=0&search=&page="+ str(y) +"&categoryFilterYear=all&categoryFilterOrderBy=vzViews&categoryFilterOrderWay=desc&categoryFilterQuantity=28")
			f = json.loads(link)
			f2 = json.dumps(f, ensure_ascii=False)
			arquivo2 = urllib.quote(f2.encode('utf8'))
			String2 = urllib.unquote(arquivo2)
			match = re.compile('url".."([^\"]+)".+?poster.+?\/([^\"]+).+?tle".."([^\"]+)').findall(String2)
			if match:
				for url2, img2, name2 in match:
					img3 = "https://image.tmdb.org/t/p/original/" + img2
					url3 = "https://vizer.tv/serie/online/" + url2
					AddDir(name2, url3, 451, img3, img3, isFolder=True, IsPlayable=True, info="")
		except:
			pass
	AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageserVZ")
def SerieMenuBZ2(): # 451
	try:
		link = common.OpenURL(url)
		match = re.compile('id="(.+?)">(.+?)<\/div>').findall(link)
        	if match:
				for url2, name2 in match:
					AddDir("Temporada "+ name2, url2, 452, iconimage, iconimage, isFolder=True, IsPlayable=False, info="")
	except:
		pass
def SeriePlayBZ(): # 452
	try:	
		url3 = ('https://vizer.tv/includes/ajax/publicFunctions.php')
		result = {'getEpisodes': url}
		f = requests.post(url3, data=result)
		match = re.compile('id"."(.+?)"."title"."(.+?)"img"....(.+?)".+?"name"."(.+?)"').findall(f.text)
        	if match:
				for url2, name2, img2, numero in match:
					img3 = "https://image.tmdb.org/t/p/w500/" + img2
					AddDir(numero+" - " + name2.replace('",',""), url2, 453, img3, img3, isFolder=False, IsPlayable=True, info="")
	except:
		pass
def SeriePlayBZ22(): # 453
	try:	
		url3 = ('https://vizer.tv/includes/ajax/publicFunctions.php')
		result = {'getEpisodeLanguages': url}
		f = requests.post(url3, data=result)
		f1 = json.loads(f.text)
		f2 = json.dumps(f1, ensure_ascii=False)
		arquivo2 = urllib.quote(f2.encode('utf8'))
		String2 = urllib.unquote(arquivo2)
		if f:
			m2 = re.compile('lang".."(.+?)".+?:.+?"(.+?)"').findall(String2)
			listar=[]
			listal=[]
			for res, link in m2:
				listal.append(link)
				listar.append(res.replace("1","[COLOR red][B]Legendado[/B][/COLOR]").replace("2","[COLOR springgreen][B]Dublado[/B][/COLOR]"))
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione o idioma", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				urlx = "https://vizer.tv/embed/getEmbed.php?orvio=" + url2
				url4 = requests.get(urlx)
				link2 = re.compile('src="(http.+?)"').findall(url4.text)
				link2= link2[0].replace("?","#")
				if 'orvio' in link2:
					url23 = requests.get(link2)
					legenda = re.compile('videoId.+?"(.+?)".\s+.+\s.+.\s+.\s.+\s.+\s.+?var subsArray.+?"(.+?)"').findall(url23.text)
					archive = re.compile('hashLink.+?"(.+?)"').findall(url23.text)
					mp4 = "https://redirect.orvio.co/hd/" + archive[0]
					if legenda:
						for legenda2, id in legenda:
							id2 = id.replace("P","-P")
							legenda2 = "https://subs.orvio.co/"+legenda2+id2+".vtt"
							PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info, sub=legenda2)
					else:
						PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info)
				else:
					sys.exit()
			else:
				sys.exit()        
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado, tente outro servidor')
		sys.exit()
def SeriePlayBZ2(): # 453 #### opção 1
	try:	
		url3 = ('https://vizer.tv/includes/ajax/publicFunctions.php')
		result = {'getEpisodeLanguages': url}
		f = requests.post(url3, data=result)
		f1 = json.loads(f.text)
		f2 = json.dumps(f1, ensure_ascii=False)
		arquivo2 = urllib.quote(f2.encode('utf8'))
		String2 = urllib.unquote(arquivo2)
		if f:
			m2 = re.compile('lang".."(\w+)".+?id".."(.+?)"').findall(String2)
			listar=[]
			listal=[]
			for res, link in m2:
				listal.append(link)
				listar.append(res.replace("1","[COLOR red][B]Legendado[/B][/COLOR]").replace("2","[COLOR springgreen][B]Dublado[/B][/COLOR]"))
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione o idioma", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				url2x = "https://vizer.tv/includes/ajax/publicFunctions.php"
				result = {'showPlayer': url2}
				fx = requests.post(url2x, data=result)
				m22 = re.compile('"(\w+)".true').findall(fx.text)
				#m22.reverse()
				listar2=[]
				for res2 in m22:
					if "xxxxxxx" in res2: False
					else:
						listar2.append(res2.replace("fembed","[B][COLOR deepskyblue]Fembed[/B][/COLOR]").replace("mixdrop","[B][COLOR lightseagreen]Mixdrop[/B][/COLOR]").replace("mystream","[B][COLOR mediumseagreen]Mystream[/B][/COLOR]"))
				if len(listar2) <1:
					xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
					sys.exit(int(sys.argv[1]))
				d2 = xbmcgui.Dialog().select("Selecione o servidor", listar2)
				if d2!= -1:
					url32 = re.sub(' ', '%20', listar2[d2].replace("[B][COLOR deepskyblue]Fembed[/B][/COLOR]","fembed").replace("[B][COLOR lightseagreen]Mixdrop[/B][/COLOR]","mixdrop").replace("[B][COLOR mediumseagreen]Mystream[/B][/COLOR]","mystream") )
					urlx = "https://vizer.tv/embed/getPlay.php?id=" + url2 + "&sv=" + url32
					url4 = requests.get(urlx)
					legenda = re.compile("(.{1,7}\/wa.+?srt)").findall(url4.text)
					link2 = re.compile('href="(http.+?)"').findall(url4.text)
					link2= link2[0].replace("?","#")
					if 'mixdrop' in link2:
						headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
						html2 = requests.get(link2, headers=headers)
						g = re.compile('location.+?"(.+?)"').findall(html2.text)
						try:
							g2 = "https://mixdrop.to" + g[0]
							html = requests.get(g2, headers=headers)
							w = re.compile("'.MDCore.(.)").findall(html.text)
							w = w[0].replace("d","a")
							w1 = re.compile("(delivery\w+)").findall(html.text)
							w2 = re.compile("delivery\w+.(\w+)").findall(html.text)
							w3 = re.compile("referrer.(.+?)[|]").findall(html.text)
							w4 = re.compile("wurl.+?\W([0-9]+)\W").findall(html.text)
							w5 = re.compile("_t.+?\W(.+?)\W").findall(html.text)
							contents = "https://" + w + "-" + w1[0] + ".mxdcontent.net/v/" + w2[0] + ".mp4?s=" + w3[0] + "&e=" + w4[0] + "&_t=" + w5[0]
							contents1 = contents.replace("|vfile", "").replace("|", "-")
							contents2 = re.sub('\W\d+-', '', contents1)
							if legenda:
								legenda = legenda[0]
								if not "http" in legenda:
									legenda = legenda
								PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info, sub=legenda)
							else:
								PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info)
						except IndexError as g2:
							pass
						headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
						html = requests.get(link2, headers=headers)
						w = re.compile("'.MDCore.(.)").findall(html.text)
						w = w[0].replace("d","a")
						w1 = re.compile("(delivery\w+)").findall(html.text)
						w2 = re.compile("delivery\w+.(\w+)").findall(html.text)
						w3 = re.compile("referrer.(.+?)[|]").findall(html.text)
						w4 = re.compile("wurl.+?\W([0-9]+)\W").findall(html.text)
						w5 = re.compile("_t.+?\W(.+?)\W").findall(html.text)
						contents = "https://" + w + "-" + w1[0] + ".mxdcontent.net/v/" + w2[0] + ".mp4?s=" + w3[0] + "&e=" + w4[0] + "&_t=" + w5[0]
						contents1 = contents.replace("|vfile", "").replace("|", "-")
						contents2 = re.sub('\W\d+-', '', contents1)
						if legenda:
							legenda = legenda[0]
							if not "http" in legenda:
								legenda = legenda
							PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info, sub=legenda)
						else:
							PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info)
                        
					if 'feurl.com' in link2:
						link2 = link2.replace("v","api/source")
						result = {'r': '&', 'd': 'feurl.com'}
						f = requests.post(link2, data=result)
						m2 = re.compile('token=(.\w+).+?:"(\w+)').findall(f.text)
						m2.reverse()
						listar=[]
						listal=[]
						for link, res in m2:
							listal.append(link)
							listar.append(res)
						if len(listal) <1:
							xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
							sys.exit(int(sys.argv[1]))
						d = xbmcgui.Dialog().select("Selecione a resolução", listar)
						if d!= -1:
							url2 = re.sub(' ', '%20', listal[d] )
						if legenda:
							legenda = legenda[0]
							if not "http" in legenda:
								legenda = legenda
							PlayUrl(name, "https://fvs.io/redirector?token="+url2, iconimage, info, sub=legenda)
						else:
							PlayUrl(name, "https://fvs.io/redirector?token="+url2, iconimage, info)

					if 'mystream.to' in link2:
						media1 = requests.get(link2)
						match = re.search(r'(\$=.+?;)\s*<', media1.text, re.DOTALL)
						data = match.group(1)
						startpos = data.find('"\\""+') + 5
						endpos = data.find('"\\"")())()')
						first_group = data[startpos:endpos]
						pos = re.search(r"(\(!\[\]\+\"\"\)\[.+?\]\+)", first_group)
						if pos:
						    first_group = first_group.replace(pos.group(1), 'l').replace('$.__+', 't').replace('$._+', 'u').replace('$._$+','o')
						    tmplist = []
						    js = re.search(r'(\$={.+?});', data)
						    if js:
						        js_group = js.group(1)[3:][:-1]
						        second_group = js_group.split(',')
						        i = -1
						        for x in second_group:
						            a, b = x.split(':')
						            if b == '++$':
						                i += 1
						                tmplist.append(("$.{}+".format(a), i))
						
						            elif b == '(![]+"")[$]':
						                tmplist.append(("$.{}+".format(a), 'false'[i]))
						
						            elif b == '({}+"")[$]':
						                tmplist.append(("$.{}+".format(a), '[object Object]'[i]))
						
						            elif b == '($[$]+"")[$]':
						                tmplist.append(("$.{}+".format(a), 'undefined'[i]))
						
						            elif b == '(!""+"")[$]':
						                tmplist.append(("$.{}+".format(a), 'true'[i]))

						        tmplist = sorted(tmplist, key=lambda z: str(z[1]))
						        for x in tmplist:
						            first_group = first_group.replace(x[0], str(x[1]))

						        first_group = first_group.replace('\\"', '\\').replace("\"\\\\\\\\\"", "\\\\").replace('\\"', '\\').replace('"', '').replace("+", "")
						        final_data = first_group.encode('ascii').decode('unicode-escape').encode('ascii').decode('unicode-escape')
						        media = re.compile("'(http.+?)'").findall(final_data)
						        mp4 = media[0]
						        if legenda:
						        	legenda = legenda[0]
						        	if not "http" in legenda:
						        		legenda = legenda
						        	PlayUrl(name, mp4+"|Referer=https://mstream.press/", iconimage, info, sub=legenda)
						        else:
							        PlayUrl(name, mp4+"|Referer=https://mstream.press/", iconimage, info)
				else:
					sys.exit()
			else:
				sys.exit()        
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado, tente outro servidor')
		sys.exit()
		#pass
#------------------ Vizer.tv SerieMenuBZ
def MenuVizer(): # 600
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaVZ11[int(CatVZ)] +"[/COLOR]", "url" ,235 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageVZ) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageVZ) ) +"][/B][/COLOR]", cPageVZ , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageVZ")
		l= int(cPageVZ)*1
		for x in range(0, 1):
			l +=0
			url3 = ('https://vizer.tv/includes/ajax/publicFunctions.php')
			result = {'getHomeSliderMovies': '1'}
			f = requests.post(url3, data=result)
			link = f.text
			if ClistaVZ10[int(CatVZ)] != "0":
				link = common.OpenURL("https://vizer.tv/includes/ajax/ajaxPagination.php?categoriesListMovies="+ClistaVZ10[int(CatVZ)]+"&search=&page="+ str(l) +"&categoryFilterYear=all&categoryFilterOrderBy=year&categoryFilterOrderWay=desc&categoryFilterQuantity=28")
			f = json.loads(link)
			f2 = json.dumps(f, ensure_ascii=False)
			arquivo2 = urllib.quote(f2.encode('utf8'))
			String2 = urllib.unquote(arquivo2)
			match = re.compile('title".."([^\"]+)".+?url".."([^\"]+).+?\/([^\"]+)".+?year".."([^\"]+)"').findall(String2)
			if match:
				for name2, url2, img2, ano in match:
					img3 = "https://image.tmdb.org/t/p/original/" + img2
					url3 = "https://vizer.tv/filme/online/" + url2
					AddDir(name2 + " - ("+ano+")", url3, 601, img3, img3, isFolder=True, IsPlayable=True, info="")
					p += 1
		if p >= 27:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageVZ) + 2) +"][/B][/COLOR]", cPageVZ , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageVZ")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def MenuVizer2(): # 601
	try:
		link = common.OpenURL(url)
		sinopse = re.compile('class="desc.+?>\s(.+?)<\/span>').findall(link)
		sinopse = sinopse[0]
		hexd = re.compile('watchMovie.(\w+)." id').findall(link)
		hexd= hexd[0]
		url3 = ('https://vizer.tv/includes/ajax/publicFunctions.php')
		result = {'watchMovie': hexd}
		f = requests.post(url3, data=result)
		f1 = json.loads(f.text)
		f2 = json.dumps(f1, ensure_ascii=False)
		arquivo2 = urllib.quote(f2.encode('utf8'))
		String2 = urllib.unquote(arquivo2)
		arquivo = open(cachefolder + "vizer.txt", "w+")
		arquivo.write(String2)
		arquivo.close()
		match = re.compile('lang".."(.+?)".+?id".."(.+?)"').findall(String2)
		#match = re.compile('lang".."(.+?)".+?:.+?"(.+?)"').findall(String2)
        	if match:
				for name2, url2 in match:
					name2 = name2.replace("Original"," [COLOR red][B]Legendado[/B][/COLOR]").replace("Dublado"," [COLOR springgreen][B]Dublado[/B][/COLOR]")
					#name2 = name2.replace("Original"," [COLOR red][B]Legendado[/B][/COLOR]").replace("Português"," [COLOR springgreen][B]Dublado[/B][/COLOR]")
					AddDir(name2, url2, 602, iconimage, iconimage, isFolder=False, IsPlayable=True, info= sinopse)
	except:
		pass
def PlayVizer1(): # 602
	try:	
				urlx = "https://vizer.tv/embed/getEmbed.php?orvio=" + url
				url4 = requests.get(urlx)
				link2 = re.compile('src="(http.+?)"').findall(url4.text)
				link2= link2[0].replace("?","#")
				if 'orvio' in link2:
					url23 = requests.get(link2)
					legenda = re.compile('videoId.+?"(.+?)".\s+.+\s.+.\s+.\s.+\s.+\s.+?var subsArray.+?"(.+?)"').findall(url23.text)
					archive = re.compile('hashLink.+?"(.+?)"').findall(url23.text)
					mp4 = "https://redirect.orvio.co/hd/" + archive[0]
					if legenda:
						for legenda2, id in legenda:
							id2 = id.replace("P","-P")
							legenda2 = "https://subs.orvio.co/"+legenda2+id2+".vtt"
							PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info, sub=legenda2)
					else:
						PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info)
	except:
		xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
		sys.exit()

def PlayVizer(): # 602 ###### opção 1
	try:	
			url2x = "https://vizer.tv/includes/ajax/publicFunctions.php"
			result = {'showPlayer': url}
			f = requests.post(url2x, data=result)
			m2 = re.compile('"(\w+)".true').findall(f.text)
			#m2.reverse()
			listar=[]
			for res in m2:
				if "xxxxxxx" in res: False
				else:
					listar.append(res.replace("fembed","[B][COLOR deepskyblue]Fembed[/B][/COLOR]").replace("mixdrop","[B][COLOR lightseagreen]Mixdrop[/B][/COLOR]").replace("mystream","[B][COLOR mediumseagreen]Mystream[/B][/COLOR]"))
			if len(listar) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione o servidor", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listar[d].replace("[B][COLOR deepskyblue]Fembed[/B][/COLOR]","fembed").replace("[B][COLOR lightseagreen]Mixdrop[/B][/COLOR]","mixdrop").replace("[B][COLOR mediumseagreen]Mystream[/B][/COLOR]","mystream") )
				urlx = "https://vizer.tv/embed/getPlay.php?id=" + url + "&sv=" + url2
				url4 = requests.get(urlx)
				legenda = re.compile("(.{1,7}\/wa.+?srt)").findall(url4.text)
				link2 = re.compile('href="(http.+?)"').findall(url4.text)
				link2= link2[0].replace("?","#")
				if 'orvio' in link2:   ###################################################
					url23 = requests.get(link2)
					archive = re.compile('hashLink.+?"(.+?)"').findall(url23.text)
					mp4 = "https://redirect.orvio.co/hd/" + archive[0]
					if legenda:
						legenda = legenda[0]
						if not "http" in legenda:
							legenda = legenda
						PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info, sub=legenda)
					else:
						PlayUrl(name, mp4+"|Referer=https://orvio.co/", iconimage, info)
				if 'mixdrop' in link2:
					headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
					html2 = requests.get(link2, headers=headers)
					g = re.compile('location.+?"(.+?)"').findall(html2.text)
					try:
						g2 = "https://mixdrop.to" + g[0]
						html = requests.get(g2, headers=headers)
						w = re.compile("'.MDCore.(.)").findall(html.text)
						w = w[0].replace("d","a")
						w1 = re.compile("(delivery\w+)").findall(html.text)
						w2 = re.compile("delivery\w+.(\w+)").findall(html.text)
						w3 = re.compile("referrer.(.+?)[|]").findall(html.text)
						w4 = re.compile("wurl.+?\W([0-9]+)\W").findall(html.text)
						w5 = re.compile("_t.+?\W(.+?)\W").findall(html.text)
						contents = "https://" + w + "-" + w1[0] + ".mxdcontent.net/v/" + w2[0] + ".mp4?s=" + w3[0] + "&e=" + w4[0] + "&_t=" + w5[0]
						contents1 = contents.replace("|vfile", "").replace("|", "-")
						contents2 = re.sub('\W\d+-', '', contents1)
						if legenda:
							legenda = legenda[0]
							if not "http" in legenda:
								legenda = legenda
							PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info, sub=legenda)
						else:
							PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info)
					except IndexError as g2:
						pass
					headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
					html = requests.get(link2, headers=headers)
					w = re.compile("'.MDCore.(.)").findall(html.text)
					w = w[0].replace("d","a")
					w1 = re.compile("(delivery\w+)").findall(html.text)
					w2 = re.compile("delivery\w+.(\w+)").findall(html.text)
					w3 = re.compile("referrer.(.+?)[|]").findall(html.text)
					w4 = re.compile("wurl.+?\W([0-9]+)\W").findall(html.text)
					w5 = re.compile("_t.+?\W(.+?)\W").findall(html.text)
					contents = "https://" + w + "-" + w1[0] + ".mxdcontent.net/v/" + w2[0] + ".mp4?s=" + w3[0] + "&e=" + w4[0] + "&_t=" + w5[0]
					contents1 = contents.replace("|vfile", "").replace("|", "-")
					contents2 = re.sub('\W\d+-', '', contents1)
					if legenda:
						legenda = legenda[0]
						if not "http" in legenda:
							legenda = legenda
						PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info, sub=legenda)
					else:
						PlayUrl(name, contents2.replace("poster-","").replace("s=-","s=").replace('-'+w4[0],"")+"|Referer=https://mixdrop.to/", iconimage, info)
                        
				if 'feurl.com' in link2:
					link2 = link2.replace("v","api/source")
					result = {'r': '&', 'd': 'feurl.com'}
					f = requests.post(link2, data=result)
					m2 = re.compile('token=(.\w+).+?:"(\w+)').findall(f.text)
					m2.reverse()
					listar=[]
					listal=[]
					for link, res in m2:
						listal.append(link)
						listar.append(res)
					if len(listal) <1:
						xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
						sys.exit(int(sys.argv[1]))
					d = xbmcgui.Dialog().select("Selecione a resolução", listar)
					if d!= -1:
						url2 = re.sub(' ', '%20', listal[d] )
					if legenda:
						legenda = legenda[0]
						if not "http" in legenda:
							legenda = legenda
						PlayUrl(name, "https://fvs.io/redirector?token="+url2, iconimage, info, sub=legenda)
					else:
						PlayUrl(name, "https://fvs.io/redirector?token="+url2, iconimage, info)
                         
				if 'mystream.to' in link2:
					media1 = requests.get(link2)
					match = re.search(r'(\$=.+?;)\s*<', media1.text, re.DOTALL)
					data = match.group(1)
					startpos = data.find('"\\""+') + 5
					endpos = data.find('"\\"")())()')
					first_group = data[startpos:endpos]
					pos = re.search(r"(\(!\[\]\+\"\"\)\[.+?\]\+)", first_group)
					if pos:
					    first_group = first_group.replace(pos.group(1), 'l').replace('$.__+', 't').replace('$._+', 'u').replace('$._$+','o')
					    tmplist = []
					    js = re.search(r'(\$={.+?});', data)
					    if js:
					        js_group = js.group(1)[3:][:-1]
					        second_group = js_group.split(',')
					        i = -1
					        for x in second_group:
					            a, b = x.split(':')
					            if b == '++$':
					                i += 1
					                tmplist.append(("$.{}+".format(a), i))
					
					            elif b == '(![]+"")[$]':
					                tmplist.append(("$.{}+".format(a), 'false'[i]))
					
					            elif b == '({}+"")[$]':
					                tmplist.append(("$.{}+".format(a), '[object Object]'[i]))
					
					            elif b == '($[$]+"")[$]':
					                tmplist.append(("$.{}+".format(a), 'undefined'[i]))
					
					            elif b == '(!""+"")[$]':
					                tmplist.append(("$.{}+".format(a), 'true'[i]))

					        tmplist = sorted(tmplist, key=lambda z: str(z[1]))
					        for x in tmplist:
					            first_group = first_group.replace(x[0], str(x[1]))

					        first_group = first_group.replace('\\"', '\\').replace("\"\\\\\\\\\"", "\\\\").replace('\\"', '\\').replace('"', '').replace("+", "")
					        final_data = first_group.encode('ascii').decode('unicode-escape').encode('ascii').decode('unicode-escape')
					        media = re.compile("'(http.+?)'").findall(final_data)
					        mp4 = media[0]
					        if legenda:
					        	legenda = legenda[0]
					        	if not "http" in legenda:
					        		legenda = legenda
					        	PlayUrl(name, mp4+"|Referer=https://mstream.press/", iconimage, info, sub=legenda)
					        else:
						        PlayUrl(name, mp4+"|Referer=https://mstream.press/", iconimage, info)
			else:
				sys.exit()
	except:
		xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
		sys.exit()
# --------------  Fim menu
def FilmesHD(): # 530
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaFHD11[int(CatHD)] +"[/COLOR]", "url" ,234 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageFHD) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageFHD) ) +"][/B][/COLOR]", cPageFHD , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageFHD")
		l= int(cPageFHD)*1
		for x in range(0, 1):
			l +=1
			link = common.OpenURL("https://verfilmeshd.gratis/"+ClistaFHD10[int(CatHD)]+"/page/"+ str(l) +"/")
			match = re.compile('href="([^\"]+)".{1,60}oldtitle="([^\"]+)".{1,30}img src="([^\"]+)".+?IMDb..([^\"].+?)<.+?tag">([^\"].+?)<').findall(link)
			if match:
				for url2, name2, img2, imdb, ano in match:
					name2= name2.replace("Online","").replace("Dublado", "[COLOR blue] (Dublado)[/COLOR]").replace("Legendado", "[COLOR blue] (Legendado)[/COLOR]").replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…').replace('&#039;',"'")
					if "tvshows" in url2: False
					else:
						AddDir(name2, url2, 531, img2, img2, isFolder=True, IsPlayable=True, info="IMDB: "+imdb+"   Ano: "+ano)
					p += 1
			else:
				break
		if p >= 30:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageFHD) + 2) +"][/B][/COLOR]", cPageFHD , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageFHD")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def FilmesHDmenu(): #531
	try:	
		link = common.OpenURL(url)
		hexd = re.compile('play-ico.php.v1=([^\"].+)" fra').findall(link)
		hexd= hexd[0]
		sinopse = re.compile('<p class="f-desc">([^\"].+?)<').findall(link)
		sinopse= sinopse[0]
		AddDir(name, hexd, 532, iconimage, iconimage, isFolder=False, IsPlayable=True, info=sinopse)
	except:
		pass
def FilmesHDPlay(): #532
        try:
            if 'waaw.tv' in url:
                    url1 = requests.get(url, headers={'Referer': 'https://waaw.tv/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
                    url1x = re.compile("<script>\s.+.\s+.+?location.replace.'(.+?)'").findall(url1.text)
                    url1x = url1x[0]
                    url2x = "https://waaw.tv" + url1x
                    url3x = requests.get(url2x,headers={'Referer': 'https://waaw.tv/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
                    url4x = re.compile('iframe src="(.+?)"').findall(url3x.text)
                    url4x = url4x[0]
                    url5x = "https://waaw.tv" + url4x
                    urlx = requests.get(url5x,headers={'Referer': 'https://waaw.tv/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
                    hls = re.compile('content="https:\/\/cdn-(\w+)').findall(urlx.text)
                    hls = hls[0]
                    date = re.compile('content="https:\/\/.+?files.\w+.(\w+.\w+.\w+.\w+)').findall(urlx.text)
                    date = date[0]
                    date2 = re.compile('content="https:\/\/.+?files.\w+.\w+.\w+.\w+.(\w+)').findall(urlx.text)
                    date2 = date2[0]
                    url1z = requests.get("https://pastebin.com/raw/cvuCJsZ2")
                    date3 = re.compile("(\w.+)").findall(url1z.text)
                    date3 = date3[0]
                    project = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=af&url=https://d5g2f6.cfeucdn.com/secip/1988/"+date3+"/hls-vod-"+ hls + "/flv/api/files/videos/" + date
                    url2 = requests.get(project)
                    url3 = url2.text.replace(date2,project)
                    arquivo = open(cachefolder + "waaw.m3u8", "w+")
                    arquivo.write(url3)
                    arquivo.close()
                    PlayUrl(name, cachefolder + "waaw.m3u8", iconimage, info)

            if 'hqq.tv' in url:
                    urlx = requests.get(url,headers={'Referer': 'https://waaw.tv/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
                    hls = re.compile('content="https:\/\/cdn-(\w+)').findall(urlx.text)
                    hls = hls[0]
                    date = re.compile('content="https:\/\/.+?files.\w+.(\w+.\w+.\w+.\w+)').findall(urlx.text)
                    date = date[0]
                    date2 = re.compile('content="https:\/\/.+?files.\w+.\w+.\w+.\w+.(\w+)').findall(urlx.text)
                    date2 = date2[0]
                    url1z = requests.get("https://pastebin.com/raw/cvuCJsZ2")
                    date3 = re.compile("(\w.+)").findall(url1z.text)
                    date3 = date3[0]
                    project = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=af&url=https://d5g2f6.cfeucdn.com/secip/1988/"+date3+"/hls-vod-"+ hls + "/flv/api/files/videos/" + date
                    url2 = requests.get(project)
                    url3 = url2.text.replace(date2,project)
                    arquivo = open(cachefolder + "waaw.m3u8", "w+")
                    arquivo.write(url3)
                    arquivo.close()
                    PlayUrl(name, cachefolder + "waaw.m3u8", iconimage, info)

            if 'waaw1.tv' in url:
                    urlx = requests.get(url,headers={'Referer': 'https://waaw.tv/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'})
                    hls = re.compile('content="https:\/\/cdn-(\w+)').findall(urlx.text)
                    hls = hls[0]
                    date = re.compile('content="https:\/\/.+?files.\w+.(\w+.\w+.\w+.\w+)').findall(urlx.text)
                    date = date[0]
                    date2 = re.compile('content="https:\/\/.+?files.\w+.\w+.\w+.\w+.(\w+)').findall(urlx.text)
                    date2 = date2[0]
                    url1z = requests.get("https://pastebin.com/raw/cvuCJsZ2")
                    date3 = re.compile("(\w.+)").findall(url1z.text)
                    date3 = date3[0]
                    project = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=af&url=https://d5g2f6.cfeucdn.com/secip/1988/"+date3+"/hls-vod-"+ hls + "/flv/api/files/videos/" + date
                    url2 = requests.get(project)
                    url3 = url2.text.replace(date2,project)
                    arquivo = open(cachefolder + "waaw.m3u8", "w+")
                    arquivo.write(url3)
                    arquivo.close()
                    PlayUrl(name, cachefolder + "waaw.m3u8", iconimage, info)                          
        except (IndexError, ValueError):
			xbmcgui.Dialog().ok('Play XD', 'Filme não encontrado')
			sys.exit()
# --------------  Inicio Assistir.biz
def AssistirbizMENU2(): # 514
	try:
			link = common.OpenURL("https://assistir.biz/home").replace('\n','').replace('\r','')
			hex2 = re.compile('<div class="tab-content" id="myTabContent">(.+?)<div class="tab-pane fade"').findall(link)
			hex2 = hex2[0]
			match = re.compile('data-src="([^\"]+)".+?rate">([^\"]+)<\/span.+?a href="([^\"]+)">([^\"]+)<\/a.+?,.([^\"]+)<\/a').findall(hex2)
			if match:
				for img2, imdb, url2,name2, ano in match:
					url2= url2.replace("/filme","https://assistir.biz/filme")
					img2= img2.replace("//image","https://image").replace("w185","original")
					if "tvshows" in url2: False
					else:
						AddDir(name2+ " - ("+ano+")", url2, 515, img2, img2, info="[COLOR yellow][B]IMDb *[COLOR green]"+imdb+"[/B][/COLOR]", isFolder=True, IsPlayable=True)
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def AssistirbizMENU(): # 514
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaBIZ11[int(CatBB)] +"[/COLOR]", "url" ,232 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
			link = common.OpenURL("https://assistir.biz/home").replace('\n','').replace('\r','')
			hex2 = re.compile('<div class="tab-content" id="myTabContent">(.+?)<div class="tab-pane fade"').findall(link)
			hex2 = hex2[0]
			match = re.compile('data-src="([^\"]+)".+?rate">([^\"]+)<\/span.+?a href="([^\"]+)">([^\"]+)<\/a.+?,.([^\"]+)<\/a').findall(hex2)
			if ClistaBIZ10[int(CatBB)] != "0":
				link = common.OpenURL("https://assistir.biz/categoria/"+ClistaBIZ10[int(CatBB)])
				match = re.compile('data-src="([^\"]+)".+\s.+.\s.+.\s.+.\s.+?">([^\"]+)<\/span>\s.+.\s.+.\s.+?a href="([^\"]+)".alt="([^\"]+)".+\s.+\s.+?">([^\"]+)<\/a').findall(link)
			if match:
				for img2, imdb, url2,name2, ano in match:
					url2= url2.replace("/filme","https://assistir.biz/filme")
					img2= img2.replace("//image","https://image").replace("w185","original")
					if "tvshows" in url2: False
					else:
						AddDir(name2+ " - ("+ano+")", url2, 515, img2, img2, info="[COLOR yellow][B]IMDb *[COLOR green]"+imdb+"[/B][/COLOR]", isFolder=True, IsPlayable=True)
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def AssistirbizLista(): #515
	try:	
		link = common.OpenURL(url)
		hexd = re.compile('content="(.+?filme.+?)"').findall(link)
		hexd = hexd[0].replace("filme","iframe")+'?player=1'
		sinopse = re.compile('<i>([^\"]+)<\/i>').findall(link)
		sinopse= sinopse[0]
		AddDir(name + "[COLOR blue] - Dublado[/COLOR]", hexd, 516, iconimage, iconimage, isFolder=False, IsPlayable=True, info=sinopse)
	except:
		pass
def AssistirbizPlay(): #516
	try:	
			linkx = requests.get(url)
			m2 = re.compile('(assistir.biz\/direct[^\"]+)".+?mp4".\w+="([^\"]+)"').findall(linkx.text)
			m2.reverse()
			legenda = re.compile('subdata..([^\"]+)').findall(url)
			listar=[]
			listal=[]
			for link, res in m2:
				listal.append(link)
				listar.append(res)
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione a resolução", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				global background
				background=background+";;;"+name+";;;MM"
				if legenda:
					legenda = legenda[0]
					if not "http" in legenda:
						legenda = "https://sub.streamservice.online/subdata/" + legenda
					PlayUrl(name,'https://' + url2, iconimage, info, sub=legenda)
				else:
					PlayUrl(name,'https://' + url2, iconimage, info)
			else:
				sys.exit()
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado')
		sys.exit()
# --------------  Inicio QueroFilmes
def QuerofilmeshdMENU(): # 510
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaQUE11[int(CatQ1)] +"[/COLOR]", "url" ,231 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageQlf) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageQlf) ) +"][/B][/COLOR]", cPageQlf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageQlf")
		l= int(cPageQlf)*1
		for x in range(0, 1):
			l +=1
			link = common.OpenURL("https://querofilmeshd.online/genero/"+ClistaQUE10[int(CatQ1)]+"/page/"+ str(l))
			match = re.compile('img src="([^\"]+)".+?alt="([^\"]+)".+?href="([^\"]+).+?<span>.+?,.(\w+)').findall(link.replace('\n','').replace('\r',''))
			if match:
				for img2,name2,url2,ano in match:
					img2= img2.replace("w185","original")
					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
					if "tvshows" in url2: False
					else:
						AddDir(name2 + " - ("+ano+")" ,url2, 511, img2, img2, info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
					p += 1
			else:
				break
		if p >= 30:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageQlf) + 2) +"][/B][/COLOR]", cPageQlf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageQlf")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def QuerofilmeshdLista(): #511
	i=0
	link2 = requests.get(url)
	link = common.OpenURL(url).replace('\n','').replace('\r','')
	sinopse = re.compile('wp-content">.+?<p>(.+?)<\/p>').findall(link)
	sinopse= sinopse[0].replace(' &#8211; Online Dublado e Legendado','').replace('Assistir ','').replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
	match2 = re.findall("online\/.p=([^\"]+)'", link2.text)
	url3 = ('https://querofilmeshd.online/wp-admin/admin-ajax.php')
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	result = {'action': 'doo_player_ajax', 'post': match2, 'nume': '1','type': 'movie'}
	f = requests.post(url3, data = result, headers=headers)
	url4 = re.compile('(http.+?)"').findall(f.text)
	url4 = url4[0].replace('\/','/')
	link3 = requests.get(url4)
	w2 = link3.text
	match4 = re.compile('idS:."(\w+)').findall(w2)
	name5 = re.compile('">\w+.#..(\w+)').findall(w2)
	for url2 in match4:
		AddDir(name5[i].replace("DUBLADO","[COLOR limegreen][B]DUBLADO[/B][/COLOR]").replace("LEGENDADO","[COLOR crimson][B]LEGENDADO[/COLOR][/B]"), match4[i], 513, iconimage, iconimage, isFolder=False, IsPlayable=True, info=sinopse)
		i+=1
def QuerofilmeshdPlay2(): #513 
    try:
		url5 = ('https://player.querofilmeshd.online//CallPlayer')
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		result = {'id': url}
		f2 = requests.post(url5, data=result, headers=headers)
		hexd = codecs.decode(f2.text, "hex_codec").decode('utf-8')
		url6 = re.compile('(id=.\w+)|url.+?(https.+?)"|(files.+?)[?]').findall(hexd)
		url7 = str(url6).replace("'', '","").replace("'","").replace("\\","").replace("[(","").replace(")]","").replace(",","").replace("uhttps","https").replace(" u","").replace("u u","").replace(" ","").replace(", ","").replace("https://player.filmesonlinetv.org/public/dist/index.html?id=", "http://player.filmesonlinetv.org/playlist/")
        
		if 'http://player.filmesonlinetv.org' in url7:
			url7x = "/1588804130818"
			url8 = url7 + url7x
			m = common.OpenURL(url8.replace("uhttp","http"))
			if m:
				url9 = m
				m2 = re.compile('x([^\"]..)\s(\/.+?m3u8)').findall(url9)
				m2.reverse()
				legenda = re.compile('subdata..([^\"]+)').findall(url)
				listar=[]
				listal=[]
				for res, link in m2:
					listal.append(link)
					listar.append(res)
				if len(listal) <1:
					xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
					sys.exit(int(sys.argv[1]))
				d = xbmcgui.Dialog().select("Selecione a resolução", listar)
				if d!= -1:
					url2 = re.sub(' ', '%20', listal[d] )
					urlx = 'https://player.filmesonlinetv.org' + url2
					url4 = requests.get(urlx)
					url5 = url4.text.replace("redirect/","")
					arquivo = open(cachefolder + "movies.m3u8", "w+")
					arquivo.write(url5)
					arquivo.close()
					x1 = randrange(300)
					x = str(x1)
					session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
					file = open(cachefolder + "movies.m3u8",'rb')
					session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
					file.close()                      
					session.quit()
					global background
					background=background+";;;"+name+";;;MM"
					if legenda:
						legenda = legenda[0]
						if not "http" in legenda:
							legenda = "https://sub.streamservice.online/subdata/" + legenda
						PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://slave3.queroserieshd.com/", iconimage, info, sub=legenda)
					else:
						PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://slave3.queroserieshd.com/", iconimage, info)

		if 'drive.google.com' in url7:
			PlayUrl(name, 'plugin://plugin.video.gdrive?mode=streamURL&amp;url='+url7.replace('uhttps','https').replace('preview','view'), iconimage, info)
            
		if 'files' in url7:
			contents = url7.replace('files','https://drive.google.com/file/d')
			contents2 = contents + '/view'
			PlayUrl(name, 'plugin://plugin.video.gdrive?mode=streamURL&amp;url='+contents2.replace('uhttps','https').replace('preview','view'), iconimage, info)
            
		else:
			sys.exit()
    except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado')
		sys.exit()
#########################################################
def ListSerieQF(): #430:
	pagina = "0" if not cPageserQF else cPageserQF
	if int(pagina) > 0:
		AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageserQF")
	y= int(pagina)*4
	for x in range(0, 4):
		try:
			y +=1
			l = common.OpenURL("https://querofilmeshd.online/genero/series/page/"+str(y)+"/")
			match = re.compile('img src="([^\"]+)".+?alt="([^\"]+)".+?href="([^\"]+).+?<span>.+?,.(\w+)').findall(l)
			if match:
				for img2,name2,url2,ano in match:
					img2= img2.replace("w185","original")
					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
					AddDir(name2 + " - ("+ano+")" ,url2, 431, img2, img2, info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
		except:
			pass
	AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageserQF")
def ListTempQF(): #431
	l = common.OpenURL(url).replace("\n","").replace("\r","")
	m = re.compile('Season.(\d+)(.+?)<\/div><\/div>').findall(l)
	for temp2,cont2 in m:
		AddDir("Temporada "+ temp2, cont2, 432, iconimage, iconimage, isFolder=True)
def ListEpiQF(): #432
	epis = re.compile("numerando'>. - (\d+).+?(http[^\"].+?)'").findall(url)
	for E,url2 in epis:
		AddDir("Episódio "+E,url2, 433, iconimage, iconimage, isFolder=False, IsPlayable=True)
def PlayEpiQF(): #433
	try:	
		link2 = requests.get(url)
		match2 = re.findall("online\/.p=([^\"]+)'", link2.text)
		match2 = match2[0]
		url3 = ('https://querofilmeshd.online/wp-admin/admin-ajax.php')
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		result = {'action': 'doo_player_ajax', 'post': match2, 'nume': '1', 'type': 'tv'}
		f = requests.post(url3, data=result, headers=headers)
		url4 = re.compile('(http.+?)"').findall(f.text)
		url4 = url4[0].replace('\/','/')
		link3 = requests.get(url4)
		w2 = link3.text
		match3 = re.findall('idS."([^\"]+)', w2)
		match3 = match3[0]
		url5 = ('https://player.querofilmeshd.online//CallEpi')
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		result = {'idS': match3}
		f2 = requests.post(url5, data=result, headers=headers)
		hexd = codecs.decode(f2.text, "hex_codec").decode('utf-8')
		url6 = re.compile('(id.\w+)').findall(hexd)
		url6 = url6[0].replace("id=", "http://player.filmesonlinetv.org/playlist/")
		url7 = "/1588804130818"
		url8 = url6 + url7
		m = common.OpenURL(url8)
		if m:
			url9 = m
			m2 = re.compile('x([^\"]..)\s(\/.+?m3u8)').findall(url9)
			m2.reverse()
			legenda = re.compile('subdata..([^\"]+)').findall(url)
			listar=[]
			listal=[]
			for res, link in m2:
				listal.append(link)
				listar.append(res)
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione a resolução", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				urlx = 'https://player.filmesonlinetv.org' + url2
				url4 = requests.get(urlx)
				url5 = url4.text.replace("redirect/","")
				arquivo = open(cachefolder + "movies.m3u8", "w+")
				arquivo.write(url5)
				arquivo.close()
				x1 = randrange(300)
				x = str(x1)
				session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
				file = open(cachefolder + "movies.m3u8",'rb')
				session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
				file.close()                      
				session.quit()
				global background
				background=background+";;;"+name+";;;MM"
				if legenda:
					legenda = legenda[0]
					if not "http" in legenda:
						legenda = "https://sub.streamservice.online/subdata/" + legenda
					PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://slave3.queroserieshd.com/", iconimage, info, sub=legenda)
				else:
					PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://slave3.queroserieshd.com/", iconimage, info)

			else:
				sys.exit()
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado')
		sys.exit()
#def QuerofilmeshdMENU(): # 510 GoFilmes
#	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaFl1[int(CatFl)] +"[/COLOR]", "url" ,230 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
#	try:
#		p= 1
#		if int(cPageFlf) > 0:
#			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageFlf) ) +"][/B][/COLOR]", cPageFlf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageFlf")
#		l= int(cPageFlf)*3
#		for x in range(0, 4):
#			l +=1
#			link = common.OpenURL("http://gofilmes.me/genero/acao")
#			match = re.compile("href=\"([^\"]+)\" title\=\"([^\"]+).{1,75}src\=\"([^\"]+)").findall(link.replace('\n','').replace('\r',''))
#			if match:
#				for url2,name2,img2, in match:
#					if name2!="Close":
#						name2 = name2.replace("Assistir","").replace("Online ","").replace("Dublado e Legendado","[COLOR blue]Dublado e Legendado[/COLOR]").replace("Dublado","[COLOR blue] Dublado[/COLOR]").replace("Legendado","[COLOR blue] Legendado[/COLOR]")
#						AddDir(name2, url2, 511, img2.replace("w150_and_h225_bestv2","w342"), img2.replace("w150_and_h225_bestv2","w342"), info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
#					p += 1
#		if p >= 97:
#			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageFlf) + 2) +"][/B][/COLOR]", cPageFlf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageFlf")
#	except:
#		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
#def QuerofilmeshdLista(): #511
#	try:	
#		link = common.OpenURL(url)
#		match = re.compile('(https://openvid[^\"]+).{1,30}">(.+?)<\/a>').findall(link)
#		#name = name.replace("Dublado","")
#		if match:
#			for url2, name2 in match:
#					url2 = url2.replace("https://openvid.xyz/v/","https://openvid.xyz/api/source/")
#					name2 = name2.replace("DUBLADO","[COLOR blue]Dublado[/COLOR]").replace("LEGENDADO","[COLOR blue]Legendado[/COLOR]")
#					AddDir(name.replace(" e ","").replace("Dublado","").replace("Legendado","") + name2, url2, 512, iconimage, iconimage, isFolder=True, IsPlayable=True, info="", background=url)
#	except:
#			pass
#def QuerofilmeshdPlay(): #512
#	try:	
#		url3 = (url)
#		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#		result = {'r': '', 'd': 'openvid.xyz'}
#		f = requests.post(url3, data = result, headers=headers)
#		match = re.compile('(redirector[^\"]+)".{1,10}"(.+?)"').findall(f.text)
		#m = re.compile("userdata..(.+?)\/poster").findall(url)
		#m2 = re.compile("(caption[^\"]+)").findall(url)
		#m3 = re.compile('hash"."(.+?)"').findall(url)
		#m4 = re.compile('"id".(.+?)"').findall(url)
		#m5 = re.compile('("srt"[^\"]+)').findall(url)
		#lista = re.compile("(.+)").findall(m[0]+m2[0]+m3[0]+m4[0]+m5[0])
		#lista = lista[0].replace('\captions', "/caption/").replace('"', "/").replace('/srt/,', ".srt")
#		if match:
#			for url2, name2 in match:
#				if url2!="":
#					url2 = url2.replace("redirector","https://fvs.io/redirector")
#					AddDir(name2, url2, 513, iconimage, iconimage, isFolder=False, IsPlayable=True, info="", background=url)
#	except:
#			pass
#def QuerofilmeshdPlay2(): #513
#	PlayUrl(name, url, iconimage, info, "", metah)               
def Filmes96(): #220
	link = common.OpenURL("https://pastebin.com/raw/ZkfFMB20")
	m = link.split("\n")
	for x in m:
		try:
			meta = eval(x)
			AddDir(meta['title'] +" [COLOR yellow]("+str(meta['year'])+")[/COLOR] "+" [COLOR blue]["+str(meta['rating'])+"][/COLOR]" , meta['mp4'] +"?play", 229, isFolder=False, IsPlayable=True, metah=meta, info='[COLOR][/COLOR]')
		except:
			pass
	setViewM()
def FilmesRC(): #221
	link = common.OpenURL("https://pastebin.com/raw/taJHVbXj")
	m = link.split("\n")
	link2 = common.OpenURL("https://pastebin.com/raw/FwSnnr65")
	i=1
	for x in m:
		try:
			meta = eval(x)
			file = meta['mp4'].split("$")
			reg = "(.+)\$"+file[1]
			m = re.compile(reg, re.IGNORECASE).findall(link2)
			url2 = m[0]
			AddDir(meta['title'] +" [COLOR yellow]("+str(meta['year'])+")[/COLOR] "+" [COLOR blue]["+str(meta['rating'])+"][/COLOR]" , url2 + file[0] +"?play|Referer=http://redecanais.xyz/", 229, isFolder=False, IsPlayable=True, metah=meta, info='[COLOR][/COLOR]')
		except:
			pass
	setViewM()
def PlayFilmes96(): #229
	PlayUrl(name, url, iconimage, info, "", metah)
# --------------  Fim Filme CB
# --------------  NETCINE
def CategoryOrdem(x):
	x2 = Addon.getSetting(eval("x"))
	name2 = "Data" if x2=="0" else "Título"
	AddDir("[COLOR green][B][Organizado por:][/B] "+name2 +" (Clique para alterar)[/COLOR]" , x, 81, "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
def CategoryOrdem2(url):
	x2 = Addon.getSetting(url)
	x = "0" if x2=="1" else "1"
	#xbmcgui.Dialog().ok("Escolha a resolução:", x + x2 + url)
	Addon.setSetting(url, x )
	xbmc.executebuiltin("XBMC.Container.Refresh()")
def Series(): #60
	try:
		CategoryOrdem("cOrdNCS")
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link = requests.get("http://netcine.biz/tvshows/page/1/",headers=headers, proxies=proxies)
		l2 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		link = requests.get("http://netcine.biz/tvshows/page/2/", headers=headers, proxies=proxies)
		l3 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		link = requests.get("http://netcine.biz/tvshows/page/3/", headers=headers, proxies=proxies)
		l4 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		link = requests.get("http://netcine.biz/tvshows/page/4/", headers=headers, proxies=proxies)
		l5 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		link = requests.get("http://netcine.biz/tvshows/page/5/", headers=headers, proxies=proxies)
		l6 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		link = requests.get("http://netcine.biz/tvshows/page/6/", headers=headers, proxies=proxies)
		l7 = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		lista = re.compile("img src\=\"([^\"]+).+?alt\=\"([^\"]+).+?f\=\"([^\"]+)").findall(l2[0]+l3[0]+l4[0]+l5[0]+l6[0]+l7[0])
		if cOrdNCS=="1":
			lista = sorted(lista, key=lambda lista: lista[1])
		for img2,name2,url2 in lista:
			if name2!="Close":
				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
				img2 = re.sub('-120x170.(jpg|png)', r'.\1', img2 )
				AddDir(name2 ,url2, 61, img2, img2, isFolder=True, info='[COLOR][/COLOR]')
	except:
		AddDir("Server NETCINE offline, tente novamente em alguns minutos" , "", 0, isFolder=False)
def ListSNC(x): #61
	try:
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link = requests.get(url,headers=headers, proxies=proxies)
		m = re.compile("(.emporada \w+)(.+?class\=\'has-sub\')").findall(link.text.encode('utf-8').replace('\n','').replace('\r','').replace('<div class="soci">',"class='has-sub'").replace('\t',""))
		info2 = re.compile("<h2>Synopsis<\/h2>+.+?[div|p].{0,15}?.+?(.+?)<\/").findall(link.text.encode('utf-8'))
		info2 = re.sub('style\=.+?\>', '', info2[0] ) if info2 else " "
		i=0
		if "None" in background:
			for season,epis in m:
				AddDir("[B]["+season+"][/B]" ,url, 61, iconimage, iconimage, isFolder=True, background=i,info=info2)
				i+=1
		else:
			m2 = re.compile("href\=\"([^\"]+).+?(\d+) - (\d+)").findall( m[int(x)][1] )
			m3 = re.compile("icon-chevron-right\W+\w\W+([^\<]+)").findall( m[int(x)][1] )
			for url2,S,E in m2:
				AddDir("S"+S+"E"+E +" - "+m3[i],url2, 62, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info)
				i+=1
	except:
		AddDir("Server NETCINE offline, tente novamente em alguns minutos" , "", 0, isFolder=False)
def PlayS(): #62
	try:
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link = requests.get(url,headers=headers, proxies=proxies)
		m = re.compile("\"play-.\".+?src=\"([^\"]+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		listan = re.compile("\#play-...(\w*)").findall(link.text.encode('utf-8'))
		i=0
		listaf=[]
		listal=[]
		for url2 in m:
			link3 = requests.get(url2,headers=headers, proxies=proxies)
			m3 = re.compile("src\=\"(.+campanha[^\"]+)").findall(link3.text.encode('utf-8'))
			if m3:
				red = requests.get(m3[0],headers=headers, proxies=proxies)
				red2 = re.compile('redirecionar\.php\?data=([^"]+)').findall(red.text.encode('utf-8'))
				link4 = requests.get(red2[0],headers=headers, proxies=proxies)
				link4 = re.sub('window.location.href.+', '', link4.text.encode('utf-8'))
				link4 = link4.replace("'",'"')
				m4= re.compile("http.+?mp4[^\"]+").findall(link4.text.encode('utf-8')) 
				m4 = list(reversed(m4))
				for url4 in m4:
					listal.append(url4.replace("';",""))
					dubleg="[COLOR green]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
					listaf.append("[B][COLOR blue]"+listan[i] +"[/COLOR] "+dubleg)
			else:
				red = requests.get(url2,headers=headers, proxies=proxies)
				m3 = re.compile("src\=\"([^\"]+)").findall(red.text.encode('utf-8'))
				red1 = requests.get(m3[0],headers=headers, proxies=proxies)
				red2 = re.compile('redirecionar\.php\?data=([^"]+)').findall(red1.text.encode('utf-8'))
				link4 = requests.get(red2[0],proxies=proxies,headers={'Cookie': "autorizado=teste; "})
				m5 = re.compile("location.href=\'([^\']+p\=[^\']+)").findall(link4.text.encode('utf-8'))
				for x in m5:
					if not "openload" in x:
						link5 = requests.get(x,headers=headers, proxies=proxies)
				link5 = re.sub('window.location.href.+', '', link5.text.encode('utf-8'))
				link5 = link5.replace("'",'"')
				m4= re.compile("http.+?mp4[^\"]+").findall(link5)
				m4 = list(reversed(m4))
				for url4 in m4:
					listal.append(url4.replace("';",""))
					dubleg="[COLOR green]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
					listaf.append("[B][COLOR blue]"+listan[i] +"[/COLOR] "+dubleg)
			i+=1
		d = xbmcgui.Dialog().select("Escolha a resolução:", listaf)
		if d!= -1:
			PlayUrl(name, listal[d]+"|Referer=http://netcine.biz&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", iconimage, info)
		else:
			sys.exit()
	except(IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Erro, tente novamente em alguns minutos')
		sys.exit()
# --------------------------------------
def MoviesNC1(): #71 Netcine
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaGO1[int(CatGO)] +"[/COLOR]", "url" ,219 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageGOf) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageGOf) ) +"][/B][/COLOR]", cPageGOf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageGOf")
		l= int(cPageGOf)*2
		for x in range(0, 2):
			l +=1
			link = common.OpenURL("https://netcine.biz/"+ClistaGO0[int(CatGO)]+"/page/"+ str(l)+"/?filmes").replace('\n','').replace('\r','')
			m = re.compile("box_movies(.+)").findall(link)
			lista = re.compile("img src\=\"([^\"]+).+?alt\=\"([^\"]+).+?f\=\"([^\"]+)").findall(m[0])
			if lista:
			 for img2,name2,url2 in lista:
			  if name2!="Close" and name2!="NetCine":
				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
				img2 = img2.replace("-120x170","")
			  if "tvshows" in url2: False
			  else:
				AddDir(name2,url2, 78, img2, img2, isFolder=True, IsPlayable=True, info='[COLOR][/COLOR]')
			  p += 1
			 #else:
			#	break
		if p >= 56:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageGOf) + 2) +"][/B][/COLOR]", cPageGOf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageGOf")
	except:
		pass
def ListMoviesNC1(): #78
	try:
		link = common.OpenURL(url).replace('\n','').replace('\r','')
		m = re.compile("\"play-.\".+?src=\"([^\"]+)").findall(link)
		m2 = re.compile("\#play-...(\w*)").findall(link)
		info2 = re.compile('<h2>Synopsis<\/h2>(.*?)<\/').findall(link)
		info2 = re.sub('<(.*?)>', '', info2[0] ) if info2 else ""
		info2 = info2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”')
		i=0
		for name2 in m2:
			AddDir(name +" [COLOR blue]("+ name2 +")[/COLOR]", m[i], 79, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
			i+=1
	except urllib2.URLError, e:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, isFolder=False)
def PlayMNC1(): #79
	try:
		i=0
		listaf=[]
		listal=[]
		link = common.OpenURL(url)
		#red = re.compile('redirecionar\.php\?data=([^"]+)').findall(link)
		#ST(red)
		#if not red:
		red2 = re.compile('http[^"]+').findall(link)
		link2 = common.OpenURL(red2[0])
		red = re.compile('redirecionar\.php\?data=([^"]+)').findall(link2)
		if not "desktop" in red[0]:
			link2 = common.OpenURL(red[0])
			red = re.compile('location.href=\'([^\']+p\=[^\']+)').findall(link2)
		link3 = common.OpenURL(red[0],headers={'Cookie': "autorizado=teste; "})
		link3 = re.sub('window.location.+', '', link3)
		link3 = link3.replace("'",'"')
		m4= re.compile("http.+?mp4[^\"]{0,150}").findall(link3) 
		m4 = list(reversed(m4))
		for url4 in m4:
			if not "openload" in url4:
				listal.append(url4.replace("';",""))
				dubleg="[COLOR springgreen]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
				listaf.append("[B]"+dubleg)
		d = xbmcgui.Dialog().select("Escolha a resolução:", listaf)
		if d!= -1:
			global background
			background=background+";;;"+name+";;;NC"
			PlayUrl(name, listal[d]+"|Referer=http://netcine.biz&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", iconimage, info)
		else:
			sys.exit()
	except urllib2.URLError, e:
		xbmcgui.Dialog().ok('Play XD', 'Erro, tente novamente em alguns minutos')
		sys.exit()
############################################ Opção Proxy
def MoviesNC(): #71 Netcine
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaGO1[int(CatGO)] +"[/COLOR]", "url" ,219 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageGOf) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageGOf) ) +"][/B][/COLOR]", cPageGOf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageGOf")
		l= int(cPageGOf)*2
		for x in range(0, 2):
			l +=1
            #####"http": "http://61.7.138.168:8080", "https": "http://61.7.138.168:8080"
			proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
			proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
			headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
			proxies = {"http": proxy2[0], "https": proxy2[0]}
			link = requests.get("https://netcine.biz/"+ClistaGO0[int(CatGO)]+"/page/"+ str(l)+"/?filmes", headers=headers, proxies=proxies)
			m = re.compile("box_movies(.+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
			lista = re.compile("img src\=\"([^\"]+).+?alt\=\"([^\"]+).+?f\=\"([^\"]+)").findall(m[0])
			if lista:
			 for img2,name2,url2 in lista:
			  if name2!="Close" and name2!="NetCine":
				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
				img2 = img2.replace("-120x170","")
			  if "tvshows" in url2: False
			  else:
				AddDir(name2,url2, 78, img2, img2, isFolder=True, IsPlayable=True, info='[COLOR][/COLOR]')
			  p += 1
		if p >= 56:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageGOf) + 2) +"][/B][/COLOR]", cPageGOf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageGOf")
	except:
		pass
def ListMoviesNC(): #78
	try:
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link = requests.get(url, headers=headers, proxies=proxies)
		arquivo = open(cachefolder + "netcine.txt", "w+")
		arquivo.write(link.text.encode('utf-8'))
		arquivo.close()
		m = re.compile("\"play-.\".+?src=\"([^\"]+)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		m2 = re.compile("\#play-...(\w*)").findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		info2 = re.compile('<h2>Synopsis<\/h2>(.*?)<\/').findall(link.text.encode('utf-8').replace('\n','').replace('\r',''))
		info2 = re.sub('<(.*?)>', '', info2[0] ) if info2 else ""
		info2 = info2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”')
		i=0
		for name2 in m2:
			AddDir(name +" [COLOR blue]("+ name2 +")[/COLOR]", m[i], 79, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
			i+=1
	except urllib2.URLError, e:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, isFolder=False)
def PlayMNC(): #79
	try:
		i=0
		listaf=[]
		listal=[]
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link = requests.get(url,headers=headers, proxies=proxies)
		red2 = re.compile('http[^"]+').findall(link.text.encode('utf-8'))
		link2 = requests.get(red2[0],headers=headers, proxies=proxies)
		red = re.compile('redirecionar\.php\?data=([^"]+)').findall(link2.text.encode('utf-8'))
		if not "desktop" in red[0]:
			link2 = requests.get(red[0],headers=headers, proxies=proxies)
			red = re.compile('location.href=\'([^\']+p\=[^\']+)').findall(link2.text.encode('utf-8'))
		link3 = requests.get(red[0],proxies=proxies, headers={'Cookie': "autorizado=teste; "})
		link3 = re.sub('window.location.+', '', link3.text.encode('utf-8'))
		link3 = link3.replace("'",'"')
		m4= re.compile("http.+?mp4[^\"]{0,150}").findall(link3) 
		m4 = list(reversed(m4))
		for url4 in m4:
			if not "openload" in url4:
				listal.append(url4.replace("';",""))
				dubleg="[COLOR springgreen]HD[/COLOR][/B]" if "ALTO" in url4 else "[COLOR red]SD[/COLOR][/B]"
				listaf.append("[B]"+dubleg)
		d = xbmcgui.Dialog().select("Escolha a resolução:", listaf)
		if d!= -1:
			global background
			background=background+";;;"+name+";;;NC"
			PlayUrl(name, listal[d]+"|Referer=http://netcine.biz&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", iconimage, info)
		else:
			sys.exit()
	except urllib2.URLError, e:
		xbmcgui.Dialog().ok('Play XD', 'Erro, tente novamente em alguns minutos')
		sys.exit()
########################opção 2
#	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaGO1[int(CatGO)] +"[/COLOR]", "url" ,219 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
#	try:
#		p= 1
#		if int(cPageGOf) > 0:
#			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageGOf) ) +"][/B][/COLOR]", cPageGOf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageGOf")
#		l= int(cPageGOf)*2
#		for x in range(0, 2):
#			l +=1
#			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
#
#			tokens, user_agent = cloudscraper2.get_tokens("https://netcine.biz/", headers = headers)
#			pickle.dump(tokens, open(cachefolder + "tokens.txt","wb"))
#			arquivo2 = open(cachefolder + 'tokens.txt', 'r')
#			url4 = arquivo2.read()
#			url5 = re.compile("rance'+\s.+\s.'(.+?)'").findall(url4)
#			url6 = url5[0]
#			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
#			cookies = {'cf_clearance': url6}
#			link = requests.get("https://netcine.biz/"+ClistaGO0[int(CatGO)]+"/page/"+ str(l)+"/?filmes", headers=headers, cookies=cookies)
#			arquivo = open(cachefolder + "netcine.txt", "w+")
#			arquivo.write(link.text.encode('utf-8'))
#			arquivo.close()
#			arquivo = open(cachefolder + 'netcine.txt', 'r')
#			url3 = arquivo.read()
#			lista = re.compile('img src="([^\"]+).+?alt="([^\"]+).+\s+.+?href="([^\"]+)').findall(url3)
#			if lista:
#			 for img2,name2,url2 in lista:
#			  if name2!="Close" and name2!="NetCine":
#				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
#				img2 = img2.replace("-120x170","")
#			  if "tvshows" in url2: False
#			  else:
#				AddDir(name2,url2, 78, img2, img2, isFolder=True, IsPlayable=True, info='[COLOR][/COLOR]')
#			  p += 1
#		if p >= 56:
#			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageGOf) + 2) +"][/B][/COLOR]", cPageGOf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageGOf")
#	except:
#		pass
########################
################# opção 2
#	try:
#		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
#		tokens, user_agent = cloudscraper2.get_tokens("https://netcine.biz/category/acao/", headers = headers)
#		pickle.dump(tokens, open(cachefolder + "tokens.txt","wb"))
#		arquivo2 = open(cachefolder + 'tokens.txt', 'r')
#		url4 = arquivo2.read()
#		url5 = re.compile("rance'+\s.+\s.'(.+?)'").findall(url4)
#		url6 = url5[0]
#		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
#		cookies = {'cf_clearance': url6}
#		link = requests.get(url, headers=headers, cookies=cookies)
#		arquivo = open(cachefolder + "netcine.txt", "w+")
#		arquivo.write(link.text.encode('utf-8'))
#		arquivo.close()
#		arquivo = open(cachefolder + 'netcine.txt', 'r')
#		url3 = arquivo.read()
#		m = re.compile("\"play-.\".+?src=\"([^\"]+)").findall(url3)
#		m2 = re.compile("\#play-.+\s+\s(\w*)").findall(url3)
#		info2 = re.compile('<h2>Synopsis<\/h2>+\s+.p>(.*?)<\/').findall(url3)
#		info2 = re.sub('<(.*?)>', '', info2[0] ) if info2 else ""
#		info2 = info2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”')
#		i=0
#		for name2 in m2:
#			AddDir(name +" [COLOR blue]("+ name2 +")[/COLOR]", m[i], 79, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
#			i+=1
#	except urllib2.URLError, e:
#		AddDir("Server error, tente novamente em alguns minutos" , "", 0, isFolder=False)
########################
def Generos(): #80
	d = xbmcgui.Dialog().select("Escolha o Genero", Clista1)
	if d != -1:
		global Cat
		Addon.setSetting("Cat", str(d) )
		Cat = d
		Addon.setSetting("cPage", "0" )
		Addon.setSetting("cPageleg", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def Generos2(): #500
	d = xbmcgui.Dialog().select("Escolha o Genero", Clista2)
	if d != -1:
		global Cat
		Addon.setSetting("Cat", str(d) )
		Cat = d
		Addon.setSetting("cPage", "0" )
		Addon.setSetting("cPageleg", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
# --------------  FIM NETCINE
# --------------  REDECANAIS FILMES
def MoviesRCD(): #90 Filme dublado
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + Clista1[int(Cat)] +"[/COLOR]", "url" ,80 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	CategoryOrdem("cOrdRCF")
	try:
		p= 1
		if int(cPage) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPage) ) +"][/B][/COLOR]", cPage , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPage")
		l= int(cPage)*5
		exurl=['']
		if "imdb" in cadulto:
			AddDir("[COLOR maroon]Reload[/COLOR]" , "", 50, isFolder=False)
			dir = re.sub('CubePlay', 'CubePlayMeta', addon_data_dir )
			file = os.path.join(dir, 'imdb.txt')
			chList = common.ReadList(file)
			exurl = re.compile('\_[^\']+').findall(str(chList))
		for x in range(0, 5):
			l +=1
			link = common.OpenURL(proxy+"https://"+RC+"browse-filmes-lancamentos-videos-"+str(l)+"-"+cOrdRCF+".html")
			if Clista0[int(Cat)] != "Lançamentos":
				link = common.OpenURL(proxy+"https://"+RC+"browse-"+Clista0[int(Cat)]+"-Filmes-videos-"+str(l)+"-"+cOrdRCF+".html")
			match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
            #match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
			if match:
			 for url2,name2,img2 in match:
					url2 = re.sub('^\.', "https://"+RC, url2 )
					img2 = re.sub('^/', "https://"+RC, img2 )
					if "criaturas-2-dublado-1989-720p" in url2: False
						#AddDir(name2 ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True)                       
					else:
						AddDir(name2 ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True)  
					p += 1
			else:
				break
		if p >= 40:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPage) + 2) +"][/B][/COLOR]", cPage , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPage")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "")
def MoviesRCL(): #91 Filme Legendado
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + Clista2[int(Cat)] +"[/COLOR]", "url" ,500 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	CategoryOrdem("cOrdRCF")
	try:
		p= 1
		if int(cPageleg) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageleg) ) +"][/B][/COLOR]", cPageleg , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageleg")
		l= int(cPageleg)*5
		for x in range(0, 5):
			l +=1
			link = common.OpenURL(proxy+"https://"+RC+"browse-filmes-legendado-videos-"+str(l)+"-"+cOrdRCF+".html")
			if Clista2[int(Cat)] != "Sem filtro (Mostrar Todos)":
				link = common.OpenURL(proxy+"https://"+RC+"browse-"+Clista2[int(Cat)]+"-Filmes-Legendado-videos-"+str(l)+"-"+cOrdRCF+".html")
			match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
			if match:
				for url2,name2,img2 in match:
					url2 = re.sub('^\.', "https://"+RC, url2 )
					img2 = re.sub('^/', "https://"+RC, img2 )
					if cPlayD == "true":
						AddDir(name2 ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True) 
					else:
						AddDir(name2 ,url2, 95, img2, img2, info="")
					p += 1
			else:
				break
		if p >= 40:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageleg) + 2) +"][/B][/COLOR]", cPageleg , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageleg")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "")
def MoviesRCN(): #92 Filmes Nacional
	CategoryOrdem("cOrdRCF")
	try:
		p= 1
		if int(cPagenac) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPagenac) ) +"][/B][/COLOR]", cPagenac , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPagenac")
		l= int(cPagenac)*5
		for x in range(0, 5):
			l +=1
			link = common.OpenURL(proxy+"https://"+RC+"browse-filmes-nacional-videos-"+str(l)+"-"+cOrdRCF+".html")
			match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
			if match:
				for url2,name2,img2 in match:
					url2 = re.sub('^\.', RC2, url2 )
					img2 = re.sub('^/', RC2, img2 )
					if cPlayD == "true":
						AddDir(name2 ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True)
					else:
						AddDir(name2 ,url2, 95, img2, img2, info="")
					p += 1
			else:
				break
		if p >= 40:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPagenac) + 2) +"][/B][/COLOR]", cPagenac , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPagenac")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def MoviesRCR(): # Lancamentos
	#CategoryOrdem("cOrdRCF")
	try:
		p= 1
		if int(cPagelan) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPagelan) ) +"][/B][/COLOR]", cPagelan , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPagelan")
		l= int(cPagelan)*5
		for x in range(0, 5):
			l +=1
			link = common.OpenURL(proxy+"https://"+RC+"browse-filmes-lancamentos-videos-"+str(l)+"-date.html")
			match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
			if match:
				for url2,name2,img2 in match:
					url2 = re.sub('^\.', "https://"+RC, url2 )
					img2 = re.sub('^/', "https://"+RC, img2 )
					if cPlayD == "true":
						AddDir(name2 ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True) 
					else:
						AddDir(name2 ,url2, 95, img2, img2, info="")
					p += 1
			else:
				break
		if p >= 40:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPagelan) + 2) +"][/B][/COLOR]", cPagelan , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPagelan")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def PlayMRC(): #95 Play filmes
	url2 = re.sub('redecanais\.[^\/]+', RC2, url.replace("http","https") )
	url2 = re.sub('^/', RC2, url2 )
	try:
		link = common.OpenURL(proxy+url2.replace("http\:","https\:"))
		desc = re.compile('itemprop=\"?description\"?>\s.{0,10}?<p>(.+)<\/p>').findall(link)
		if desc:
			desc = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), desc[0]).encode('utf-8')
		player = re.compile('<iframe.{1,50}src=\"([^\"]+)\"').findall(link)
		if player:
			#player = re.sub('.php', "playerfree.php", player[0] )
			player = re.sub('^/', "https://"+RC, player[0])
			mp4 = common.OpenURL(player ,headers={'referer': "https://cometa.top/"})
			file=re.compile('[^"|\']+\.mp4').findall(mp4)
			#mp4 = re.compile('server(f?\d*).+vid\=(\w+)').findall(player[0])
			#reg = "(.+)\\$rc"+mp4[0][0]
			#pb = common.OpenURL("https://pastebin.com/raw/FwSnnr65")
			#ss = re.compile('(.{1,65})RCFServer.{1,35}\.mp4').findall(pb)
			#pb = re.sub('\$s1\/', ss[0], pb )
			#pb = re.sub('\$s2\/', ss[1], pb )
			#m = re.compile(reg, re.IGNORECASE).findall(pb)
			#url2 = m[0]
			#file = mp4[0][1]+".mp4"
			AddDir("[B][COLOR yellow]"+ name +" [/COLOR][/B]"  , file[0] + reference2, 3, iconimage, iconimage, index=0, isFolder=False, IsPlayable=True, info=desc, background=url+";;;"+name+";;;RC")
		else:
			AddDir("[B]Ocorreu um erro[/B]"  , "", 0, iconimage, iconimage, index=0, isFolder=False, IsPlayable=False, info="Erro")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "")
#def PlayMRC21(): #96 Play filmes
#	url2 = re.sub('redecanais\.[^\/]+', RC2, url.replace("http\:","https\:") )
#	url2 = re.sub('^/', RC2, url2 )
#	try:
#		link = common.OpenURL(proxy+url2.replace("http\:","https\:"))
#		desc = re.compile('itemprop=\"?description\"?>\s.{0,10}?<p>(.+)<\/p>').findall(link)
#		if desc:
#			desc = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), desc[0]).encode('utf-8')
#		player = re.compile('Player "" src=\"([^\"]+)\"').findall(link)
#		if player:
			#mp4 = re.compile('server(f?\d*).+vid\=(\w+)').findall(player[0])
			#reg = "(.+)\\$rc"+mp4[0][0]
			#pb = common.OpenURL("https://pastebin.com/raw/FwSnnr65")
			#ss = re.compile('(.{1,65})RCFServer.{1,35}\.mp4').findall(pb)
			#pb = re.sub('\$s1\/', ss[0], pb )
			#pb = re.sub('\$s2\/', ss[1], pb )
			#m = re.compile(reg, re.IGNORECASE).findall(pb)
			#url2 = m[0]
			#file = url2 + mp4[0][1]+".mp4"
#			player = re.sub('^/', "https://"+RC, player[0])
			#player = re.sub('\.php', "-bk3.php", player)
			#auth = common.OpenURL(player ,headers={'referer': "https://dietafitness.fun/"})
			#exp = re.compile('expires\=([^\'|\"]+)').findall(auth)
#			player = re.sub('\.php', "hlb.php", player)
			#mp4 = common.OpenURL(player + "&expires=" + exp[0] ,headers={'referer': "https://dietafitness.fun/"})
#			mp4 = common.OpenURL(player, headers={'referer': "https://redecanais.se/"})
#			file=re.compile('<source src="([^"|\']+)" type=').findall(mp4)
#			global background
#			background=url+";;;"+name+";;;RC"
#			file[0] = re.sub('https', 'http', file[0])
#			PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", file[0] + reference2, iconimage, desc) #aqui
#		else:
#			AddDir("[B]Ocorreu um erro[/B]"  , "", 0, iconimage, iconimage, index=0, isFolder=False, IsPlayable=False, info="Erro")
#	except:
#		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "")
def PlayMRC2(): #96 Play filmes direto
	url2 = re.sub('redecanais\.[^\/]+', RC, url.replace("http\:","https\:") )
	if not "redecanais" in url2:
		url2 = "https://"+RC+ url2
	try:
		link = requests.get(url2)
		desc = re.compile('itemprop=\"?description\"?>\s.{0,10}?<p>(.+)<\/p>').findall(link.text)
		player = re.compile('<iframe name.+?src=.(.+?)"').findall(link.text)
		complement = re.compile('<iframe name.+?src=.(.+?)\/').findall(link.text)
		player2 = player[0]
		complement = complement[0]
		if desc:
			desc = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), desc[0]).encode('utf-8')
		if player2:
			player2 = re.sub('.php', "hlb.php", player2)
			player3 = "https://bemestarglobal.fun" + player2
			mp4 = common.OpenURL(player3 ,headers={'referer': "https://bemestarglobal.fun/"})
			file=re.compile('<source src=".([^"|\']+)" type=').findall(mp4)
			global background
			background=url+";;;"+name+";;;RC"
			try:
				file[0] = re.sub('\n', '', file[0])
				#file[0] = re.sub('https', 'https', file[0])
				#PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "https://bemestarglobal.fun" + complement + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc) #aqui
				PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "h" + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc)
			except IndexError as file:
				pass
			player2 = re.sub('.php', ".php", player2)
			player3 = "https://bemestarglobal.fun" + player2
			mp4 = common.OpenURL(player3 ,headers={'referer': "https://bemestarglobal.fun/"})
			file=re.compile('<source src=".([^"|\']+)" type=').findall(mp4)
			file[0] = re.sub('\n', '', file[0])
			#file[0] = re.sub('https', 'https', file[0])
			#PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "https://bemestarglobal.fun" + complement + file[0] + "|referer=https://bemestarglobal.fun/" , iconimage, desc) #aqui
			PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "h" + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc)
	except:
		#xbmcgui.Dialog().ok('Play XD', 'Erro, tente novamente em alguns minutos')
		sys.exit()
# ----------------- FIM REDECANAIS
# --------------  REDECANAIS SERIES,ANIMES,DESENHOS
def PlaySRC(): #133 Play series
	url2 = re.sub('redecanais\.[^\/]+', RC, url.replace("http\:","https\:") )
	if not "redecanais" in url2:
		url2 = "https://"+RC+ url2
	try:
		link = requests.get(url2)
		desc = re.compile('itemprop=\"?description\"?>\s.{0,10}?<p>(.+)<\/p>').findall(link.text)
		player = re.compile('<iframe name.+?src=.(.+?)"').findall(link.text)
		complement = re.compile('<iframe name.+?src=.(.+?)\/').findall(link.text)
		player2 = player[0]
		complement = complement[0]
		if desc:
			desc = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), desc[0]).encode('utf-8')
		if player2:
			player2 = re.sub('.php', "hlb.php", player2)
			player3 = "https://bemestarglobal.fun" + player2
			mp4 = common.OpenURL(player3 ,headers={'referer': "https://bemestarglobal.fun/"})
			file=re.compile('<source src=".([^"|\']+)" type=').findall(mp4)
			global background
			background=url+";;;"+name+";;;RC"
			try:
				file[0] = re.sub('\n', '', file[0])
				#file[0] = re.sub('https', 'https', file[0])
				#PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "https://bemestarglobal.fun" + complement + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc) #aqui
				PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "h" + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc)
			except IndexError as file:
				pass
			player2 = re.sub('.php', ".php", player2)
			player3 = "https://bemestarglobal.fun" + player2
			mp4 = common.OpenURL(player3 ,headers={'referer': "https://bemestarglobal.fun/"})
			file=re.compile('<source src=".([^"|\']+)" type=').findall(mp4)
			file[0] = re.sub('\n', '', file[0])
			#file[0] = re.sub('https', 'https', file[0])
			#PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "https://bemestarglobal.fun" + complement + file[0] + "|referer=https://bemestarglobal.fun/" , iconimage, desc) #aqui
			PlayUrl("[B][COLOR white]"+ name +" [/COLOR][/B]", "h" + file[0] + "|referer=https://bemestarglobal.fun/", iconimage, desc)
	except:
		sys.exit()
def TemporadasRC(x): #135 Episodios
	url2 = re.sub('redecanais\.[^\/]+', RC, url.replace("http\:","https\:") )
	if not "redecanais" in url2:
		url2 = "https://"+RC+ url2
	link = common.OpenURL(proxy+url2).replace('\n','').replace('\r','').replace('</html>','<span style="font').replace("http\:","https\:")
	temps = re.compile('(<span style="font-size: x-large;">(.+?)<\/span>)').findall(link)
	i= 0
	if background=="None":
		for b,tempname in temps:
			tempname = re.sub('<[\/]{0,1}strong>', "", tempname)
			try:
				tempname = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), tempname).encode('utf-8')
			except:
				tempname = tempname
			if not "ilme" in tempname:
				AddDir("[B]["+tempname+"][/B]" , url, 135, iconimage, iconimage, info="", isFolder=True, background=i)
			i+=1
		AddDir("[B][Todos Episódios][/B]" ,url, 139, iconimage, iconimage, info="")
	else:
		temps2 = re.compile('size: x-large;\">.+?<span style\=\"font').findall(link)
		epi = re.compile('<strong>(E.+?)<a .+?(\/.+?)".+?(<br|<\/p)').findall(temps2[int(x)])
		for name2,url2,brp in epi:
			h = HTMLParser()
			name3 = h.unescape(name2).encode('utf-8')
			AddDir(name3.replace("</strong>","").replace("-",""), "https://" + RC+url2, 133, iconimage, iconimage, info="", isFolder=False, IsPlayable=True)
def SeriesRC(urlrc,pagina2): #130 Lista as Series RC
	try:
		CategoryOrdem("cOrdRCS")
		pagina=eval(pagina2)
		p= 1
		if int(pagina) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background=pagina2)
		l= int(pagina)*5
		for x in range(0, 5):
			l +=1
			link = common.OpenURL(proxy+"https://" + RC + "browse-"+urlrc+"-videos-"+str(l)+"-"+cOrdRCS+".html")
			match = re.compile('href=\"([^\"]+).{0,10}title=\"([^\"]+)\".{20,350}echo=\"([^\"]+)').findall(link.replace('\n','').replace('\r',''))
			if match:
				for url2,name2,img2 in match:
					url2 = re.sub('^\.', RC2, url2 )
					img2 = re.sub('^/', RC2, img2 )
					if not "index.html" in url2:
						AddDir(name2 ,url2, 135, img2, img2, info="")
						p += 1
			else:
					break
		if p >= 40:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background=pagina2)
	except urllib2.URLError, e:
		AddDir("Server error, tente novamente em alguns minutos" , url, 0, "", "")
def AllEpisodiosRC(): #139 Mostrar todos Epi
	url2 = re.sub('redecanais\.[^\/]+', RC, url.replace("http\:","https\:") )
	if not "redecanais" in url2:
		url2 = "https://"+ RC + url2
	link = common.OpenURL(url2)
	match = re.compile('<strong>(E.+?)<\/strong>(.+?)(<br|<\/p)').findall(link)
	S= 0
	if match:
		for name2,url2,brp in match:
			name3 = re.compile('\d+').findall(name2)
			if name3:
				name3=name3[0]
				if int(name3) == 1:
					S = S + 1
			else:
				name3=name2

			urlm = re.compile('href\=\"(.+?)\"').findall(url2)
			try:
				namem = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), re.compile('([^\-]+)').findall(url2)[0] ).encode('utf-8')
			except:
				namem = re.compile('([^\-]+)').findall(url2)[0]
			if "<" in namem:
				namem = ""
			if urlm:
				if "http" not in urlm[0]:
					urlm[0] = "https://"+ RC + urlm[0]
			if len(urlm) > 1:
				if "http" not in urlm[1]:
					urlm[1] = "https://"+ RC  + urlm[1]
				AddDir("[COLOR yellow][Dub][/COLOR] S"+str(S)+" E"+ name3 +" "+namem ,urlm[0], 133, iconimage, iconimage, info="", isFolder=False, IsPlayable=True)
				AddDir("[COLOR blue][Leg][/COLOR] S"+str(S)+" E"+ name3 +" "+namem ,urlm[1], 133, iconimage, iconimage, info="", isFolder=False, IsPlayable=True)
			elif urlm:
				AddDir("S"+str(S)+" E"+ name3 +" "+namem ,urlm[0], 133, iconimage, iconimage, info="", isFolder=False, IsPlayable=True)
# ----------------- FIM REDECANAIS SERIES,ANIMES,DESENHOS
# ----------------- BUSCA
def Busca(): # 160
	AddDir("[COLOR pink][B][Nova Busca][/B][/COLOR]", "" , 50 ,"https://uploaddeimagens.com.br/images/002/376/135/original/941129_stock-photo-illustration-of-a-magnifying-glass.jpg", isFolder=False)
	d = xbmcgui.Dialog().input("Busca (poder demorar a carregar os resultados)").replace(" ", "+")
	d = urllib.quote_plus(d)
	progress = xbmcgui.DialogProgress()
	progress.create('Buscando...')
	progress.update(0, "0%", "Netcine", "")
	if not d:
		return Categories()
		sys.exit(int(sys.argv[1]))
#	try:
#		p= 1
#		AddDir("[COLOR blue][B]RedeCanais[/B][/COLOR]", "" , 0 ,"", isFolder=False)
#		l= 0
#		for x in range(0, 10):
#			l +=1
#			link = common.OpenURL(proxy+"https://" + RC +"search.php?keywords="+d+"&page="+str(l))
#			match = re.compile('data\-echo\=\"([^\"]+).{10,150}href=\"([^\"]+).{0,10}title=\"([^\"]+)\"').findall(link.replace('\n','').replace('\r',''))
#			if match:
#				for img2,url2,name2 in match:
#					#url2 = re.sub('^\.', "http://www." + RC, url2 )
#					url2 = re.sub('^\.', "https://"+RC, url2 )
#					img2 = re.sub('^/', "https://"+RC, img2 )
#					if re.compile('\d+p').findall(name2):
#						if cPlayD == "true":
#							AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True)
#						else:
#							AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 95, img2, img2)
#					elif "Lista" in name2:
#						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 135, img2, img2)
#			else:
#				break
#	except:
#		pass
	try:
		proxy = requests.get("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/proxy")
		proxy2 = re.compile('proxy = "(.+?)"').findall(proxy.text)
		AddDir("[B][COLOR yellow]|||[/COLOR][COLOR white]|||[/COLOR][COLOR yellow]|||[/COLOR][COLOR yellow] [NetCine] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",'Cache-Control': 'no-cache','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7#','Referer': 'https://netcine.biz/','Keep-Alive': '','Connection': 'keep-alive'}
		proxies = {"http": proxy2[0], "https": proxy2[0]}
		link2 = requests.get("http://netcine.biz/?s="+d,headers=headers, proxies=proxies)
		lista = re.compile("\s.{1,12}<img src\=\"([^\"]+).+?alt\=\"([^\"]+).+?f\=\"([^\"]+)").findall(link2.text.encode('utf-8').replace('\n','').replace('\r',''))
		for img2,name2,url2 in lista:
			if name2!="Close" and name2!="NetCine":
				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
				img2 = img2.replace("-120x170","")
				if "tvshows" in url2:
					AddDir("[COLOR yellow]" +name2+ "[/COLOR]",url2, 61, img2, img2, isFolder=True)
				else:
					AddDir("[COLOR yellow]" +name2+ "[/COLOR]",url2, 78, img2, img2, isFolder=True)
	except:
		pass
	progress.update(32, "32%", "MMfilmes", "")
	l=0
	i=0
	try:
		AddDir("[B][COLOR cyan]|||[/COLOR][COLOR white]|||[/COLOR][COLOR cyan]|||[/COLOR][COLOR cyan] [MMfilmes] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		links = common.OpenURL("http://www.mmfilmes.tv/series/")
		ms = re.compile('href\=\"(.+www.mmfilmes.tv.+)\" rel\=\"bookmark\"').findall(links)
		for x in range(0, 3):
			l+=1
			link = common.OpenURL("http://www.mmfilmes.tv/page/"+str(l)+"/?s="+d).replace('\n','').replace('\r','')
			m = re.compile('<li id=.+?" title="(.+?)".+?href="(.+?)".+?boxxer.+?boxxer">(.+?)<.+?src="(.+?)".+?audioy..(.+?)<').findall(link)
			if m:
				for name2, url2, dubleg, jpg, res in m:
					name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'")
					dubleg = dubleg.replace("</div>","")
					if not url2 in ms:
						AddDir("[COLOR cyan]" +name2+ "[/COLOR] [COLOR yellow]"+res+"[/COLOR] [COLOR green]"+dubleg+"[/COLOR]", url2, 181, jpg, jpg,isFolder=True,IsPlayable=False)
					else:
						AddDir("[COLOR cyan]" +name2+ "[/COLOR]", url2, 191, jpg, jpg, isFolder=True,IsPlayable=False)
					i+=1
			i=0
	except:
		pass
	progress.update(48, "48%", "TopFlix", "")
	try:
		p= 1
		AddDir("[B][COLOR red]|||[/COLOR][COLOR white]|||[/COLOR][COLOR red]|||[/COLOR][COLOR red] [TopFlix] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		l= 0
		for x in range(0, 1):
			url = ('https://topflix.tv/landing')
			result = {'search': d.replace("%2B"," ")}
			f = requests.post(url, data=result)
			f = f.text.replace("color='white'>", " title='").replace("</font>", "'").replace("><font ", "")
			arquivo = urllib.quote(f.encode('utf8'))
			arquivo2 = urllib.unquote(arquivo)
			match = re.compile("'(.{5,30}[^\']jpg).+?href.+?href.+?href.+?href='([^\']+).+?tle='(\w.+?)'").findall(arquivo2)
			if match:
				for img2, url2, name2 in match:
					img2 = img2.replace('170255',"330490")
 					if "series" in url2: False
					else:
						AddDir("[COLOR red]" +name2+ "[/COLOR]" , RC4 + url2, 211, RC4 + img2, info="", isFolder=True, IsPlayable=False)
	except:
		pass
	progress.update(64, "64%", "Vizer.tv", "")
	try:
		i=0
		p= 1
		AddDir("[B][COLOR mediumpurple]|||[/COLOR][COLOR white]|||[/COLOR][COLOR mediumpurple]|||[/COLOR][COLOR mediumpurple] [Vizer.tv] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		l= 0
		for x in range(0, 1):
			l +=1
			link = common.OpenURL("https://vizer.tv/pesquisar/"+d.replace("%2B","%20"))
			match = re.compile('Assistir (.+?) online" class="(.+?)".href="(.+?)".+\s.+?="(.+?)" class="lazy"').findall(link)
			if match:
				for name2, tipo,url2, img2 in match:
					url3 = "https://vizer.tv/" + url2
					img2= img2.replace("w185","original")
					if "serie" in tipo:
						AddDir("[COLOR mediumpurple]" +name2+ "[/COLOR]" ,url3, 451, img2, img2, info="", isFolder=True, IsPlayable=True)
					else:
						AddDir("[COLOR mediumpurple]" +name2+ "[/COLOR]" ,url3, 601, img2, img2, info="", isFolder=True, IsPlayable=True)
						i+=1
	except:
		pass    
	progress.update(75, "75%", "Assistir.Biz", "")
	try:
		p= 1
		AddDir("[B][COLOR deepskyblue]|||[/COLOR][COLOR white]|||[/COLOR][COLOR deepskyblue]|||[/COLOR][COLOR deepskyblue] [Assistir.Biz] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		l= 0
		for x in range(0, 1):
			l +=1
			link = common.OpenURL("https://assistir.biz/busca?q="+d)
			match = re.compile('data-src="([^\"]+)".+\s.+.\s.+.\s.+.\s.+.\s.+.\s.+.\s.+?a href="([^\"]+)".alt="([^\"]+)".+\s.+\s.+?">([^\"]+)<\/a').findall(link)
			if match:
				for img2,url2,name2, ano in match:
					url2= url2.replace("/filme","https://assistir.biz/filme")
					img2= img2.replace("//image","https://image").replace("w185","original")
					if "tvshows" in url2: False
					else:
						AddDir("[COLOR deepskyblue]" +name2+ " - ("+ano+")[/COLOR]", url2, 515, img2, img2, info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
	except:
		pass
	#progress.update(73, "73%", "VerFilmesHD", "")
	#try:
	#	p= 1
	#	AddDir("[B][COLOR palevioletred]|||[/COLOR][COLOR white]|||[/COLOR][COLOR palevioletred]|||[/COLOR][COLOR palevioletred] [VerFilmesHD] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
	#	l= 0
	#	for x in range(0, 1):
	#		l +=1
	#		link = common.OpenURL("https://verfilmeshd.gratis/?s="+d)
	#		match = re.compile('href="([^\"]+)".{1,60}oldtitle="([^\"]+)".{1,30}img src="([^\"]+)".+?IMDb..([^\"].+?)<.+?tag">([^\"].+?)<').findall(link)
	#		if match:
	#			for url2, name2, img2, imdb, ano in match:
	#				name2= name2.replace("Online","").replace("Dublado", "[COLOR blue] (Dublado)[/COLOR]").replace("Legendado", "[COLOR blue] (Legendado)[/COLOR]").replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…').replace('&#039;',"'")
	#				if "tvshows" in url2: False
	#				else:
	#					AddDir("[COLOR palevioletred]" +name2+"[/COLOR]", url2, 531, img2, img2, isFolder=True, IsPlayable=True, info="IMDB: "+imdb+"   Ano: "+ano)
	#except:
	#	pass
	#progress.update(80, "80%", "QueroFilmesHD", "")        
	#try:
	#	p= 1
#		AddDir("[B][COLOR springgreen]|||[/COLOR][COLOR white]|||[/COLOR][COLOR springgreen]|||[/COLOR][COLOR springgreen] [QueroFilmesHD] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
#		l= 0
#		for x in range(0, 1):
#			l +=1
#			link = common.OpenURL("https://querofilmeshd.online/?s="+d).replace('\n','').replace('\r','')
#			match = re.compile('<img src="([^\"]+)".+?alt="([^\"]+)".+?href="([^\"]+).+?"year">(\w+)').findall(link.replace('\n','').replace('\r',''))
#			if match:
#				for img2,name2,url2,ano in match:
#					img2= img2.replace("w92","original")
#					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
#					if "tvshows" in url2:
#						AddDir("[COLOR springgreen]" +name2+ " - ("+ano+")"+"[/COLOR]" ,url2, 431, img2, img2, info="", isFolder=True, IsPlayable=True)#.replace('original','w92')
#					else:
#						AddDir("[COLOR springgreen]" +name2+ " - ("+ano+")"+"[/COLOR]" ,url2, 511, img2, img2, info="", isFolder=True, IsPlayable=True)
#	except:
#		pass        
#	try:
#		p= 1
#		AddDir("[COLOR red][B][TopFlix][/B][/COLOR]", "" , 0 ,"", isFolder=False)
#		l= 0
#		for x in range(0, 1):
#			link = common.OpenURL("https://www.ecosia.org/search?q=topflix.tv+"+d+"")
#			l +=1
#			match = re.compile('href\=\"(https?\:.{0,50}topflix.tv\/[^\"]+)\"\s+>\s+TopFlix.-.Assistir.([^\"]+)Online').findall(link.replace('\n','').replace('\r',''))
#			if match:
#				for url2,name2 in match:
#					if "lista" in url2 or "Lista" in name2:
#						AddDir("[COLOR red]" +name2+ "[/COLOR]" , url2, 211, " ", " ", info="", isFolder=True, IsPlayable=False)
#					else:
#						AddDir("[COLOR red]" +name2+ "[/COLOR]" , url2, 211, " ", " ", info="", isFolder=True, IsPlayable=True)
#	except:
#		pass
#	progress.update(80, "80%", "RedeCanais", "")
#	try:
#		i=0
#		p= 1
#		AddDir("[B][COLOR blue]|||[/COLOR][COLOR white]|||[/COLOR][COLOR blue]|||[/COLOR][COLOR blue] [RedeCanais] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
#		l= 0
#		for x in range(0, 1):
#			l +=1
#			url3 = ('https://redecanais.se/ajax_search.php')
#			result = {'queryString': d}
#			f = requests.post(url3, data=result)
#			arquivo2 = urllib.quote(f.text.encode('utf8'))
#			String2 = urllib.unquote(arquivo2)
#			match = re.compile('href="(.+?)">(.+?)<').findall(String2)
#			img2 = re.compile('href=".+?>(.+?) -').findall(String2.replace(" (Dublado)", "").replace(" (Legendado)", ""))
#			if match:
#				for url2, name2 in match:
#					if "browse" in url2 or "lista" in url2:
#						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 135, "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20")+".jpg", "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20")+".jpg", info="", isFolder=True, IsPlayable=False)
#					#if "lista" in url2:
#					else:
#						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 96, "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20").replace(":"," -")+".jpg", "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20")+".jpg", info="", isFolder=False, IsPlayable=True)
#					i+=1
#	except:
#		pass
	progress.update(90, "90%", "RedeCanais", "")
	try:
		p= 1
		AddDir("[COLOR blue][B]RedeCanais[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		l= 0
		for x in range(0, 10):
			l +=1
			link = common.OpenURL(proxy+"https://" + RC +"search.php?keywords="+d+"&page="+str(l))
			match = re.compile('data\-echo\=\"([^\"]+).{10,150}href=\"([^\"]+).{0,10}title=\"([^\"]+)\"').findall(link.replace('\n','').replace('\r',''))
			if match:
				for img2,url2,name2 in match:
					#url2 = re.sub('^\.', "http://www." + RC, url2 )
					url2 = re.sub('^\.', "https://"+RC, url2 )
					img2 = re.sub('^/', "https://"+RC, img2 )
					if re.compile('\d+p').findall(name2):
						if cPlayD == "true":
							AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 96, img2, img2, info="", isFolder=False, IsPlayable=True)
						else:
							AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 95, img2, img2)
					elif "Lista" in name2:
						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 135, img2, img2)
			else:
				break
	except:
		pass
#	try:
#		i=0
#		p= 1
#		AddDir("[B][COLOR blue]|||[/COLOR][COLOR white]|||[/COLOR][COLOR blue]|||[/COLOR][COLOR blue] [RedeCanais] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
#		l= 0
#		for x in range(0, 2):
#			link = common.OpenURL("https://www.google.com/search?q="+d+"+site:redecanais.se&hl=pt-BR&&start="+str(l))
#			l +=2
#			match = re.compile('href\=\"(https?\:.{0,50}redecanais[^\"]+)\".{50,200}\>([^\<]+)').findall(link.replace('\n','').replace('\r',''))
#			img2 = re.compile('href\=\"https?\:.{0,50}redecanais[^\"]+\".{50,200}\>([^\<].+?) -').findall(link.replace('\n','').replace('\r','').replace(" (Dublado)", "").replace(" (Legendado)", ""))
#			if match:
#				for url2, name2 in match:
#					if "browse" in url2 or "lista" in url2:
#						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 135, "https://redecanais.se/imgs-videos/Series/"+ img2[i].replace(" ","%20")+"%201.jpg", "https://redecanais.se/imgs-videos/Series/"+ img2[i].replace(" ","%20")+"%201.jpg", info="", isFolder=True, IsPlayable=False)
#					if "lista" in url2 or "Lista" in name2 or "browse-filmes-dublado-videos" in url2 or "topvideos" in url2 or "tags" in url2 or "Filmes em Lançamentos - RedeCanais" in name2: False
#					else:
#						AddDir("[COLOR blue]" +name2+ "[/COLOR]" ,url2, 96, "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20").replace(":"," -")+".jpg", "https://redecanais.se/imgs-videos/Filmes/"+ img2[i].replace(" ","%20")+".jpg", info="", isFolder=False, IsPlayable=True)
#					i+=1
#	except:
#		pass
	progress.update(100, "100%", "SuperFlix", "")        
	try:
		p= 1
		AddDir("[B][COLOR lightgreen]|||[/COLOR][COLOR white]|||[/COLOR][COLOR lightgreen]|||[/COLOR][COLOR lightgreen] [SuperFlix] •[/B][/COLOR]", "" , 0 ,"", isFolder=False)
		l= 0
		for x in range(0, 1):
			l +=1
			link = common.OpenURL("https://www.superflix.net/?s="+d).replace('\n','').replace('\r','')
			match = re.compile('"> <art.+?title">([^\"].+?)<.+?src="([^\"].+?)".+?sm">Ver.([^\"].+?)<.+?href="([^\"].+?)"').findall(link.replace('\n','').replace('\r',''))
			if match:
				for name2, img2, tvmovie, url2 in match:
					img2 = img2.replace("w185", 'original').replace("https:", '').replace("w220_and_h330_face", 'original').replace("-185x278", "")
					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
					if "Filme" in tvmovie:
						AddDir("[COLOR lightgreen]"+name2+"[/COLOR]", url2, 405, "http:"+img2, "http:"+img2,isFolder=True,IsPlayable=False, info='[COLOR][/COLOR]')
					if "Série" in tvmovie:
						AddDir("[COLOR lightgreen]"+name2+"[/COLOR]", url2, 402, "http:"+img2, "http:"+img2,isFolder=True,IsPlayable=False)
	except:
		pass        
	progress.update(100, "100%", "", "")
	progress.close()
    
	#l=0
	#i=0
	#try:
	#	AddDir("[COLOR maroon][B][Gofilmes.me][/B][/COLOR]", "" , 0 ,"", isFolder=False)
	#	for x in range(0, 3):
	#		l+=1
	#		link = common.OpenURL("http://gofilmes.me/search?s="+d+"&p="+str(l)).replace("</div><div","\r\n")
	#		m = re.compile('href=\"([^\"]+)\" title\=\"([^\"]+).+b\" src\=\"([^\"]+).+').findall(link)
	#		for url2,name2,img2 in m:
	#			AddDir(name2, url2, 211, img2, img2, isFolder=False, IsPlayable=True)
	#except:
	#	pass
# ----------------- FIM BUSCA
# ----------------- TV Cubeplay
def TVCB(x): #102
	#AddDir("reload", "", 50, "", "", isFolder=False, IsPlayable=False, info="")
	link = common.OpenURL("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/redecanaisall").replace("\n","")
	if cadulto!="8080":
		link = re.sub('Adulto.+', "", link)
	m = re.compile('url="(.+?)".mg="(.+?)".ame="(.+?)"').findall(link)
	#ST(m)
	for url2,img2,name2 in m:
		AddDir(name2 , url2, 103, img2, img2, isFolder=False, IsPlayable=True, info='[COLOR][/COLOR]')
	
	#try:
	#AddDir("Play", m[0], 50, "", "", isFolder=False, IsPlayable=True, info="")
	#	link = common.OpenURL(x)
	#	link = re.sub('^.{3}', "", link )
	#	m = re.compile('(.+)\?(.+)').findall(link)
	#	i=0
	#	for name2,url2 in m:
	#		if cadulto=="8080":
	#			AddDir(getmd5(name2), url2, 103, " ", " ", isFolder=False, IsPlayable=True, info="")
	#			i+=1
	#		elif not "dulto" in getmd5(name2):
	#			AddDir(getmd5(name2), url2, 103, " ", " ", isFolder=False, IsPlayable=True, info="")
	#			i+=1
	#except:
	#	AddDir("Servidor offline, tente novamente em alguns minutos" , "", 0, "", "", 0)
def PlayTVCB(): #103
	link = requests.get("https://redecanaistv.com/"+url, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"})
	player = re.compile('<iframe.{1,50}src=\"([^\"]+)\"').findall(link.text)
	player = re.sub('^/', "https://lojadebicicleta.com.br/", player[0])
	player = re.sub('.php', ".php", player)
	m3u = requests.get(player, headers={'referer': "https://lojadebicicleta.com.br/", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'})
	m = re.compile('http.{10,250}?m3u8[^"|\n|\']{0,100}').findall(m3u.text)
	try:
		m2 = re.sub('https', 'https', m[0])
		PlayUrl(name, m2 + reference3, iconimage, name, "")
	except IndexError as m2:
		pass
	player = re.sub('.php', "hlb.php", player)
	m3u = requests.get(player, headers={'referer': "https://lojadebicicleta.com.br/", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'})
	m = re.compile('http.{10,250}?m3u8[^"|\n|\']{0,100}').findall(m3u.text)
	m2 = re.sub('https', 'https', m[0])
	PlayUrl(name, m2 + reference3, iconimage, name, "")
        
##########################################################################################
###########################################################################################
# ----------------- Fim TV Cubeplay
# ----------------- REDECANAIS TV
def Acento(x):
	x = x.replace("\xe7","ç").replace("\xe0","à").replace("\xe1","á").replace("\xe2","â").replace("\xe3","ã").replace("\xe8","è").replace("\xe9","é").replace("\xea","ê").replace("\xed","í").replace("\xf3","ó").replace("\xf4","ô").replace("\xf5","õ").replace("\xfa","ú")
	return x
def EPG():
	epg1 = "{"
	try:
		xbmc.executebuiltin("Notification({0}, {1}, 7000, {2})".format(AddonName, "Carregando lista EPG. Aguarde um momento!", icon))
		link = common.OpenURL("http://www.epg.com.br/~mysql41/vertv.php").replace('	','')
		m = re.compile('javascript:toggleCanal\(\d+,.([^\']+)\h*(?s)(.+?)\<\!-- orig').findall(link)
		for c,f in m:
			hora = ""
			m2 = re.compile('(.+)(\(\d+.\d+\))\s').findall(f)
			if m2:
				for prog1,prog2 in m2:
					hora += prog2 +" "+ prog1 + ";;;"
					try:
						hora= Acento(hora)
					except:
						hora = hora
			hora = hora.replace("'","")
			epg1 += "'"+c+"' : '"+hora+"' , "
		return epg1+"'none':''}"
	except urllib2.URLError, e:
		return ""
		xbmc.executebuiltin("Notification({0}, {1}, 7000, {2})".format(AddonName, "Erro. tente novamente!", icon))
def TVRC(): #100
	c = ["Categoria","Alfabético"]
	d = xbmcgui.Dialog().select("Qual a ordem dos canais?", c)
	link = common.OpenURL("http://cubeplay.000webhostapp.com/epg/_rc.php?c="+str(d))
	#link = common.OpenURL("http://localhost:8080/epg/_rc.php?c="+str(d))
	match = re.compile('tvg\-logo\=\"([^\"]+).+,(.+)\s(.+)|,(.+)\s(.+)').findall(link)
	for img2,name2,url2,a,c in match:
		AddDir(name2, url2, 3, img2, img2, isFolder=False, IsPlayable=True, info='[COLOR][/COLOR]')
def PlayTVRC(): # 101
	#url2 = re.sub('redecanais\.[^\/]+', "redecanais.xyz", url.replace("https","http") )
	try:
		link = common.OpenURL(url)
		#player = re.compile('<iframe name=\"Player\".+src=\"([^\"]+)\"').findall(link)
		player = re.compile('<iframe name=\"Player\".+src=\"[^\"]+\=([^\"]+)').findall(link)
		#ST(player[0])
		#link2 = common.OpenURL(player[0])
		#m2 = re.compile('action="[^\"]+\=([^\"]+)').findall(link2)
		#m2[0] = re.sub('.\/', 'https://canais.ink/', m2[0])
		link3 = common.OpenURL("http://cometa.top/player3/canaisvibfree.php?canal="+player[0],headers={'referer': "http://social.olimpicusads.com/"})
		ST(link3)
		#ST(link3)
		#http://cometa.top/player3/canaisvibfree.php?canal=
		urlp = re.compile('(http[^\"]+m3u[^\"]+)').findall(link3)
		#ST(urlp[0])
		if urlp:
			#ST(urlp[0])
			PlayUrl(name, urlp[0] + "|Referer=http://canaisgratis.info/player3/canaisvibfree.php?canal=", iconimage, info)
		else:
			xbmcgui.Dialog().ok('Play XD', "Erro, aguarde atualização")
	except:
		xbmcgui.Dialog().ok('Play XD', 'Erro, tente novamente em alguns minutos')
# ----------------- FIM REDECANAIS TV
# ----------------- Inicio Filmes Online
def GenerosFO(): #85
	d = xbmcgui.Dialog().select("Escolha o Genero", Clistafo1)
	if d != -1:
		global Cat
		Addon.setSetting("Catfo", str(d) )
		Cat = d
		Addon.setSetting("cPagefo1", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
		
def MoviesFO(urlfo,pagina2): #170
	AddDir("[COLOR yellow][B][Gênero dos Filmes]:[/B] " + Clistafo1[int(Catfo)] +"[/COLOR]", "url" ,85 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False)
	CategoryOrdem("cOrdFO")
	try:
		pagina=eval(pagina2)
		l= int(pagina)*5
		p= 1
		if int(pagina) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background=pagina2)
		for x in range(0, 5):
			l +=1
			ordem = "asc" if cOrdFO=="title" else "desc"
			link = common.OpenURL("https://hdfilmes.pro/index.php?do=search&subaction=search&search_start="+str(l)+"&story="+urlfo+"&sortby="+cOrdFO+"&resorder="+ordem+"&catlist[]="+Clistafo0[int(Catfo)]).replace("\r","").replace("\n","")
			link = re.sub('Novos Filmes.+', '', link)
			m = re.compile('src=\"(.upload[^\"]+).+?alt=\"([^\"]+).+?href=\"([^\"]+)').findall(link)
			m2 = re.compile('numb-serial..(.+?)\<.+?afd..(\d+)').findall(link)
			i=0
			if m:
				#xbmcgui.Dialog().ok('Play XD', str(m))
				for img2,name2,url2 in m:
					AddDir(name2 + " ("+m2[i][0]+") - " + m2[i][1], url2, 171, "https://hdfilmes.pro/"+img2, "https://hdfilmes.pro/"+img2, info="", background=url)
					p+=1
					i+=1
		if p >= 80:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background=pagina2)
	except urllib2.URLError, e:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "")
		
def PlayMFO1(): #172
	if re.compile('\d+').findall(str ( background )) :
		s = background.split(",")
		sel = xbmcgui.Dialog().select("Selecione a resolução", s)
		if sel!=-1:
			link = common.OpenURL(url+"?q="+s[sel] )
			#ST(link)
			m = re.compile('https[^\"]+\.mp4').findall(link)
			PlayUrl(name, m[0],"",info)
	else:
		link = common.OpenURL(url)
		m = re.compile('https[^\"]+\.mp4').findall(link)
		background = "None"
		PlayUrl(name, m[0],"",info)
		
def GetMFO1(): #171
	try:
		link = common.OpenURL( url )
		m = re.compile('href\=\"(.+?\#Rapid)').findall(link)
		t = re.compile('class=\"titleblock\"\>\s\<h1\>([^\<]+)').findall(link)
		i = re.compile('class=\"p-info-text\"\>\s\<span\>([^\<]+)').findall(link)
		if m:
			link2 = common.OpenURL( "https://hdfilmes.pro"+m[0] )
			m2 = re.compile('iframe.+?src\=\"([^\"]+)').findall(link2)
			#ST(m2)
			if m2:
				title = t[0] if t else name
				info = i[0] if i else ""
				link3 = common.OpenURL("https:"+m2[0] )
				#ST(link3 )
				m3 = re.compile('https[^\"]+\.mp4').findall(link3)
				if m3:
					pp = re.compile('q=(\d+p)').findall(link3)
					pp = list(reversed(pp))
					AddDir( title , "https:"+m2[0], 172, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info, background= ",".join(pp))
				else:
					AddDir( "Video offline!!" ,"", 0, "", "", isFolder=False)
	except urllib2.URLError, e:
		AddDir( "Video offline" ,"", 0, "", "", isFolder=False)
# ----------------- FIM Filmes Online
# ----------------- Inicio MM filmes
def GenerosMM(): #189
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaMM1)
	if d != -1:
		global Cat
		Addon.setSetting("CatMM", str(d) )
		Cat = d
		Addon.setSetting("cPageMMf", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def ListFilmeLancMM(): #184
	l=0
	i=0
	try:
		links = common.OpenURL("http://www.mmfilmes.tv/series/")
		ms = re.compile('href\=\"(.+www.mmfilmes.tv.+)\" rel\=\"bookmark\"').findall(links)
		for x in range(0, 5):
			l+=1
			link = common.OpenURL("http://www.mmfilmes.tv/ultimos/page/"+str(l)+"/")
			m = re.compile('id\=\"post\-\d+\".+?\=.([^\"]+)\h*(?s)(.+?)(http[^\"]+)').findall(link)
			res = re.compile('audioy..([^\<]*)').findall(link)
			jpg = re.compile('src=\"(http.+?www.mmfilmes.tv\/wp-content\/uploads[^\"]+)').findall(link)
			dubleg = re.compile('boxxer.+\s.+boxxer..([^\<]*)').findall(link)
			if m:
				for name2,b,url2 in m:
					name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'").replace("&#8230;","")
					if not url2 in ms:
						AddDir(name2+ " [COLOR yellow]"+res[i]+"[/COLOR] [COLOR green]"+dubleg[i]+"[/COLOR]", url2, 181, jpg[i], jpg[i],isFolder=True,IsPlayable=False, info='[COLOR][/COLOR]')
					i+=1
			i=0
	except:
		pass
def ListFilmeMM(pagina2): #180
	AddDir("[COLOR yellow][B][Gênero dos Filmes]:[/B] " + ClistaMM1[int(CatMM)] +"[/COLOR]", "url" ,189 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	pagina=eval(pagina2)
	l= int(pagina)*4
	p=1
	if int(pagina) > 0:
		AddDir("[COLOR lime][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background=pagina2, info='[COLOR][/COLOR]')
	try:
		links = common.OpenURL("http://www.mmfilmes.tv/series/")
		ms = re.compile('href\=\"(.+www.mmfilmes.tv.+)\" rel\=\"bookmark\"').findall(links)
		for x in range(0, 4):
			l+=1
			link = common.OpenURL("http://www.mmfilmes.tv/"+ ClistaMM0[int(CatMM)] +"/page/"+str(l)+"/").replace('\n','').replace('\r','')
			m = re.compile('<li id=.+?" title="(.+?)".+?href="(.+?)".+?boxxer.+?boxxer">(.+?)<.+?src="(.+?)".+?audioy..(.+?)<').findall(link)
			if m:
				for name2, url2, dubleg, jpg, res in m:
					name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'").replace("&#8230;","")
					dubleg = dubleg.replace("</div>","")
					if not url2 in ms:
						AddDir(name2+ " [B][COLOR yellow]"+res+"[/COLOR][/B] [B][COLOR cyan]"+dubleg+"[/COLOR][/B]", url2, 181, jpg, jpg,isFolder=True,IsPlayable=False, info='[COLOR][/COLOR]')
					p+=1
			if p >= 40:
				AddDir("[COLOR lime][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background=pagina2)
	except:
		pass
def OpenLinkMM(): #181
	link = common.OpenURL(url)
	m = re.compile('boxp\(.([^\']+)').findall(link) #princi
	info2 = re.compile('mCSB_container..\s(\h*(?s)(.+?))\<\/div').findall(link)
	info2= info2[0][0].replace("\t","") if info2 else ""
	if m:
		link2 = common.OpenURL(m[0],headers={'referer': "http://www.mmfilmes.tv/"})
		m2 = re.compile('opb\(.([^\']+).+?.{3}.+?[^\\>]+.([^\<]+)').findall(link2)
		if m2:
			name2 = re.sub(' \[.+', '', name )
			for link,dubleg in m2:
				AddDir( name2 +" [B][COLOR lime]("+dubleg+")[/COLOR][/B]" ,link, 182, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
def PlayLinkMM(): #182
	link = requests.get(url, headers={'referer': "http://www.mmfilmes.tv/"})
	m = re.compile("addiframe.'https:\/\/player.openload.network\/qweowqie.php.([^\']+)").findall(link.text)
	#result = {'mm': '1', 'url': m2, 'auth': 'benefits-and-risks-of-credit-cards'}
	#r = requests.post('https://noticiasemfoco.online/benefits-and-risks-of-credit-cards/', cookies=result)
	if m:
		m[0] = "https://player.openload.network/abcde.php?" + m[0] if not "http" in m[0] else m[0]
		link2 = common.OpenURL(re.sub('(\/.{1,25}\/).{1,10}\/', r'\1', m[0]),headers={'referer': "http://player.openload.network"}).replace("file","\nfile")
		#m2 = re.compile("file.+?(h[^\']+).+?(\,)").findall(link2)
		m2 = re.compile('(:\/\/[^\']+).+?(\d+p)\'').findall(link2)  #player mp4
		legenda = re.compile('([^\']+\.(vtt|srt|sub|ssa|txt|ass))').findall(link2)
		listar=[]
		listal=[]
		for link,res in m2:
			listal.append(link)#.replace("360","720"))
			#listar.append("[COLOR green][B]HD[/COLOR][/B]")
			listar.append(res)#.replace("360p","720p"))
		if len(listal) <1:
			xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
			sys.exit(int(sys.argv[1]))
		d = xbmcgui.Dialog().select("Selecione a resolução", listar)
		if d!= -1:
			url2 = re.sub(' ', '%20', listal[d] )
			global background
			background=background+";;;"+name+";;;MM"
			if legenda:
				legenda = re.sub(' ', '%20', legenda[0][0] )
				if not "http" in legenda:
					legenda = "http://player.openload.network/" + legenda
				PlayUrl(name,'https' + url2+"|Referer=https://player.openload.network/", iconimage, info, sub=legenda)
			else:
				PlayUrl(name,'https' + url2+"|Referer=https://player.openload.network/", iconimage, info)
		else:
			sys.exit()
# -----------------
def ListSerieMM(): #190
	try:
		link = common.OpenURL("http://www.mmfilmes.tv/series/")
		m = re.compile('id\=\"post\-\d+\".+?\=.([^\"]+)\h*(?s)(.+?)(http[^\"]+)').findall(link)
		jpg = re.compile('src=\"(http.+?www.mmfilmes.tv\/wp-content\/uploads[^\"]+)').findall(link)
		i=0
		m2=[]
		if m:
			for name2,b,url2 in m:
				m2.append([name2,url2,jpg[i]])
				i+=1
			m2 = sorted(m2, key=lambda m2: m2[0])
			for name2,url2,jpg2 in m2:
				name2 = name2.replace("&#8211;","-").replace("&#038;","&").replace("&#8217;","\'").replace("&#8230;","")
				AddDir(name2, url2, 191, jpg2, jpg2, isFolder=True,IsPlayable=False, info='[COLOR][/COLOR]')
	except:
		AddDir( "Server offline" ,"", 0, "", "", isFolder=False)
def ListSMM(x): #191
	link = common.OpenURL(url)
	m = re.compile('boxp\(.([^\']+)').findall(link)
	info2= re.compile('mCSB_container..\s(\h*(?s)(.+?))\<\/div').findall(link)
	info2= info2[0][0].replace("\t","") if info2 else ""
	i=0
	if m:
		if x=="None":
			link2 = common.OpenURL(m[0],headers={'referer': "http://www.mmfilmes.tv/"})
			m2 = re.compile('opb\(.([^\']+).+?.{3}.+?[^\\>]+.([^\<]+)').findall(link2)
			listar=[]
			listal=[]
			for link,res in m2:
				listal.append(link)
				listar.append(res)
			if len(listar)==1:
				d=0
			else:
				d = xbmcgui.Dialog().select("Selecione o server:", listar)
			if d== -1:
				d= 0
			if m2:
				link3 = common.OpenURL(m2[0][0],headers={'referer': "http://www.mmfilmes.tv/"}).replace("\n","").replace("\r","").replace('".Svplayer"',"<end>").replace('\t'," ")
				link3 = re.sub('(\(s \=\= \d+\))', r'<end>\1', link3 )
				m3 = re.compile('s \=\= (\d+)(.+?\<end\>)').findall(link3)
				for temp in m3:
					AddDir("[B][Temporada "+ temp[0] +"][/B]" ,listal[d], 192, iconimage, iconimage, isFolder=True, info=info2, background=i)
					i+=1
def ListEpiMM(x): #192
	link3 = common.OpenURL(url,headers={'referer': "http://www.mmfilmes.tv/"}).replace("\n","").replace("\r","").replace('".Svplayer"',"<end>").replace('\t'," ")
	link3 = re.sub('(\(s \=\= \d+\))', r'<end>\1', link3 )
	m3 = re.compile('s \=\= (\d+)(.+?\<end\>)').findall(link3)
	r=-1
	p=1
	dubleg = re.compile("t \=\= \'([^\']+)(.+?\})").findall( m3[int(x)][1] )
	epi = re.compile("e \=\= (\d+).+?addiframe\(\'([^\']+)").findall( m3[int(x)][1] )
	for e,url2 in epi:
		url2 = "http://player.openload.network" + url2 if not "http" in url2 else url2
		if p == int(e) :
			r+=1
		if len(dubleg[r][1]) < 30:
			r+=1
		name2 = "[COLOR yellow](Dub)[/COLOR]" if "dub" in dubleg[r][0] else "[COLOR blue](Leg)[/COLOR]"
		AddDir("Episódio "+ e + " [COLOR blue]" + name2 ,url2, 194, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info)
#172
def PlaySMM(): #194
	if "drive.google" in url:
		#xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, drive')
		PlayUrl(name, "plugin://plugin.video.gdrive?mode=streamURL&amp;url="+url.encode('utf-8'), iconimage, info)
		sys.exit()
	cdn = re.compile('(\d+)\=(.+?.mp4)|\&l\=(.+)').findall(url)
	if cdn:
		cdn = list(reversed(cdn))
		listar=[]
		listal=[]
		legenda=""
		for res,link,leg in cdn:
			if link <> "":
				listal.append(link)
				listar.append(res)
			if leg:
				legenda = leg
				if not "http" in legenda:
					legenda = "http://player.openload.network/" + legenda
				legenda = re.sub(' ', '%20', legenda )
		d = xbmcgui.Dialog().select("Selecione a resolução", listar)
		if d!= -1:
			url2 = re.sub(' ', '%20', listal[d] )
			PlayUrl(name, url2, iconimage, info, sub=legenda)
	else:
		link2 = common.OpenURL( re.sub('(\/.{1,25}\/).{1,10}\/', r'\1', url) ,headers={'referer': "http://player.openload.network"}).replace('"',"'")
		m2 = re.compile('(h[^\']+).+?label...(\w+)').findall(link2)
		legenda = re.compile('([^\']+\.(vtt|srt|sub|ssa|txt|ass))').findall(link2)
		listar=[]
		listal=[]
		for link,res in m2:
			listal.append(link)
			listar.append(res)
		if len(listal) < 1:
			xbmcgui.Dialog().ok('Play XD', 'Erro!')
			sys.exit(int(sys.argv[1]))
		d = xbmcgui.Dialog().select("Selecione a resolução", listar)
		if d!= -1:
			url2 = re.sub(' ', '%20', listal[d] )
			if legenda:
				legenda = re.sub(' ', '%20', legenda[0][0] )
				if not "http" in legenda:
					legenda = "http://player.openload.network/" + legenda
				PlayUrl(name, url2+"|Referer=https://player.openload.network/", iconimage, info, sub=legenda)
			else:
				PlayUrl(name, url2+"|Referer=https://player.openload.network/", iconimage, info)
# ----------------- Fim MM filmes
def TVCB2(x): #104
	AddDir("[COLOR yellow]Atualizar Lista[/COLOR]" , "", 50, isFolder=False)
	t = requests.get("https://cutt.ly/canalTop", verify=False)
	jq_ = json.loads(t.text)
	jq = sorted(jq_, key=lambda jq_: jq_['name'])
	for jq1 in jq:
		if "FILMES" in jq1['category'] or "LEGENDADO EN" in jq1['category'] or "ENTRETENIMENTO" in jq1['category'] or "DOCUMENTARIOS" in jq1['category'] or "NOTICIAS" in jq1['category'] or "TV ABERTA" in jq1['category'] or "INFANTIS" in jq1['category'] or "MUSICA" in jq1['category'] or "PAY PER VIEW" in jq1['category'] :
			try:
				AddDir( "[COLOR white]" + jq1['name'] + "[/COLOR]", jq1['id'] , 1212, jq1['logo'], jq1['logo'], isFolder=False, IsPlayable=True, info="")
			except:
				pass
def PlayTVB3(): #1212
	t = requests.get("https://cutt.ly/canalTop", verify=False)
	jq_ = json.loads(t.text.replace("\\","//"))
	for jq1 in jq_:
		if jq1['id'] == url:
			PlayUrl(jq1['name'], jq1['link'],jq1['logo'],"")
def TVCB3(): #107
	link = common.OpenURL("http://nordestv.gabserv.com.br/Sertao/Brasil/LISTA-IPTV/brlive002").replace("\n","").replace('\r','')
	m = re.compile('1,(.+?)plugin:\/\/(.+?)#').findall(link)
	for name2, url2 in m:
		url2 = url2.replace('BR-LIVE-TODO MUNDO USA',"[COLOR green][B]HD[/B][/COLOR]").replace('Juntos Vamos Derrotar o Virus',"[COLOR green][B]HD[/B][/COLOR]").replace('BR-LIVE-SEMPRE 0800',"[COLOR green][B]HD[/B][/COLOR]")
		AddDir(name2,"plugin://"+url2.replace(";","&"), 212, isFolder=False, IsPlayable=True, info='[COLOR][/COLOR]')   
def TVCB4(): #108
	t = requests.get("https://cutt.ly/canalR", verify=False)
	jq_ = json.loads(t.text.replace("\\","//").replace("http://files.rednetcontent.com/chlogo2/Brasil/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/Portuguese/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/english/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/french/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/arabic/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/dutch/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/russian/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("http://files.rednetcontent.com/chlogo2/German/","https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/imagens/").replace("1280px-SporTV_2017_logo.png","SporTV_2_logo_20167.png").replace("SporTV_2_logo_2016.png","Sportv2.png").replace("TVBAH//u0130A.png","bahia.png"))
	jq = sorted(jq_, key=lambda jq_: jq_['name'])
	for jq1 in jq:
		if "Action 1" in jq1['name']or "Action 2" in jq1['name'] or "Action 3" in jq1['name'] or "Action 4" in jq1['name'] or "Action 5" in jq1['name'] or "Action 6" in jq1['name'] or "Action 7" in jq1['name'] or "Action 8" in jq1['name'] or "Action 9" in jq1['name'] or "Action 10" in jq1['name'] or "Adventure" in jq1['name'] or "Crime" in jq1['name'] or "Documentary" in jq1['name'] or "Drama" in jq1['name'] or "Horror" in jq1['name'] or "Sci-Fi" in jq1['name'] or "Comedy 1" in jq1['name'] or "Comedy 2" in jq1['name'] or "Comedy 3" in jq1['name'] or "Comedy 4" in jq1['name'] or "Comedy 5" in jq1['name'] or "Comedy 6" in jq1['name'] or "Comedy 7" in jq1['name'] or "Comedy 8" in jq1['name'] or "Comedy 9" in jq1['name'] or "Comedy 10" in jq1['name'] or "Kids 1" in jq1['name'] or "Kids 2" in jq1['name'] or "Kids 3" in jq1['name'] or "Kids 4" in jq1['name'] or "Kids 5" in jq1['name'] or "Kids 6" in jq1['name'] or "Kids 7" in jq1['name'] or "Kids 8" in jq1['name'] or "Kids 9" in jq1['name'] or "Kids 10" in jq1['name']: False
		else:
			if jq1['language']== "Brasil" or jq1['language'] == "Brazilian" or jq1['name'] == "MTV Live HD":
				try:
					jq1['name'] = jq1['name'].replace("HD","[COLOR lime]HD[/COLOR]").replace("HEVC", "[COLOR lime]+[/COLOR]").replace("A E", "A&E")
					AddDir( "[B]" + jq1['name'] + "[/B]", jq1['id'] , 109, jq1['logo'], jq1['logo'], isFolder=False, IsPlayable=True, info="")
				except:
					pass
def TVCB4PLAY(): #109
	t = requests.get("https://cutt.ly/canalR", verify=False)
	jq_ = json.loads(t.text.replace("\\","//"))
	for jq1 in jq_:
		if jq1['id'] == url:
			EPG = common.OpenURL('https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/EPG2')
			contents = re.compile(jq1['name']+' = "(.+?)"').findall(EPG)
			try:
				url2 = common.OpenURL(contents[0]).replace('\n','').replace('\t','').replace('<h2>','"/>').replace('/><img','').replace('synopsis">','title">').replace('.</p>','</span')
				url4 = re.compile('<li class=("ongoing">.+)').findall(url2)
				url4x = re.compile('restantes(.+)').findall(url2)
				title = re.compile('"ongoing">.+?class="time">.+?<.+?\/>(.+?)<\/h2.+?title">.+?<.+?progress-container">.+?<div').findall(url4[0])
				program = re.compile('"ongoing">.+?class="(time">.+?)<.+?\/>(.+?<\/h2).+?title">(.+?)<.+?progress-(container">.+?<div).+?(:.+?)"').findall(url4[0])
				program2 = re.compile('lass="(time">.+?)<.+?\/>(.+?<\/h2).+?title">(.+?<\/span)').findall(url4x[0])
				ir1 = str(program).replace('<div','').replace("')]","").replace("('","").replace('"), ',"").replace("'), ","").replace("', '"," - ").replace("[","").replace("', ","").replace('"',' - ').replace('time - >','[COLOR red]AO VIVO:[/COLOR] ').replace("</h2"," | Gênero/EP").replace(" <span class='rating'>"," IMDB: ").replace("<span class='rating good'>"," IMDB: ").replace("container - >","Tempo:").replace('</span>','').replace(' - Tempo:','\n[COLOR yellow]TEMPO:[/COLOR] ').replace('- :',' : ').replace('%',"% concluído\n\n").replace("'Tempo:",'\n[COLOR yellow]TEMPO:[/COLOR] ')
				ir2 = str(program2).replace('</span','\n\n').replace("')]","").replace("('","").replace('"), ',"").replace("'), ","").replace("', '"," - ").replace("[","").replace("', ","").replace('"',' - ').replace('time - >','Horário: ').replace("</h2"," | Gênero/EP").replace(" <span class='rating'>"," IMDB: ").replace("<span class='rating good'>"," IMDB: ").replace('><p class= - title - >','').replace(']','').replace('- )','').replace("-,",'')
				title = " - "+title[0]
				url5 = "[B]"+'\n\n\n'+ir1+"[/B]" + ir2
				url6 = url5.decode('string_escape')
				PlayUrl(name + title, jq1['link']+"&t=0&s=12&p=1&c=BR&r=65|Referer=https://android.rediptvmobile.com/",iconimage, url6)
			except IndexError as url2:
				pass
				PlayUrl(name, jq1['link']+"|Referer=https://android.rediptvmobile.com/",iconimage,"") 

def PlayTVCB2(): #212
	PlayUrl(name, url, iconimage, info, "", metah)       
def RadioTV(x): #106
	link = common.OpenURL("https://raw.githubusercontent.com/GladistonXD/Filmes-2017/master/Radios-tv").replace("\n","").replace('\r','')
	m = re.compile('<title>(.+?)<\/title><link>(.+?)<\/link><thumbnail>(.+?)<\/thumbnail>').findall(link)
	for name2, url2, img2 in m:
		if url2!="Close":
		 #url2 = url2.replace('BR-LIVE-TODO MUNDO USA',"[COLOR green][B]HD[/B][/COLOR]")
		 AddDir(name2, url2, 212,img2, img2, isFolder=False, IsPlayable=True, info='[COLOR][/COLOR]')
def TVCB5(): #111
	link = common.OpenURL("https://canaismax.com/assistir-redetv-ao-vivo-gratis-24-horas-online")
	m3 = re.compile('<a href="([^\"]+)".\s.+?data-src="([^\"]+)".+?alt="Assistir ([^\"]+) ao').findall(link)
	if m3:
		for url2,img2,name2 in m3:
			name2 = name2.replace('HD',"[COLOR lime]HD[/COLOR]")
			if url2!="Close":
				AddDir("[B]"+name2+"[/B]",url2, 112, img2, img2, isFolder=False, IsPlayable=True, info='[COLOR][/COLOR]')
def TVCB5PLAY(): #112
	try:
		link2 = requests.get(url)
		url2 = re.compile('data-link="(https:\/\/canaismax.com\/canal[^\"]+)"').findall(link2.text)
		url2 = url2[0]
		m = requests.get(url2)
		url3 = re.compile('<a href="([^\"]+)"').findall(m.text)
		url3 = url3[0]
		m2 = requests.get(url3)
		url4 = re.compile('source: "([^\"]+)"').findall(m2.text)
		for url2 in url4:
			if url2!="Close":
			 PlayUrl(name, url2+"|Referer=https://canaismax.com/&User-Agent=Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30", iconimage, info)
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Canal indisponível no momento.')
		sys.exit()         
# ----------------- Inicio Go Filmes
def GenerosGO(): #219
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaGO1)
	if d != -1:
		global Cat
		Addon.setSetting("CatGO", str(d) )
		Cat = d
		Addon.setSetting("cPageGOf", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosFl(): #230
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaFl1)
	if d != -1:
		global Cat
		Addon.setSetting("CatFl", str(d) )
		Cat = d
		Addon.setSetting("cPageFlf", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosQUE1(): #231
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaQUE11)
	if d != -1:
		global Cat
		Addon.setSetting("CatQ1", str(d) )
		Cat = d
		Addon.setSetting("cPageQlf", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosBIZ(): #232
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaBIZ11)
	if d != -1:
		global Cat
		Addon.setSetting("CatBB", str(d) )
		Cat = d
		Addon.setSetting("cPageBIZ", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosMEG(): #233
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaMEG11)
	if d != -1:
		global Cat
		Addon.setSetting("CatMG", str(d) )
		Cat = d
		Addon.setSetting("cPageMEG", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosFHD(): #234
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaFHD11)
	if d != -1:
		global Cat
		Addon.setSetting("CatHD", str(d) )
		Cat = d
		Addon.setSetting("cPageFHD", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")
def GenerosVZ(): #235
	d = xbmcgui.Dialog().select("Escolha o Genero", ClistaVZ11)
	if d != -1:
		global Cat
		Addon.setSetting("CatVZ", str(d) )
		Cat = d
		Addon.setSetting("cPageVZ", "0" )
		xbmc.executebuiltin("XBMC.Container.Refresh()")          
def ListGO(): #210 Topflix Dublado --------------------------------------------
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaFl1[int(CatFl)] +"[/COLOR]", "url" ,230 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageFlf) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageFlf) ) +"][/B][/COLOR]", cPageFlf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageFlf")
		l= int(cPageFlf)*4
		for x in range(0, 4):
			l +=1
			link = common.OpenURL("https://topflix.tv/lancamentos/"+ str(l))
			match = re.compile("'(.{5,30}[^\']jpg).{4,41}<a href=\'([^\']+).'>([^\']+)<\/span>").findall(link.replace('\n','').replace('\r',''))
			if ClistaFl0[int(CatFl)] != "0":
				link = common.OpenURL("https://topflix.tv/"+ClistaFl0[int(CatFl)]+"/"+ str(l))
				match = re.compile("'(.{5,30}[^\']jpg).{4,41}<a href=\'([^\']+).{4,300}'>([^\']+)<\/a").findall(link.replace('\n','').replace('\r',''))
			if match:
				for img2,url2,name2, in match:
					img2 = img2.replace('170255',"330490")
					url2 = re.sub('^\.', RC4, url2 )
					if name2!="Close":
						name2 = name2.replace("</font>","").replace("<span>","- ").replace("</span>","")
					if "series" in url2: False
					else:                        
						AddDir(name2 ,RC4 + url2, 211, RC4 +img2, RC4 + img2, info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
					p += 1
		if p >= 96:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageFlf) + 2) +"][/B][/COLOR]", cPageFlf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageFlf")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def ListGOL(): #310 Lançamentos ---------------------------------------
	try:
		p= 1
		if int(cPageFlf) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageFlf) ) +"][/B][/COLOR]", cPageFlf , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageFlf")
		l= int(cPageFlf)*7
		for x in range(0,7):
			l +=1
			link = common.OpenURL("https://topflix.tv/lancamentos/"+ str(l))
			match = re.compile("'(.{5,30}[^\']jpg).{4,41}<a href=\'([^\']+).'>([^\']+)<\/span>").findall(link.replace('\n','').replace('\r',''))
			if match:
				for img2,url2,name2, in match:
					img2 = img2.replace('170255',"330490")
					url2 = re.sub('^\.', RC4, url2 )
					if name2!="Close":
						name2 = name2.replace("</font>","").replace("<span>","- ").replace("</span>","")
					if "series" in url2: False
					else:                        
						AddDir(name2 ,RC4 + url2, 211, RC4 +img2, RC4 + img2, info='[COLOR][/COLOR]', isFolder=True, IsPlayable=True)
					p += 1
		if p >= 72:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageFlf) + 2) +"][/B][/COLOR]", cPageFlf , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageFlf")
	except:
		AddDir("Server error, tente novamente em alguns minutos" , "", 0, "", "", 0)
def ListTop(): #211
	try:	
		link = common.OpenURL(url).replace('\n','').replace('\r','').replace(' ','%20')
		m = re.compile("globalUri='([^\']+)'").findall(link)
		m2 = re.compile('idJs%20=%20"([^\"]+";var%20_ano)').findall(link)
		m3 = re.compile('ChangeSource."([^\"]+mp4",%20")').findall(link)
		m4 = re.compile('data%20=%20"([^\"]+";var%20lnc)%20=').findall(link)
		m5 = re.compile('ctm%20=%20"([^\"]+";_data)=').findall(link)
		m1 = re.compile("globalUri='([^\']+)'").findall(link)
		m12 = re.compile('idJs%20=%20"([^\"]+";var%20_ano)').findall(link)
		m13 = re.compile('ChangeSource."([^\"]+mp4",%20"5)').findall(link)
		m14 = re.compile('data%20=%20"([^\"]+";var%20lnc)%20=').findall(link)
		m15 = re.compile('ctm%20=%20"([^\"]+";_data)=').findall(link)
		lista = re.compile("(.+)").findall(m[0]+m2[0]+m3[0]+m4[0]+m5[0])
		lista2 = re.compile("(.+)").findall(m1[0]+m12[0]+m13[0]+m14[0]+m15[0])
		info2 = re.compile('12"><p>(.+?)<\/p>').findall(link)
		info2= info2[0].replace("%20"," ")
		lista= lista[0].replace('.php',"/").replace('";var%20_ano',"&url=").replace('",%20"',"&mediaType=filme&mediaName=").replace('";var%20lnc',"&idfy=3&lnc=s&vid=").replace('";_data',"&out=null&webv=nao&cdn=cdn11#Dublado#").replace('\n','')
		lista2= lista2[0].replace('.php',"/").replace('";var%20_ano',"&url=").replace('",%20"5',"&mediaType=filme&mediaName=").replace('";var%20lnc',"&idfy=5&lnc=s&vid=").replace('";_data',"&out=null&webv=nao&cdn=cdn11#Legendado#").replace('\n','')
		lista3 = lista + lista2
		arquivo = open(cachefolder +"lista", "w+")
		arquivo.write(lista3)
		arquivo.close()
		AddDir(name + "[COLOR blue] - Dublado e Legendado[/COLOR]", "", 213, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
	except IndexError as lista2:
			pass
	try:     
            info2 = re.compile('12"><p>(.+?)<\/p>').findall(link)
            info2= info2[0].replace("%20"," ")
            for url2 in lista:
				name2 = re.compile('(\w|-|leg+.+)p4').findall(url2)
				name2= name2[0].replace("m", "[COLOR blue] - Dublado[/COLOR]")
				url2= url2.replace('.php',"/").replace('";var%20_ano',"&url=").replace('",%20"',"&mediaType=filme&mediaName=").replace('";var%20lnc',"&idfy=3&lnc=s&vid=").replace('";_data',"&out=null&webv=nao&cdn=cdn11#Dublado#").replace('\n','')
				arquivo = open(cachefolder +"lista", "w+")
				arquivo.write(url2)
				arquivo.close()
				AddDir(name + name2, "", 213, iconimage, iconimage, isFolder=False, IsPlayable=True, info=info2, background=url)
	except:
			pass     
def ListPlay(): #213 play =====================================================================
    try:
			arquivo = open(cachefolder + 'lista', 'r')
			url3 = arquivo.read()
			m2 = re.compile('(https.+?)#(.+?)#').findall(url3)
			listar=[]
			listal=[]
			for link, res in m2:
				listal.append(link)
				listar.append(res.replace("Dublado","[COLOR blue][B]Dublado[/B][/COLOR]").replace("Legendado","[COLOR red][B]Legendado[/B][/COLOR]"))
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione o idioma", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				link2 = common.OpenURL(url2).replace("\n","")
				url2x = re.compile("var mp4Id = '(https:.+?.mp4)").findall(link2)
				url2x = url2x[0]
				legenda = re.compile('(filmes\/subtitles.+?vtt)').findall(link2)
				global background
				background=background+";;;"+name+";;;MM"
				if legenda:
					legenda = "https://topflix.tv/" + legenda[0]
					if not "http" in legenda:
						legenda = "https://sub.streamservice.online/subdata/" + legenda
					PlayUrl(name, url2x+"|Referer=https://topflix.tv/&Connection=Keep-Alive&Accept-Language=en&User-Agent=Mozilla%2F5.0+%28compatible%3B+MSIE+10.6%3B+Windows+NT+6.1%3B+Trident%2F6.0%29", iconimage, info, sub=legenda)
				else:
					PlayUrl(name, url2x+"|Referer=https://topflix.tv/&Connection=Keep-Alive&Accept-Language=en&User-Agent=Mozilla%2F5.0+%28compatible%3B+MSIE+10.6%3B+Windows+NT+6.1%3B+Trident%2F6.0%29", iconimage, info)
			else:
				sys.exit()
    except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Video não encontrado')
		sys.exit()           
# ----------------- Inicio Superflix
def ListMovieSF(): #411:
	AddDir("[COLOR yellow][B][Genero dos Filmes]:[/B] " + ClistaMEG11[int(CatMG)] +"[/COLOR]", "url" ,233 ,"https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", "https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300", isFolder=False, info='[COLOR][/COLOR]')
	try:
		p= 1
		if int(cPageMEG) > 0:
			AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(cPageMEG) ) +"][/B][/COLOR]", cPageMEG , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageMEG")
		l= int(cPageMEG)*3
		for x in range(0, 3):
			l +=1
			movie = "https://www.superflix.net/categoria/"+ClistaMEG10[int(CatMG)]+"/page/"+str(l)+"/"
			link = common.OpenURL(movie.replace("page/1/",""))
			match = re.compile('"> <art.+?title">([^\"].+?)<.+?src="([^\"].+?)".+?year">([^\"].+?)<.+?sm.+? (.+?)<.+?href="([^\"].+?)"').findall(link.replace('\n','').replace('\r',''))
			if match:
				for name2, img2, year2, tvmovie, url2 in match:
					img2 = img2.replace("w185", 'original').replace("https:", '').replace("w220_and_h330_face", 'original').replace("-185x278", "")
					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
					if "Série" in tvmovie: False
					else:
						AddDir(name2+" ("+year2+")", url2, 405, "http:"+img2, "http:"+img2,isFolder=True,IsPlayable=True, info='[COLOR][/COLOR]')
					p += 1
		if p >= 33:
			AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(cPageMEG) + 2) +"][/B][/COLOR]", cPageMEG , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageMEG")
	except:
		pass
# -----------------
def PlaySSF(): #405
	i=0
	link = common.OpenURL(url).replace("</span><span>","").replace("                                ","").replace("SuperFlix-Nacional","[COLOR springgreen][B]Dublado[/B][/COLOR]").replace("- Full HD","").replace("- HD 720p","").replace("SuperFlix-Dublado","[COLOR springgreen][B]Dublado[/B][/COLOR]").replace("SuperFlix-Legendado","[COLOR red][B]Legendado[/B][/COLOR]").replace("- HD","").replace("- SD","")
	desc = re.compile('(<p>Filme.+?<\/p>|>Assistir.+?<\/p|"><p>.+?<\/p>)').findall(link)
	desc = desc[0].replace("Assistir","").replace(">","").replace("</p","").replace('"',"").replace("<p","").replace("Filme ","").replace("Online","").replace("Dublado","").replace("Legendado","").replace("  "," ").replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”')
	m = re.compile("href='\/\/.+?=(.+?)'").findall(link)
	m2 = re.compile('class="server">(.+?)<').findall(link)
	if m:
		for url2 in m:
			hexd = codecs.decode(url2, "hex_codec").decode('utf-8')
			if "SuperFliX" in m2[i] or "SuperFlix FB" in m2[i] or "OK.RU" in m2[i] or "OpenLoad" in m2[i] or "Mega" in m2[i] or "Ok" in m2[i] or "The Vid" in m2[i] or "Vid.To" in m2[i] or "Alta" in m2[i]: False
			else:
				AddDir(m2[i].replace("</span>",""), hexd.replace("#038;",""), 407, iconimage, iconimage, isFolder=False, IsPlayable=True, info = desc)
			i+=1	
                i+=1
def Play2SFS(): #407
        try:         
                url3Play = common.OpenURL(url)
                url4Play = re.compile('(https.+?")').findall(url3Play)
                url4Play= url4Play[0]
        except IndexError as url4Play:
			sys.exit()
        
        try:

            if 'http' in url4Play:  ###### Ja saquei a do ‰PNG fica suave.
                    urlxx = re.compile('x.html.(.+?)"').findall(url4Play)
                    urlxx = urlxx[0]
                    legenda = re.compile('sub=(.+?srt)').findall(url4Play)
                    url1 = re.compile('(id=.+?\w+)').findall(urlxx)
                    inver = re.compile('id=(\w+)').findall(urlxx)
                    url1 = url1[0].replace("id=", "https://lbsuper.sfplayer.net/playlist/") + "/1590191456752"
                    url2 = requests.get(url1)
                    url3x = re.compile('x([^\"]\w+)\s(\/.+?m3u8)').findall(url2.text)
                    url3x.reverse()
                    listar=[]
                    listal=[]
                    for res, link in url3x:
                    	listal.append(link)
                    	listar.append(res.replace("1080","[COLOR springgreen][B]HD[/B][/COLOR]").replace("360","[COLOR crimson][B]SD[/B][/COLOR]").replace("720","[COLOR springgreen][B]HD[/B][/COLOR]").replace("480","[COLOR crimson][B]SD[/B][/COLOR]"))
                    if len(listal) <1:
                    	xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
                    	sys.exit(int(sys.argv[1]))
                    d = xbmcgui.Dialog().select("Selecione a resolução", listar)
                    if d!= -1:
                    	url2x = re.sub(' ', '%20', listal[d] )
                    	url3 = url2x.replace("/hls/", "https://lbsuper.sfplayer.net/hls/").replace(".m3u8", "")
                    	url4 = requests.get(url3)
                    	url4 = url4.text
                    	inverter = inver[0]
                    	invertida = ''.join(palavra[::-1] for palavra in inverter.split())
                    	url7 = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=" + invertida + "&url=https"
                    	server = re.compile('-0.html.msKey=m(\w+)').findall(url4)
                    	#url8 = url4.replace('://', '%3A%2F%2F').replace('/', '%2F').replace('.png', '').replace('?', '%3F').replace('=','%3D').replace('https', url7).replace('lbsuper.sfplayer.net','s'+server[0]+'.sfslave.com')
                        url8 = url4.replace('://', '%3A%2F%2F').replace('/', '%2F').replace('.png', '').replace('?', '%3F').replace('=','%3D').replace('https', url7).replace('lbsuper.sfplayer.net','s1.sfslave.com')
                    	arquivo = open(cachefolder + "movies.m3u8", "w+")
                    	arquivo.write(url8)
                    	arquivo.close()
                    	x1 = randrange(300)
                    	x = str(x1)
                    	session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
                    	file = open(cachefolder + "movies.m3u8",'rb')
                    	session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
                    	file.close()                      
                    	session.quit()
                    	if legenda:
                    	    for legenda2 in legenda:
                    	        legenda3 = urllib.quote(legenda2)
                    	        legenda4 = "https://sub.sfplayer.net/subdata/" + legenda3
                    	        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info, sub=legenda4)
                    	else:
                    	    PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info)
                    else:
                        sys.exit()
                        
            if 'xxxxxxxx' in url4Play:
                    urlxx = re.compile('tid=(.+?)&"').findall(url4Play)
                    urlxx = urlxx[0]
                    inverter1 = urlxx
                    invertida1 = ''.join(palavra[::-1] for palavra in inverter1.split())
                    hexd = codecs.decode(invertida1, "hex_codec").decode('utf-8')
                    legenda = re.compile('sub=(.+?srt)').findall(hexd)
                    url1 = re.compile('(id=.+?\w+)').findall(hexd)
                    url1= url1[0].replace("id=","https://lbsuper.sfplayer.net/playlist/") + "/1590191456752"
                    url2 = common.OpenURL(url1)
                    url3 = re.compile('EXTM3U\s.+\s.+\s.+\s(.+?m3u8)').findall(url2)
                    url3= url3[0].replace("/hls/","https://lbsuper.sfplayer.net/hls/").replace(".m3u8","")
                    url4 = common.OpenURL(url3)
                    url4x = common.OpenURL(url3)
                    url6 = re.compile('playlist.(\w+)').findall(url1)
                    url6 = url6[0]
                    inverter = url6
                    invertida = ''.join(palavra[::-1] for palavra in inverter.split())
                    url7 = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container="+invertida+"&url=https"
                    url8 =url4.replace('://','%3A%2F%2F').replace('/','%2F').replace('.png','').replace('?','%3F').replace('=','%3D').replace('https',url7)
                    arquivo = open(cachefolder + "movies.m3u8", "w+")
                    arquivo.write(url8)
                    arquivo.close()
                    x1 = randrange(300)
                    x = str(x1)
                    session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
                    file = open(cachefolder + "movies.m3u8",'rb')
                    session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
                    file.close()                      
                    session.quit()
                    if legenda:
                        legenda = legenda[0]
                        #legenda2 = urllib.quote(legenda.encode('utf8'))
                        #if not "http" in legenda:
                        #   legenda3 = "https://sub.sfplayer.net/subdata/"
                        #    legenda4 = legenda3 + legenda2
                        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info, sub=legenda)
                    else:
                        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info)

            elif 'xxxxxxxxx' in url4Play:
                    legenda3 = re.compile('vl(.+?)"').findall(url4Play)
                    url12 = re.compile('net\/(.+?\w+.\w+)').findall(url4Play)
                    url12= url12[0].replace("embedplay","https://fb.sfplayer.net/getLinkStreamMd5")
                    url2x2 = common.OpenURL(url12)
                    url3x2 = re.compile('(https.+?)"').findall(url2x2)
                    url3x2= url3x2[0]
                    if legenda3:
                        legenda3 = legenda3[0]
                        if not "http" in legenda3:
                            legenda3= legenda3.replace("sub=","https://sub.sfplayer.net/subdata/").replace("à","%C3%A0").replace("é","%C3%A9").replace("ó","%C3%B3").replace("ô","%C3%B4").replace("ã","%C3%A3").replace("ç","%C3%A7").replace("í","%C3%AD")
                        PlayUrl(name, url3x2, iconimage, info, sub = legenda3)
                    else:
                        PlayUrl(name, url3x2, iconimage, info)
        except (IndexError, ValueError):
			xbmcgui.Dialog().ok('Play XD', 'Filme não encontrado')
			sys.exit()
# ----------------- Fim Superflix
# ----------------- Inicio Superflix
def ListSerieSF(): #401:
	pagina = "0" if not cPageserSF else cPageserSF
	if int(pagina) > 0:
		AddDir("[COLOR blue][B]<< Pagina Anterior ["+ str( int(pagina) ) +"][/B][/COLOR]", pagina , 120 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Previous-icon.png", isFolder=False, background="cPageserSF")
	y= int(pagina)*4
	for x in range(0, 4):
		try:
			y +=1
			l = common.OpenURL("http://www.superflix.net/assistir-series-online/page/"+str(y)+"/")
			link = re.compile('<section class="section movies">(.+?)class="page-link current').findall(l)
			match = re.compile('<h2 class="entry-title">([^\"].+?)<.+?src="([^\"].+?)".+?class.+?class="\w+">([^\"].+?)<.+?Série.{1,52}h.+?"(.+?)"').findall(link[0])
			if match:
				for name2, img2, year2, url2 in match:
					img2 = img2.replace("w185", 'original').replace("https:", '').replace("w220_and_h330_face", 'original').replace("-185x278", "")
					name2 = name2.replace('&#8217;','’').replace('&#8211;','–').replace('&#038;','&').replace('&#8216;','‘').replace('&#8220;','“').replace('&#8221;','”').replace('&#8230;','…')
					AddDir(name2+" ("+year2+")", url2, 402, "http:"+img2, "http:"+img2,isFolder=True,IsPlayable=False)
		except:
			pass
	AddDir("[COLOR blue][B]Proxima Pagina >> ["+ str( int(pagina) + 2) +"][/B][/COLOR]", pagina , 110 ,"http://icons.iconarchive.com/icons/iconsmind/outline/256/Next-2-2-icon.png", isFolder=False, background="cPageserSF")
def ListTempSF(): #402
	l = common.OpenURL(url).replace("\n","").replace("\r","")
	m = re.compile('drp choose-season">.+?href="(.+?)".+?ne">(.+?)<').findall(l)
	for cont2, temp2 in m:
		AddDir("Temporada "+ temp2, cont2, 403, iconimage, iconimage, isFolder=True)
def ListEpiSF(): #403
	l = common.OpenURL(url).replace("\n","").replace("\r","")
	epis = re.compile('"num-epi">(.+?)<.+?href="(.+?)"').findall(l)
	for E,url2 in epis:
		AddDir("Episódio "+E,url2, 406, iconimage, iconimage, isFolder=False, IsPlayable=True)
def PlaySSFS(): #406
	try:
		i=0
		link = common.OpenURL(url).replace("</span><span>","").replace("SuperFlix - Nacional","[COLOR springgreen][B]Dublado[/B][/COLOR]").replace("- Full HD","").replace("- HD 720p","").replace("SuperFlix - Dublado","[COLOR springgreen][B]Dublado[/B][/COLOR]").replace("SuperFlix - Legendado","[COLOR red][B]Legendado[/B][/COLOR]").replace("- HD","").replace("- SD","")
		m = re.compile("href='\/\/.+?=(.+?)'").findall(link)
		m2 = re.compile('class="server">(.+?)<').findall(link)
		if m:
			legenda = re.compile('subdata..([^\"]+)').findall(url)
			listar=[]
			listal=[]
			for url3 in m:
				if "SuperFliX" in m2[i] or "SuperFlix FB" in m2[i] or "OK.RU" in m2[i] or "OpenLoad" in m2[i] or "Mega" in m2[i] or "Ok" in m2[i] or "The Vid" in m2[i] or "Vid.To" in m2[i] or "Alta" in m2[i]: False
				else:
					listal.append(url3)
					listar.append(m2[i].replace("</span>",""))
				i+=1
			if len(listal) <1:
				xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado')
				sys.exit(int(sys.argv[1]))
			d = xbmcgui.Dialog().select("Selecione a resolução", listar)
			if d!= -1:
				url2 = re.sub(' ', '%20', listal[d] )
				hexd = codecs.decode(url2, "hex_codec").decode('utf-8')
                url3Play = common.OpenURL(hexd.replace("#038;",""))
                url4Play = re.compile('(https.+?")').findall(url3Play)
                url4Play= url4Play[0]
                
                if 'http' in url4Play:
                    urlxx = re.compile('x.html.(.+?)"').findall(url4Play)
                    urlxx = urlxx[0]
                    legenda = re.compile('sub=(.+?srt)').findall(url4Play)
                    url1 = re.compile('(id=.+?\w+)').findall(urlxx)
                    inver = re.compile('id=(\w+)').findall(urlxx)
                    url1 = url1[0].replace("id=", "https://lbsuper.sfplayer.net/playlist/") + "/1590191456752"
                    url2 = requests.get(url1)
                    url3x = re.compile('x([^\"]\w+)\s(\/.+?m3u8)').findall(url2.text)
                    url3x.reverse()
                    listar=[]
                    listal=[]
                    for res, link in url3x:
                    	listal.append(link)
                    	listar.append(res.replace("1080","[COLOR springgreen][B]HD[/B][/COLOR]").replace("360","[COLOR crimson][B]SD[/B][/COLOR]").replace("720","[COLOR springgreen][B]HD[/B][/COLOR]").replace("480","[COLOR crimson][B]SD[/B][/COLOR]"))
                    if len(listal) <1:
                    	xbmcgui.Dialog().ok('Play XD', 'Erro, video não encontrado, tente outro servidor')
                    	sys.exit(int(sys.argv[1]))
                    d = xbmcgui.Dialog().select("Selecione a resolução", listar)
                    if d!= -1:
                    	url2x = re.sub(' ', '%20', listal[d] )
                    	url3 = url2x.replace("/hls/", "https://lbsuper.sfplayer.net/hls/").replace(".m3u8", "")
                    	url4 = requests.get(url3)
                    	url4 = url4.text
                    	inverter = inver[0]
                    	invertida = ''.join(palavra[::-1] for palavra in inverter.split())
                    	url7 = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=" + invertida + "&url=https"
                    	server = re.compile('-0.html.msKey=m(\w+)').findall(url4)
                    	#url8 = url4.replace('://', '%3A%2F%2F').replace('/', '%2F').replace('.png', '').replace('?', '%3F').replace('=','%3D').replace('https', url7).replace('lbsuper.sfplayer.net','s'+server[0]+'.sfslave.com')
                        url8 = url4.replace('://', '%3A%2F%2F').replace('/', '%2F').replace('.png', '').replace('?', '%3F').replace('=','%3D').replace('https', url7).replace('lbsuper.sfplayer.net','s1.sfslave.com')
                    	arquivo = open(cachefolder + "movies.m3u8", "w+")
                    	arquivo.write(url8)
                    	arquivo.close()
                    	x1 = randrange(300)
                    	x = str(x1)
                    	session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
                    	file = open(cachefolder + "movies.m3u8",'rb')
                    	session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
                    	file.close()                      
                    	session.quit()
                    	if legenda:
                    	    for legenda2 in legenda:
                    	        legenda3 = urllib.quote(legenda2)
                    	        legenda4 = "https://sub.sfplayer.net/subdata/" + legenda3
                    	        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info, sub=legenda4)
                    	else:
                    	    PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info)
                    else:
                        sys.exit()
                if 'www.superflix.net' in url4Play:
                    urlxx = re.compile('html.(.+?)"').findall(url4Play)
                    urlxx = urlxx[0]
                    inverter1 = urlxx
                    invertida1 = ''.join(palavra[::-1] for palavra in inverter1.split())
                    hexd = codecs.decode(invertida1, "hex_codec").decode('utf-8')
                    legenda = re.compile('sub=(.+?srt)').findall(hexd)
                    url1 = re.compile('(id=.+?\w+)').findall(hexd)
                    url1= url1[0].replace("id=","https://lbsuper.sfplayer.net/playlist/") + "/1590191456752"
                    url2 = common.OpenURL(url1)
                    url3 = re.compile('EXTM3U\s.+\s.+\s.+\s(.+?m3u8)').findall(url2)
                    url3= url3[0].replace("/hls/","https://lbsuper.sfplayer.net/hls/").replace(".m3u8","")
                    url4 = common.OpenURL(url3)
                    url6 = re.compile('playlist.(\w+)').findall(url1)
                    url6 = url6[0]
                    inverter = url6
                    invertida = ''.join(palavra[::-1] for palavra in inverter.split())
                    url7 = "https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container="+invertida+"&url=https"
                    url8 =url4.replace('://','%3A%2F%2F').replace('/','%2F').replace('.png','').replace('?','%3F').replace('=','%3D').replace('https',url7)
                    arquivo = open(cachefolder + "movies.m3u8", "w+")
                    arquivo.write(url8)
                    arquivo.close()
                    x1 = randrange(300)
                    x = str(x1)
                    session = ftplib.FTP('files.000webhost.com','unlikely-terms','gladiston')
                    file = open(cachefolder + "movies.m3u8",'rb')
                    session.storbinary('STOR /public_html/Cacheflix/movies'+x+'.m3u8', file)
                    file.close()                      
                    session.quit()
                    if legenda:
                        legenda = legenda[0]
                        legenda2 = urllib.quote(legenda.encode('utf8'))
                        if not "http" in legenda:
                            legenda3 = "https://sub.sfplayer.net/subdata/"
                            legenda4 = legenda3 + legenda2
                        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info, sub=legenda4)
                    else:
                        PlayUrl(name, "https://unlikely-terms.000webhostapp.com/Cacheflix/movies"+x+".m3u8|Referer=https://s5.sfslave.com/", iconimage, info)

                elif 'xxxxxxxxx' in url4Play:
                    legenda3 = re.compile('vl(.+?)"').findall(url4Play)
                    url12 = re.compile('net\/(.+?\w+.\w+)').findall(url4Play)
                    url12= url12[0].replace("embedplay","https://fb.sfplayer.net/getLinkStreamMd5")
                    url2x2 = common.OpenURL(url12)
                    url3x2 = re.compile('(https.+?)"').findall(url2x2)
                    url3x2= url3x2[0]
                    if legenda3:
                        legenda3 = legenda3[0]
                        if not "http" in legenda3:
                            legenda3= legenda3.replace("sub=","https://sub.sfplayer.net/subdata/").replace("à","%C3%A0").replace("é","%C3%A9").replace("ó","%C3%B3").replace("ô","%C3%B4").replace("ã","%C3%A3").replace("ç","%C3%A7").replace("í","%C3%AD")
                        PlayUrl(name, url3x2, iconimage, info, sub = legenda3)
                    else:
                        PlayUrl(name, url3x2, iconimage, info)
	except UnboundLocalError:
		sys.exit()
	except (IndexError, ValueError):
		xbmcgui.Dialog().ok('Play XD', 'Episódio não encontrado')
		sys.exit()
def GetChoice(choiceTitle, fileTitle, urlTitle, choiceFile, choiceUrl, choiceNone=None, fileType=1, fileMask=None, defaultText=""):
	choice = ''
	choiceList = [getLocaleString(choiceFile), getLocaleString(choiceUrl)]
	if choiceNone is not None:
		choiceList = [getLocaleString(choiceNone)] + choiceList
	method = GetSourceLocation(getLocaleString(choiceTitle), choiceList)	
	if choiceNone is None and method == 0 or choiceNone is not None and method == 1:
		if not defaultText.startswith('http'):
			defaultText = ""
		choice = GetKeyboardText(getLocaleString(fileTitle), defaultText).strip().decode("utf-8")
	elif choiceNone is None and method == 1 or choiceNone is not None and method == 2:
		if defaultText.startswith('http'):
			defaultText = ""
		choice = xbmcgui.Dialog().browse(fileType, getLocaleString(urlTitle), 'files', fileMask, False, False, defaultText).decode("utf-8")
	return choice			
def PlayUrl(name, url, iconimage=None, info='', sub='', metah=''):
	#try:
	#	f = common.OpenURL("http://sstor.000webhostapp.com/imdb/i.txt")
	#	if "year" in f:
	#		metah = eval(f)
	#		f = common.OpenURL("http://sstor.000webhostapp.com/imdb/deleta.php")
	#except:
	#	pass
	if ";;;" in background:
		b = background.split(";;;")
		if "RC" in b[2]:
			AddFavorites(b[0], iconimage, b[1], "95", "historic.txt")
		elif "NC" in b[2]:
			AddFavorites(b[0], iconimage, b[1], "78", "historic.txt")
		elif "MM" in b[2]:
			AddFavorites(b[0], iconimage, b[1], "181", "historic.txt")
	url = re.sub('\.mp4$', '.mp4?play', url)
	url = common.getFinalUrl(url)
	xbmc.log('--- Playing "{0}". {1}'.format(name, url), 2)
	#ST(url)
	listitem = xbmcgui.ListItem(path=url)
	if cSIPTV:
		urllib2.urlopen( "http://cubeplay.000webhostapp.com/siptv/index.php?u="+cSIPTV+"&"+url ).read()
	if metah:
		listitem.setInfo(type="Video", infoLabels=metah)
	else:
		listitem.setInfo(type="Video", infoLabels={"mediatype": "video", "Title": name, "Plot": info })
	if sub!='':
		listitem.setSubtitles(['special://temp/example.srt', sub ])
	if iconimage is not None:
		try:
			listitem.setArt({'thumb' : iconimage})
		except:
			listitem.setThumbnailImage(iconimage)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def AddDir(name, url, mode, iconimage='', logos='', index=-1, move=0, isFolder=True, IsPlayable=False, background=None, cacheMin='0', info='', metah='', sub=''):
	urlParams = {'name': name, 'url': url, 'mode': mode, 'iconimage': iconimage, 'logos': logos, 'cache': cacheMin, 'info': info, 'background': background, 'metah': metah, 'sub': sub}
	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage )
	if metah:
		liz.setInfo(type="Video", infoLabels=metah)
		liz.setArt({"thumb": metah['cover_url'], "poster": metah['cover_url'], "banner": metah['cover_url'], "fanart": metah['backdrop_url'] })
	else:
		liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": info })
		#liz.setProperty("Fanart_Image", logos)
		liz.setArt({"poster": iconimage, "banner": logos, "fanart": logos })
	#listMode = 21 # Lists
	if IsPlayable:
		liz.setProperty('IsPlayable', 'true')
	items = []
	if mode == 1 or mode == 2:
		items = []
	elif mode== 61 and info=="":
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 78:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=72&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif (mode== 95 or mode== 96) and "imdb" in cadulto:
		liz.addContextMenuItems(items = [("IMDB", 'XBMC.RunPlugin({0}?url={1}&mode=350&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name))),
		("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=93&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 95 or mode== 96:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=93&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 135:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=131&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 171:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=175&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 181:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=185&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	elif mode== 191:
		liz.addContextMenuItems(items = [("Add ao fav. do Play XD", 'XBMC.RunPlugin({0}?url={1}&mode=195&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))])
	if info=="Filmes Favoritos":
		items = [("Remover dos favoritos", 'XBMC.RunPlugin({0}?index={1}&mode=333)'.format(sys.argv[0], index)),
		(getLocaleString(30030), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=-1)'.format(sys.argv[0], index, 338)),
		(getLocaleString(30031), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=1)'.format(sys.argv[0], index, 338)),
		(getLocaleString(30032), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=0)'.format(sys.argv[0], index, 338))]
		liz.addContextMenuItems(items)
	if info=="Séries Favoritas":
		items = [("Remover dos favoritos", 'XBMC.RunPlugin({0}?index={1}&mode=334)'.format(sys.argv[0], index)),
		(getLocaleString(30030), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=-1)'.format(sys.argv[0], index, 339)),
		(getLocaleString(30031), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=1)'.format(sys.argv[0], index, 339)),
		(getLocaleString(30032), 'XBMC.RunPlugin({0}?index={1}&mode={2}&move=0)'.format(sys.argv[0], index, 339))]
		liz.addContextMenuItems(items)
	if mode == 10:
		urlParams['index'] = index
	u = '{0}?{1}'.format(sys.argv[0], urllib.urlencode(urlParams))
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def GetKeyboardText(title = "", defaultText = ""):
	keyboard = xbmc.Keyboard(defaultText, title)
	keyboard.doModal()
	text = "" if not keyboard.isConfirmed() else keyboard.getText()
	return text

def GetSourceLocation(title, chList):
	dialog = xbmcgui.Dialog()
	answer = dialog.select(title, chList)
	return answer
def Imdbreturn(n):
	n = urllib.quote(n)
	urlq = common.OpenURL("https://api.themoviedb.org/3/search/movie?api_key=bd6af17904b638d482df1a924f1eabb4&query="+n+"&language=pt-BR")
	jq = json.loads(urlq)
	return jq

def AddImdb(url): #350
	urlm= re.compile("_.+?html$").findall(url)
	urlm = urlm[0]
	dir = re.sub('CubePlay', 'CubePlayMeta', addon_data_dir )
	file = os.path.join(dir, 'imdb.txt')
	file2 = os.path.join(dir, Cat+'\\imdb'+cPage+'.txt')
	favList = common.ReadList(file)
	for item in favList:
		if item["url"].lower() == urlm.decode("utf-8").lower():
			if "imdb" in file:
				xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, getLocaleString(30011), icon))
			return	
	q = re.sub(' ?\((Dub|Leg|Nac).+', '', name )
	q = re.sub('\[\/?COLOR.{0,10}\]', '', q )
	#q = "xmen"
	nomes=[]
	Ano=""
	Vote = 0.0
	jq = Imdbreturn(q)
	for x in jq['results']:
		try:
			rd = re.sub('\d{2}(\d{2})\-.+', r'\1', x['release_date'] )
			nomes.append("["+ str(rd) + "] " +x['title'].encode("utf-8") + " [COLOR blue]("+x['original_title'].encode("utf-8")+")[/COLOR]")
		except:
			nomes.append("[xx]"+x['title'].encode("utf-8") + " [COLOR blue]("+x['original_title'].encode("utf-8")+")[/COLOR]")
	s=-1
	if nomes:
		s = xbmcgui.Dialog().select(name, nomes)
	if s == -1:
		nomes=[]
		d = xbmcgui.Dialog().input("TheMovie id")
		if re.compile("\w").findall(d):
			jq = Imdbreturn(d)
			if jq['total_results']==0:
				xbmc.executebuiltin("Notification({0}, {1}, 5000, {2})".format(AddonName, "Nada encontrado".encode("utf-8"), icon))
				return
			for x in jq['results']:
				try:
					rd = re.sub('\d{2}(\d{2})\-.+', r'\1', x['release_date'] )
					nomes.append("["+ str(rd) + "] " +x['title'].encode("utf-8") + " [COLOR blue]("+x['original_title'].encode("utf-8")+")[/COLOR]")
				except:
					nomes.append("[xx]"+x['title'].encode("utf-8") + " [COLOR blue]("+x['original_title'].encode("utf-8")+")[/COLOR]")
			if nomes:
				s = xbmcgui.Dialog().select(name, nomes)
			if s == -1:
				return
		else:
			#d = "503314"
			if not d:
				return
			url2 = common.OpenURL("https://api.themoviedb.org/3/movie/"+d+"?api_key=bd6af17904b638d482df1a924f1eabb4&language=pt-BR")
			j = json.loads(url2)
			url3 = common.OpenURL("https://api.themoviedb.org/3/movie/"+str(j['id'])+"?api_key=bd6af17904b638d482df1a924f1eabb4&language=en-US")
			j3 = json.loads(url3)
			Nome=j['title']
			Id=d
			Name=j3['title']
			Ano = j['release_date']
			d2 = xbmcgui.Dialog().yesno("Kodi",Nome+" ?")
			if not d2:
				return
			jq = ""
	if jq:
		Nome=jq['results'][s]['title']
		Id=str(jq['results'][s]['id'])
		Name=jq['results'][s]['original_title']
		Ano = jq['results'][s]['release_date']
		Vote = jq['results'][s]['vote_average']
		if jq['results'][s]['original_language'] != 'en':
			url2 = common.OpenURL("https://api.themoviedb.org/3/movie/"+str(jq['results'][s]['id'])+"?api_key=bd6af17904b638d482df1a924f1eabb4&language=en-US")
			j2 = json.loads(url2)
			Name=j2['title']
	Ano = re.sub('\-.+', '', Ano )
	chList = []
	for channel in chList:
		if channel["name"].lower() == name.decode("utf-8").lower():
			urlm = channel["url"].encode("utf-8")
			break
	data = {"url": urlm.decode("utf-8"), "id": Id, "nome": Nome, "name": Name, "ano": Ano, "vote": Vote}
	#ST(data)
	#return
	favList.append(data)
	common.SaveList(file, favList)
	common.SaveList(file2, favList)
	if "imdb" in file:
		xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, Nome.encode("utf-8"), getLocaleString(30012), icon))

def AddFavorites(url, iconimage, name, mode, file):
	file = os.path.join(addon_data_dir, file)
	favList = common.ReadList(file)
	for item in favList:
		if item["url"].lower() == url.decode("utf-8").lower():
			if "favorites" in file:
				xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, getLocaleString(30011), icon))
			return
	chList = []	
	for channel in chList:
		if channel["name"].lower() == name.decode("utf-8").lower():
			url = channel["url"].encode("utf-8")
			iconimage = channel["image"].encode("utf-8")
			break
	if not iconimage:
		iconimage = ""
	data = {"url": url.decode("utf-8"), "image": iconimage.decode("utf-8"), "name": name.decode("utf-8"), "mode": mode}
	favList.append(data)
	common.SaveList(file, favList)
	if "favorites" in file:
		xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, getLocaleString(30012), icon))
	
def ListFavorites(file, info):
	file = os.path.join(addon_data_dir, file)
	chList = common.ReadList(file)
	i = 0
	for channel in chList:
		if cPlayD == "true" and channel["mode"]=="95":
			AddDir(channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), "96", channel["image"].encode("utf-8"), channel["image"].encode("utf-8"), isFolder=False, IsPlayable=True, info=info)
		else:
			AddDir(channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), channel["mode"], channel["image"].encode("utf-8"), channel["image"].encode("utf-8"), index=i, isFolder=True, IsPlayable=False, info=info)
		i += 1
		
def ListHistoric(file, info):
	file = os.path.join(addon_data_dir, file)
	chList = common.ReadList(file)
	for channel in reversed(chList):
		if cPlayD == "true" and channel["mode"]=="95":
			AddDir(channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), "96", channel["image"].encode("utf-8"), channel["image"].encode("utf-8"), isFolder=False, IsPlayable=True, info=info)
		else:
			AddDir(channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), channel["mode"], channel["image"].encode("utf-8"), channel["image"].encode("utf-8"), isFolder=True, IsPlayable=False, info=info)
		
def RemoveFromLists(index, listFile):
	chList = common.ReadList(listFile) 
	if index < 0 or index >= len(chList):
		return
	del chList[index]
	common.SaveList(listFile, chList)
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def AddNewFavorite(file):
	file = os.path.join(addon_data_dir, file)
	chName = GetKeyboardText(getLocaleString(30014))
	if len(chName) < 1:
		return
	chUrl = GetKeyboardText(getLocaleString(30015))
	if len(chUrl) < 1:
		return
	image = GetChoice(30023, 30023, 30023, 30024, 30025, 30021, fileType=2)
		
	favList = common.ReadList(file)
	for item in favList:
		if item["url"].lower() == chUrl.decode("utf-8").lower():
			xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, chName, getLocaleString(30011), icon))
			return			
	data = {"url": chUrl.decode("utf-8"), "image": image, "name": chName.decode("utf-8")}	
	favList.append(data)
	if common.SaveList(file, favList):
		xbmc.executebuiltin("XBMC.Container.Refresh()")
	
def MoveInList(index, step, listFile):
	theList = common.ReadList(listFile)
	if index + step >= len(theList) or index + step < 0:
		return
	if step == 0:
		step = GetIndexFromUser(len(theList), index)
	if step < 0:
		tempList = theList[0:index + step] + [theList[index]] + theList[index + step:index] + theList[index + 1:]
	elif step > 0:
		tempList = theList[0:index] + theList[index +  1:index + 1 + step] + [theList[index]] + theList[index + 1 + step:]
	else:
		return
	common.SaveList(listFile, tempList)
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def GetNumFromUser(title, defaultt=''):
	dialog = xbmcgui.Dialog()
	choice = dialog.input(title, defaultt=defaultt, type=xbmcgui.INPUT_NUMERIC)
	return None if choice == '' else int(choice)

def GetIndexFromUser(listLen, index):
	dialog = xbmcgui.Dialog()
	location = GetNumFromUser('{0} (1-{1})'.format(getLocaleString(30033), listLen))
	return 0 if location is None or location > listLen or location <= 0 else location - 1 - index

def Refresh():
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def TogglePrevious(url, background):
	Addon.setSetting(background, str(int(url) - 1) )
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def ToggleNext(url, background):
	#xbmcgui.Dialog().ok('Play XD', url + " " +background)
	Addon.setSetting(background, str(int(url) + 1) )
	xbmc.executebuiltin("XBMC.Container.Refresh()")

def getmd5(t):
	value_altered = ''.join(chr(ord(letter)-1) for letter in t)
	return value_altered

def CheckUpdate(msg): #200
	try:
		uversao = urllib2.urlopen( "https://raw.githubusercontent.com/GladistonXD/Play-XD/master/version.txt" ).read().replace('\n','').replace('\r','')
		uversao = re.compile('[a-zA-Z\.\d]+').findall(uversao)[0]
		#xbmcgui.Dialog().ok(Versao, uversao)
		if uversao != Versao:
			Update()
			xbmc.executebuiltin("XBMC.Container.Refresh()")
		elif msg==True:
			xbmcgui.Dialog().ok('Play XD', "O addon já esta na última versao: "+Versao+"\nAs atualizações normalmente são automáticas\nUse esse recurso caso nao esteja recebendo automaticamente")
			xbmc.executebuiltin("XBMC.Container.Refresh()")
	except urllib2.URLError, e:
		if msg==True:
			xbmcgui.Dialog().ok('Play XD', "Não foi possível checar")

def Update(): #futura atualização automatica
	Path = xbmc.translatePath( xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
	try:
		fonte = urllib2.urlopen( "https://raw.githubusercontent.com/GladistonXD/Play-XD/master/default.py" ).read().replace('\n','')
		prog = re.compile('#checkintegrity25852').findall(fonte)
		if prog:
			py = os.path.join( Path, "default.py")
			file = open(py, "w")
			file.write(fonte)
			file.close()
		fonte = urllib2.urlopen( "https://raw.githubusercontent.com/GladistonXD/Play-XD/master/resources/settings.xml" ).read().replace('\n','')
		prog = re.compile('</settings>').findall(fonte)
		if prog:
			py = os.path.join( Path, "resources/settings.xml")
			file = open(py, "w")
			file.write(fonte)
			file.close()
		fonte = urllib2.urlopen( "https://raw.githubusercontent.com/GladistonXD/Play-XD/master/addon.xml" ).read().replace('\n','')
		prog = re.compile('</addon>').findall(fonte)
		if prog:
			py = os.path.join( Path, "addon.xml")
			file = open(py, "w")
			file.write(fonte)
			file.close()
		xbmc.executebuiltin("Notification({0}, {1}, 9000, {2})".format(AddonName, "Atualizando o addon. Aguarde um momento!", icon))
		xbmc.sleep(2000)
	except:
		xbmcgui.Dialog().ok('Play XD', "Ocorreu um erro, tente novamente mais tarde")

def ST(x):
	x = str(x)
	Path = xbmc.translatePath( xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
	py = os.path.join( Path, "study.txt")
	file = open(py, "w")
	file.write(x)
	file.close()

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))
url = params.get('url')
logos = params.get('logos', '')
name = params.get('name')
iconimage = params.get('iconimage')
cache = int(params.get('cache', '0'))
index = int(params.get('index', '-1'))
move = int(params.get('move', '0'))
mode = int(params.get('mode', '0'))
info = params.get('info')
background = params.get('background')
metah = params.get('metah')

if mode == 0:
	Categories()
	setViewM()
	if not "update" in cadulto:
		ST(1)
		CheckUpdate(False)
elif mode == -1: 
	MCanais()
	setViewS()
elif mode == -2: MFilmes()
elif mode == -3: MSeries()
elif mode == 3 or mode == 32:
	PlayUrl(name, url, iconimage, info)
elif mode == 301:
	ListFavorites('favoritesf.txt', "Filmes Favoritos")
	setViewS()
elif mode == 302:
	ListFavorites('favoritess.txt', "Séries Favoritas")
	setViewM()
elif mode == 305:
	ListHistoric('historic.txt', "Historico")
	setViewM()
elif mode == 31: 
	AddFavorites(url, iconimage, name, "61", 'favoritess.txt')
elif mode == 72: 
	AddFavorites(url, iconimage, name, "78", 'favoritesf.txt')
elif mode == 93: 
	AddFavorites(url, iconimage, name, "95", 'favoritesf.txt')
elif mode == 131: 
	AddFavorites(url, iconimage, name, "135", 'favoritess.txt')
elif mode == 175: 
	AddFavorites(url, iconimage, name, "171", 'favoritesf.txt')
elif mode == 185: 
	AddFavorites(url, iconimage, name, "181", 'favoritesf.txt')
elif mode == 195: 
	AddFavorites(url, iconimage, name, "191", 'favoritess.txt')
elif mode == 196: 
	AddFavorites(url, iconimage, name, "602", 'favoritess2.txt')
elif mode == 333:
	RemoveFromLists(index, favfilmesFile)
elif mode == 338:
	MoveInList(index, move, favfilmesFile)
elif mode == 334:
	RemoveFromLists(index, favseriesFile)
elif mode == 339:
	MoveInList(index, move, favseriesFile)
elif mode == 38:
	dialog = xbmcgui.Dialog()
	ret = dialog.yesno('Play XD', 'Deseja mesmo deletar todos os filmes favoritos?')
	if ret:
		common.DelFile(favfilmesFile)
		sys.exit()
elif mode == 39:
	dialog = xbmcgui.Dialog()
	ret = dialog.yesno('Play XD', 'Deseja mesmo deletar todos os seriados favoritos?')
	if ret:
		common.DelFile(favseriesFile)
		sys.exit()
elif mode == 40:
	dialog = xbmcgui.Dialog()
	ret = dialog.yesno('Play XD', 'Deseja mesmo deletar todo o historico?')
	if ret:
		common.DelFile(historicFile)
		sys.exit()
elif mode == 50:
	Refresh()
elif mode == 60:
	Series()
	setViewS()
elif mode == 61:
	ListSNC(background)
	setViewS()
elif mode == 62:
	PlayS()
	setViewS()
elif mode == 71:
	MoviesNC()
	setViewM()
elif mode == 600:
	MenuVizer()
	setViewM()
elif mode == 601:
	MenuVizer2()
	setViewM()
elif mode == 602:
	PlayVizer()
	setViewM()        
elif mode == 530:
	FilmesHD()
	setViewM()
elif mode == 531:
	FilmesHDmenu()
	setViewM()
elif mode == 532:
	FilmesHDPlay()
	setViewM()
elif mode == 78:
	ListMoviesNC()
	setViewS()
elif mode == 79:
	PlayMNC()
	setViewS()
elif mode == 80:
	Generos()
elif mode == 500:
	Generos2()
elif mode == 81:
	CategoryOrdem2(url)
elif mode == 90:
	MoviesRCD()
	setViewM()
elif mode == 91:
	MoviesRCL()
	setViewM()
elif mode == 92:
	MoviesRCN()
	setViewM()
elif mode == 95:
	PlayMRC()
	setViewM()
elif mode == 96:
	PlayMRC2()
elif mode == 100:
	TVRC()
	setViewM()
elif mode == 101:
	PlayTVRC()
elif mode == 102:
	TVCB(url)
	setViewS()
elif mode == 103:
	PlayTVCB()
elif mode == 104:
	TVCB2(url)
	setViewS()
elif mode == 107:
	TVCB3()
	setViewS()    
elif mode == 108:
	TVCB4()
	setViewS()    
elif mode == 109:
	TVCB4PLAY()
elif mode == 111:
	TVCB5()
	setViewS()  
elif mode == 112:
	TVCB5PLAY()
	setViewS()   
elif mode == 106:
	RadioTV(url)
	setViewS()    
elif mode == 105:
	Addon.setSetting("cEPG", "1")
	xbmc.executebuiltin("XBMC.Container.Refresh()")
elif mode == 110:
	ToggleNext(url, background)
elif mode == 120:
	TogglePrevious(url, background)
elif mode == 130:
	SeriesRC("series","cPageser")
	setViewS()
elif mode == 135:
	TemporadasRC(background)
	setViewS()
elif mode == 133:
	PlaySRC()
	setViewS()
elif mode == 139:
	AllEpisodiosRC()
	setViewS()
elif mode == 140:
	SeriesRC("animes","cPageani")
	setViewS()
elif mode == 150:
	SeriesRC("desenhos","cPagedes")
	setViewS()
elif mode == 160:
	Busca()
	setViewM()
elif mode == 170:
	MoviesFO("Rapidvideo","cPagefo1")
	setViewM()
elif mode == 171:
	GetMFO1()
	setViewM()
elif mode == 172:
	PlayMFO1()
elif mode == 85:
	GenerosFO()
elif mode == 180:
	ListFilmeMM("cPageMMf")
	setViewM()
elif mode == 181:
	OpenLinkMM()
	setViewM()
elif mode == 182:
	PlayLinkMM()
elif mode == 184:
	ListFilmeLancMM()
	setViewM()
elif mode == 189:
	GenerosMM()
elif mode == 190:
	ListSerieMM()
	setViewS()
elif mode == 191:
	ListSMM(background)
	setViewS()
elif mode == 192:
	ListEpiMM(background)
	setViewS()
elif mode == 194:
	PlaySMM()
elif mode == 200:
	CheckUpdate(True)
elif mode == 210:
	ListGO()
	setViewM()
elif mode == 310:
	ListGOL()
	setViewM()    
elif mode == 211:
	ListTop()
	setViewS()
elif mode == 213:
	ListPlay()
	setViewS()    
elif mode == 311:
	ListTopL()
	setViewS()    
elif mode == 212:
	PlayTVCB2()  
elif mode == 1212:
	PlayTVB3()      
elif mode == 219:
	GenerosGO()
elif mode == 230:
	GenerosFl()
elif mode == 231: 
	GenerosQUE1()
elif mode == 232: 
	GenerosBIZ()
elif mode == 233: 
	GenerosMEG()
elif mode == 234: 
	GenerosFHD()
elif mode == 235: 
	GenerosVZ()       
elif mode == 220:
	Filmes96()
elif mode == 221:
	MoviesRCR() ###
	setViewM()
elif mode == 229:
	PlayFilmes96()
elif mode == 350:
	AddImdb(url)
elif mode == 411:
	ListMovieSF()
	setViewM()
elif mode == 405:
	PlaySSF()
	setViewM()
elif mode == 406:
	PlaySSFS()
elif mode == 407:
	Play2SFS()
elif mode == 401:
	ListSerieSF()
	setViewS()
elif mode == 402:
	ListTempSF()
	setViewS()
elif mode == 403:
	ListEpiSF()
	setViewS()
elif mode == 430:
	ListSerieQF()
	setViewS()
elif mode == 431:
	ListTempQF()
	setViewS()
elif mode == 432:
	ListEpiQF()
	setViewS()
elif mode == 433:
	PlayEpiQF()
	setViewS()
elif mode == 450:
	SerieMenuBZ()
	setViewS() 
elif mode == 451:
	SerieMenuBZ2()
	setViewS()
elif mode == 452:
	SeriePlayBZ()
	setViewS()   
elif mode == 453:
	SeriePlayBZ2()
	setViewS()      
elif mode == 510:
	QuerofilmeshdMENU()
	setViewM()    
elif mode == 511:
	QuerofilmeshdLista()
	setViewM()
elif mode == 512:
	QuerofilmeshdPlay()
	setViewM()
elif mode == 513:
	QuerofilmeshdPlay2()
	setViewM()    
elif mode == 514:
	AssistirbizMENU()
	setViewM()    
elif mode == 517: 
	AssistirbizMENU2()
	setViewM()    
elif mode == 515:
	AssistirbizLista()
	setViewM()
elif mode == 516:
	AssistirbizPlay()
	setViewM()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#checkintegrity25852
