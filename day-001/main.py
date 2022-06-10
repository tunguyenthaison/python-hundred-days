
def band_name_generator_1() -> None:
    print("Greeting! Welcome to the Band Name Generator program!")
    print("Please enter the name of the city you grew up in: ", end='')
    city = input()
    print("Please enter a  name of a  pet: ", end='')
    pet = input()
    band_name = city + " " + pet
    print("A suggested band name is: " + band_name)


def band_name_generator_2() -> None:
    print("Greeting! Welcome to the Band Name Generator program!")
    city = input("Please enter the name of the city you grew up in: \n")
    pet = input("Please enter a  name of a  pet: \n")
    band_name = city + " " + pet
    print("A suggested band name is: " + band_name)


if __name__ == "__main__":
    band_name_generator_2()
