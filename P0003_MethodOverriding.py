class Car:

    def __init__(self, company, color, price, status):
        self.company = company
        self.color = color
        self.price = price
        self.status = status or "new"

    def get_car_details(self):
        return f"""
        Company : {self.company} | 
        Color : {self.color} |
        Price : {self.price} |
        Status : {self.status.upper()}
        """


class Car_Model(Car):
    def __init__(
        self,
        company,
        color,
        price,
        status,
        model,
        transmission,
        technology,
        mileage,
        engine_type="EV",
    ):
        super().__init__(company, color, price, status)
        self.model = model
        self.transmission = transmission
        self.engine_type = engine_type
        self.technology = technology
        self.mileage = mileage

    def get_car_details(self):
        return f"""
        Company : {self.company} | 
        Model : {self.model.title()} |
        Color : {self.color} |
        Transmission : {self.transmission.upper()} |
        Engine Type : {self.engine_type} |
        Technology : {self.technology} |
        Mileage : {self.mileage} km/l |
        Vehicle Status : {self.status.upper()} |
        Price : INR {self.price} |
        """


c1 = Car_Model(
    "Suzuki", "Red", 809000.45, "new", "celerio zxi+", "automatic", "4matic", 23
)
print(c1.get_car_details())
