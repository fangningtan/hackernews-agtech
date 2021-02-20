# hackernews-agtech
The purpose of this project was to analyse the coverage of agricultural technology (aka agritech) on Hacker News over the past 10 years. Through this first data science project, I aimed to familiarise myself with working with SQL, data science libraries in Python, and git.

#### -- Project Status: [Active]

### Methods used
* Term Frequency-Inverse Document Frequency (TDIDF)
* K-means clustering

### Technologies
* Python (libraries: pandas, numpy, matplotlib, sklearn, scipy)
* Jupyter notebook
* SQL (BigQuery API)

### Process 
1. Introduction to the BigQuery API to query the public HN dataset
2. Using bigrams to identify more relevant stories
3. K-means clustering of data

The main steps in the project correspond to the notebooks in this repository.

### Learning points
This exercise in k-means clustering of headlines was not very successful because of the limitations of the dataset I chose:
* Dataset with 375 rows might not be sufficientlly large to perform clustering (some recommend using smaples sizes of >500). With small datasets, the number of clusters you aim to get will generally be much smaller than the number of variables you use as input, which increases the risk of spurious groupings.
* Dataset might not be sufficiently varied in terms of themes.
* Titles of the HN stories are quite sparse, making them more challenging to cluster compared to longer texts.  

Nonetheless, this exercise still allowed me examine the concepts of text clustering (td-idf, k-means algorithm, silhouette coefficient) in greater detail, which will help me in future text clustering projects. Furthermore, I got to practice other often overlooked skills such as  managing virtual environments, installing packages, version control that are integral to carrying data science projects.  

Setting up my own data science project, in contrast to following a designed tutorial, gave me a taste of how the process of obtaining, processing and analysing real world data can be messy and not straightforward, thus requiring pivots along the way. Still, the completion of this small project gives me confidence to embark on exploring other topics of interest through data.