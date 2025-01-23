from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import winsound  # Pour l'alerte sonore sur Windows

# Configuration du navigateur Selenium (mode headless pour ne pas afficher le navigateur)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL de la billetterie
url = "https://ticketchange.24h-lemans.com/content"

# Sélecteur CSS précis pour le produit spécifique
product_id = "10229247452868"
sold_out_selector = f"div.stx-SoldOutIndicator[id='{product_id}']"

def check_availability():
    driver.get(url)
    time.sleep(5)  # Attendre le chargement de la page

    try:
        # Vérifier la présence de l'élément "ÉPUISÉ" spécifique au produit
        driver.find_element(By.CSS_SELECTOR, sold_out_selector)
        print("❌ Place Toujours épuisé pour beausejour")
    except NoSuchElementException:
        # Si l'élément n'est plus trouvé, une place est disponible !
        print("🚨 PLACE DISPONIBLE POUR Beausejour ! 🚨")
        winsound.Beep(1000, 500)  # Émettre un bip sonore sur Windows
        return True  # Arrêter la boucle si une place est dispo
    
    return False  # Continuer la surveillance

# Vérification en boucle toutes les 1.30 minutes
while True:
    if check_availability():
        break  # Arrêter le script si une place est dispo
    time.sleep(90)  # Attendre 1.5 minutes avant de revérifier
