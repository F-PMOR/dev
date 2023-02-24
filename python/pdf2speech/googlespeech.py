#!/bin/env python3
from gtts import gTTS
import os

mytest = """
Depuis que tu vas dans ton école hôtelière, c’est le train que tu prends tous les vendredis soir pour rentrer, le temps du week‑end.À 19 heures, t’arrives chez ta mère. Tu dînes avec elle et ton frère. Une heure et demie plus tard tu sonnes chez moi, dans la maison d’à côté. On se retrouve, et le week‑end commence enfin. On a une semaine de silence à combler, toi et moi.Mais là, aujourd’hui, dis‑moi que t’es monté dans un autre train, un qui part plus tard. Un qui arrivera plus tard. Voilà, c’est ça. Alors arrête de déconner, c’est pas drôle. T’es pas parti, donc t’as du réseau, donc tu peux m’appeler. Et si tu m’appelles pas, c’est que…Suite au déraillement d’un train à quelques kilomètres de la petite gare de Moissy-Bourgeron, le trafic est totalement interrompu sur la ligne Nantes –…Totalement interrompu, ils disent. To‑ta‑le‑ment interrompu.T’as déjà senti ça, dans ta vie ? La vague glacée sur tes bras, tes jambes, ton ventre, tu sens le froid qui monte, ton sang se fige, tu ne peux plus respirer, et c’est si froid que ça te brûle les chairs en dedans ? Et ça fait si mal que tu ne peux même plus crier, hurler, ou gémir ? T’as plus rien à toi, ni larmes ni colère ni dégoût, qu’une seringue de douleur qui s’enfonce dans tes veines.Moi, ça m’est arrivé une fois dans le métro, à Paris.
"""
audio = gTTS(text=mytest, lang='fr', slow=False)

#bodies = audio.get_bodies()
#print(bodies)
audio.save("gTTS.mp3")
os.system("play -t alsa gTTS.mp3 tempo 1.33")