import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Loading data
data = pd.read_csv("C:/Users/AK/Downloads/datas.csv")

#Creating data frame including Physician ID and State
new_data = pd.DataFrame(data=data[["Physician ID"," State"]])

#Calculating total prescriptions
new2 =  pd.DataFrame(data=data[["Jan 2019","Feb 2019","Mar 2019","Apr 2019", "May 2019","Jun 2019","Jul 2019", "Aug 2019","Sep 2019", "Oct 2019","Nov 2019", "Dec 2019"]]) 
new_data["Total"] = new2.sum(axis=1)

#Grouping by State
final2 = new_data.groupby(' State').sum()

#Sorting wrt total prescriptions
rank=final2.sort_values(by="Total",ascending=False)

#Visualizing using bar graph
rank = rank.plot(y=["Total"],kind = 'bar',title='Market Share of Different Sates',figsize=(15,5))
rank.set_xlabel(" State")
rank.set_ylabel("Market Share of Different Sates")
