import modeleai

obj1 = modeleai.ModelAI('model1', 1)
obj2 = modeleai.ModelAI('model2', 2)
obj3 = modeleai.ModelAI(modeleai.ModelAI.z_pliku('modele.json')[0], modeleai.ModelAI.z_pliku('modele.json')[1])
print(obj1.nazwa_modelu)
print(obj2.nazwa_modelu)
print(obj3.nazwa_modelu)
print(modeleai.ModelAI.ile_modeli())