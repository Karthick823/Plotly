import plotly.express as px
df=px.data.gapminder()
df
#df.groupby(['lifeExp']).mean()
#d1=df.groupby("country")['lifeExp'].min()
#print(d1)
fig=px.bar(df.groupby("country")['lifeExp'].mean(),y="lifeExp")
#fig=px.density_contour(df.groupby("country")['lifeExp'].mean(),y="lifeExp")
#fig=px.bar(df.groupby("country")["pop"].mean(),y="pop")
#fig=px.bar(df[df["year"]==1952]["pop"],y="pop")
fig.show()