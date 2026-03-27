class TodoPage:
    def __init__(self, page):
        self.page = page
        self.category_input = page.get_by_role("textbox", name="Add List")
        self.add_category_button = page.get_by_role("button", name="+").first
        self.todo_input = page.get_by_role("textbox", name="Enter your todo")
        self.add_todo_button = page.get_by_role("button", name="+").nth(1)
        
    def create_category(self, category_name):
        self.category_input.fill(category_name)
        self.add_category_button.click()

    def navigate_to_category(self, category_name):
        self.page.get_by_role("button", name=category_name).click()
        
    def create_task(self, todo_name):
        self.todo_input.wait_for(state="visible") 
        self.todo_input.fill(todo_name)
        self.add_todo_button.click()    
    
    def check_task(self,task_name):
        
        task_row=self.page.locator(".todo-item").filter(has_text=task_name)
        task_row.locator("form input[type='checkbox']").check()
        
    def uncheck_task(self,task_name):
        
        task_row=self.page.locator(".todo-item").filter(has_text=task_name)    
        task_row.locator("form input[type='checkbox']").uncheck()
        
    def edit_task(self,old_task_name,new_task_name):
        
        task_row=self.page.locator(".todo-item").filter(has_text=old_task_name)
        task_row.get_by_text("Edit").click()
        task_row.locator("input[name=\"content\"]").fill(new_task_name)
        task_row.get_by_role("button", name="Save").click()
        
    def delete_task(self,task_name):
        
        task_row=self.page.locator(".todo-item").filter(has_text=task_name)
        task_row.get_by_role("button", name="Delete").click()
        
    def delete_category(self,category_name):
        category_row=self.page.locator(".category-item").filter(has_text=category_name)
        category_row.get_by_role("button", name="✕").click()  
        
    def get_task_by_name(self,task_name):
        return self.page.locator(".todo-item").filter(has_text=task_name)
    
    def get_category_by_name(self,category_name):
        return self.page.locator(".category-item").filter(has_text=category_name)      
        
        
        
                



