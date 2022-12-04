# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:33:46 2022

@author: Satrio Adi Prawiro
"""

import pickle
import json
import csv
import os
from tabulate import tabulate
from time import sleep


list_address_book = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Name': ['Adelia P.', 'Aditiya C.', 'Arif H.', 'Cynthia A.','Dana R.','Danang H.', 'Ernasanti', 'Erik R.','F. Ridwan', 'Fadillatin S.', 'Ghani D.', 'Ghina B. C.'],
    'Gender (Male/Female)': ['Female', 'Male', 'Male', 'Female','Female','Male','Female','Male', 'Male','Female', '', 'Female'],
    'Address': ['', 'Pondok Sari', '', 'Jl. Kemang 4', 'Perum Batu Indah','','Jl. Rasing 20','Sukasari Mall','Pantai Selatan 4','', 'Depok', 'Bojong aja'],
    'Phone Number': ['078784738', '067294667', '012968344', '','088637112','073667321','','033293859','088736211','', '099372911', '093738271'],
    'Age': ['34', '22', '13', '9','20','16','','35','33','', '20', '23'],
    'Profession': ['Docter', 'Student', 'Employee', 'Student','Freelancer','','Analyst','Director', 'Employee','', 'Police', 'Nurse']
}

colmn = ['ID', 'Name', 'Gender (Male/Female)', 'Address', 'Phone Number', 'Age', 'Profession']


homescreen = [
    '================================================================',
    '                       ADDRESS BOOK APP                         ',
    '================================================================']


def header():
    for i in homescreen:
        print(i, '\n')


def home():
    os.system('cls')
    header()
    menu = [
        '                          MAIN MENU                           \n',
        '    (1) View All Contacts         (6) Delete All Contacts       ',
        '    (2) Create New Contact        (7) Search       ',
        '    (3) Get Contact (ID)          (8) Download Contact (All)                    ',
        '    (4) Update Contact (ID)       (9) Exit App    ',
        '    (5) Delete Contact (ID)       ',
    ]
    for i in menu:
        print(i)


def start():
    home()
    choose_menu()


def wrong_cn():
    homescreen[1] = '                 Wrong Number\Character!\n                        Try Again  '
    start()


def contact_nf():
    homescreen[1] = '                     Contact Not Found!\n                        Try Again.'
    start()


def choose_menu():
    number = int(input('\nChoose one Menu Number : '))
    if number == 1:
        return view_all_contacts()
    elif number == 2:
        return create_user_contact()
    elif number == 3:
        return get_contact_id()
    elif number == 4:
        return update_contact_id()
    elif number == 5:
        return delete_contact_id()
    elif number == 6:
        return delete_all()
    elif number == 7:
        return search()
    elif number == 8:
        return download()
    elif number == 9:
        return exit_app()
    else:
        wrong_cn()


def mini_menu():
    print('\n',homescreen[0])
    back = input('Press Enter to go back to Main Menu.')
    if back == '':
        homescreen[1] = '                  WELCOME TO ADDRESS BOOK APP                   '
        return start()


def view_all_contacts():
    os.system('cls')
    print('\nALL CONTACTS\n')
    #header()
    if list_address_book != {}:
        print(tabulate(list_address_book, headers='keys', tablefmt='fancy_grid'))
    else:
        print('                All contacs has been reset.\n           You can create the new one in Menu')
    
    mini_menu()


def create_user_contact():
    os.system('cls')
    homescreen[1] = '                     CREATE NEW CONTACT                      '
    header()
    print('Input your data below\nPlease fill the data carefully\n=====================================\n')
    name = input('Name                 : ')
    gender = input('Gender (Male/Female) : ')
    address = input('Address              : ')
    ph_number = input('Phone Number         : ')
    age = input('Age                  : ')
    profes = input('Profession           : ')

    submit = input('\nSubmit your data (Y/N)? ')
    if submit == 'Y':
        new_id = len(list_address_book['ID']) + 1
        list_address_book['ID'].append(new_id)
        list_address_book['Name'].append(name)
        list_address_book['Gender (Male/Female)'].append(gender)
        list_address_book['Address'].append(address)
        list_address_book['Phone Number'].append(ph_number)
        list_address_book['Age'].append(age)
        list_address_book['Profession'].append(profes)
        
        homescreen[1] = '                 Your data has been submitted!\n   Check View All Contacts or your last data in Get Contact (ID)  '
        start()
    elif submit == 'N':
        homescreen[1] = '                 Submit has been canceled!'
        start()
    else:
        wrong_cn()


def get_contact_id():
    os.system('cls')
    homescreen[1] = '                   GET CONTACT ID                      '
    header()
    id_ = int(input('Select one ID you will choose: '))
    #os.system('cls')
    dict_new = {'ID': [],
                    'Name': [],
                    'Gender (Male/Female)': [],
                    'Address': [],
                    'Phone Number': [],
                    'Age': [],
                    'Profession': []}
    for i in range(len(list_address_book['ID'])):
        if list_address_book['ID'][i] == id_:
            for i in range(len(list_address_book)):
                dict_new[colmn[i]].append(list_address_book[colmn[i]][id_ - 1])
            
            '''
            dict_new['ID'].append(list_address_book['ID'][id_])
            dict_new['Name'].append(list_address_book['Name'][id_])
            dict_new['Gender (Male/Female)'].append(
                list_address_book['Gender (Male/Female)'][id_])
            dict_new['Address'].append(list_address_book['Address'][id_])
            dict_new['Phone Number'].append(
                list_address_book['Phone Number'][id_])
            dict_new['Age'].append(list_address_book['Age'][id_])
            dict_new['Profession'].append(list_address_book['Profession'][id_])
            
            '''
            
            print('\n', homescreen[0])
            print('\nTABLE RESULT\n')
            print(tabulate(dict_new, headers='keys', tablefmt='fancy_grid'))
            mini_menu()
            
    else:
        wrong_cn()


def update_contact_id():
    head_update = '    UPDATE CONTACT ID                    '
    os.system('cls')
    print(head_update)
    
    print(tabulate(list_address_book, headers='keys', tablefmt='fancy_grid'))
    id_ = int(input('\nSelect one ID you will update :  '))
    
    os.system('cls')
    print(head_update)
    print('\nUpdate the data below\nPlease fill the data carefully\nIf you want to empty the data, press Enter\n=====================================\n')
    #Space, then 
    
    name2 = input('Name                 : ')
    gender2 = input('Gender (Male/Female) : ')
    address2 = input('Address              : ')
    ph_number2 = input('Phone Number         : ')
    age2 = input('Age                  : ')
    profes2 = input('Profession           : ')
    
    res_upd = [name2,gender2,address2,ph_number2,age2,profes2]

    update = input('\nUpdate your data (Y/N)? ')
    
    if update == 'Y':
        for i in range(len(res_upd)):
            list_address_book[colmn[i + 1]][id_ - 1] = res_upd[i]
        homescreen[1] = '                 Your data has been updated!\n   Check View All Contacts or your updated data in Get Contact (ID)  '
        start()
    elif update == 'N':
        homescreen[1] = '                 Update has been canceled!'
        start()
    else:
        wrong_cn()


def delete_contact_id():
    head_update = '                DELETE CONTACT ID                    '
    os.system('cls')
    print(head_update)
    #header()
    print(tabulate(list_address_book, headers='keys', tablefmt='fancy_grid'))
    id2_ = int(input('\nSelect ID from contact you will delete wisely :  '))
    
    confirm_del=input('\nThis will delete only contact based on choosed ID\nAre you sure (Y/N)? ')
    if confirm_del == 'Y':
        for i in range(len(colmn)):
            del list_address_book[colmn[i]][id2_ - 1];
        
        #for x in range((id2_ - 1), len(list_address_book)):
        #    list_address_book['ID'][x] = x - 1
            
        
        homescreen[1] = '                 The ID data has been deleted!\n            Check View All Contacts or Get Contact (ID)  '
        start()
        
    elif confirm_del == 'N':
        homescreen[1] = '                 Data has not been deleted/removed!'
        start()
    else:
        wrong_cn();
    
    
def delete_all():
    os.system('cls')
    homescreen[1] = '                     !!!WARNING!!!\n                  DELETE ALL CONTACTS            '
    header()
    confirm_del_all = input('\nThis will delete ALL CONTACS\nAre you sure (Y/N)? ')
    if confirm_del_all == 'Y':
        list_address_book.clear()
        homescreen[1] = '                   All data has been deleted!'
        start()
    elif confirm_del_all == 'N':
        homescreen[1] = '                 Data has not been deleted/removed!'
        start()


def search():
    os.system('cls')
    homescreen[1] = '                    SEARCH CONTACT              '
    header()
    search = [
        '                            SEARCH MENU                 \n',
        '    (1) Name                         (4) Phone Number     ',
        '    (2) Gender (Male/Female)         (5) Age              ',
        '    (3) Address                      (6) Profession      \n']
    for i in search:
        print(i)
    key = int(input('Which one number will you search contact: '))
    if key > 6 :
        wrong_cn()
    
    word = str(input('Enter the keyword to search: '))
    if word == '' or word == ' ':
        wrong_cn()
    
    dict_search = {'ID': [],
                   'Name': [],
                   'Gender (Male/Female)': [],
                   'Address': [],
                   'Phone Number': [],
                   'Age': [],
                   'Profession': []}
    
    for w in range(len(list_address_book['ID'])):
        for x in colmn:
            if list_address_book[x][w] == word:
                dict_search['ID'].append(list_address_book['ID'][w])
                dict_search['Name'].append(list_address_book['Name'][w])
                dict_search['Gender (Male/Female)'].append(
                list_address_book['Gender (Male/Female)'][w])
                dict_search['Address'].append(list_address_book['Address'][w])
                dict_search['Phone Number'].append(list_address_book['Phone Number'][w])
                dict_search['Age'].append(list_address_book['Age'][w])
                dict_search['Profession'].append(
                    list_address_book['Profession'][w])
                
    os.system('cls')
    print('\nTABLE SEARCH RESULT\n')
    print(tabulate(dict_search, headers='keys', tablefmt='fancy_grid'))
    mini_menu()


def download():
    os.system('cls')
    homescreen[1] = '                  DOWNLOAD ALL CONTACT (EXPERIMENTAL)                           '
    header()
    search = [
        '                                FORMAT FILE                         ',
        '   (1) Comma Seperated Value (.csv)        (3) Text file (.txt)   ',
        '   (2) Json file (.json)                   (4) Pickle file (.pkl) -> binary file only\n']
    for i in search:
        print(i)
    ext = int(input('Select format file to download: '))
    if ext > 4 or type(ext) != int:
        wrong_cn();
    confirm_dow=input("This may be CRUCIAL to leak/braeach user's PRIVATE contact. Are you sure (Y/N)?")
    if confirm_dow =='Y':
        if ext == 1:
            c = csv.writer(open("download.csv", "w"))
            for key, val in list_address_book.items():
                c.writerow([key, val])
        elif ext == 2:
            jfile = json.dumps(list_address_book)
            j = open("download.json", "w") 
            j.write(jfile)
            j.close()
        elif ext == 3:
            t = open("download.txt", "w")
            t.write(str(list_address_book))
            t.close()
        elif ext == 4:
            p = open("download.pkl", "wb") 
            pickle.dump(list_address_book, p)
            p.close()
        homescreen[1] = "            Download has been complete!\n   You can check the file with name 'download'\n         with choosed extention later."
        start()

    elif confirm_dow == 'N':
        homescreen[1] = '                 Download has been canceled!'
        start()
    else:
        wrong_cn()
    

def exit_app():
    os.system('cls')
    homescreen[1] = '                         CONFIRM EXIT                  '
    header()
    confirm = input(
        "All contact changed will not be saved, \nunless you can download into file (experimental).\nAre you sure (Y/N)?  ")
    if confirm == 'Y':
        os.system('cls')
        homescreen[1] = '                    THANK YOU FOR USING APP\n                This app will exit in 3 seconds  '
        header()
        sleep(3)
        os.system('cls')
        exit()
    else:
        start()


start()
