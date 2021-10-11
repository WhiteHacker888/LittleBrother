from core.facebookSearchTool import facebookSearchTool
import webbrowser, colorama
from colorama import init, Fore,  Back,  Style

init()
warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

def facebookStalk():
	profile = input(" Facebook username: ")
	if profile.startswith("http"):
		profile = profile.split("/")
		profile = profile[3]

	menuStalk = """

        TAGS              ODAMLAR              LIEUX
    ------------        -------------        -------------
    [1] Rasmlar          [4] Oila          [10] Hammasi
    [2] Videolar          [5] Do'stlar             [11] Barlar
    [3] Nashr     [6] Umumiy do'stlar   [12] Restarantlar
                        [7] Ish          [13] Magazinlar
        LIKE            [8] Oqish            [14] Tashqarida
    ------------        [9] Mahalliy           [15] Mehmonxonalar
    [17] Rasmlar                              [16] Teatr
    [18] Videolar          FIKRLAR
    [19] Nashrlar   -------------          QIZIQISHLAR     
                        [20] Rasmlar          -------------
        PROFIL                               [29] Sahifalar
    -------------                            [30] Siyosatlar
    [21] Rasmlar                              [31] Din
    [22] Videolar                              [32] Musiqalar
    [23] Nashrlar                        [33] Filmlar
    [24] Guruhlar                             [34] Kitoblar
    [25] Kelgusi voqealar                    [35] Binolar
    [26] O'tgan voqealar
    [27] O'yinlar
    [28] Ilovalar

        [b] Orqaga    [c] Ekranni tozalash    [e] Chiqish
	"""

	dicFbStalk = {
	# <
	# TAGS 
	"1": "https://www.facebook.com/search/%s/photos-of/intersect",
	"2": "https://www.facebook.com/search/%s/videos-of/intersect",
	"3": "https://www.facebook.com/search/%s/stories-tagged/intersect",
	# PERSONNE
	"4": "https://www.facebook.com/search/%s/relatives/intersect",
	"5": "https://www.facebook.com/search/%s/friends/intersect",
	"6": "https://www.facebook.com/search/%s/friends/friends/intersect",
	"7": "https://www.facebook.com/search/%s/employees/intersect/",
	"8": "https://www.facebook.com/search/%s/schools-attended/ever-past/intersect/students/intersect/",
	"9": "https://www.facebook.com/search/%s/current-cities/residents-near/present/intersect",
	# LEUX
	"10": "https://www.facebook.com/search/%s/places-visited/",
	"11": "https://www.facebook.com/search/%s/places-visited/110290705711626/places/intersect/",
	"12": "https://www.facebook.com/search/%s/places-visited/273819889375819/places/intersect/",
	"13": "https://www.facebook.com/search/%s/places-visited/200600219953504/places/intersect/",
	"14": "https://www.facebook.com/search/%s/places-visited/935165616516865/places/intersect/",
	"15": "https://www.facebook.com/search/%s/places-visited/164243073639257/places/intersect/",
	"16": "https://www.facebook.com/search/%s/places-visited/192511100766680/places/intersect/",
	# LIKE
	"17": "https://www.facebook.com/search/%s/photos-liked/intersect",
	"18": "https://www.facebook.com/search/%s/videos-liked/intersect",
	"19": "https://www.facebook.com/search/%s/stories-liked/intersect",
	# COMMENTAIRE
	"20": "https://www.facebook.com/search/%s/photos-commented/intersect",
	# PROFIL
	"21": "https://www.facebook.com/search/%s/photos-by/",
	"22": "https://www.facebook.com/search/%s/videos-by/",
	"23": "https://www.facebook.com/search/%s/stories-by/",
	"24": "https://www.facebook.com/search/%s/groups",
	"25": "https://www.facebook.com/search/%s/events-joined/",
	"26": "https://www.facebook.com/search/%s/events-joined/in-past/date/events/intersect/",
	"27": "https://www.facebook.com/search/%s/apps-used/game/apps/intersect",
	"28": "https://www.facebook.com/search/%s/apps-used/",
	# INTERETS
	"29": "https://www.facebook.com/search/%s/pages-liked/intersect",
	"30": "https://www.facebook.com/search/%s/pages-liked/161431733929266/pages/intersect/",
	"31": "https://www.facebook.com/search/%s/pages-liked/religion/pages/intersect/",
	"32": "https://www.facebook.com/search/%s/pages-liked/musician/pages/intersect/",
	"33": "https://www.facebook.com/search/%s/pages-liked/movie/pages/intersect/",
	"34": "https://www.facebook.com/search/%s/pages-liked/book/pages/intersect/",
	"35": "https://www.facebook.com/search/%s/places-liked/"
	}

	helpMsgFbStalk = """
		back : Revenir au menu principal.
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

	resultProfile = """
    [Name]  %s
    [Work]  %s
    [Loc]   %s
    [ID]    %s"""

	fbtool = facebookSearchTool()

	try:
		fbtool.getInfoProfile(profile)
		
		loc = fbtool.address
		work = fbtool.job
		name = fbtool.name
		ID = fbtool.facebookId
		facebookID = ID

	except:
		print("\n"+warning+" Xatolik yuz berdi!")

	while True:

		if not facebookID:
			print("\n"+warning+" Qayta tiklanmadi l'ID.")
			print(question+"\n Bilasizmi l'ID ?")
			_id_  = input(question+" [O/N]: ")
			if _id_.upper() == "O" or _id_.upper() == "Y":
				facebookID = input(" ID: ")
				input(facebookID)
			else:
				break

		print(resultProfile % (name, work, loc, ID))
		print(menuStalk)
		
		while True:
			s = input("\n LittleBrother("+Fore.BLUE + "Lookup/facebookStalk" + Fore.RESET + ")$ ")
			if s == "help":
				print(helpMsgFbStalk)
			elif s.lower() == "c":
				clear()
				print(menuStalk)
			elif s.lower() == "b":
				break
			elif s.lower() == "e":
				quit()
			else:
				if str(s) == '29':
					pages = fbtool.searchPageLiked(profile)
					for p in pages:
						print("[Liked] %s" % (p))
				try:
					int(s)
					facebookUrl = dicFbStalk.get(str(s))
					webbrowser.open(facebookUrl % (facebookID))
				except ValueError:
					pass
		break