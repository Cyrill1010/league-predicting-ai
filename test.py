import pandas as pd
from glom import glom

df = pd.read_json('data/match_timeline.json')
df.columns = ["test", "test1"]

dic={
    1:5,2:0
}
print(dic.values())