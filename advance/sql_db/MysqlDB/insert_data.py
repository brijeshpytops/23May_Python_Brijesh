from .dbConnection import db, cursor

# def insert_record():
#     Query = """INSERT INTO users (first_name, last_name, email, mobile, password) VALUES ('John', 'Doe', 'johndoe@example.com', '1234567890', 'password123');"""
#     cursor.execute(Query)
#     db.commit()


def insert_records():
    Query = """INSERT INTO users (first_name, last_name, email, mobile, password) VALUES
('Alice', 'Wonderland', 'alice@wonderland.com', '1234567890', 'password123'),
('Bob', 'Builder', 'bob@builder.com', '9876543210', 'builder123'),
('Charlie', 'Brown', 'charlie@peanuts.com', '5555555555', 'charliebrown123'),
('David', 'Copperfield', 'david@copperfield.com', '1111111111', 'copperfield123'),
('Emily', 'Post', 'emily@post.com', '2222222222', 'post123'),
('Frank', 'Sinatra', 'frank@sinatra.com', '3333333333', 'sinatra123'),
('Grace', 'Kelly', 'grace@kelly.com', '4444444444', 'kelly123'),
('Henry', 'Ford', 'henry@ford.com', '5555555555', 'ford123'),
('Isabella', 'Bird', 'isabella@bird.com', '6666666666', 'bird123'),
('Jack', 'Sparrow', 'jack@sparrow.com', '7777777777', 'sparrow123'),
('Kate', 'Winslet', 'kate@winslet.com', '8888888888', 'winslet123'),
('Liam', 'Neeson', 'liam@neeson.com', '9999999999', 'neeson123'),
('Mia', 'Farrow', 'mia@farrow.com', '1010101010', 'farrow123'),
('Noah', 'Centineo', 'noah@centineo.com', '2020202020', 'centineo123'),
('Olivia', 'Rodrigo', 'olivia@rodrigo.com', '3030303030', 'rodrigo123'),
('Parker', 'Posey', 'parker@posey.com', '4040404040', 'posey123'),
('Queen', 'Elizabeth', 'queen@elizabeth.com', '5050505050', 'elizabeth123'),
('Roger', 'Federer', 'roger@federer.com', '6060606060', 'federer123'),
('Sarah', 'Jessica Parker', 'sarah@parker.com', '7070707070', 'parker123'),
('Thomas', 'Edison', 'thomas@edison.com', '8080808080', 'edison123');"""
    cursor.execute(Query)
    db.commit()
