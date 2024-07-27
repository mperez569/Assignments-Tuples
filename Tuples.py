#1. Tuple Mastery in Python
#Task 1: Formatting Flight Itineraries
def format_itineraries(itineraries):
formatted_itineraries = []
    
    for index, (name, origin, destination) in enumerate(itineraries, start=1):
        itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)
    
    return "\n".join(formatted_itineraries)

itinerary_list = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

formatted_string = format_itineraries(itinerary_list)
print(formatted_string)

#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement
def add_book():
    title = input("Enter Title of book: ")
    author = input("Enter author of book: ")
    if len(title) == 0 or len(author) == 0:
        print("Author or Title have not been entered. Try Again!")
    
    else:
        new_book = (title, author)
      
        if new_book in library:
            print(f"The book '{title}' by {author} is already in the library. \n")
          
        else:
            library.append(new_book)
            print(f"The book '{title}' by {author} has been added to the library.")

# Existing library
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
while True:
    #ans = input("Do you want to enter a book? (y/n):")
    add_book()
    ans = input("Add another book? (y/n): ")
    if ans == 'y'or ans == 'Y':
        continue
      
    elif ans == 'n'or ans == 'N':
        print("Thank you!")
        print("Here is a list of the books!")
        break
      
    else:
        print("Invalid input. Try Again!!")
      
print(library)

#3. Mastering Tuple Packing and Unpacking in Python
#Task 1:
def order_details(orders):
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name} ordered {quantity} {product}(s).")
      
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Headphones", 3),
    ("David", "Smartphone", 1)
]
order_details(orders)
