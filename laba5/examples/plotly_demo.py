import plotly.express as px

# Ładowanie wbudowanego zbioru danych o krajach
df = px.data.gapminder().query("year == 2007")

# Tworzenie wykresu bąbelkowego
fig = px.scatter(df, x="gdpPercap", y="lifeExp",
                 size="pop", color="continent",
                 hover_name="country", log_x=True, 
                 title="PKB vs Średnia długość życia (2007)")

fig.show()