import pandas as pd

""" +---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values] for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author] on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+ """

data = [
    ['1', '3', '5', '2019-08-01'],
    ['1', '3', '6', '2019-08-02'],
    ['2', '7', '7', '2019-08-01'],
    ['2', '7', '6', '2019-08-02'],
    ['4', '7', '1', '2019-07-22'],
    ['3', '4', '4', '2019-07-21'],
    ['3', '4', '4', '2019-07-21']
]

views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({
        'article_id':'Int64',
        'author_id':'Int64',
        'viewer_id':'Int64',
        'view_date':'datetime64[ns]'
    })

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_that_read = []
    for article in views["article_id"].unique():
        loc_df = views.loc[views['article_id'] == article]
        for author in loc_df['author_id'].unique():
            if author in loc_df['viewer_id'].tolist():
                authors_that_read.append(author)
    
    authors_that_read.sort()
    author_df = pd.DataFrame(authors_that_read, columns=["id"])
    
    return author_df

authors_that_read_the_article = article_views(views)