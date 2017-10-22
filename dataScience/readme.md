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

|          Country | Number of Critic Badge Holders|
|----------------- | -----------------------------|
|   United States  |                            14|
|         Germany  |                             8|
|  United Kingdom  |                             6|
|           India  |                             6|
|          France  |                             3|
|         Belgium  |                             2|
|          Turkey  |                             2|
|           Spain  |                             2|
|       Singapore  |                             2|



*Country wise Revival Badge Holders*

|           Country | Number of Revial Badge Holders|
| ----------------- |------------------------------|
|    United States  |                            12|
|            India  |                            10|
|          Germany  |                            10|
|   United Kingdom  |                             5|
|  Between 0 and 1  |                             3|
|  Series of tubes  |                             3|
|          Romania  |                             3|



*Country wise Scholar Badge Holders*

|           Country  | Number of Scholar Badge Holders|
|--------------------|--------------------------------|
|    United States    |                           22|
|           India     |                          20|
|   United Kingdom    |                          10|
|         Germany     |                          10|
|           Russia    |                            7|
|             Iran    |                            6|
|           Israel    |                            6|
|           France    |                            5|
|        Australia    |                            5|
|        Singapore    |                            3|
|         HongKong    |                            3|
|      Netherlands    |                            3|
|           China     |                           3|



*Country wise Citizen Patrol Badge Holders*

|          Country  | Number of Citizen Patrol Badge Holders|
|------------------- | ------------------------------------ |
|  United Kingdom   |                                   10|
|         Germany   |                                    7|
|   United States   |                                    6|
|          France   |                                    6|
|           India   |                                    3|
|          Poland   |                                    3|
|         Belgium   |                                    3|


##### Most Popular Tags Used in Posts

|Tag| Number of Appearance |
|---|--------------------- |
| \<machine-learning\> |                   92|
| \<r\>                |                  58|
| \<neuralnetwork\>    |                  48|
| \<machine-learning\>\<neuralnetwork\>  |  41|
| \<classification\>   |                  28|
| \<data-mining\>      |                  27|


##### Source Code & Output
* Country wise comparison source code is [here](https://github.com/mohitsh/seDataDump/tree/master/dataScience/badgeAnalysis)
* All the resulting plots are [here](https://github.com/mohitsh/seDataDump/tree/master/dataScience/plots)
* Only one Recepient badge holder source code is [here](https://github.com/mohitsh/seDataDump/blob/master/dataScience/badgeAnalysis/ds_onlyOneRecepient.py)

