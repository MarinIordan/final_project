from functionalities import *



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




# cd Tekwill/final_project/
# flask --app main run


