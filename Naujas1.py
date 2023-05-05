from bs4 import BeautifulSoup
import requests

print("iveskite pasirinktą miestą iš paduoto sąrašo apačioje")
print(" ")
Miestas = input("iveskite norimą miestą: Vilniuje, Kaune, Palangoje, Jonavoje, Jurbake, Klaipėdoje: ")
print(" ")
print("išfiltruoto miesto informacija pagal pasirinkimą: ")
print(" ")
svetaine = requests.get("https://www.cvbankas.lt")
svetaines_kodas = svetaine.text

Sriuba = BeautifulSoup(svetaines_kodas, 'html.parser')
Skelbimai = Sriuba.find_all("article")
for Skelbimas in Skelbimai:
    Miestai = Skelbimas.find('span', class_="list_city").text
    Atlyginimai = getattr(Skelbimas.find('span', class_="salary_amount"),"text", None)
    Darbo_skelbimas = Skelbimas.find('h3', class_="list_h3").text
    if Miestas in Miestai:
        print(f"Darbo skelbimas:  {Darbo_skelbimas}")
        print(f"Miestas - {Miestai}   Atlyginimas: {Atlyginimai}")
        print(" ")