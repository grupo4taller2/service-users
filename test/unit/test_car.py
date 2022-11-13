from src.domain.car import Car


def test_car_creation():
    car = Car(
        plate='AAA 111',
        manufacturer='Tesla',
        model='Model X',
        year_of_production=2020,
        color='Neon Blue'
    )
    assert car.model == 'Model X'
    assert car.plate == 'AAA 111'
    assert car.manufacturer == 'Tesla'
    assert car.year_of_production == 2020
    assert car.color == 'Neon Blue'
