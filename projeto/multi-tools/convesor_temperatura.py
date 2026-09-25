def conversor_temperatura():
    temp_celsius = float(input('Temperatura em Celsius:=> '))

    temp_F = (temp_celsius * 9/5) + 32
    temp_Kelvin = temp_celsius + 273.15

    print(f'Sua temperatura em Celsius {temp_celsius}°C equivale a:')
    print(f'{temp_F:.2f}°F')
    print(f'{temp_Kelvin:.2f}K')
