def clear():
	import platform
	czy_linux=platform.system()
	if(czy_linux=="Linux"):
		import os
		os.system("clear")
	elif(czy_linux=="Windows"):
		import os
		os.system("cls")
	elif(czy_linux=="Darwin"):
		import os
		os.system("clear")
	else:
		print("No to problem, ekran zasrany")
		print("\n\n\n")

ilosc=int(input("Podaj ile wierzcholkow ma miec graf: "))
if(ilosc==0):
	print("Graf jest pusty, nie ma stopnia")
else:
	wierzcholki=[]
	krawedzie=[]
	suma_stopni=0
	for i in range(ilosc):
		wierzcholki.append(input("Podaj nazwe wierzcholka: "))
		krawedzie.append(input("Podaj z ktorymi wierzcholkami ma byc polaczony(odstepy-spacja): "))
		if(i==0):
			pomocnicza=krawedzie[i].count(" ")
			stopien_grafu=len(krawedzie[i])-pomocnicza
			suma_stopni=len(krawedzie[i])-pomocnicza
		if(i>=1):
			szukanie=krawedzie[i]
			szukanie=szukanie.split(" ")
			pomocnicza=krawedzie[i].count(" ")
			suma_stopni=len(krawedzie[i])-pomocnicza+suma_stopni
			if((len(krawedzie[i])-pomocnicza)>stopien_grafu):
				stopnien_grafu=len(krawedzie[i])-pomocnicza
			else:
				stopien_grafu=stopien_grafu
			for x in range(len(szukanie)):
				if(szukanie[x]==""):
					break
				elif(szukanie[x]==wierzcholki[i-1]):
					szukanie[x]=""
			krawedzie[i]=szukanie[x]

	graf={}
	for a in range(ilosc):
		graf[wierzcholki[a]]=krawedzie[a]

	clear()
	import pprint
	print("Twoj graf: ")
	pprint.pprint(graf)
	print("Stopien tego grafu to "+str(stopien_grafu))
	print("Suma stopni tego grafu to "+str(suma_stopni))
