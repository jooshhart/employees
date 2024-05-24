import sqlite3

def create_tables():
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_department(name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO departments (name) VALUES (?)
    ''', (name,))
    
    conn.commit()
    conn.close()

def insert_employee(name, email, department_name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM departments WHERE name = ?', (department_name,))
    department_id = cursor.fetchone()
    if department_id:
        department_id = department_id[0]
        cursor.execute('''
        INSERT INTO employees (name, email, department_id) VALUES (?, ?, ?)
        ''', (name, email, department_id))
    
    conn.commit()
    conn.close()

def search_employee_by_name(name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT employees.id, employees.name, employees.email, departments.name 
    FROM employees
    JOIN departments ON employees.department_id = departments.id
    WHERE employees.name LIKE ?
    ''', ('%' + name + '%',))
    
    employees = cursor.fetchall()
    
    conn.close()
    return employees

def get_employees():
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT employees.id, employees.name, employees.email, departments.name 
    FROM employees 
    JOIN departments ON employees.department_id = departments.id
    ''')
    employees = cursor.fetchall()
    
    conn.close()
    return employees

def get_departments():
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM departments')
    departments = cursor.fetchall()
    
    conn.close()
    return departments

def update_department(old_name, new_name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE departments SET name = ? WHERE name = ?', (new_name, old_name))
    
    conn.commit()
    conn.close()

def update_employee(employee_id, name=None, email=None, department_name=None):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    if name:
        cursor.execute('UPDATE employees SET name = ? WHERE id = ?', (name, employee_id))
    if email:
        cursor.execute('UPDATE employees SET email = ? WHERE id = ?', (email, employee_id))
    if department_name:
        cursor.execute('SELECT id FROM departments WHERE name = ?', (department_name,))
        department_id = cursor.fetchone()
        if department_id:
            department_id = department_id[0]
            cursor.execute('UPDATE employees SET department_id = ? WHERE id = ?', (department_id, employee_id))
    
    conn.commit()
    conn.close()

def delete_department(name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM departments WHERE name = ?', (name,))
    department_id = cursor.fetchone()
    if department_id:
        department_id = department_id[0]
        cursor.execute('DELETE FROM employees WHERE department_id = ?', (department_id,))
        cursor.execute('DELETE FROM departments WHERE id = ?', (department_id,))
    
    conn.commit()
    conn.close()

def delete_employee(name):
    conn = sqlite3.connect('employee_directory.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM employees WHERE name = ?', (name,))
    
    conn.commit()
    conn.close()