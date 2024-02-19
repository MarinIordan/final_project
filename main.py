import json
from flask_cors import CORS

from flask import Flask

app = Flask(__name__)
CORS(app)

def new_slide():
    while True:
        title = input("Add a title to Slide: ")
        description = input("Add description to Slide: ")
        photo = input("Add a link to photo: ")
        slides = all_slide()

        slide_data = slides+[{
            "title": title,
            "description": description,
            "photo": photo
        }]
        with open('slides.json', 'w') as file:
            json.dump(slide_data, file)
            file.write('\n')

        add_more = input("Do you want to add another slide? (yes/no): ").lower()
        if add_more != "yes":
            break


def modify_slide():
    slides = all_slide()
    if not slides:
        print("No slides found.")
        return
    while True:
        print("Slides available for modification:")
        for i, slide in enumerate(slides):
            print(f"{i + 1}. {slide['title']}")

        choice = input("Enter the number of the slide you want to modify (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(slides):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        slide_to_modify = slides[choice - 1]

        print(f"\nModifying slide: {slide_to_modify['title']}")
        new_title = input(f"Enter new title (press Enter to keep current '{slide_to_modify['title']}'): ")
        new_description = input(
            f"Enter new description (press Enter to keep current '{slide_to_modify['description']}'): ")
        new_photo = input(f"Enter new photo link (press Enter to keep current '{slide_to_modify['photo']}'): ")

        if new_title:
            slide_to_modify['title'] = new_title
        if new_description:
            slide_to_modify['description'] = new_description
        if new_photo:
            slide_to_modify['photo'] = new_photo

        slides[choice - 1] = slide_to_modify  # Update the slide in the list
        save_slides(slides)  # Save the modified slides
        print("Slide modified successfully.")

def delete_slide():
    slides = all_slide()
    if not slides:
        print("No slides found.")
        return

    while True:
        print("Slides available for deletion:")
        for i, slide in enumerate(slides):
            print(f"{i + 1}. {slide['title']}")

        choice = input("Enter the number of the slide you want to delete (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(slides):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        del slides[choice - 1]
        save_slides(slides)  # Save the modified slides after deletion
        print("Slide deleted successfully.")

def all_slide():
    try:
        with open('slides.json', 'r') as file:
            slides = json.load(file)
    except FileNotFoundError:
        slides = []
    return slides


def save_slides(slides):
    with open('slides.json', 'w') as file:
        json.dump(slides, file)

def main():
    while True:
        print('Choose the number corresponding to your option')
        print('1. Add new slide')
        print('2. Modify a slide')
        print('3. Delete a slide')
        print('4. See all slide')
        print('0. Exit')
        main_option = input('Choose: ')
        match main_option:
            case '1':
                new_slide()
            case '2':
                modify_slide()
            case '3':
                delete_slide()
            case '4':
                slides = all_slide()
                for slide in slides:
                    print(f"Title: {slide['title']}, Description: {slide['description']}, Photo: {slide['photo']}")
            case '0':
                  exit()

if __name__ == "__main__":
    main()



@app.route("/")
def getSlides():
    slides = all_slide()

    return slides

# cd Tekwill/final_project/
# flask --app main run