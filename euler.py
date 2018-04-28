from copy import copy

def polaczenie(graf):
	start = list(graf)[0]
	dupa = {i: '1' for i in graf}
	dupa[start] = '2'
	S = [start]
	while len(S) != 0:
		u = S.pop()
		for i in graf[u]:
			if dupa[i] == '1':
				dupa[i] = '2'
				S.append(i)
			dupa[u] = '3'
	return list(dupa.values()).count('3') == len(graf)


def stopien(graf):
	stopien_w = []
	for i in graf:
		if len(graf[i]) % 2 != 0:
			stopien_w.append(i)
	return stopien_w

def krawedzie(graf):
	krawedz = []
	for i in graf:
		for x in graf[i]:
			krawedz.append((i, x))
	return krawedz

def fleury(graf):
	kupa = stopien(graf)
	if len(kupa) > 2 or len(kupa) == 1:
		return 'To nie graf Eulerowy'
	else:
		g = copy(graf)
		lista = []
		if len(kupa) == 2:
			u = kupa[0]
		else:
			u = list(g)[0]
		while len(krawedzie(g)) > 0:
			ten_w = u
			for u in g[ten_w]:
				g[ten_w].remove(u)
				g[u].remove(ten_w)
				most = not polaczenie(g)
				if most:
					g[ten_w].append(u)
					g[u].append(ten_w)
				else:
					break
			if most:
				g[ten_w].remove(u)
				g[u].remove(ten_w)
				g.pop(ten_w)
			lista.append((ten_w, u))
	return lista

graf = {
    0: [1, 4, 6, 8],
    1: [0, 2, 3, 8],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [0, 3],
    5: [3, 6],
    6: [0, 5, 7, 8],
    7: [6, 8],
    8: [0, 1, 6, 7]
}
print(fleury(graf))
