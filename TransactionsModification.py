__author__ = 'anupdudani'
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

ParticipantsDF= pd.read_csv("data_for_task/Participants.csv")
TransactionsDF=pd.read_csv("data_for_task/Transactions.csv")

modifiedTransactionsDF=pd.merge(TransactionsDF,ParticipantsDF, left_on='assigned.to',right_on='badge.id')
print modifiedTransactionsDF.columns
del modifiedTransactionsDF["badge.id"]
print modifiedTransactionsDF.head()
print modifiedTransactionsDF.info()
print modifiedTransactionsDF.describe()
#modifiedTransactionsDF.to_csv("modified_transactions.csv")

aggregatedDF=modifiedTransactionsDF.groupby( [ "assigned.to", 'complexity','team']).count().reset_index()
print aggregatedDF.info()
print aggregatedDF
plt.figure()



sns.factorplot(x="assigned.to", y="assign.date", data=aggregatedDF.groupby(['assigned.to']).sum().reset_index(),
                   size=6, kind="bar", palette="muted")

sns.factorplot(x="assigned.to", y="assign.date", data=aggregatedDF,
                   size=6, kind="bar", palette="muted")

plt.show()

