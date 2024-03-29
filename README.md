# Restaurant-Chatbot - Mukul Dev
Restaurant chatbot developed using RASA NLU and python 3.


## Trained Models 
- Latest Trained model Model -> **models/20210601-004834.tar.gz**  


## Pre-requisites

- python 3.7.9
- rasa 2.6.0
- spacy 3.0.6
- en_core_web_md 3.0.0
- Dependency Requirement File can be found here `req.txt`


### Data Files

- **data/nlu/nlu.md** : contains training examples for the NLU model  
- **data/core/stories.md** : contains training stories for the Core model  

### Config Files

- **config.yml** contains model configuration and custom policy
- **domain.yml** defines chatbot domain like entities, actions, templates, slots  
- **endpoints.yml** contains the webhook configuration for custom action

## Bot Snapshots
### Sample conversation GIF
[![asciicast](https://asciinema.org/a/BRiwfvf6e2EyXKGbsCzjs9xhZ.svg)](https://asciinema.org/a/BRiwfvf6e2EyXKGbsCzjs9xhZ)

### Sample conversation Snapshot
![image](https://user-images.githubusercontent.com/15700993/120261991-40698300-c2c3-11eb-83e9-54bff87c0e99.png)

### Email sent by bot:
![image](https://user-images.githubusercontent.com/15700993/120262060-6131d880-c2c3-11eb-960f-5e17b89ecc94.png)


## Installation

#### create new env
```conda create -n rasa python==3.7.9```

#### Activate env:
```conda activate rasa```

#### Install Requirements
```pip install -r req.txt```

## RASA Commands 

### train nlu
```rasa train nlu```

### test nlu
```rasa shell nlu```

### train both nlu & core
```rasa train```

### start action server
```rasa run actions```

### test models
```rasa shell```

### create new training data interactively
```rasa interactive```
