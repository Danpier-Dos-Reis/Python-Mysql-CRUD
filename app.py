from Engine import engine
import json

def main():
    engine.initialize()

    while True:
        print("\nCRUD Menu:")
        print("1. Create item")
        print("2. Read all items")
        print("3. Read item by ID")
        print("4. Update item")
        print("5. Delete item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            nombre = input("Enter name: ")
            fecha = input("Enter date (YYYY-MM-DD): ")
            linkurl = input("Enter URL: ")
            nulos = input("Enter additional info (or leave empty): ")
            engine.create_item(nombre, fecha, linkurl, nulos)
            print("Item created successfully.")

        elif choice == "2":
            items = engine.read_items()
            serializable_items = [
                {
                    "id": item[0],
                    "nombre": item[1],
                    "fecha": str(item[2]) if item[2] else None,
                    "linkurl": item[3],
                    "nulos": item[4],
                }
                for item in items
            ]
            print(json.dumps(serializable_items, indent=4))

        elif choice == "3":
            item_id = int(input("Enter item ID: "))
            item = engine.read_item(item_id)
            if item:
                serializable_item = {
                    "id": item[0],
                    "nombre": item[1],
                    "fecha": str(item[2]) if item[2] else None,
                    "linkurl": item[3],
                    "nulos": item[4],
                }
                print(json.dumps(serializable_item, indent=4))
            else:
                print("Item not found.")

        elif choice == "4":
            item_id = int(input("Enter item ID: "))
            nombre = input("Enter new name: ")
            fecha = input("Enter new date (YYYY-MM-DD): ")
            linkurl = input("Enter new URL: ")
            nulos = input("Enter new additional info (or leave empty): ")
            engine.update_item(item_id, nombre, fecha, linkurl, nulos)
            print("Item updated successfully.")

        elif choice == "5":
            item_id = int(input("Enter item ID: "))
            engine.delete_item(item_id)
            print("Item deleted successfully.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()