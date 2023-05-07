This repository contains a comprehensive set of files and models used for classifying the time range during which an airdrop token is sold off by a wallet after a specific period of time. The training samples used in the analysis were obtained from the Optimism Airdrop 2 dataset. Below is a detailed guide to the files within the repository:

- `classified_data`: This file contains labeled data from the Optimism Airdrop 2 dataset and DeepDao's List 1 and 2, based on their respective sell-off dates.

- [**data**](https://github.com/franfran20/airdrop_analysis/tree/main/data): This file contains unprocessed and unlabeled raw data.

- [**deepdao_metrics**](https://github.com/franfran20/airdrop_analysis/tree/main/deepdao_metrics): This file contains account information associated with the addresses from List 1 and List 2 provided by DeepDao.

- [**queried_data**](https://github.com/franfran20/airdrop_analysis/tree/main/queried_data): This file contains data obtained from specific addresses queried using the Etherscan API, including List 1, List 2, training and testing data.

- [**report**](https://github.com/franfran20/airdrop_analysis/blob/main/report.pdf): This file contains a comprehensive summary of the analysis, including the findings and methodology employed.

- [**on_chain_analysis.ipynb**](https://github.com/franfran20/airdrop_analysis/blob/main/on_chain_analysis.ipynb): This is a Jupyter notebook file containing code for querying specific wallet details from Ethereum addresses.

- [**model_weights.zip**](https://github.com/franfran20/airdrop_analysis/blob/main/model_weights.zip): This file contains saved weights for the wallet classifier model.

- [**Modelling.ipynb**](https://github.com/franfran20/airdrop_analysis/blob/main/Modelling.ipynb): This is a Jupyter notebook file containing code used for feature engineering and modeling.

- [**DDA.ipynb**](https://github.com/franfran20/airdrop_analysis/blob/main/Analysist.ipynb): This is a Jupyter notebook file containing code for data analysis on the addresses provided in DeepDao's List.

- [**Classifier.py**](https://github.com/franfran20/airdrop_analysis/blob/main/Classifier.py): This is a Python script used for running the classification model. It takes in an Ethereum address and outputs the likely sell date.
