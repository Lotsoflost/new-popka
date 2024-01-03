from typing import List
import pandas as pd

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(views)

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    new_id = views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().sort_values(by= 'author_id')
    return new_id
print(article_views(views))

# def big_countries(world: pd.DataFrame) -> pd.DataFrame:
#     mask = world['area'] >= 3000000
#     mask2 = world['population'] >= 25000000
#     big_con = world[mask|mask2][['name','population', 'area']].sort_values( by = 'area', ascending= False)
#     return big_con
#
# print(big_countries(world))
