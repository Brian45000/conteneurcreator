# tests/test_conteneurcreator_subprocess.py
import subprocess
import sys
import platform
import pytest

def test_detect_os():
    # Exécuter le script avec un argument spécifique pour tester la détection de l'OS
    result = subprocess.run([sys.executable, "conteneurcreator.py", "--detect-os"], capture_output=True, text=True)
    expected_os = platform.system()
    assert expected_os in result.stdout, f"Attendu : {expected_os}, Obtenu : {result.stdout}"

def test_check_docker_installed():
    # Exécuter le script avec un argument spécifique pour tester la vérification de Docker
    result = subprocess.run([sys.executable, "conteneurcreator.py", "--check-docker"], capture_output=True, text=True)
    if docker_installed():
        assert "Docker est installé." in result.stdout
    else:
        assert "Docker n'est pas installé." in result.stdout

def test_create_container():
    # Exécuter le script avec un argument spécifique pour tester la création de conteneur
    image_name = "hello-world"
    result = subprocess.run([sys.executable, "conteneurcreator.py", "--create-container", image_name], capture_output=True, text=True)
    if docker_installed():
        assert "Conteneur créé avec succès." in result.stdout
    else:
        assert "Docker n'est pas installé." in result.stdout

def docker_installed():
    """Fonction utilitaire pour vérifier si Docker est installé sur le système."""
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
