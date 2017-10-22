#### Data Science Exchange Data Dump


#### Part 1

>Analysis of [data science exchange](https://datascience.stackexchange.com) data dump. First part of the analysis is based on [badges](https://datascience.stackexchange.com/help/badges) awarded by DS Exchange.

##### Badge Description 

|Badge|Property|
|-----|--------|
| Scholar    | Ask a question and accept an answer        |
| Critic    |  First down vote        |
| Revival    | Answer more than 30 days after a question was asked as first answer scoring 2 or more       |
| Citizen Patrol    |  First flagged post       |

##### Analysis Pipeline
* Badges awarded by the data science exchange are are analyzed in this part
* Goal is to find coutry wise badge recepients
* Not all of the coutries have been considered (ofcourse). Instead top 8-14 coutires have been selected dependent on data.
* A threshold value (typically 3) has been used for number of award recepients per country




##### Badges with Only One Recepient

|Badge|User Name|Location|Reputation
|-----|--------|---------|----------|
| [Inquisitive](https://datascience.stackexchange.com/help/badges/88/inquisitive) | Martin Thoma | Karlsruhe, Germany | 2314|
| [Stellar Question](https://datascience.stackexchange.com/help/badges/36/stellar-question)  | Amir Ali Akbari | Tehran, Iran | 740 |
| [Synonymizer](https://datascience.stackexchange.com/help/badges/72/synonymizer)   |Sean Owen | United Kingdom | 2931 |


*Country wise Critic Badge Holders*

*Country wise Revival Badge Holders*

*Country wise Scholar Badge Holders*

*Country wise Citizen Patrol Badge Holders*



##### Source Code & Output
* Country wise comparison source code is [here](https://github.com/mohitsh/seDataDump/tree/master/dataScience/badgeAnalysis)
* All the resulting plots are [here](https://github.com/mohitsh/seDataDump/tree/master/dataScience/plots)
* Only one Recepient badge holder source code is [here]()

