# sql_requests.py
# MM 2020 7 avril
# module of sql request string

# ----------------------------------------------
# -----------
# CATEGORY  |
# -----------

# get all category
index_category = "SELECT * FROM T_Category"

# show one category NEED ARGUMENT id_category
show_category = "SELECT * FROM `T_Category` WHERE `id_category` = %(id_category)s "

# create category
create_category = "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, " \
                  "%(name)s, %(description)s, CURRENT_TIMESTAMP); "

# update category

update_category = "UPDATE `T_Category` SET `name` = %(name)s, `description` = %(description)s WHERE " \
                  "`T_Category`.`id_category` = %(id)s; "

# ----------------------------------------------
# -----------
# ITEM  |
# -----------

# create item
create_item = "INSERT INTO `T_Item` (`id_item`, `fk_category`, `name`, `description`, `created_at`) VALUES (NULL, " \
              "%(id_category)s, %(name)s, %(description)s, CURRENT_TIMESTAMP); "

# update item
update_item = "UPDATE `T_Item` SET `name` = %(name)s, `description` = %(description)s WHERE `T_Item`.`id_item` = %(" \
              "id)s; "

# show item by category NEED ID_CATEGORY
show_item_by_category = "SELECT * FROM `T_Item` WHERE `fk_category` = %(id_category)s "

# ----------------------------------------------
# -----------
# TIQET  |
# -----------

# create tiqet
create_tiqet = """INSERT INTO `T_Tiqet` (`id_tiqet`, `fk_priority`, `fk_reporter`, `fk_assigned`, `fk_item`, `title`, 
`content`, `fk_state`, `created_at`) VALUES (NULL, %(id_priority)s, %(id_reporter)s, %(id_assigned)s, %(id_item)s, 
%(title)s, %(content)s, %(id_state)s, CURRENT_TIMESTAMP); """

# get index of tiqet, inner join STATE, PRIORITY etc
index_tiqet = """ SELECT T_Tiqet.id_tiqet, T_Tiqet.title, T_Tiqet.content, T_Tiqet.created_at, 
                  T_Priority.id_priority, T_Priority.name AS "name_priority", 
                  T_State.id_state, T_State.name as "name_state",
                  T_Item.id_item, T_Item.name as "name_item", T_Item.fk_category as "id_category",
                  T_User.id_user, T_User.username
                  FROM T_Tiqet 
                  LEFT OUTER JOIN T_Priority ON T_Tiqet.fk_priority= T_Priority.id_priority
                  LEFT OUTER JOIN T_State ON T_Tiqet.fk_state = T_State.id_state
                  LEFT OUTER JOIN T_Item ON T_Tiqet.fk_item = T_Item.id_item
                  LEFT OUTER JOIN T_User ON T_Tiqet.fk_assigned = T_User.id_user  """

# edit only the state of the tiqet
edit_state_tiqet = "UPDATE `T_Tiqet` SET `fk_state` = %(id_state)s WHERE `T_Tiqet`.`id_tiqet` = %(id_tiqet)s;"

# ----------------------------------------------
# -----------
# STATE  |
# -----------

#  index of state
index_state = "SELECT * FROM `T_State`"

# ----------------------------------------------
# -----------
# PRIORITY  |
# -----------

#  index of priority
index_priorities = "SELECT * FROM `T_Priority`"

# ----------------------------------------------
# -----------
# USERS     |
# -----------

# index of users
index_users_admin = "SELECT * FROM `T_User` WHERE `admin` = 1"
