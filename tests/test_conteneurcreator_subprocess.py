# tests/test_conteneurcreator_subprocess.py
import subprocess
import sys
import platform
import pytest

def docker_installed():
    """Vérifie si Docker est installé."""
    try:
        result = subprocess.run(
            ["docker", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return True, result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, ""

def test_detect_os():
    """Teste la détection du système d'exploitation."""
    result = subprocess.run(
        [sys.executable, "conteneurcreator.py"],
        capture_output=True,
        text=True
    )
    expected_os = platform.system()
    assert f"Vous êtes sur {expected_os}." in result.stdout, (
        f"Attendu : Vous êtes sur {expected_os}., Obtenu : {result.stdout}"
    )

def test_check_docker_installed():
    """Teste la vérification de l'installation de Docker."""
    docker_present, docker_version = docker_installed()
    result = subprocess.run(
        [sys.executable, "conteneurcreator.py"],
        capture_output=True,
        text=True
    )
    if docker_present:
        assert "Docker est installé." in result.stdout, (
            "Le script devrait indiquer que Docker est installé."
        )
    else:
        assert "Docker n'est pas installé." in result.stdout, (
            "Le script devrait indiquer que Docker n'est pas installé."
        )

def test_create_container():
    """Teste la création d'un conteneur Docker."""
    docker_present, _ = docker_installed()
    if docker_present:
        result = subprocess.run(
            [sys.executable, "conteneurcreator.py"],
            capture_output=True,
            text=True
        )
        # On suppose que le script tente de créer un conteneur 'hello-world'
        assert (
            "Conteneur créé avec succès." in result.stdout or
            "Échec de la création du conteneur." in result.stdout
        ), "Le script devrait essayer de créer un conteneur."
    else:
        pytest.skip("Docker n'est pas installé. Skipping container creation test.")
