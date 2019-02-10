import shutil

def h1():
    pass

with open('./header.md') as mon_fichier:
    for ligne in mon_fichier:
        h1 = 'h1'.replace('#', 'h1')
        print(ligne)



shutil.copyfile('header.md', 'headear.html')