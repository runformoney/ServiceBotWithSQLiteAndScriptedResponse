from getknowledge import GetKnowledge
import pandas as pd
gk = GetKnowledge()
import warnings
warnings.filterwarnings("ignore")

query = "aaaaaaaa"

cat_resp = pd.read_csv("cat_resp.csv")
#cat_resp = cat_resp.set_index('Category')

print(list(cat_resp.Category.unique()))
topScoringIntent = gk.get_intent(query)
print("Type of Query: " + topScoringIntent)

if topScoringIntent != 'None':
    print(cat_resp.loc[topScoringIntent]["Reply"])