from db.DELETE.delete_db import DBDelete

print("Write id of you're table.")
number = input("> ")
request = "DELETE FROM `T_Category` WHERE `T_Category`.`id_category` = %(id)s"
x = DBDelete.delete_one_record(request, number)




