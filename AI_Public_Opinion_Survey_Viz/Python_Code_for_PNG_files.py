# Python Notebook - AI_Public_Opinion_Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting
plt.style.use('ggplot')

dat = pd.DataFrame(datasets["AI_Public_Opinion_data"]) ## Query data from SQL



pd.set_option('display.max_columns', 500)
dat.head(5)

## Select all questions start with Q6: Confidence in organizations to develop AI in best public interests
q6 = [col for col in dat if col.startswith('Q6')]
q6 = q6[15:]
q6dat=dat[q6]

## column stack counts
q6freq = q6dat.apply(pd.Series.value_counts, axis = 0).transpose()
q6freq.drop([9], axis = 1, inplace= True)
q6freq = q6freq.iloc[:,[4,3,2,1,0]]
q6freq

## Plot stacked bar plot
ax = q6freq.apply(lambda r: r/r.sum()*100, axis = 1).plot.bar(stacked = True, figsize = (18,8))
for p in ax.patches:
  width, height = p.get_width(),p.get_height()
  x, y = p.get_xy()
  ax.text(x+width/2, y+ height/2, '{:.2f}%'.format(height), horizontalalignment='center',verticalalignment='center')

## Make sure the order of legend is the same as bar
handles, labels = ax.get_legend_handles_labels()
labels = ['A great deal of confidence', 'A fair amount of confidence','Not too much confidence','No confidence',"Don't know"] #get the handles
plt.legend(reversed(handles), labels, bbox_to_anchor=(1,1))

plt.title("Confidence in Organizations to Develop AI in best public interests")
plt.xlabel('Organizations', fontsize = 14)
plt.ylabel('Percentage',fontsize = 14)
plt.xticks(np.arange(15),['US Military',"US Gov't",'NSA','FBI','CIA','NATO',"Int'l Research Org",'Tech Companies','Google','Facebook','Apple','Microsoft','Amazon','Non-profit AI Research Org','Uni Researchers'],rotation = 20)



## Get columns for Q2: estimated sizes for global risks
q2 = [col for col in dat if col.startswith('Q2')]
q2.append("educ")
Q2 = dat[q2]
Q2_NA = Q2.replace(9,np.nan)
Q2_NA.head()

q2 = [col for col in dat if col.startswith('Q2')]
q2.append("educ")
Q2 = dat[q2]
Q2_NA = Q2.replace(9,np.nan)

ls = []
for col in Q2.columns:
  ls.append(col)

clr = []
for x in ls:
  if x != "Q2_9":
    clr.append("grey")
  else:
    clr.append("red")

plt.figure(figsize = (15,10))
Q2_NA.mean().plot.bar(color = clr)
xlocs=[i+1 for i in range(-1,15)]
y = Q2_NA.mean().round(2)
for i, v in enumerate(y):
    plt.text(xlocs[i] - 0.25, v + 0.04, str(v))
y = Q2_NA.mean()
plt.errorbar(ls,Q2_NA.mean(),Q2_NA.std(), fmt = "o", marker = "h", color = "blue")
plt.title("Average Estimated Size of 15 Global Risks", fontsize = 20)
plt.xlabel('Global Risks', fontsize=14)
plt.ylabel('Average Size', fontsize=14)
plt.xticks(np.arange(15),['Failure to address climate change','Failure of regional or global governance','Conflict between major countries','Weapons of mass destruction','Large-scale involuntary migration','Infectious diseases','Water crises','Food crises','Harmful consequences of AI','Harmful consequences of synthetic biology','Large-scale cyber attacks','Large-scale terrorist attacks','Global recession','Extreme weather events','Major natural disasters'],rotation = 65)
plt.show()

q29edu = datasets["Query 9"] ## Query data directly from SQL
f, axes = plt.subplots (1,1,figsize = (10,8))
g = sns.boxplot(x = "educ", y = "Q2_9", data = q29edu)
plt.xlabel('Education', fontsize = 12)
plt.ylabel('Risk level', fontsize = 12)
plt.xticks(np.arange(6),["No HS","High School Graduate","Some College","2-year","4-year","Post-Graduate"], rotation = 45)
plt.yticks(np.arange(5),['Minimal','Minor','Moderate','Severe','Catastrophic'])
plt.title('AI harmful conseuqnces size break down by education level')



## Q6: Trust for orgs to develop AI in public interest
Q6_A = Q6.replace(9,np.nan)
Q6_A = Q6_A.replace(8,np.nan)
Q6_A = Q6_A.replace(5,np.nan)


## Highlight small and large values
ls = []
for col in Q6_A.columns:
  ls.append(col)

clr = []
for x in Q6_A.mean().round(2):
  if x < 2.5:
    clr.append("green")
  elif x > 3:
    clr.append("red")
  else:
    clr.append("blue")

plt.figure(figsize = (12,8))
Q6_A.mean().plot.bar(color = clr)
xlocs=[i+1 for i in range(-1,14)]
y = Q6_A.mean().round(2)
for i, v in enumerate(y):
    plt.text(xlocs[i] - 0.25, v + 0.03, str(v))
y = Q6_A.mean()
plt.title("Average Trust for developing AI in interest of the public", fontsize = 20)
plt.xlabel('Entity/Organization', fontsize=14)
plt.ylabel('Average Trust (The lower the more trusted)', fontsize=14)
plt.xticks(np.arange(15), ['US military',"US Civilian Gov't",'NSA','FBI','CIA','NATO','Intl Research Org','Tech Companies','Google',"Facebook",'Apple','Microsoft','Amazon','Non-profit AI Research org','University Researchers'],rotation = 60)
plt.show()


## Pie chart
labels = 'Very unlikely','Unlikely','Somewhat unlikely','Equally likely as unlikely','Somewhat likely','Likely','Very likely'
sizes = [19,22,50,118,123,147,190]
explode = [0,0,0,0,0.1,0.1,0.1]
fig1, ax1 = plt.subplots(figsize= (10,10))
ax1.pie(sizes, labels=labels, explode = explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title ("Impact of AI surveillance", fontsize = 14)
plt.show()


labels = "Very unlikely",'Unlikely','Somewhat unlikely','Equally likely as unlikely','Somewhat likely','Likely','Very Likely'
sizes = [4,12,13,9,8,5,2]
explode = [0.1,0.1,0.1,0,0,0,0]
fig1, ax1 = plt.subplots(figsize= (10,10))
ax1.pie(sizes, labels=labels, explode = explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title ("Likelihood of harmful AI consequences for people with CS/CE degrees", fontsize = 14)
plt.show()


