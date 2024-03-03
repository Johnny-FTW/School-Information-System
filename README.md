[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# School Information System

This is a Django-based School Information System that facilitates the management of school-related information, including schedules, exams, subjects, and user profiles. The system provides different roles with specific permissions: superuser, teacher, and student.

## Built With
* [![Python][Python.org]][Python-url]
* [![Django][Django.com]][Django-url]
* [![HTML][HTML.com]][HTML-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![SQL][SQL.com]][SQL-url]


## Features

- **Roles:**
  - Superuser: Has administrative privileges to manage users.
  - Teacher: Can add, delete, and modify exams with grades for their students.
  - Student: Can view personal information, schedules, exams, subjects, classmates and more.

- **Permissions:**
  - Only superuser/admin can create users.
  - Teachers have permission to add, delete, and modify exams for their students.
  - All users can change their profiles, which are visible to all users of the information system.
  - Students can also upload own profile picture.

- **Accessible Information:**
  - All logged-in users can access:
    - Own schedule
    - Own exams
    - Own subjects
    - Own classmates
    - Classroom details
    - User profiles
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Johnny-FTW/School-Information-System.git

2. Navigate to the project directory:

   ```bash
   cd school-information-system

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Apply migrations:

   ```bash
   python manage.py migrate

5. Run the development server:

   ```bash
   python manage.py runserver

6. Access the application at http://localhost:8000 in your web browser.

## Usage
- **Creating Users:**
  - Log in as a superuser/admin.
  - Navigate to the user management section.
  - Create new users with appropriate roles.
  - Managing Exams (Teachers Only):

- **Log in as a teacher.**
  - Access the exam management section.
  - Add, delete, or modify exams and grades for students.
  
- **Updating Profiles:**
  - All users can update their profiles.
  -Changes made to profiles are visible to all users.
  -Students can upload their profile pictures 

- **Viewing Information:**
  - Log in as any user (teacher or student).
  - Access personal schedules, exams, subjects, classmates, and more from the respective sections.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch: git checkout -b feature/NewFeature.
3. Commit your changes: git commit -am 'Add some feature'.
4. Push to the branch: git push origin feature/NewFeature.
5. Submit a pull request.


## License

This project is licensed under the MIT License. See <a href="https://github.com/Johnny-FTW/School-Information-System/blob/main/LICENSE">`LICENSE`</a> for more information.


[Python.org]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/

[HTML.com]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://html.com/

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[SQL.com]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[SQL-url]: https://www.sqlite.org/index.html



[contributors-shield]: https://img.shields.io/github/contributors/Johnny-FTW/School-Information-System.svg?style=for-the-badge
[contributors-url]: https://github.com/Johnny-FTW/School-Information-System/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Johnny-FTW/School-Information-System.svg?style=for-the-badge
[forks-url]: https://github.com/Johnny-FTW/School-Information-System/network/members

[stars-shield]: https://img.shields.io/github/stars/Johnny-FTW/School-Information-System.svg?style=for-the-badge
[stars-url]: https://github.com/Johnny-FTW/School-Information-System/stargazers

[issues-shield]: https://img.shields.io/github/issues/Johnny-FTW/School-Information-System.svg?style=for-the-badge
[issues-url]: https://github.com/Johnny-FTW/School-Information-System/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Johnny-FTW/School-Information-System/blob/main/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jan-hatapka-6b970b205/
