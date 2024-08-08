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



# ------- IF CONDITION MET --- item1 has most occurences = highest_item
# ------- one set of duplicates = 1 winner
def test_get_most_often_winner():
    often = MostOften([])
    often.add_new("item1")
    often.add_new("item1")
    often.add_new("item2")
    assert often.get_most_often() == "item1"
    


# ------- ELSE CONDITION -- no clear winner for all other conditions
# ------- two sets of duplicates = no winner
def test_get_most_often_no_clear_winner():
    often = MostOften([])
    often.add_new("item1")
    often.add_new("item1")
    often.add_new("item2")
    often.add_new("item2")
    assert often.get_most_often() == "no clear winner"
    

# ------ EMPTY LIST
def test_get_most_often_with_nothing():
    often = MostOften([])
    assert often.get_most_often() == "no clear winner"





