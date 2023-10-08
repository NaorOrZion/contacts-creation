from flask import Blueprint, render_template, request, flash, get_flashed_messages, send_file
from pathlib import Path
import os
from website import google_contacts

navigation = Blueprint('navigation', __name__)

XLSX_TEMPLATE_PATH = "../website/downloads/contacts_template.xlsx"

def run_create_contacts_script(file_path: str, key_words: str):
    names, phone_numbers, current_courses, is_error = google_contacts.add_contacts_from_excel(file_path=file_path, key_words=key_words)
    return names, phone_numbers, current_courses, is_error


def delete_file_uploaded(file_path: str):
    os.remove(file_path)


def save_file():
    file = request.files['contacts_file']
    file_name = file.filename
    file_path = 'website/uploads/' + file_name

    if file_name == "":
        flash("צריך לבחור קובץ לפני שמתחילים", "warning")
        file.close()
        return "No file was found"
    
    file.save(file_path)
    file.close()

    return file_path


@navigation.route('/', methods=['GET', 'POST'])
def create_contacts():
    if request.method == 'POST':
        file_path = save_file()
        if file_path == "No file was found": 
            return render_template("create_contacts.html")
        else:
            key_words = request.form.get('text_box')
            print(key_words)
            names, phone_numbers, current_courses, is_error = run_create_contacts_script(file_path, key_words)
            delete_file_uploaded(file_path=file_path)

            if is_error:
                return render_template("create_contacts.html")
            
            return render_template("contacts_created.html", names=names, phone_numbers=phone_numbers, current_courses=current_courses)
        
    else:
        return render_template("create_contacts.html")
    

@navigation.route('/download_template', methods=['GET'])
def download_template_xlsx():
    return send_file(XLSX_TEMPLATE_PATH, as_attachment=True)
