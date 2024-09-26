number_of_clouds = int(input("Enter number of clouds: "))
temperature = int(input("Enter temperature: "))

sky = [number_of_clouds, temperature, "sun", "wind"]

if "sun" in sky:
    print("It is sunny")

if "wind" in sky:
    print("It is windy")

if number_of_clouds > 9:
    print("The weather is cloudy")
else:
    print("The weather is bright")

if temperature > 20:
    print("The temperature is ", temperature, "it's warm")
else:
    print("The temperature is", temperature, "stay home")

