a = input("Entrez plusieurs valeurs séparées par des virgules: ")
values = a.split(',')

float_values = [float(v.strip()) for v in values]
print(sum(float_values))
# for v in values:
#     float_value = float(v.strip())
