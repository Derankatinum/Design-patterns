"""Contains Developer, QAEngineer and PM implementation.

class Developer
class QAEngineer
class ProjectManager

"""

from __future__ import annotations
import itertools
from abc import abstractmethod
from random import random
from typing import List, TYPE_CHECKING, Any
from dataclasses import dataclass
if TYPE_CHECKING:
    from project import Project, Assignment


@dataclass
class personal_info:
    id: int
    name: str
    surname: str
    adress: str
    phone_number: str
    position: str
    rank: str
    salary: float
    """lab 2 abstract methods"""
class Employee(personal_info):
    @abstractmethod
    def calculate_salary(self, salary: Developer) -> None:
        pass

    @abstractmethod
    def ask_sick_leave(self, project_manager: ProjectManager) -> bool:
        pass

class Developer(Employee):
    """Developer representation.

    Attributes:
        _id (int): Developers ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        projects (List[Projects]): List of assigned projects
                            (many-to-many with Project instance).
        assignments (List[Assignment]): List of assigned tasks in
                                    Assignment container.

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str) -> None:
        """Developer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.projects: List[Project] = []
        self.assignments: List[Assignment] = []

    """lab 2 abstract methods"""
    def calculate_salary(self, salary: Developer) -> None:
        print(f'Salary of {self.full_name} is {self.salary}')

    def ask_sick_leave(self, project_manager: ProjectManager) -> None:
        project_manager.ill_requests.append(f'student {self.name} is ill')
        rand = bool(random.getrandbits(1))
        if rand is True:
            return print(f'{self.name} are free')
        else:
            return print('sit on your assignment')

    """lab 2 abstract methods finish"""
    def get_assigned_projects(self) -> List[str]:
        """Returns all project titles assigned to developer.

         Arguments:
            None.

        Returns:
            List[str], list of project titles

        """
        return [project.title for project in self.projects]

    def __str__(self):
        """String representation of the Developer"""
        return f"Developer {self.full_name}"


class QAEngineer(Employee):
    """QA engineer representation.

    Attributes:
        _id (int): QAEngineer ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        projects (List[Projects]): List of assigned projects
                        (many-to-many with Project instance).

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str) -> None:
        """QAEngineer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.projects: List[Project] = []

    def test_feature(self, assignment: Assignment) -> str:
        """Simply the stub method, will be implemented in future.

        Arguments:
            assignment (Assignment): assignment obtained from the developer.

        Returns:
            String contains dummy info about testing:).
        """
        return f"Assignment {assignment.description} has been tested " \
               f"by {self.full_name}"

    def calculate_salary(self, salary: Developer) -> None:
        print(f'Salary of {self.full_name} is {self.salary}')

    def ask_sick_leave(self, project_manager: ProjectManager) -> None:
        project_manager.ill_requests.append(f'student {self.name} is ill')
        rand = bool(random.getrandbits(1))
        if rand is True:
            return print(f'{self.name} are free')
        else:
            return print('sit on your assignment')


class ProjectManager(Employee):
    """Project manager representation.

    Attributes:
        _id (int): PM's ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        project (Projects): Assume PM -> Project relation.

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str,
                 project: Project) -> None:
        """ProjectManager initializer.
        """
        self._id = next(self.id_iter)
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.project: project = project
        self.ill_requests: List[Any] = []
    def discuss_progress(self, developer: Developer) -> str:
        """Simply the stub method, will be implemented in future.

        Arguments:
            developer (Developer): Processing the developer's progress.

        Returns:
            String contains dummy discussion:).

        """

        # Let's obtain each assignment description.
        descriptions = [assignment.description for assignment in developer.assignments]
        # concat list of strings (descriptions) into one string
        descriptions = " ".join(descriptions)
        return f"Task's progress of {descriptions} has been tested " \
               f"by {self.full_name}"

    def calculate_salary(self, salary: Developer) -> None:
        print(f'Salary of {self.full_name} is {self.salary}')

    def ask_sick_leave(self, project_manager: ProjectManager) -> None:
        project_manager.ill_requests.append(f'student {self.name} is ill')
        rand = bool(random.getrandbits(1))
        if rand is True:
            return print(f'{self.name} are free')
        else:
            return print('sit on your assignment')


class AssignManagement:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def assign(developer: Developer, project: Project) -> None:
        """Assigns current developer to project instance.

        Args:
            project (Project): Project instance to be assigned to developer.

        Returns:
            None.
        Moved function in lab 2
        """
        if project in developer.projects:
            raise ValueError(f"Project {project.title} already exists")
        developer.projects.append(project)
        print(f"Project {project.title} has been added to developer "
              f"{developer.full_name}")
    @staticmethod
    def unassign(developer: Developer, project: Project) -> None:
        """Assigns current developer to project instance.

        Arguments:
            project (Project): Project instance to be removed from developer.

        Returns:
            None.
        Moved function in lab 2
        """
        if project in developer.projects:
            developer.projects.remove(project)
            print(f"Project {project.title} has been removed from developer {developer.full_name}")