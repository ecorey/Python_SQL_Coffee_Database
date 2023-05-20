import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db_config_file
import db_functions as db
from PIL import ImageTk, Image

####################FUNCTIONS####################

####defining an event####

rows = None
num_of_rows = None
row_counter = 0
blank_text_boxes_tab_two = True


def on_tab_selected(event):
    global blank_textboxes_tab_two

    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "All Records":
        load_database_results()

    if tab_text == "Add New Record":
        blank_textboxes_tab_two = True


###load database result###

def load_database_results():
    global rows
    global num_of_rows

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()
    messagebox.showinfo("Connected to Database", "DB Connection OK")

    try:
        sql = "SELECT * from `sie557`.`coffee_information`"
        num_of_rows, rows = db.query_database(con, sql, None)
    except Exception as e:
        print(e)
    print(rows)

    return True


####################IMAGE HANDELING###################
file_name = "coffee1.png"
file_name2 = "coffee2.png"
file_name3 = "coffee3.png"
file_name4 = "coffee4.png"

path = db_config_file.PHOTO_DIRECTORY + file_name
path2 = db_config_file.PHOTO_DIRECTORY + file_name2
path3 = db_config_file.PHOTO_DIRECTORY + file_name3
path4 = db_config_file.PHOTO_DIRECTORY + file_name4

image_selected = False
image_file_name = None
file_to_copy = None
file_new_home = None


def image_path(file_path):
    open_image = Image.open(file_path)
    image = ImageTk.PhotoImage(open_image)
    return image


####################SEARCH TAB FUNCTIONS####################

###select by id###
def search_by_id():
    global rows
    global num_of_rows

    coffee_id = fcoffee_id.get()

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    try:
        sql = "SELECT * FROM `sie557`.`coffee_information` WHERE coffee_id = %s"
        num_of_rows, rows = db.query_database(con, sql, (coffee_id,))
    except Exception as e:
        print(e)
    print(rows)

    # Display search results in a message box
    if num_of_rows > 0:
        result_text = "Search results:\n\n"
        for row in rows:
            result_text += f"Coffee ID: {row[0]}\nName: {row[1]}\nRoaster: {row[2]}\nRoast: {row[3]}\nOrigin: {row[5]}\n" \
                           f"Price USD per 100g: {row[6]}\nRating: {row[7]}\nDate: {row[8]}\nReview: {row[9]}\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No records found with the given coffee_id.")

    return True


def search_by_name():
    global rows
    global num_of_rows

    coffee_name = fcoffee_name.get()

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    try:
        sql = "SELECT * FROM `sie557`.`coffee_information` WHERE name = %s"
        num_of_rows, rows = db.query_database(con, sql, (coffee_name,))
    except Exception as e:
        print(e)
    print(rows)

    # Display search results in a message box
    if num_of_rows > 0:
        result_text = "Search results:\n\n"
        for row in rows:
            result_text += f"Coffee ID: {row[0]}\nName: {row[1]}\nRoaster: {row[2]}\nRoast: {row[3]}\nOrigin: {row[5]}\n" \
                           f"Price USD per 100g: {row[6]}\nRating: {row[7]}\nDate: {row[8]}\nReview: {row[9]}\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No records found with the given coffee_id.")

    return True


### search by roast###
def search_by_roast(offset=0):
    global rows
    global num_of_rows

    selected_roast = roast_var.get()

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    try:
        sql = "SELECT * FROM `sie557`.`coffee_information` WHERE roast = %s LIMIT %s OFFSET %s"
        num_of_rows, rows = db.query_database(con, sql, (selected_roast, 5, offset))  # limit the results to 10
    except Exception as e:
        print(e)

    if num_of_rows > 0:
        result_text = "Roast Search results:\n\n"
        for row in rows:
            result_text += f"Coffee ID: {row[0]}\nName: {row[1]}\nRoaster: {row[2]}\nRoast: {row[3]}\nOrigin: {row[5]}\n" \
                           f"Price USD per 100g: {row[6]}\nRating: {row[7]}\nDate: {row[8]}\nReview: {row[9]}\n---------------\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", f"No records found with the roast type: {selected_roast}.")

    return True


def search_by_roast_next():
    global row_counter
    row_counter += 10
    search_by_roast(offset=row_counter)


def search_by_roast_prev():
    global row_counter
    row_counter -= 10
    if row_counter < 0:
        row_counter = 0
    search_by_roast(offset=row_counter)


###search by origin###
def search_by_origin(offset=0):
    global rows
    global num_of_rows

    origin_selected = forigin.get()

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    try:
        sql = "SELECT * FROM `sie557`.`coffee_information` WHERE origin = %s LIMIT %s OFFSET %s"
        num_of_rows, rows = db.query_database(con, sql, (origin_selected, 5, offset))  # limit the results to 10
    except Exception as e:
        print(e)

    if num_of_rows > 0:
        result_text = "Origin Search results:\n\n"
        for row in rows:
            result_text += f"Coffee ID: {row[0]}\nName: {row[1]}\nRoaster: {row[2]}\nRoast: {row[3]}\nOrigin: {row[5]}\n" \
                           f"Price USD per 100g: {row[6]}\nRating: {row[7]}\nDate: {row[8]}\nReview: {row[9]}\n---------------\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", f"No records found with the origin type: {origin_selected}.")

    return True


def search_by_origin_next():
    global row_counter
    row_counter += 10
    search_by_origin(offset=row_counter)


def search_by_origin_prev():
    global row_counter
    row_counter -= 10
    if row_counter < 0:
        row_counter = 0
    search_by_origin(offset=row_counter)


###search by rating###
def search_by_rating(offset=0):
    global rows
    global num_of_rows

    rating_selected = frating.get()

    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    try:
        sql = "SELECT * FROM `sie557`.`coffee_information` WHERE rating = %s LIMIT %s OFFSET %s"
        num_of_rows, rows = db.query_database(con, sql, (rating_selected, 5, offset))  # limit the results to 10
    except Exception as e:
        print(e)

    if num_of_rows > 0:
        result_text = "Rating Search results:\n\n"
        for row in rows:
            result_text += f"Coffee ID: {row[0]}\nName: {row[1]}\nRoaster: {row[2]}\nRoast: {row[3]}\nOrigin: {row[5]}\n" \
                           f"Price USD per 100g: {row[6]}\nRating: {row[7]}\nDate: {row[8]}\nReview: {row[9]}\n---------------\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", f"No records found with the rating type: {rating_selected}.")

    return True


def search_by_rating_next():
    global row_counter
    row_counter += 10
    search_by_rating(offset=row_counter)


def search_by_rating_prev():
    global row_counter
    row_counter -= 10
    if row_counter < 0:
        row_counter = 0
    search_by_rating(offset=row_counter)


####################FUNCTIONS FOR INSERT TAB####################
###add new record###
def add_new_record():
    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()

    cursor = con.cursor()

    # Get the highest coffee_id in the database
    cursor.execute('SELECT MAX(coffee_id) FROM coffee_information')
    max_id = cursor.fetchone()[0]

    if max_id is None:
        next_id = 1247
    else:
        next_id = max_id + 1

    name = fnameTabTwo.get()
    roaster = froasterTabTwo.get()
    roast = froastTabTwo.get()
    loc_country = floc_countTabTwo.get()
    origin = foriginTabTwo.get()
    price = fpriceTabTwo.get()
    rating = fratingTabTwo.get()
    date = fdateTabTwo.get()
    review = freviewTabTwo.get()

    if not all([name, roaster, roast, loc_country, origin, price, rating, date, review]):
        messagebox.showerror("Error", "All fields must be filled.")
        return

    cursor.execute(
        "INSERT INTO coffee_information (coffee_id, name, roaster, roast, loc_count, origin, price, rating, date, review) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (next_id, name, roaster, roast, loc_country, origin, price, rating, date, review))

    con.commit()
    con.close()

    messagebox.showinfo("Success", f"Record with coffee_id {next_id} was successfully added.")


####################FUNCTIONS UPDATE TAB####################
###update coffee entry###
def update_coffee_entry():
    # Connect to the database
    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()
    cursor = con.cursor()

    # Get the values from the entry boxes
    coffee_id = entry_boxes['coffee_id'].get()
    if not coffee_id:
        messagebox.showerror("Error", "Please enter a Coffee ID.")
        return

    update_values = {}
    for key, entry_box in entry_boxes.items():
        if key == 'coffee_id':
            continue
        value = entry_box.get()
        if value:
            update_values[key] = value

    # Update the database with the new values
    if update_values:
        update_query = f"UPDATE coffee_information SET "
        for key, value in update_values.items():
            update_query += f"{key} = '{value}', "
        update_query = update_query.rstrip(", ")
        update_query += f" WHERE coffee_id = {coffee_id}"
        cursor.execute(update_query)
        con.commit()
        messagebox.showinfo("Success", "Entry updated successfully.")
    else:
        messagebox.showwarning("No Changes", "No fields were filled, nothing to update.")


##################FUNCTIONS DELETE TAB##################
### delete by id###
def delete_by_id():
    coffee_id = int(delete_id_entry.get())
    delete_from_database(coffee_id)

### delete from database###
def delete_from_database(coffee_id):
    # Connect to the database
    try:
        con = db.open_database()
    except db.DatabaseError as e:
        messagebox.showinfo("Database connection error", e)
        exit()
    cursor = con.cursor()

    # Execute the DELETE query
    cursor.execute("DELETE FROM coffee_information WHERE coffee_id=%s", (coffee_id,))

    # Commit the changes and close the connection
    con.commit()
    con.close()

    messagebox.showinfo("Success", f"Record with coffee_id {coffee_id} was successfully deleted.")


######################################MAIN APPLICATION######################################

app = tk.Tk()
app.title("Coffee Information Database")
app.geometry("1550x850")
tab_parent = ttk.Notebook(app)


tabAdd = ttk.Frame(tab_parent)
tabSearch = ttk.Frame(tab_parent)
tabUpdate = ttk.Frame(tab_parent)
tabDelete = ttk.Frame(tab_parent)

tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

tab_parent.add(tabSearch, text="Search coffee")  # Move the "Search coffee" tab to the first position
tab_parent.add(tabAdd, text="Add coffee")
tab_parent.add(tabUpdate, text="Update coffee")
tab_parent.add(tabDelete, text="Delete coffee")



###################CODE FOR INSERT TAB###################
###widgets###
fnameTabTwo = tk.StringVar()
froasterTabTwo = tk.StringVar()
froastTabTwo = tk.StringVar()
floc_countTabTwo = tk.StringVar()
foriginTabTwo = tk.StringVar()
fpriceTabTwo = tk.StringVar()
fratingTabTwo = tk.StringVar()
fdateTabTwo = tk.StringVar()
freviewTabTwo = tk.StringVar()

nameLabelTabTwo = tk.Label(tabAdd, text="Coffee Name: ", font=('Rockwell', 12))
roasterLabelTabTwo = tk.Label(tabAdd, text="Roaster: ", font=('Rockwell', 12))
roastLabelTabTwo = tk.Label(tabAdd, text="Roast: ", font=('Rockwell', 12))
loc_countLabelTabTwo = tk.Label(tabAdd, text="Loc Country: ", font=('Rockwell', 12))
originLabelTabTwo = tk.Label(tabAdd, text="Origin: ", font=('Rockwell', 12))
priceLabelTabTwo = tk.Label(tabAdd, text="Price (100G USD): ", font=('Rockwell', 12))
ratingLabelTabTwo = tk.Label(tabAdd, text="Rating: ", font=('Rockwell', 12))
dateLabelTabTwo = tk.Label(tabAdd, text="Date: ", font=('Rockwell', 12))
reviewLabelTabTwo = tk.Label(tabAdd, text="Review: ", font=('Rockwell', 12))

nameEntryTabTwo = tk.Entry(tabAdd, textvariable=fnameTabTwo)
roasterEntryTabTwo = tk.Entry(tabAdd, textvariable=froasterTabTwo)
roastEntryTabTwo = tk.Entry(tabAdd, textvariable=froastTabTwo)
loc_countEntryTabTwo = tk.Entry(tabAdd, textvariable=floc_countTabTwo)
originEntryTabTwo = tk.Entry(tabAdd, textvariable=foriginTabTwo)
priceEntryTabTwo = tk.Entry(tabAdd, textvariable=fpriceTabTwo)
ratingEntryTabTwo = tk.Entry(tabAdd, textvariable=fratingTabTwo)
dateEntryTabTwo = tk.Entry(tabAdd, textvariable=fdateTabTwo)
reviewEntryTabTwo = tk.Entry(tabAdd, textvariable=freviewTabTwo)

buttonCommit = tk.Button(tabAdd, text="Add Record to Database", command=add_new_record, font=('Rockwell', 13))

###image###
imgSearchTab2 = image_path(path2)
imgLabelSearchTab2 = tk.Label(tabAdd, image=imgSearchTab2)

###layout###
nameLabelTabTwo.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
nameEntryTabTwo.grid(row=0, column=1, padx=10, pady=10)

roasterLabelTabTwo.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
roasterEntryTabTwo.grid(row=1, column=1, padx=10, pady=10)

roastLabelTabTwo.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
roastEntryTabTwo.grid(row=2, column=1, padx=10, pady=10)

loc_countLabelTabTwo.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
loc_countEntryTabTwo.grid(row=3, column=1, padx=10, pady=10)

originLabelTabTwo.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
originEntryTabTwo.grid(row=4, column=1, padx=10, pady=10)

priceLabelTabTwo.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
priceEntryTabTwo.grid(row=5, column=1, padx=10, pady=10)

ratingLabelTabTwo.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
ratingEntryTabTwo.grid(row=6, column=1, padx=10, pady=10)

dateLabelTabTwo.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)
dateEntryTabTwo.grid(row=7, column=1, padx=10, pady=10)

reviewLabelTabTwo.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
reviewEntryTabTwo.grid(row=8, column=1, padx=10, pady=10)

buttonCommit.grid(row=9, column=1, padx=15, pady=15, sticky=tk.W)

###image layout###
imgLabelSearchTab2.grid(row=0, rowspan=10, column=3, padx=175, pady=30)

###################CODE FOR SEARCH TAB###################
###widgets###
fcoffee_id = tk.StringVar()
fcoffee_name = tk.StringVar()
fname = tk.StringVar()
roast_var = tk.StringVar()
roast_var.set("Light")  # Set default value for the dropdown menu
forigin = tk.StringVar()
forigin.set("Bolivia")  # Set default value for the dropdown menu
frating = tk.StringVar()
frating.set("97")  # Set default value for the dropdown menu


firstLabelTabThree = tk.Label(tabSearch, text="Search by Coffee ID: ", font=('Rockwell', 12))
firstEntryTabThree = tk.Entry(tabSearch, textvariable=fcoffee_id)
Search_by_id_Button = tk.Button(tabSearch, text="Search by id", command=search_by_id, font=('Rockwell', 10))

# Search by name
secondLabelTabThree = tk.Label(tabSearch, text="Search by Coffee Name: ", font=('Rockwell', 12))
secondEntryTabThree = tk.Entry(tabSearch, textvariable=fcoffee_name)
Search_by_name_Button = tk.Button(tabSearch, text="Search by name", command=search_by_name, font=('Rockwell', 10))

# Search by roast
roast_label = tk.Label(tabSearch, text="Search by Roast:", font=('Rockwell', 12))
roast_option_menu = tk.OptionMenu(tabSearch, roast_var, "Light", "Medium-Light", "Medium", "Medium-Dark", "Dark",)
roast_search_button = tk.Button(tabSearch, text="Search by Roast", command=search_by_roast, font=('Rockwell', 10))

roast_prev_button = tk.Button(tabSearch, text="Previous Roast Result Page", command=search_by_roast_prev, font=('Rockwell', 10))
roast_next_button = tk.Button(tabSearch, text="Next Roast Result Page", command=search_by_roast_next, font=('Rockwell', 10))

# Search by origin
origin_list = ["Bolivia", "Brazil", "Burundi", "Colombia", "Costa Rica", "Democratic Republic Of The Congo",
               "Dominican Republic", "Ecuador", "El Salvador", "Ethiopia", "Guatemala", "Hawai'I", "Honduras",
               "Indonesia", "Kenya", "Mexico", "Nepal", "Nicaragua", "Panama", "Peru", "Philippines", "Rwanda",
               "Taiwan", "Tanzania", "Thailand", "Uganda", "Yemen"]

origin_label = tk.Label(tabSearch, text="Search by Origin:", font=('Rockwell', 12))
origin_option_menu = tk.OptionMenu(tabSearch, forigin, *origin_list)
origin_search_button = tk.Button(tabSearch, text="Search by Origin", command=search_by_origin, font=('Rockwell', 10))

origin_prev_button = tk.Button(tabSearch, text="Previous Origin Result Page", command=search_by_origin_prev, font=('Rockwell', 10))
origin_next_button = tk.Button(tabSearch, text="Next Origin Result Page", command=search_by_origin_next, font=('Rockwell', 10))

# Search by rating
rating_list = [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

rating_label = tk.Label(tabSearch, text="Search by Rating:", font=('Rockwell', 12))
rating_option_menu = tk.OptionMenu(tabSearch, frating, *rating_list)
rating_search_button = tk.Button(tabSearch, text="Search by Rating", command=search_by_rating, font=('Rockwell', 10))

rating_prev_button = tk.Button(tabSearch, text="Previous Rating Result Page", command=search_by_rating_prev, font=('Rockwell', 10))
rating_next_button = tk.Button(tabSearch, text="Next Rating Result Page", command=search_by_rating_next, font=('Rockwell', 10))

# Image
imgSearchTab3 = image_path(path)
imgLabelSearchTab3 = tk.Label(tabSearch, image=imgSearchTab3)

###SEARCH TAB LAYOUT###
# Search by ID
firstLabelTabThree.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabThree.grid(row=0, column=1, padx=15, pady=15)
Search_by_id_Button.grid(row=0, column=2, padx=15, pady=15)

# Search by name
secondLabelTabThree.grid(row=1, column=0, padx=15, pady=15)
secondEntryTabThree.grid(row=1, column=1, padx=15, pady=15)
Search_by_name_Button.grid(row=1, column=2, padx=15, pady=15)

# Search by roast
roast_label.grid(row=2, column=0, padx=15, pady=15)
roast_option_menu.grid(row=2, column=1, padx=15, pady=15)
roast_search_button.grid(row=2, column=2, padx=15, pady=15)

roast_prev_button.grid(row=3, column=1, padx=15, pady=15)
roast_next_button.grid(row=3, column=2, padx=15, pady=15)

# search by origin
origin_label.grid(row=4, column=0, padx=15, pady=15)
origin_option_menu.grid(row=4, column=1, padx=15, pady=15)
origin_search_button.grid(row=4, column=2, padx=15, pady=15)

origin_prev_button.grid(row=5, column=1, padx=15, pady=15)
origin_next_button.grid(row=5, column=2, padx=15, pady=15)

# search by rating
rating_label.grid(row=6, column=0, padx=15, pady=15)
rating_option_menu.grid(row=6, column=1, padx=15, pady=15)
rating_search_button.grid(row=6, column=2, padx=15, pady=15)

rating_prev_button.grid(row=7, column=1, padx=15, pady=15)
rating_next_button.grid(row=7, column=2, padx=15, pady=15)

###image layout###
imgLabelSearchTab3.grid(row=0, rowspan=8, column=3, padx=75, pady=15)

###################UPDATE TAB###################
###widgets###
# Create labels and entry boxes for each attribute
entry_boxes = {}

# Update by ID
update_by_id_label = ttk.Label(tabUpdate, text="Update by ID:", font=('Rockwell', 12))
update_by_id_entry = ttk.Entry(tabUpdate)
entry_boxes['coffee_id'] = update_by_id_entry

# Name
name_label = ttk.Label(tabUpdate, text="Name:", font=('Rockwell', 12))
name_entry = ttk.Entry(tabUpdate)
entry_boxes['name'] = name_entry

# Roaster
roaster_label = ttk.Label(tabUpdate, text="Roaster:", font=('Rockwell', 12))
roaster_entry = ttk.Entry(tabUpdate)
entry_boxes['roaster'] = roaster_entry

# Roast
roast_label = ttk.Label(tabUpdate, text="Roast:", font=('Rockwell', 12))
roast_entry = ttk.Entry(tabUpdate)
entry_boxes['roast'] = roast_entry

# Loc_country
loc_country_label = ttk.Label(tabUpdate, text="Loc_country:", font=('Rockwell', 12))
loc_country_entry = ttk.Entry(tabUpdate)
entry_boxes['loc_country'] = loc_country_entry

# Origin
origin_label = ttk.Label(tabUpdate, text="Origin:", font=('Rockwell', 12))
origin_entry = ttk.Entry(tabUpdate)
entry_boxes['origin'] = origin_entry

# Price
price_label = ttk.Label(tabUpdate, text="Price:", font=('Rockwell', 12))
price_entry = ttk.Entry(tabUpdate)
entry_boxes['price'] = price_entry

# Rating
rating_label = ttk.Label(tabUpdate, text="Rating:", font=('Rockwell', 12))
rating_entry = ttk.Entry(tabUpdate)
entry_boxes['rating'] = rating_entry

# Date
date_label = ttk.Label(tabUpdate, text="Date:", font=('Rockwell', 12))
date_entry = ttk.Entry(tabUpdate)
entry_boxes['date'] = date_entry

# Review
review_label = ttk.Label(tabUpdate, text="Review:", font=('Rockwell', 12))
review_entry = ttk.Entry(tabUpdate)
entry_boxes['review'] = review_entry

update_button = ttk.Button(tabUpdate, text="Update Entry", command=update_coffee_entry)

# Image
imgSearchTab4 = image_path(path3)
imgLabelSearchTab4 = tk.Label(tabUpdate, image=imgSearchTab4)

#####################SEARRCH TAB LAYOUT###################
update_by_id_label.grid(column=0, row=0, padx=10, pady=10)
update_by_id_entry.grid(column=1, row=0)

name_label.grid(column=0, row=1, padx=10, pady=10)
name_entry.grid(column=1, row=1)

roaster_label.grid(column=0, row=2, padx=10, pady=10)
roaster_entry.grid(column=1, row=2)


roast_label.grid(column=0, row=3, padx=10, pady=10)
roast_entry.grid(column=1, row=3)

loc_country_label.grid(column=0, row=4, padx=10, pady=10)
loc_country_entry.grid(column=1, row=4)

origin_label.grid(column=0, row=5, padx=10, pady=10)
origin_entry.grid(column=1, row=5)

price_label.grid(column=0, row=6, padx=10, pady=10)
price_entry.grid(column=1, row=6)

rating_label.grid(column=0, row=7, padx=10, pady=10)
rating_entry.grid(column=1, row=7)

date_label.grid(column=0, row=8, padx=10, pady=10)
date_entry.grid(column=1, row=8)

review_label.grid(column=0, row=9, padx=10, pady=10)
review_entry.grid(column=1, row=9)

update_button.grid(column=0, row=10, columnspan=2, pady=10)

###image layout###
imgLabelSearchTab4.grid(row=0, rowspan=11, column=3, padx=200, pady=30)


###################TAB DELETE##################################
delete_id_label = tk.Label(tabDelete, text="Delete by ID:", font=('Rockwell', 12))

delete_id_entry = tk.Entry(tabDelete)

delete_id_button = tk.Button(tabDelete, text="Delete", command=delete_by_id, font=('Rockwell', 13))

# Image
imgSearchTab5 = image_path(path4)
imgLabelSearchTab5 = tk.Label(tabDelete, image=imgSearchTab5)

###################DELETE TAB LAYOUT#################
delete_id_label.grid(row=0, column=0, padx=5, pady=5)
delete_id_entry.grid(row=0, column=1, padx=5, pady=5)
delete_id_button.grid(row=0, column=2, padx=5, pady=5)

###image layout###
imgLabelSearchTab5.grid(row=0, rowspan=8, column=3, padx=200, pady=30)



######################################MAIN CODE######################################
success = load_database_results()

if success:
    fcoffee_id.set(rows[0][0])
    fname.set(rows[0][1])

tab_parent.pack(expand=1, fill='both')
app.mainloop()
