class Ferry(db.Model):

    __tablename__ = "ferries"

    id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)


class Trip(db.Model):

    __tablename__ = "trips"

    date = db.Column(db.DateTime, nullable=False, unique=True)
    passenger_count = db.Column(db.Integer, nullable=False)
    ten_foot_vehicles = db.Column(db.Integer, nullable=False)
    twenty_foot_vehicles = db.Column(db.Integer, nullable=False)
