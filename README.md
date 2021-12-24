<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/AlexandraChiritaACS">
    <img src="https://i.ibb.co/P9zzfNC/220-2205436-free-inventory-management-system-logo-clipart-for-warehouse.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Inventory App</h3>

  <p align="center">
    A simple inventory app for a game store implemented with Django and Bootstrap4.
    <br />
    <a href="https://safe-fjord-76052.herokuapp.com/"><strong>View Live »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an inventory app, with multiple sections for the different entities needed to administrate a warehouse:
  - Acquire new products
  - Track shipments and contracts
  - Register clients

The database was created using [the Django admin site](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/) and migrated to PostgreSQL at deployment. The authenication app is created with [User authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/). A diagram is available below:

![Database Diagram](https://i.ibb.co/3sRJByG/Screenshot-4.png)
![Pages](https://i.ibb.co/pZvWnD1/Screenshot-6.pn)
![Charts](https://i.ibb.co/grnHQCb/Screenshot-8.png)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

The project was built with:

* [Django](https://www.djangoproject.com/)
* [Bootstrap4](https://reactjs.org/)
* [ChartJS](https://www.chartjs.org/)
* [PostgreSQL](https://vuejs.org/)
* [Heroku](https://www.heroku.com/about)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

1. Start the server using the command:
  ```sh
  python manage.py runserver
  ```
2. To migrate the updates of the database:
  ```sh
  python manage.py makemigrations
  ```
  ```sh
  python manage.py migrate
  ```
3. To access the admin site, create a superuser:
  ```sh
  python manage.py createsuperuser
  ``` 

The recommended editors for this project are VS Code and Sublime.

### Demo
Visit [here](https://safe-fjord-76052.herokuapp.com/) for a live demo. Use the credentials to test the app.

username: Bob
password: SuperTest

### Prerequisites

* python
  ```sh
  sudo apt-get install python3.8
  ```
* pip
  ```sh
  sudo apt install python3-pip
  ```
* virtualenv
  ```sh
  pip install virtualenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AlexandraChiritaACS/Inventory-Django
   ```

2. Activate virtual environment
  ```sh
  source venv/bin/activate
  ```

3. Install requirements
  ```sh
  pip install -r requirements.txt
  ```

4. Start server
  ```sh
  python manage.py runserver
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project can be used as a template for a new management project of personal inventory.


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

The following resources were used to develop the app.

* [Get started with Django](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
* [Inventory Management System Example](https://github.com/KenBroTech/Django-Inventory-Management-System)
* [STOCK MANAGEMENT SYSTEM IN DJANGO Example](https://www.youtube.com/watch?v=YUiykhw9yGs&list=PL6RgKo1nB4TlJDfWz3czfXHkg8wSn8THV)
* [CodingEntrepreneurs ChartJS Tutorial](https://www.youtube.com/watch?v=B4Vmm3yZPgc&t=504s)
* [Coder Foundry Project Idea](https://www.youtube.com/watch?v=6dxXNvatsZQ&t=524s)
* [Pretty Printed Deploy](https://www.youtube.com/watch?v=GMbVzl_aLxM)

<p align="right">(<a href="#top">back to top</a>)</p>

