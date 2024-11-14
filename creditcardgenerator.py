import random
import string

names = [
    "Sofia McCormick", "Jasiah Blair", "Frances Gray", "Nicholas Truong", "Judith Manning",
    "Seth Schmitt", "Queen Manning", "Seth Parrish", "Tiana Dougherty", "Brett Young",
    "Zoey Villalobos", "Reuben Sanford", "Emerald Wheeler", "Kenneth Romero", "Eliza Pineda",
    "Gerardo Turner", "Brooklyn Lawson", "Lane Reeves", "Lana Woodward", "Jeremias Gentry",
    "Amelie Wang", "Cohen Massey", "Clementine Leon", "Marshall Richards", "Trinity Berg",
    "Cayson Sierra", "Marceline Cruz", "Ryan McKee", "Kori Montoya", "Ford Castro",
    "Eloise Stanton", "Zyair Barajas", "Keilani Zhang", "Isaias Durham", "Tiffany Conner",
    "Phillip Allison", "Chelsea Coleman", "Micah Hester", "Zendaya Hess", "Lawrence McConnell",
    "Denise Terry", "Armani Vasquez", "Rose Burnett", "Davis Castro", "Eloise Velez",
    "Kareem Gutierrez", "Savannah Magana", "Rey Burns", "Emerson Martin", "Mateo Conley",
    "Salem House", "Yehuda Anderson", "Ella Gill", "Matthias Drake", "Jayleen Hoffman",
    "Steven Meadows", "Pearl Palacios", "Thaddeus Osborne", "Shelby Rosas", "Remi Potts",
    "Ellison Craig", "Odin Leblanc", "Novalee Nava", "Stefan Olson", "Isabel Howell",
    "Bradley Blake", "Amanda Greer", "Koda Calderon", "Serena Harrell", "Nelson Tucker",
    "Esther Reyna", "Reginald Kim", "Gabriella Hubbard", "Forrest Rubio", "Hadassah Solomon",
    "Musa Russo", "Tinsley Wall", "Issac Salas", "Amber Stewart", "Nolan Sharp", "Camryn Roy",
    "Marcelo Clark", "Chloe Cabrera", "Cade Strickland", "Nia Foley", "Mohammad Wilcox",
    "Ashlyn Blankenship", "Ernesto Luna", "Journey Singh", "Louis Bauer", "Haley Brown",
    "Elijah McCormick", "Macie Pratt", "Rowen Weber", "Alayah Benitez", "Justice Bradshaw",
    "Berkley Warner", "Jaxton Yang", "Angelina McFarland", "Dane Richmond", "Whitney Armstrong",
    "Grant Bentley", "Jaylin Jordan", "Sawyer Johnson", "Emma Patton", "Moises Pruitt",
    "Brylee Michael", "Bronson O’Connell", "Jillian Jefferson", "Raylan Moyer", "Zola Fitzpatrick",
    "Blaze Berger", "Laylah Villanueva", "Huxley Schneider", "Delaney Holmes", "King Paul",
    "Daphne Fitzgerald", "Peyton Ho", "Calliope Camacho", "Tatum Taylor", "Sofia Richards",
    "Holden Abbott", "Melany Cruz", "Ryan Walker", "Hazel Sheppard", "Trent Martin", "Mila Osborne",
    "Augustus Wolfe", "Hallie Carrillo", "Wade Eaton", "Miley Tucker", "Ivan Davenport",
    "Adrianna Mathews", "Jamir McDonald", "Daisy Frost", "Dario Alfaro", "Yasmin Walter",
    "Lochlan Aguilar", "Josie Harrison", "Gavin Yu", "Navy Friedman", "Darwin Stanton",
    "Jaycee Townsend", "Alexis Sellers", "Mercy Flores", "Lincoln Beltran", "Kaydence Duffy",
    "Kyng Black", "Molly Whitney", "Jeffery Paul", "Daphne Floyd", "Pierce Woodward", "Drew Ali",
    "Arjun Bridges", "Elora Gonzalez", "Ethan Lane", "Amy Howell", "Bradley Saunders",
    "Meadow Mendez", "Arthur Galindo", "Corinne Newton", "Santino Moon", "Naya Miles", "Jared Bond",
    "Alena Copeland", "Axton Macias", "Adley Tang", "Rogelio Enriquez", "Nellie Romero", "Bryson Caldwell",
    "Evelynn Massey", "Donald Pope", "Aurelia Krueger", "Jones Morse", "Kairi Lynch", "Zane Salazar",
    "Freya Dougherty", "Brett Lambert", "Nina Warner", "Jaxton King", "Victoria Thornton", "Malik Maddox",
    "Zainab Sosa", "Emir Bell", "Melody Dalton", "Fletcher Finley", "Jovie Vaughn", "Remy Reed",
    "Valentina Clay", "Yosef Stevens",
    ]

def generate_fake_credit_card():
    card_number = '4' + ''.join(random.choice(string.digits) for _ in range(15))  # Assuming Visa starts with '4'
    expiry_month = str(random.randint(1, 12)).zfill(2)
    expiry_year = str(random.randint(2023, 2030))
    cvc = ''.join(random.choice(string.digits) for _ in range(3))
    card_holder_name = random.choice(names)

    return {
        'Card Number': card_number,
        'Expiry Date': f"{expiry_month}/{expiry_year}",
        'CVC': cvc,
        'Card Holder Name': card_holder_name
    }

def main():
    fake_credit_card = generate_fake_credit_card()
    print("Generated Credit Card Information:")
    for key, value in fake_credit_card.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
