def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Entrada do usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Conversão
fahrenheit, kelvin = converter_temperatura(celsius)

# Exibição do resultado
print(f"{celsius}°C equivalem a:")
print(f"{fahrenheit:.2f}°F (Fahrenheit)")
print(f"{kelvin:.2f}K (Kelvin)")