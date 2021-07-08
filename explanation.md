# What is a bot ? 

Defining what counts as a bot account is not as direct as it seems. For instance, some accounts are sometimes used by bots and sometimes by humans; these accounts are called cyborg and further complicate the definition.
In this work we do not try to define what a bot account is (many attempts have already been made in the scientific literature). 
We consider as a bot the accounts marked as so in the bot repository of the Indiana University (https://botometer.osome.iu.edu/bot-repository/datasets.html). We then classify a Twitter account according to how similar it is to these accounts, based on several features detailed below.

## How does the bot probability score work ?

To compute the probability for an account to be a bot, we train a Random Forest classifier on the data aggregated from the bot repository, which is available (as a csv file) in DatasetConsolidated.zip in this repository.

We use 21 different features : 
- statuses_count : the number of statuses (tweets) posted by the account 
- followers_count : the number of followers of the account
- favourites_count : the number of tweets the account has marked as favourite
- friends_count : the number of friends (following accounts) this account has
- listed_count : the number of public list this account is member of
- default_profile : whether the account has uploaded a new profile image or uses the default image instead
- profile_use_background_image : whether the account has uploaded a new background image
- verified : whether the account has been verified by the Twitter team
- age : the age (in days) of the account (this is rounded to the upper number so that there is no dividing by zero for the subsequent features)
- name_length : the length (in number of characters) of the name (which is @name) of the account
- screenname_length : the length (in number of characters) of the screen name (which is the name that is most visible) of the account
- name_digits : the number of digits in the name (which is @name) of the account
- screen_name_digits : the number of digits in the screen name (which is the name that is most visible) of the account
- description_length : the length (in number of characters) of the account description
- tweet_frequence : the growth rate of the tweets (statuses) posted - this is equal to : statuses_count/age
- followers_growth_rate : the growth rate of followers acquired - this is equal to : followers_count/age
- favourites_growth_rate : the growth rate of tweets favorited - this is equal to : favourites_count/age
- friends_growth_rate : the growth rate of friends acquired - this is equal to : friends_count/age
- listed_count_growth_rate : the growth rate of list - this is equal to : listed_count/age
- friends_followers_ratio : number of friends per follower - this is equal to friends_count/(followers_count+1)
- followers_friends_ratio : number of followers per friend - this is equal to followers_count/(friends_count+1)


Based on the features observed in the data, we follow the Random Forest classifier algorithm : we creates several (in our case 250) Decision Trees (https://en.wikipedia.org/wiki/Decision_tree_learning) to help us classify unknown (that is : unlabeled) Twitter accounts. Each Decision Tree is trained using only a subset of the training data (this technique is called _bootstrap aggregating_).

When computing the class of an account using a single Decision Tree, the account is assigned to a specific leaf in the decision tree : its class probability of being a bot is then the number of bot training samples which were assigned this leaf over the total number of training samples which were assigned this leaf.

**The probability that an account is a bot is then computed as the average of the class probability of the account for all the different decision trees.**

## Example

Suppose for instance that an account has an abnormally high tweet frequence. In the training dataset some accounts also have this particularity and are labeled as "bot". During the building of the random forest, some Decision Tree will be created that uses the tweet_frequence feature to assign a bot label to the accounts that have a high tweet_frequence feature. 

When we have ended the training phase we now have a forest of Decision Trees. We pick an account for which we want to have a probability. For each of the Decision Tree in our forest, the account will follow the different nodes of the tree up to a specific leaf in the tree. This leaf will be labeled either "bot" or "human" and it will have a probability for each of these labels. The probability of the label "bot" is equal to how many training examples of 'bot' account ended up in this leaf divided by the total number of training examples, whether they are labeled 'bot' or 'human', that ended up in this leaf. The same process hapens for the label "human".

Because many Decision Trees inside our forest have used the tweet_frequence feature as an important piece of information to classify whether some accounts are bot or not, they will classify our unknown Twitter account as being a 'bot', unless some other features points towards the fact that the account is genuine : for instance the account could be verified by twitter.

To obtain the final probability that the account is a bot, we compute the average of the probability obtained by each Decision Tree and we are done !

---

## Qu’est-ce qu’un bot ?

Etiqueter un compte comme « bot » est plus complexe qu’il n’y paraît. Certains comptes sont tour à tour utilisés par des bots et par des humains; ces comptes, baptisés cyborgs, viennent complexifier encore davantage la détection d’un bot pur et simple. En l’espèce, nous nous sommes ainsi abstenus d’élaborer la définition d’un bot – de nombreuses tentatives ont déjà été initiées à cet effet et figurent dans la littérature scientifique.
Nous considérons comme bots les comptes marqués comme tels dans le bot repository de l’Université d’Indiana (https://botometer.osome.iu.edu/bot-repository/datasets.html). Nous qualifierons un compte Twitter de bot en fonction de sa similarité avec ces comptes, sur la base de plusieurs caractéristiques détaillées ci-dessous.

## Comment fonctionne le score de probabilité d’être un bot ?

Pour calculer la probabilité d’un compte donné d’être un bot, nous entraînons une forêt d’arbres de décisions sur les données agrégées par le bot repository.
21 caractéristiques différentes sont utilisées :
- statuses_count : le nombre de statuts (tweets) postés par le compte
- followers_count : le nombre d’abonnés du compte
- favourites_count : le nombre de tweets marqués comme favoris par le compte
- friends_count : le nombre de comptes suivis par le compte étudié
- listed_count : le nombre de listes publiques dont le compte est membre
- default_profile : le fait que le compte ait chargé une nouvelle image de profil ou choisi de s’en remettre à l’image définie par défaut
- profile_use_background_image : le fait que le compte ait chargé, ou non, une image de bannière
- verified : le fait que le compte ait obtenu, ou non, une certification Twitter
- age: l’âge, en jours, du compte – ce dernier est arrondi au nombre supérieur pour éviter toute éventuelle division par zéro
- name_length : la longueur, en nombre de caractères, du nom d’utilisateur (@nom) du compte
- screenname_length : la longueur, en nombre de caractères, du nom d’affichage du compte - name_digits : le nombre de chiffres contenus dans le nom d’utilisateur (@nom)
- screen_name_digits : le nombre de chiffres contenus dans le nom d’affichage
- description_length : la longueur, en nombre de caractères, de la description d’un compte
- tweet_frequence : la fréquence à laquelle tweete un compte – à savoir le ratio nombre de tweets/âge du compte
- followers_growth_rate : le taux de croissance du nombre d’abonnés – à savoir le ratio nombre de followers/ âge du compte
- favourites_growth_rate : le taux de croissance du nombre de tweets marqués comme favoris – à savoir le ratio nombre de tweets marqués comme favoris/âge du compte
 
- friends_growth_rate : le taux de croissance du nombre d’abonnements – à savoir le ratio nombre d’abonnements/ âge du compte
- listed_count_growth_rate : le taux de croissance du nombre de listes auxquelles appartient le compte – à savoir le ratio nombre de listes/ âge du compte
- friends_followers_ratio : le ratio nombre d’abonnements/(nombre d’abonnés +1) 
- followers_friends_ratio : le ratio nombre d’abonnés/(nombre d’abonnements +1)

Sur la base des caractéristiques observées dans les données, nous suivons l'algorithme de classification Random Forest : nous créons plusieurs (dans notre cas 250) arbres de décision (https://en.wikipedia.org/wiki/Decision_tree_learning) pour nous aider à classer les nouveaux comptes Twitter non étiquetés. Chaque arbre de décision est entraîné en utilisant seulement un sous-ensemble des données (une technique qui porte le nom de _bootstrap aggregating_).

Lorsque l'on calcule la classe d'un compte en utilisant un seul arbre de décision, le compte est assigné à une feuille spécifique de l'arbre de décision : sa probabilité d'être un bot est alors le nombre d'échantillons pour l'entraînement des bots qui ont été assignés à cette feuille sur le nombre total d'échantillons pour l'entraînement ayant été assignés à cette feuille.

**La probabilité qu'un compte soit un bot est alors calculée comme la moyenne de la probabilité de classe du compte pour tous les différents arbres de décision.**

## Exemple

Supposons par exemple qu'un compte ait une fréquence de tweet anormalement élevée. Dans l'ensemble de données d'apprentissage, certains comptes présentent également cette particularité et sont étiquetés comme "bot". Pendant la construction de la forêt aléatoire, un arbre de décision sera créé et utilisera la caractéristique de fréquence des tweets pour attribuer une étiquette "bot" aux comptes qui ont une caractéristique de fréquence des tweets élevée.

À la fin de la phase de formation, nous avons maintenant une forêt d'arbres de décision. Nous choisissons un compte pour lequel nous voulons avoir une probabilité. Pour chacun des arbres de décision de notre forêt, le compte suivra les différents nœuds de l'arbre jusqu'à une feuille spécifique de l'arbre. Cette feuille sera étiquetée "bot" ou "human" et aura une probabilité pour chacune de ces étiquettes.

La probabilité de l'étiquette "bot" est égale au nombre d'exemples d'apprentissage du compte "bot" qui ont abouti dans cette feuille, divisé par le nombre total d'exemples d'apprentissage, qu'ils soient étiquetés "bot" ou "humain", qui ont abouti dans cette feuille. Le même processus se produit pour l'étiquette "human".

Parce que de nombreux arbres de décision dans notre forêt ont utilisé la caractéristique tweet_frequence comme un élément d'information important catégoriser certains comptes comme bots ou non, ils classeront notre compte Twitter inconnu comme étant un "bot", à moins que d'autres caractéristiques indiquent que le compte est authentique : par exemple, une certification Twitter.
