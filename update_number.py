#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    try:
        subprocess.run(['git', 'add', 'number.txt'], check=True)
        date = datetime.now().strftime('%Y-%m-%d')
        commit_message = f"Update number: {date}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed: {e}")
        exit(1)

def git_push():
    try:
        result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        if result.returncode != 0:
            raise Exception("Git push failed")
    except Exception as e:
        print(f"Git push failed: {e}")
        exit(1)

def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)
        git_commit()
        git_push()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 
