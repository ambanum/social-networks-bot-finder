# What is a bot ? 

Defining what counts as a bot account is not as direct as it seems. For instance, some accounts are sometimes used by bots and sometimes by humans; these accounts are called cyborg and further complicate the definition.
In this work we do not try to define what a bot account is (many attempts have already been made in the scientific literature). 
We consider as a bot the accounts marked as so in the bot repository of the Indiana University (https://botometer.osome.iu.edu/bot-repository/datasets.html). We then classify a Twitter account according to how similar it is to these accounts, based on several features detailed below.

# How does the bot probability score work ?

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
- followers_friends_ratio : number of followers per friend - this is equal to followers_count/(friends_count+1) (the redundancy with the friends_followers_ratio feature is intentional : the reason being that if the number of friends is dwarfed by the number of followers, the friends_followers_ratio vanishes and this information would be more schematic).


Based on the features observed in the data, we follow the Random Forest classifier algorithm : we creates several (in our case 250) Decision Trees (https://en.wikipedia.org/wiki/Decision_tree_learning) to help us classify unknown (that is : unlabeled) Twitter accounts. Each Decision Tree is trained using only a subset of the training data (this technique is called _bootstrap aggregating_). 

When computing the class of an account using a single Decision Tree, the account is assigned to a specific leaf in the decision tree : its class probability of being a bot is then the number of bot training samples which were assigned this leaf over the total number of training samples which were assigned this leaf.

The probability that an account is a bot is then computed as the average of the class probability of the account for all the different decision trees. 
