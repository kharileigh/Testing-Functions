from lib.most_often import *


# ------ constructor function creates empty list 
# ------ arg : starting_list
def test_starting_list_created():
    often = MostOften([])
    result = often.starting_list
    assert result == []


# ------ add new 
# ------ initialise object with empty starting list
# ------ add_new(new_item) 
# ------ assert starting list has new item
def test_add_new_item():
    often = MostOften([])
    often.add_new("item1")
    assert often.starting_list == ["item1"]



# -------LOOP get most often - count number of occurences of item
def test_get_most_often():
    pass


# ------- if condition 
# ------- set count
# ------- set highest count
# ------- set highest items list
# ------- get count of current item
# ------- check if greater than count
# ------- assert added to highest_item




# ------- elif condition 
# ------- set count 8
# ------- set highest count 8
# ------- set highest items list
# ------- count = highest count
# ------- assert added item to highest_item


