# BadgeuseDokos
Système de badge pour espace de coworking basé sur Dokos. Utilisation d’un lecteur RFID branché à un Raspberry et intégration dans l’ERP du lieu (ici DOKOS).

Plus d'informations : https://movilab.org/wiki/Syst%C3%A8me_de_badge_basé_sur_Dokos


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

Quand les commandes ont fini de s'exécuter vous pouvez essayer d'exécuter la commande nfc-poll pour savoir si l’installation s’est faite avec succès. Si jamais un message apparaît disant que “nfc-poll : commande introuvable” c’est que l’installation n’a pas réussi.
Dès que ces commandes sont faites, l'installation des logiciels pour utiliser le lecteur NFC est réalisée

## Lancement automatique de la badgeuse

Déplacez le dossier "lancement.sh" à la racine du dossier /home.
Pour que la fenêtre de la badgeuse s’affiche automatiquement au démarrage de la Raspberry : 
Dans un terminal, lancez la commande « sudo nano /etc/xdg/lxsession/LXDE-pi/autostart ».
Sous la dernière ligne (« @xscreensaver… »), rajoutez la ligne de code « @/home/pi/lancement.sh ». Sauvegardez et quittez le document.


## Configuration pour accéder à votre Dokos

Une fois que l’installation est réalisée, il faut configurer le logiciel de badgeuse pour pouvoir se connecter à Dokos. Il y a besoin de plusieurs choses
pour pouvoir se connecter à Dokos. 

Ces informations seront à mettre dans le fichier config.py :


- Dans un premier temps, vous devez accéder au serveur dokos avec l’user Administrator à partir de votre navigateur web. Une fois cela fait accéder aux
utilisateurs pour cela tapez “Utilisateur Liste” dans la barre de recherche ensuite une fois arriver dans la liste des utilisateurs.

Allez voir l’utilisateur Administrator en cliquant dessus, une fois sur la page de l'utilisateur descendez la page jusqu’à arriver à Accès API, cliquer sur le texte pour voir apparaître le bouton “Générer des clés”

Cliquez sur ce bouton pour avoir les clés. Dans un premier temps vous allez voir apparaître un message dans une fenêtre au-dessus du site web avec la clé
à mettre dans “dokos_token” du fichier config.py.

- Ensuite vous allez apercevoir dans la page web la clé à mettre dans “dokos_client” cette clé est la case clé API

- Pour remplir la ligne “api_url” du fichier config.py il suffit de taper l’URL du site par lequel vous accédez à votre serveur dokos (par exemple https://
monsitedokos.fr) et ensuite de placer un /api (par exemple https://monsitedokos.fr/api) après cette URL. 


# Configuration de DOKOS pour activer l'API 

Code modifié sur Dokos (pour les développeurs)
https://github.com/Elronde62/Dokos-badge-management

Pour les non développeurs, vous pouvez ajouter manuellement les Doctypes dans Dokos
