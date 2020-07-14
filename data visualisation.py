#%%exploratory data analysis using visualisation 
##premodel building graphs
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\hp\Desktop\imarticus\python\datasets\Pokemon1.csv',header=0,index_col=0)
df
df.info()
#%% work  on two quantative variable
plt.bar(data=df,x='Attack',y="Defense")
plt.show()
#%% changing dimentions
plt.figure(figsize=(20,10))
plt.scatter(data=df,x='Attack',y='Defense',s=200,c='green',marker='*')

##change axes range
plt.xlim(0,50)
plt.ylim(0,200)

#add title
plt.title('Relationsheep Between Attack ans Defense')

##add x and y labels
plt.xlabel('Attacks')
plt.ylabel('Defense')
plt.grid(True)

##show plot
plt.savefig('test,jpg')
plt.show()
#%% by using seaborn library
sns.lmplot(data=df,x='Attack',y='Defense')
##if showing warning use
##import warning
##warnings.filterwarnings('ignore')
#%%
sns.lmplot(data=df, x='Attack',y='Defense',
           fit_reg=False, ##no regression line
           hue='Stage',palette='twilight') ## color by evslustion stage
#%% pairplot
sns.pairplot(df,x_vars=['Attack','Defense','Speed'],y_vars='Total',kind='reg', hue='Stage',palette='twilight')
#%%line plot(most sitable for timr series model
x=[20,30,40]
y=[10,45,70]
plt.plot(x,y,c="red")
plt.xlim(0,100)
plt.ylim(0,100)
plt.title('a simple line plot')
plt.grid(True)
plt.savefig('test.jpg')
plt.show()
#%% histograms (distribution of a single quantataive variable) divide data into bins
plt.subplot(121)
plt.hist(x='Attack',data=df,bins=20,color='red')
plt.title('Attack')
plt.subplot(122)
plt.hist(x='Defense',data=df,bins=20,color="darkred")
plt.title('Defense')
#%% distribution plot
sns.distplot(df.Attack)
#%% count plot
sns.countplot(x='Type 2',data=df,palette="Set3")
## rotate x labels
plt.xticks(rotation=48)
#%%
df['Type 2'].value_counts()
#%% bphsargra
import numpy as np
sns.barplot(x="Type 1",y="Attack",data=df,estimator=np.mode)
plt.xticks(rotation=45)
#%% boxplt
sns.boxplot(data=df)
#%% preformat dataz frame
stats_df=df.drop(['Total','Stage','Legendary'],axis=1)
#new boxplot using stats_df
sns.boxplot(data=stats_df)
sns.boxplot(y=df.HP)
#%%using pandas
df.boxplot(column="HP")
plt.show()
#%% violin graph
sns.violinplot(x='Type 1',y='Attack',data=df)
plt.xticks(rotation=60)
#%%7profilinh
pip install pandas-profiling
#%%%
import pandas_profiling as pf
import pandas as pd
#%%%
titanic_df=pd.read_excel(r'C:\Users\hp\Desktop\imarticus\python\Titanic_Survival_Train.xls')
#%%%
df=pf.ProfileReport(titanic_df)
#%%%
df
#%%%
df.to_file('test.html')
#%%













