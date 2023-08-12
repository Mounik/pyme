import argparse


def mon_programme(options):
    print("Mon programme ")
    print("Options : %s " % options)

if __name__ == '__main__':
    ## gestion des arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fichier', help='Nom de Fichier')
    parser.add_argument('-v', '--verbose', help='Mode Verbeux', action='store_true')

    options = parser.parse_args()

    # Lancement de ma fonction avec passage des options
    # en paramètre
    mon_programme(options)