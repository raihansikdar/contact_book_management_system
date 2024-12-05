import csv

def remove_contact_function(phone_to_remove: int, all_contact: list):
    try:
        with open("all_contact_book.csv", mode="r", encoding='utf-8') as fp:
            fpReader = csv.DictReader(fp)
            headers = fpReader.fieldnames

            if not headers:
                print("-----The CSV file is empty or malformed.-----")
                return
            
            contact_found = False
            updated_contacts = []
            
            for contact in fpReader:
                if contact['phone_number'] == str(phone_to_remove):  
                    print("Yes, contact found!")
                    contact_found = True
                    continue  
                updated_contacts.append(contact)
            
            all_contact[:] = [c for c in all_contact if c['phone_number'] != str(phone_to_remove)]

        if contact_found:
            with open("all_contact_book.csv", mode="w", newline="", encoding='utf-8') as fp:
                csv_writer = csv.DictWriter(fp, fieldnames=headers)
                csv_writer.writeheader()
                csv_writer.writerows(updated_contacts)
            print("------ Contact removed successfully!------")
        else:
            print("------ Contact not found!---------")

    except FileNotFoundError:
        print("-----The file was not found. Please ensure the file exists.-----")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


