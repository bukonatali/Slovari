songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
a = songsdict ['World in My Eyes']
b = songsdict ['Sweetest Perfection']
c = songsdict ['Personal Jesus']
d = songsdict ['Halo']
e = songsdict ['Waiting for the Night']
f = songsdict ['Enjoy the Silence']
g = songsdict ['Policy of Truth']
i = songsdict ['Blue Dress']
h = songsdict ['Clean']
summ_d = a+b+c+d+e+f+g+i+h
print("общее время звучания всех песен ", (summ_d))
print([x for x in songsdict if songsdict[x]>5])
print(dict(filter(lambda x: len(x[0].split()) == 1, songsdict.items())))





