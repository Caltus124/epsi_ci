import subprocess
import os

# https://github.com/Caltus124/epsi_ci.git
# main
#  e4910b6

def git():
    os.system('clear')
    NUM_URL = input("Sélctionner une URL de repot : ")
    NUM_COMMIT = input("Selectionner le numéro du commit : ")
    PATH_CLONE = "/tmp/github/"
    
    os.system('clear')
    
    subprocess.run(["rm", "-rf", PATH_CLONE])
    subprocess.run(["git", "clone", NUM_URL, PATH_CLONE])
    
    print("\nClone succesful!\n")

    subprocess.run(["git", "checkout", NUM_COMMIT])

def build_test():
    script_path = "/tmp/github/test/test.py"
    result = subprocess.run(["pytest", script_path], capture_output=True, text=True, check=True)

    # Affichez la sortie standard du script
    print(result.stdout)

    if result.returncode == 0:
        print("les tests sont bon pour le master !")
    else:
        print("erreur")


git()
build_test()