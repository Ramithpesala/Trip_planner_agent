from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_list:List[str] = []

    try:
        # Open and read the requirments.txt file
        with open('requiremnts.txt', 'r') as file:
            # Read lines from the file
            lines = file.readline()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileExistsError:
        print("requirements.txt file not found.")

    return requirement_list
print(get_requirements())
setup(
    name="AI Trip Planner Agent",
    version=0.0.1,
    author="Ramith Pesala",
    packages=find_packages(),
    install_requires=get_requirements()
)