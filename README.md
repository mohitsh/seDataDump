#### About


This project presents analysis of various data sets available at [Stack Exchange Data Dump](https://archive.org/details/stackexchange)

##### Data I/O
* Data Downloaded in zip form from [the soruce](https://archive.org/details/stackexchange)
* Unzipping data will typically produce eight xml files (Badges, Comments, PostHistory, PostLinks, Posts, Tags, Users, Votes)
* Storing xml data in sql database to facilitate further operatios [XML to SQL](http://mohitsh.github.io/2016-12-03/XML-to-SQL/)
* Once SQL database is populated, data I/O can be done using PyMySql and pandas (or any other medium) [MySql with Python](http://mohitsh.github.io/2016-11-25/MySql-with-Python/)

##### Footnotes
* Each stack exchnage data set should have one seperate data base with correspnoding tables (typically 8)
* There are various ways for data dump I/O. I have taken the above mentioned road.
* At the time of writing this Publication date of data dump: 2017-08-31


##### File Structure
* [Data Science Exchange](https://datascience.stackexchange.com/) data dump analysis
