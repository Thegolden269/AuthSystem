# 🔐 AuthSystem – Système d'authentification avec Django & Djoser

Bienvenue dans AuthSystem, un projet simple et moderne qui met en place un **système d'authentification complet** en utilisant **Django Rest Framework** (DRF), **Djoser** et **React**.

Ce projet peut servir de base solide pour toute application web qui nécessite une gestion des utilisateurs sécurisée via une API.

---

## 🚀 Fonctionnalités

- Création de compte avec confirmation par e-mail
- Connexion / Déconnexion via tokens JWT
- Rafraîchissement automatique des tokens
- Réinitialisation du mot de passe par e-mail
- Modification du mot de passe
- Modification de l’adresse e-mail avec confirmation
- Consultation et modification du profil utilisateur

---

## 🛠️ Technologies utilisées

### Backend (API)

- Python / Django
- Django REST Framework
- Djoser
- SimpleJWT


## Routes Front

Méthode	URL	
- POST	/auth/users/	Création de compte

- POST	/auth/users/activation/	Activation du compte via e-mail

- POST	/auth/token/logout/	Déconnexion (blacklist du token)

- GET	/users/me/	Récupérer les infos du profil

- PUT	/users/me/	Modifier les infos du profil

- POST	/auth/users/reset_password_confirm/	Confirmation de réinitialisation mdp

- POST	/set_password/	Modification du mot de passe
- 

---


