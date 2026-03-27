import pytest
from playwright.sync_api import expect
from pages.todo import TodoPage

Base_url = "http://127.0.0.1:5000/"

def test_create_category_and_task(page):
    page.goto(Base_url)
    todo=TodoPage(page)
    category="blockchain crowdfunding"
    task="write the smart contract"
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    expect(todo.get_task_by_name(task)).to_be_visible()
    
def test_edit_task(page):
    page.goto(Base_url)
    todo=TodoPage(page)
    category="VibeTuber project"
    initial_task="create the website"
    updated_task="create the website and add the blog section"
    
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(initial_task)
    todo.edit_task(initial_task,updated_task)
    expect(todo.get_task_by_name(updated_task)).to_be_visible()

def test_check_and_uncheck_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)  
    category = "Daily Tasks"
    task="Go for a run"  
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    todo.check_task(task)
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).to_be_checked()
    todo.uncheck_task(task)
    expect(checkbox).not_to_be_checked()

def test_check_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    category="checking tasks"
    task="check this task"
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    todo.check_task(task)
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).to_be_checked()

def test_uncheck_task(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)   
    category="unchecking tasks"
    task="uncheck this task"
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    todo.check_task(task)
    todo.uncheck_task(task)
    checkbox=page.locator(".todo-item").filter(has_text=task).locator("form input[type='checkbox']")
    expect(checkbox).not_to_be_checked()

def test_delete_task(page):
    
    page.goto(Base_url)
    todo =TodoPage(page)
    category ="temp list"
    task="task to be deleted"
    todo.create_category(category)
    todo.navigate_to_category(category)
    todo.create_task(task)
    todo.delete_task(task)
    expect(todo.get_task_by_name(task)).not_to_be_visible()
    


def test_delete_category(page):
    
    page.goto(Base_url)
    todo=TodoPage(page)
    category="old project"
    todo.create_category(category)
    todo.delete_category(category)
    expect(todo.get_category_by_name(category)).not_to_be_visible()    
    
    

    
    