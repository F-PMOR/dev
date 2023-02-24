#!/bin/env python3

import os,re
from pypdf import PdfReader
from gtts import gTTS

"""
Script à continuer, 
le but est de récupérer un fichier pdf.
- de traiter une page -> fait
- de supprimer la dernière ligne -> fait
- de supprimer les retours chariots -> fait
-> Reste à faire: 
- Lire plusieurs pages
- merger l'ensemble des pages pour creer un gros fichier text. 
    - tester déjà avec deux ou trois pages
- transformer en text to speech via googlespeech

puis de transformer le text en speech grace à googlespeech

"""

livre="./livre_pdf/small.pdf"
page_debut=7
page_fin=8

def f_readfile(_file="./livre_pdf/small.pdf", _page = 7) -> str:
    reader = PdfReader(livre)
    #number_of_pages = len(reader.pages)
    #print(f"number of pages : {number_of_pages}")
    page = reader.pages[_page]
    _text = page.extract_text()
    return _text

def f_input():
    """
    on demande : 
    - le nom du fichier pdf à traiter avec une valeur par defaut.
    - la page de début
    - la page de fin

    return : 
    - le fichier : file descripteur
    - page debut : int
    - page fin : int

    """
    _boucle = True
    while _boucle:
        _file=input("quel fichier pdf voulez-vous traiter ? (defaut : ./livre_pdf/small.pdf) : ")
        print(_file)
        if len(_file) == 0:
            _file = "./livre_pdf/small.pdf"
        try:
            if not os.path.isfile(_file):
                raise Exception("Fichier impossible à ouvrir") 
        except:
            print("Fichier impossible à ouvrir")
            _boucle = True
            continue
        print("Vous devez entrer la page de début et fin de traitement du fichier pdf")
        try:
            _page_debut=input("Quelle est le numéro de la page de debut ?")
            _page_debut=int(_page_debut)
            _page_fin=input("Quelle est le numéro de page de fin ?")
            _page_fin=int(_page_fin)
            _boucle=False
        except:
            print("Entrez un numéro de page svp")
            _boucle=True    
    return _file,_page_debut, _page_fin

def f_text_traitement(_text):
    """
    Traitement du text 
    - suppression des deux dernières lignes
    - 

    input: 
    - text: string
    return : 
    - text : string
    """
    # suppression des deux derniere ligne de la page
    _splittext = _text.splitlines()
    _splittext.pop(-1)
    _splittext.pop(-1)
    _newtext = ''.join(_splittext)
    print(f"text avant regex : {_newtext}\n")
    # regex substitution - change text with no space after a dot "test.test -> test. test"
    regex = r"(\w\.)(\w)"
    subst = r"\1 \2"
    _newtext = re.sub(regex, subst, _newtext, 0, re.MULTILINE)
    # regex substitution - change text with no space after multiple dot "que...Suite -> que... Suite"
    # the "..." are not three dot, but a char that is compose of three dot !
    regex = r"(\w|\W)(…)(\w)"
    subst = r"\1... \3"
    _newtext = re.sub(regex, subst, _newtext, 0, re.MULTILINE)

    print(f"text après regex : {_newtext}\n")
    return _newtext


def f_text2mp3(_page, _text):
#    mytest = """
#    Depuis que tu vas dans ton école hôtelière, c’est le train que tu prends tous les vendredis soir pour rentrer, le temps du week‑end.À 19 heures, t’arrives chez ta mère. Tu dînes avec elle et ton frère. Une heure et demie plus tard tu sonnes chez moi, dans la maison d’à côté. On se retrouve, et le week‑end commence enfin. On a une semaine de silence à combler, toi et moi.Mais là, aujourd’hui, dis‑moi que t’es monté dans un autre train, un qui part plus tard. Un qui arrivera plus tard. Voilà, c’est ça. Alors arrête de déconner, c’est pas drôle. T’es pas parti, donc t’as du réseau, donc tu peux m’appeler. Et si tu m’appelles pas, c’est que…Suite au déraillement d’un train à quelques kilomètres de la petite gare de Moissy-Bourgeron, le trafic est totalement interrompu sur la ligne Nantes –…Totalement interrompu, ils disent. To‑ta‑le‑ment interrompu.T’as déjà senti ça, dans ta vie ? La vague glacée sur tes bras, tes jambes, ton ventre, tu sens le froid qui monte, ton sang se fige, tu ne peux plus respirer, et c’est si froid que ça te brûle les chairs en dedans ? Et ça fait si mal que tu ne peux même plus crier, hurler, ou gémir ? T’as plus rien à toi, ni larmes ni colère ni dégoût, qu’une seringue de douleur qui s’enfonce dans tes veines.Moi, ça m’est arrivé une fois dans le métro, à Paris.
#    """
    audio = gTTS(text=_text, lang='fr', slow=False)
    #bodies = audio.get_bodies()
    #print(bodies)
    audio_file="./mp3/pdf2mp3_"+ str(_page) + ".mp3"
    audio.save(audio_file)
    #os.system("play -t alsa gTTS.mp3 tempo 1.33")

# on rentre le fichier et la page à lire
file, page_debut, page_fin = f_input()
# text=f_readfile(file,page)
# Shunt de l'input
for page in range(page_debut,page_fin + 1):
    print(f"traitement de la page : {page}")
    #text=f_readfile(livre, page)
    text=f_readfile(file, page)
    newtext=f_text_traitement(text)
    #print(newtext)
    # traitement du fichier
    filetext= "./livre_txt/pdf2text_" + str(page) + ".txt"
    print(f"ecriture du fichier : {filetext}")
    with open(filetext,"w") as file:
        file.write(newtext)
    f_text2mp3(page, newtext)
    print("Pour lire les fichiers audio : play  -t alsa ./mp3/fichier.mp3 tempo 1.33")






