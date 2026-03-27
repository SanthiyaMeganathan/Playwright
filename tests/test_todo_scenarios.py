import pytest
from playwright.sync_api import expect
from pages.todo import TodoPage

Base_url = "http://127.0.0.1:5000/"


#for creating a new category and put new task in it:

def test_create_category_and_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    category="blockchain crowdfunding"
    task="write the smart contract"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    
    
    expect(todo.get_task_by_name(task)).to_be_visible()
    
#updating the existing task:

def test_edit_task(page):
    page.goto(Base_url)
    todo=TodoPage(page)
    
    category="VibeTuber project"
    initial_task="create the website"
    updated_task="create the website and add the blog section"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(initial_task)
    
    #here comes the editing , only this part is different from the previous test case:
    todo.edit_task(initial_task,updated_task)
    
    
    expect(todo.get_task_by_name(updated_task)).to_be_visible()
    

#checking and unchecking a task:

def test_check_and_uncheck_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    
    category = "Daily Tasks"
    task="Go for a run"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    
    #checking the task, by saying 0 we check the first task in the list.
    todo.check_task(task)
    
    #asserting that the task is actually checked?
    
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).to_be_checked()
    
    #unchecking the task:
    
    todo.uncheck_task(task)
    
    #checking do we unchecked:?
    expect(checkbox).not_to_be_checked()
    
#checking only:

def test_check_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    
    category="checking tasks"
    task="check this task"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    
    #here we check the task:
    
    todo.check_task(task)
    #asserting that the task is checked:
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).to_be_checked()

#unchecking only:

def test_uncheck_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    
    category="unchecking tasks"
    task="uncheck this task"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    
    #first we check the task:
    todo.check_task(task)
    
    #then we uncheck the task:
    todo.uncheck_task(task)
    
    #asserting that the task is unchecked:
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).not_to_be_checked()
    
    

#deleting a task:

def test_delete_task(page):
    
    page.goto(Base_url)
    todo =TodoPage(page)
    
    category ="temp list"
    task="task to be deleted"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    
    #here comes the deleting part:
    todo.delete_task(task)
    
    #asserting that the task is deleted:
    expect(todo.get_task_by_name(task)).not_to_be_visible()
    
#deleting a category:

def test_delete_category(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    
    category="old project"
    
    todo.create_category(category)
    
    #deleting the category:
    todo.delete_category(category)
    
    #asserting that the category is deleted:
    expect(todo.get_category_by_name(category)).not_to_be_visible()    
    
    

    
    