## General Requirements

The Web application should use the following technologies, frameworks, and development techniques:

- The application must be implemented using **Django Framework**
    - The application must have at least **10 web pages** :
      - Can be created using **function-based views** or/and **class based-views** ;
      - At least **5 of them must be class-based views**.
    - The application must have at least **5 independent models** (models created by extending, inheritance,
         and one-to-one relation are considered as one model ( for example User <–> Profile )).
    - The application must have at least **5 forms**.
    - The application must have at least **5 templates**.
- Use **PostgreSQL** as a **Database Service**
    - Optionally, you can use **multiple storages** (including PostgreSQL), e.g., files, other Web services,
       databases (e.g., **MySQL** / **MariaDB** / **Oracle** / etc.)
- Use **Django Template Engine** or make the **Front-End** using **JavaScript**.
- **Templates** (your views must return HTML files) **- the same template could be re-used/ used multiple times**
    (according to adjustments, if such needed).
- Implement **Web Page Design** based on **Bootstrap / Google Material Design,** or **design your own**.
- The application must have **login/register/logout** functionality.
- The application must have **a public part** (A part of the website, which is accessible by everyone -
    un/authenticated users and admins).
- The application must have **a private** part (accessible only by authenticated users and admins).
- The application must have **a customized admin site** (accessible only by admins):
    - Add at least 5 custom options (in total) to the admin interface (e.g., filters, list display, ordering, etc.).
- **Unauthenticated users** (public part) **have only 'get' permissions, e.g., landing page, details, about page, and**
    **login/ register 'post' permissions**.
- **Authenticated users** (private part) **have full CRUD for all their created content.**
- **Admins** - at **least 2 groups** of admins:
    - One **must** have permission to do **full CRUD functionalities (superusers)** ;
    - The other/s have permission to do **limited CRUD functionalities (staff)**.
    - User **roles** could be **manageable** from the admin site.
    - Make sure the **role management** is **secured** and **error-safe**.
- Implement **Exception Handling** and **Data Validation** to avoid **crashes** when **invalid data** is entered
    (both **client-side** and **server-side** )
  - When validating data, show appropriate messages to the user


# Project presentation

A blog community platform for the lovers of Philosophy. Each user can create his own content
and comment or like the content of other users.

## <code>Functionality</code>

### Main technologies used:

- Python (Django 4.2.4)
- PostgreSQL
- HTML & CSS
- JavaScript

### Additional technologies used:

- TinyMCE - a widget used for text formatting and styling of the posts

## <code>Pages</code>

### 1. Index page (unauthorized)

![index_page_unauth](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/03594963-0930-41e5-81bb-45f6963c77b3)

### 2. Index page (authorized)

![index_page_auth](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/dbc64cec-7544-4b89-9d66-be7777f6c84c)

### 3. Register page

![register_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/545652a9-486e-4aca-9cd7-185b33eb3ade)

### 4. Login page

![login_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/c539d544-8390-44d7-9a6b-d1e2430b7570)

### 5. Create post page

![create_post_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/3b3015d2-f5c8-4629-bf49-e1025b3eb8b0)

### 6. Edit post page

![edit_post_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/0a09b12d-9a67-474f-937e-918d07a2677a)

### 7. My posts page

![my_posts_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/0acdadfa-729f-4173-9be4-01ef3032b2a1)

### 8. Categories page

![categories_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/fd8af4f6-c61b-4f09-834e-9afe6187fe10)

### 9. Post details page + comments section

![post_details_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/1ee8b903-1e05-4eeb-afaf-53a8c94409bc)
![comments_section](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/0e7d6e00-40b4-493c-b0a5-4c3e284ea230)

### 10. My profile page

![my_profile_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/4b2a3f2f-8061-40a5-9dad-f022fb9b58f9)

### 11. Edit profile page

![edit_profile_page](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/90f2b4e6-1e68-4875-9fe9-d886785dcbea)

### 12. Admin panel

![admin_panel](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/49b7123b-1e42-40fb-bd44-8b727de2b771)
![admin_panel_1](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/082a28ed-6ab4-401a-8f0c-c51dc9c82ede)
![admin_panel_2](https://github.com/b-hristov/PhilosophersBlog_Django_final_project/assets/77896833/8b469704-c3ef-42b2-9f1a-f762f678af8b)