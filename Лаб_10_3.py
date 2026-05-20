import json
import matplotlib.pyplot as plt

with open("countries_data.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

names = [country["name"] for country in countries]
populations = [country["population"] for country in countries]

plt.figure(figsize=(12, 8))
colors = plt.cm.tab20c.colors

total_population = sum(populations)
percentages = [pop / total_population * 100 for pop in populations]

labels = [f"{name} - {pop:.1f} млн ({percent:.1f}%)"
          for name, pop, percent in zip(names, populations, percentages)]

wedges, texts, autotexts = plt.pie(
    populations,
    labels=None,  # Без підписів на секторах
    colors=colors[:len(countries)],
    startangle=90,
    autopct='%1.1f%%',  # Тільки відсотки всередині
    pctdistance=0.7,
    wedgeprops={"edgecolor": "black", "linewidth": 1, "linestyle": "solid", "antialiased": True},
    textprops={'fontsize': 10, 'fontweight': 'bold'}
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)

plt.legend(wedges, labels, title="Країни",
           loc="center left", bbox_to_anchor=(1, 0.5),
           fontsize=9)

plt.title("Частка населення країн (у відсотках)", fontsize=14, pad=20)
plt.axis("equal")
plt.tight_layout()
plt.show()