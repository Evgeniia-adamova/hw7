number_of_clouds = 10
sky = [number_of_clouds, "sun", "wind"]
temperature = 15
for obj in sky:
    if number_of_clouds > 9:
        print("The weather is cloudy")
    if obj == "sun":
        print("It is sunny")
    if obj == "wind":
        print("It is windy, so the temperature is", temperature, "degrees")
    else:
        print("The temperature is", temperature + 10, "degrees")

