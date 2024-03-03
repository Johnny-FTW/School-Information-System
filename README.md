# School Information System

This is a Django-based School Information System that facilitates the management of school-related information, including schedules, exams, subjects, and user profiles. The system provides different roles with specific permissions: superuser, teacher, and student.

## Features

- **Roles:**
  - Superuser: Has administrative privileges to manage users.
  - Teacher: Can add, delete, and modify exams with grades for their students.
  - Student: Can view personal information, schedules, exams, subjects, classmates, and more.

- **Permissions:**
  - Only superuser/admin can create users.
  - Teachers have permission to add, delete, and modify exams for their students.
  - All users can change their profiles, which are visible to all users of the information system.

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
   git clone https://github.com/yourusername/school-information-system.git
