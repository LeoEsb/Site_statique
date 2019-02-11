import os
import argparse
import markdown2


parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', type = str, required = True, metavar = '', help = 'dossier avec des fichiers en markdown à convertir en fichier html')
parser.add_argument('-o','--output', type = str, required = True, metavar = '', help='dossier où seront mis les fichiers html créé pour les afficher sur le site site statique')
args = parser.parse_args()


conversion_md = args.input
resultat_html = args.output

dossier = os.listdir(conversion_md)


def converter(fichier_md, resultat_html) :
    compteur = 0
    for fichiers in dossier:
        with open (f'{conversion_md}/{fichiers}',"r") as file :
            convert_html = markdown2.markdown(file.read())
            resultat_html = open(f'{resultat_html}/index{compteur}.html',"w")
            resultat_html.write(convert_html)
            resultat_html.close()
            compteur += 1

converter(conversion_md, resultat_html)
