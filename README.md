# Blog App

[Visit the Project](http://3.27.149.95/)

Welcome to the Blog App repository! This is a simple Django-based blogging platform that allows users to create, read, update, and delete blog posts. Users can also log in using their GitHub account for added convenience.

## Features

- User Registration and Authentication
  - Users can sign up and log in using their email and password.
  - Social authentication via GitHub is also available.

- Blog Management
  - Authenticated users can create, edit, and delete their own blog posts.
  - Blog list displays the title and owner of each blog post.
  - Users can search for specific blog posts by title.

- Styling and UI
  - Basic CSS styling enhances the visual appeal of the application.
  - Forms are styled using Crispy Forms with Bootstrap.

## Setup

1. Clone the Repository:
```bash
git clone https://github.com/your-username/blog-app.git
```

```bash
cd blog-app
```

2. Create and Activate a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate
```


3. Install Dependencies:
```bash
pip install -r requirements.txt
```


4. Configure Environment Variables:
- Create a `.env` file in the root directory.
- Add your Django secret key and GitHub API credentials as environment variables. Example:
  ```
  SECRET_KEY=your_django_secret_key
  GITHUB_CLIENT_ID=your_github_client_id
  GITHUB_CLIENT_SECRET=your_github_client_secret
  ```

5. Apply Migrations:
```
python manage.py migrate
```


6. Run the Development Server:
```
python manage.py runserver
```


7. Access the Application:
Open your browser and go to `http://127.0.0.1:8000/` to access the blog app.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
