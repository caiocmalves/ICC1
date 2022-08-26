tempo = int(input("Por favor, entre com o número de segundos que deseja converter: "))
segundos = tempo % 60
dias = (((tempo // 60) // 60) // 24)
hora = ((tempo - (dias * 24 * 60 * 60)) // 60 // 60)
minutos = ((tempo - ((dias * 24 * 60 * 60) + (hora * 60 * 60))) // 60)

print(dias, "dias,", hora, "horas,", minutos, "minutos e", segundos, "segundos.")