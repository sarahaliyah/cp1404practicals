from prac_09.unreliable_car import UnreliableCar


def main():
    """Test and simulate the driving reliability of UnreliableCar instances"""
    good_car = UnreliableCar("Mostly Good Car", 100, 90)
    bad_car = UnreliableCar("Really Unreliable car", 100, 20)

    print(f"{good_car.name}:")
    print(good_car)
    for i in range(5):
        distance_driven = good_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance_driven} km")

    print(f"\n{bad_car.name}:")
    print(bad_car)
    for i in range(5):
        distance_driven = bad_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance_driven} km")


if __name__ == "__main__":
    main()
