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
    """Program to manage and track project details and completion status."""
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


def load_projects(filename):
    """Load projects from a file and return a list of project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(completion_percentage)))
    return projects


def save_projects(filename, projects):
    """Save projects to a file in tab-separated format."""
    with open(filename, "w", newline="") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")