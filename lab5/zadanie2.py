# Wypisz wszystkie pary klucz:wartość występujące w słowniku:
# sample_dict = {
#  "name": "Kelly",
#  "surname": "Jones",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"}
# • Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
# Wskazówki:
# − przejdź za pomocą pętli po kluczach zapisanych w liście;
# − następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
# klucz:wartość) do nowego słownika.
# • Usuń ze słownika wartości, których klucze występują w liście.
# • Sprawdź, czy wartość „Jones” występuje w słowniku.
# • Zmień w słowniku klucz ‘city’ na ‘location’.

sample_dict={"name":"Kelly","surname": "Jones","age": 25,"salary": 8000,"city": "New york"}
for key, value in sample_dict.items():
 print(f'{key:<10} : {value:>10}')
for key in sample_dict.keys():
 print(key, sample_dict[key])
newdict={}
l1=["age", "salary", "name"]
for key in l1:
 if key in sample_dict:
  newdict[key]=sample_dict[key]
print(newdict)

for i in l1:
 sample_dict.pop(i)
print(sample_dict)

if "Jones" in sample_dict.values():
 print("tak")
else:
 print("nie")
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)

