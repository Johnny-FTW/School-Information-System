# School Information System

This is a Django-based School Information System that facilitates the management of school-related information, including schedules, exams, subjects, and user profiles. The system provides different roles with specific permissions: superuser, teacher, and student.

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

This project is licensed under the MIT License.
