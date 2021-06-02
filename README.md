# BadgeuseDokos
Système de badge pour espace de coworking basé sur Dokos. Utilisation d’un lecteur RFID branché à un Raspberry et intégration dans l’ERP du lieu (ici DOKOS).

Plus d'informations : https://movilab.org/wiki/Syst%C3%A8me_de_badge_bas%C3%A9_sur_Dokos


# Installation : 

## Préparation de la Raspberry 

Connectez l’écran, le clavier, la souris, le lecteur de badge, la carte SD sur la Raspberry et activez l’alimentation. La Raspberry devrait se lancer après quelques secondes. Assurez-vous que le lecteur de badge soit connecté au bon port USB (de préférence le port bleu supérieur).

## Configuration de la Raspberry

Configurez la langue, le type de clavier, la timezone, l’heure, la date, la LAN zone, le réseau Wi-Fi et la taille de l’écran dans les paramètres de la Raspberry (onglet Préférences).

## Formater la carte SD
Formatez la carte SD
Commencez par formater la carte SD de la Raspberry via votre ordinateur. (Sur Windows,  utiliser le logiciel SD Card Formatter, téléchargeable sous le lien suivant : https://sd-card-formatter.fr.uptodown.com/windows)

Si vous comptez utiliser le petit écran, il faut écrire, sur la carte SD, une image permettant à la Raspberry de reconnaître l’écran. Pour cela, sur Windows, téléchargez le logiciel WIN32DiskImager, téléchargeable au lien suivant : https://sourceforge.net/projects/win32diskimager/

L’image à écrire sur la carte SD est téléchargeable au lien suivant :
https://mega.nz/folder/6uR0SYLS#t4DJRQLX6F-Uv-i7jCaCKQ


## Importation des documents
Ajoutez le dossier git dans le dossier /home/pi :

Commande  : git clone https://github.com/CommonsDev/BadgeuseDokos.git 

## Installation du lecteur NFC

Assurez-vous que le lecteur de badge soit bien connecté au bon port USB (leport bleu supérieur). Vous pouvez vérifier que la Raspberry reconnaisse le lecteur en tapant la commande « lsusb » dans un terminal. Cette commande permet de lister tous les périphériques USB connectés.

Une fois le lecteur de badge bien connecté et reconnu par la Raspberry, exécutez le document « InstallNFCDevice.sh » via un terminal grâce à la commande « sudo bash InstallNFCDevice.sh ». Confirmez par O ou Y sur le terminal lorsque cela est requis. Le processus prend quelques minutes.

## Lancement automatique de la badgeuse

Déplacez le dossier "lancement.sh" à la racine du dossier /home.
Pour que la fenêtre de la badgeuse s’affiche automatiquement au démarrage de la Raspberry : 
Dans un terminal, lancez la commande « sudo nano /etc/xdg/lxsession/LXDE-pi/autostart ».
Sous la dernière ligne (« @xscreensaver… »), rajoutez la ligne de code « @/home/pi/lancement.sh ». Sauvegardez et quittez le document.


# Configuration de DOKOS pour afficher l'API 

Code modifié sur Dokos (pour les développeurs)
https://github.com/Elronde62/Dokos-badge-management

Pour les non développeurs, vous pouvez ajouter manuellement les Doctypes dans Dokos
