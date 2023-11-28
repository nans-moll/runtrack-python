def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    resultat = f"{heures} heures et {minutes_restantes} minutes"
    print(resultat)


time_to_text(135)