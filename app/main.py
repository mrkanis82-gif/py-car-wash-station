class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.clean_mark = clean_mark
        self.brand = brand
        self.comfort_class = comfort_class

class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power: int, average_rating: float, count_of_ratings: int ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def calculate_washing_price(self, car: Car):
        cost = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return cost.round(1)


    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark > self.clean_power:
                pass
            else:
                self.wash_single_car(car)
                income += self.calculate_washing_price(car)
        return income

    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        self.count_of_ratings += 1
        self.average_rating = rate + self.count_of_ratings / 2