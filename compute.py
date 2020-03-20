import pandas as pd 

import plotly.express as px

df = pd.read_excel("COVID-19-geographic-disbtribution-worldwide-2020-03-18.xls")
df = df.set_index(["DateRep", "Countries and territories"])
df = df.sort_values(by = "DateRep", axis = 'index')
df['deathcumsum'] = df.groupby(level=-1)['Deaths'].cumsum()
df['casescumsum'] = df.groupby(level=-1)['Cases'].cumsum()
df["mortality"] = df["deathcumsum"] / df["casescumsum"]


# cases = df.groupby("Countries and territories").agg({"Deaths" : "sum", "Cases" : "sum"})
# cases["mortality"] = round(cases["Deaths"] / cases["Cases"] * 100, 2)
# cases.sort_values("Cases", inplace = True, ascending = False)
# cases["country"] = cases.index
# print(cases)

# fig = px.scatter(cases, x="Cases", y="Deaths", color="country", log_x = True, log_y = True)
#         # , marginal_y="violin", marginal_x="box", trendline="ols")
# fig.show()

df = df.reset_index()
print(df)

fig = px.line(df[df["casescumsum"] > 1000], 
              x="casescumsum", 
              y="mortality", 
              color="Countries and territories", 
              line_group="Countries and territories", 
              hover_name="Countries and territories",
              log_x = True,
              log_y = True
        ) #line_shape="spline") #, render_mode="svg")

fig.update_xaxes(title_text='Cumulative number of cases')
fig.update_yaxes(title_text='Mortality')
# fig.write_image("fig1.html")
fig.show()
