"""
Estimated Time: 30 minutes
Actual Time: 67 minutes
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects \n"
        "- (S)ave projects \n"
        "- (D)isplay projects \n"
        "- (F)ilter projects by date \n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    """Program for a project management that track project completion and project details that user wish to complete."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Load {len(projects)} projects from {FILENAME}")
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
           filename = input("Filename: ")
           projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
    if save_choice in ["yes", "y"]:
        save_projects(FILENAME, projects)
        print(f"Projects saved to {FILENAME}.")
    else:
        print("No changes were saved.")
    print("Thank you for using custom-built project management software.")

