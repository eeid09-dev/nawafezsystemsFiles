# Happy Fatora : Conditions d'utilisation et Politique de confidentialité

**Dernière mise à jour :** 14 novembre 2026  
**Version :** 1.1.0

Happy Fatora (« l'Application », « nous ») est une application de gestion de point de vente (POS) et de facturation développée par **Nawafez Systems for Software Solutions** (« Nawafez Systems »). Ce document contient à la fois les Conditions d'utilisation et la Politique de confidentialité. En installant ou en utilisant l'Application, vous acceptez les deux.

---

## 1. Acceptation des conditions

En téléchargeant, en installant ou en utilisant l'Application, vous acceptez d'être lié par les présentes Conditions. Si vous n'êtes pas d'accord, n'utilisez pas l'Application.

Nous pouvons modifier ces Conditions à tout moment. En cas de modifications importantes, nous mettrons à jour la date de « Dernière mise à jour » et vous en informerons dans l'Application ou via la fiche Google Play. La poursuite de l'utilisation après les modifications vaut acceptation des Conditions modifiées.

Vous devez avoir au moins 18 ans pour utiliser l'Application.

## 2. Description du service

Happy Fatora est une application de point de vente et de facturation destinée aux entreprises. Elle vous permet de :

- Créer, gérer et imprimer des factures
- Gérer les produits, l'inventaire et les niveaux de stock
- Suivre les ventes, les achats et les retours
- Gérer les clients et les fournisseurs
- Générer et scanner des codes-barres et des codes QR
- Exporter des données (PDF, CSV, Excel)
- Suivre les dépenses et les dettes
- Générer des rapports et des statistiques financières
- Créer des sauvegardes locales et, en option, des sauvegardes sur votre propre Google Drive
- Personnaliser les modèles de factures

L'Application fonctionne sur Android (version 5.0 et supérieure) et stocke les données de votre entreprise localement sur votre appareil, dans une base de données SQLite.

## 3. Données que nous collectons et utilisation

### 3.1 Données professionnelles que vous saisissez

- Produits (nom, code-barres, prix, coût, stock, images)
- Clients et fournisseurs (nom, téléphone, adresse, solde)
- Factures et transactions
- Documents financiers (dépenses, dettes, paiements)
- Catégories et unités

Ces données sont stockées sur votre appareil. **Nous ne les recevons pas et nous ne les stockons pas sur nos serveurs.**

### 3.2 Données d'appareil et d'utilisation (automatiques)

- Modèle de l'appareil et version du système d'exploitation
- Version de l'Application
- Un identifiant d'appareil utilisé pour la licence
- Rapports de plantage, journaux d'erreurs et données de performance
- Identifiant publicitaire et données associées collectés par Google AdMob (version gratuite uniquement)

### 3.3 Comment nous utilisons les données

- Pour faire fonctionner les fonctionnalités principales de l'Application
- Pour générer des factures et des rapports
- Pour créer des sauvegardes et restaurer des données
- Pour corriger les bugs et améliorer les performances
- Pour vérifier votre licence
- Pour afficher des publicités dans la version gratuite (via Google AdMob)

### 3.4 Où les données sont stockées

- **Sur votre appareil :** toutes les données professionnelles sont stockées localement dans une base de données SQLite.
- **Sur votre Google Drive (facultatif) :** uniquement si vous activez la sauvegarde cloud, des copies de vos fichiers de sauvegarde sont stockées dans votre propre compte Google Drive (voir la section 4).
- **Sur nos serveurs :** nous ne stockons pas les données de votre entreprise sur nos serveurs.

### 3.5 Partage des données

Nous ne vendons pas vos données personnelles. Nous ne les partageons qu'avec :

- **Google AdMob**, pour l'affichage des publicités (version gratuite)
- **Google Drive**, uniquement si vous choisissez d'utiliser la sauvegarde cloud, et uniquement vers votre propre compte
- **Les autorités légales**, lorsque la loi l'exige

## 4. Sauvegarde cloud sur Google Drive (données utilisateur Google)

La sauvegarde cloud est facultative. Elle ne fonctionne que si vous vous connectez avec votre compte Google et accordez l'autorisation.

**Accès que nous demandons**

- `https://www.googleapis.com/auth/drive.file` : permet à l'Application de créer et de gérer uniquement les fichiers et dossiers qu'elle a elle-même créés dans votre Google Drive. L'Application ne peut pas voir, lire ni modifier d'autres fichiers de votre Drive.

**Ce que nous faisons avec cet accès**

- Créer un dossier nommé `HappyFatora_Backups` dans votre Google Drive
- Téléverser les fichiers de sauvegarde que vous créez (ou que votre paramètre de sauvegarde automatique crée)
- Lister, télécharger et supprimer les fichiers de sauvegarde créés par l'Application, afin que vous puissiez les restaurer ou les supprimer
- Lire l'adresse e-mail de votre compte Google pour afficher le compte connecté

**Ce que nous ne faisons pas**

- Nous ne lisons, n'analysons et n'accédons à aucun autre fichier de votre Drive.
- Nous n'envoyons pas vos données utilisateur Google ni vos fichiers de sauvegarde à nos serveurs ni à un tiers.
- Nous n'utilisons pas les données utilisateur Google à des fins publicitaires et nous ne les vendons pas.
- Personne chez nous ne lit vos fichiers de sauvegarde.

**Politique relative aux données utilisateur des services d'API Google.** L'utilisation par l'Application des informations reçues des API Google, et leur transfert à toute autre application, respectera la [Politique relative aux données utilisateur des services d'API Google](https://developers.google.com/terms/api-services-user-data-policy), y compris les exigences d'utilisation limitée (Limited Use).

**Déconnexion et suppression**

- Vous pouvez vous déconnecter de Google dans l'Application à tout moment. Cela déconnecte l'Application de votre Drive.
- Vous pouvez révoquer l'accès de l'Application à tout moment sur https://myaccount.google.com/permissions
- Les fichiers de sauvegarde restent dans votre Google Drive jusqu'à ce que vous les supprimiez. Vous pouvez les supprimer depuis l'Application ou directement depuis le dossier `HappyFatora_Backups` dans Google Drive.

**Note de sécurité.** Les fichiers de sauvegarde envoyés sur votre Google Drive sont protégés par la sécurité de votre compte Google. Il vous incombe de sécuriser votre compte Google.

## 5. Autorisations

L'Application demande les autorisations Android suivantes :

- **Appareil photo :** pour scanner les codes-barres et les codes QR
- **Stockage :** pour enregistrer les factures PDF, les sauvegardes et les exports
- **Internet :** pour afficher des publicités, effectuer la sauvegarde cloud et vérifier les mises à jour
- **Notifications :** pour envoyer des rappels de sauvegarde
- **Biométrie :** pour l'authentification facultative par empreinte digitale ou reconnaissance faciale

Chaque autorisation est utilisée uniquement pour la finalité indiquée. Vous pouvez refuser ou révoquer les autorisations à tout moment dans les paramètres de votre appareil. L'Application n'accède pas à vos contacts, SMS, journaux d'appels, position, microphone, ni aux données d'autres applications.

## 6. Publicités

La version gratuite affiche des publicités fournies par Google AdMob (bannières et publicités interstitielles). Nous ne contrôlons pas le contenu de ces publicités. AdMob peut utiliser l'identifiant publicitaire de votre appareil et d'autres informations sur l'appareil pour diffuser des publicités, comme décrit dans la [Politique de confidentialité de Google](https://policies.google.com/privacy).

Vous pouvez :

- Réinitialiser votre identifiant publicitaire ou désactiver la personnalisation des annonces dans les paramètres Google de votre appareil
- Supprimer les publicités en achetant une licence premium

## 7. Conservation et suppression des données

- **Données locales :** elles restent sur votre appareil jusqu'à ce que vous les supprimiez ou désinstalliez l'Application. La désinstallation de l'Application supprime la base de données locale.
- **Sauvegardes cloud :** elles restent dans votre Google Drive jusqu'à ce que vous les supprimiez.
- **Données sur nos serveurs :** nous ne détenons pas les données de votre entreprise, il n'y a donc rien à supprimer de notre côté.
- **Les données d'appareil et d'utilisation** collectées par des services tiers (comme AdMob) sont traitées selon les politiques et les durées de conservation propres à ces services.

Si vous avez des questions sur vos données, contactez-nous à l'adresse indiquée à la section 16.

## 8. Vos droits

Selon votre lieu de résidence, vous pouvez avoir le droit d'accéder à vos données, de les rectifier, de les supprimer ou de les exporter, et de vous opposer à certains traitements. Comme les données de votre entreprise se trouvent sur votre appareil et sur votre propre Google Drive, vous pouvez exercer la plupart de ces droits directement. Pour tout autre cas, contactez-nous et nous répondrons dans le délai prévu par la loi applicable.

## 9. Comportement de l'utilisateur et usage acceptable

Vous vous engagez à utiliser l'Application uniquement à des fins légales et dans le respect des réglementations fiscales et comptables, des lois de protection des consommateurs et des lois de protection des données qui vous sont applicables.

Vous ne devez pas utiliser l'Application pour :

- Générer des factures frauduleuses
- Échapper à l'impôt ou commettre une fraude financière
- Distribuer des logiciels malveillants
- Enfreindre une loi ou une réglementation

Vous êtes seul responsable de :

- Vous assurer que vos factures sont conformes aux réglementations locales
- Collecter et reverser les taxes applicables
- Tenir des registres financiers exacts
- Obtenir tout consentement requis pour stocker les données personnelles de vos propres clients et fournisseurs

## 10. Propriété intellectuelle

Happy Fatora et son contenu appartiennent au développeur et sont protégés par les lois sur le droit d'auteur et les marques.

Vous recevez une licence limitée, non exclusive, non transférable et révocable pour utiliser l'Application à des fins personnelles ou commerciales.

Vous ne pouvez pas :

- Copier, modifier ou faire de l'ingénierie inverse de l'Application
- Distribuer, vendre ou sous-licencier l'Application
- Supprimer les mentions de droit d'auteur
- Extraire le code source

Vous conservez l'entière propriété de toutes les données professionnelles que vous saisissez dans l'Application.

## 11. Licence et activation

L'Application peut être proposée sous les formes suivantes :

- **Version gratuite :** fonctionnalités limitées avec publicités
- **Version premium :** toutes les fonctionnalités avec une licence
- **Version d'essai :** toutes les fonctionnalités pour une durée limitée

Les licences sont liées à votre appareil (une licence pour un appareil), ne sont pas remboursables après utilisation sauf dans les cas prévus à la section 12, et ne peuvent pas être transférées sans autorisation.

## 12. Paiements et remboursements

Les licences premium peuvent être achetées via :

- Google Play (achat intégré)
- Achat direct d'une licence (lorsque disponible)

**Remboursements**

- Les achats effectués sur Google Play sont soumis à la politique de remboursement de Google Play.
- Les achats directs sont examinés au cas par cas dans un délai de 14 jours.
- Aucun remboursement n'est accordé pour les clés de licence utilisées ou après la période de remboursement, sauf si la loi en dispose autrement.

## 13. Services tiers

L'Application utilise :

- Les services Google Play
- Google AdMob (publicités)
- L'API Google Drive (sauvegarde cloud facultative)
- Google Fonts

Ces services ont leurs propres conditions et politiques de confidentialité. Nous ne sommes pas responsables de leurs pratiques.

## 14. Exclusions de garantie et limitation de responsabilité

L'APPLICATION EST FOURNIE « TELLE QUELLE », SANS GARANTIE D'AUCUNE SORTE.

Nous ne garantissons pas que l'Application répondra à vos besoins spécifiques, sera toujours disponible, sera exempte d'erreurs, ni que les données ne seront jamais perdues.

Dans la mesure maximale permise par la loi, nous ne sommes pas responsables des dommages indirects, consécutifs ou punitifs, de la perte de bénéfices ou d'opportunités commerciales, de la perte ou de l'altération de données, ni de l'interruption d'activité. Notre responsabilité totale ne dépassera pas le montant que vous avez payé pour la licence de l'Application (le cas échéant) au cours des 12 mois précédant la réclamation.

L'Application ne fournit pas de conseils juridiques, fiscaux ou comptables.

## 15. Responsabilité en matière de sauvegarde et perte de données

Il vous appartient de sauvegarder vos données. Nous vous recommandons vivement de :

- Créer régulièrement des sauvegardes locales
- Activer la sauvegarde cloud sur votre Google Drive
- Exporter périodiquement les données importantes

Nous ne sommes pas responsables de la perte de données causée par une panne, un dommage ou un vol de l'appareil, une erreur de l'utilisateur telle qu'une suppression accidentelle, des problèmes liés au système d'exploitation, ou des défaillances de services tiers. Rien dans cette section ne limite une responsabilité qui ne peut pas être limitée par la loi.

## 16. Nous contacter

Pour toute question, demande relative à la vie privée ou préoccupation :

- **Développeur :** Nawafez Systems for Software Solutions
- **E-mail :** info@nawafezsystems.com
- **Site web :** https://www.nawafezsystems.com
- **Dans l'Application :** Paramètres > Nous contacter

Nous nous efforçons de répondre dans un délai de 48 heures.

## 17. Confidentialité des enfants

L'Application est un outil professionnel destiné aux adultes âgés de 18 ans et plus. Elle n'est pas destinée aux enfants, et nous ne collectons pas sciemment de données personnelles auprès d'enfants. Si vous pensez qu'un enfant nous a fourni des données, contactez-nous et nous prendrons les mesures appropriées.

## 18. Résiliation

Vous pouvez cesser d'utiliser l'Application à tout moment en la désinstallant. Nous pouvons suspendre ou mettre fin à votre accès si vous enfreignez ces Conditions ou vous livrez à une activité frauduleuse.

Lorsque l'accès prend fin, votre licence est révoquée, les données locales restent sur votre appareil jusqu'à la désinstallation de l'Application, et les sauvegardes cloud restent dans votre Google Drive jusqu'à ce que vous les supprimiez.

## 19. Mises à jour et modifications de l'Application

Nous pouvons publier des mises à jour pour corriger des bugs, ajouter des fonctionnalités ou renforcer la sécurité. Nous pouvons modifier ou supprimer des fonctionnalités, et introduire des frais pour des fonctionnalités auparavant gratuites, moyennant un préavis.

## 20. Droit applicable et litiges

Les présentes Conditions sont régies par les lois de **[Votre pays]**. Avant d'engager un litige formel, veuillez nous contacter afin que nous puissions tenter de le résoudre à l'amiable.

## 21. Reconnaissance

En utilisant Happy Fatora, vous confirmez avoir lu et compris ces Conditions et cette Politique de confidentialité, vous acceptez d'être lié par celles-ci et vous vous engagez à respecter toutes les lois applicables.

---

© 2026 Happy Fatora. Tous droits réservés.
