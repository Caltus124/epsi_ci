from datetime import datetime
import subprocess
import os

# https://github.com/Caltus124/epsi_ci.git
# main
#  e4910b6

NUM_COMMIT = ""
PATH_CLONE = ""

def git():
    global NUM_COMMIT
    global PATH_CLONE
    os.system('clear')
    NUM_URL = input("Sélctionner une URL de repot : ")
    NUM_COMMIT = input("Selectionner le numéro du commit : ")
    PATH_CLONE = "/tmp/github/"
    
    os.system('clear')

    subprocess.run(["git", "clone", NUM_URL, PATH_CLONE])
    
    print("\nClone succesful!\n")

    subprocess.run(["git", "checkout", NUM_COMMIT])

def build_test():
    try:
        script_path = "/tmp/github/test/test.py"
        try:
            result = subprocess.run(["pytest", script_path], capture_output=True, text=True, check=True)
        except:
            print("Les tests ne sont pas bon !")
            build_test_fail()
        # Affichez la sortie standard du script
        print(result.stdout)

        if result.returncode == 0:
            print("les tests sont bon pour le master !")
            build_test_good()


    except subprocess.CalledProcessError as e:
        # En cas d'erreur lors de l'exécution du script
        print(f"Erreur lors de l'exécution du script : {e}")
    except FileNotFoundError as e:
        # En cas de fichier introuvable
        print(f"Fichier introuvable : {e}")
    except Exception as e:
        # En cas d'autres erreurs
        print(f"Erreur inattendue : {e}")
    
def build_test_good():
    subprocess.run(["git", "checkout", "main"], check=True)
    subprocess.run(["git", "pull"], check=True)
    subprocess.run(["git", "merge", NUM_COMMIT, "--ff-only"], check=True)
    print("\nLe code dev est bien merge dans main !")
    subprocess.run(["rm", "-rf", PATH_CLONE])

def build_test_fail():
    try:
        # Générez un nom de branche basé sur la date et l'heure actuelles
        now = datetime.now()
        branch_name = f"failure/{now.strftime('%Y-%m-%d_%H-%M-%S')}"

        # Créez la nouvelle branche localement
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)

        # Poussez la nouvelle branche vers le référentiel distant (GitHub)
        subprocess.run(["git", "push", "origin", branch_name], check=True)

        print(f"Branche '{branch_name}' créée et poussée avec succès sur GitHub.")
        subprocess.run(["rm", "-rf", PATH_CLONE])

    except subprocess.CalledProcessError as e:
        print(f"Erreur Git : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


git()
build_test()
