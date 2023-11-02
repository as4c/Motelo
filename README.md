# Motelo - Hotel Booking Django App

![Home Page](screenshot/home-page.png)

This is a Django web application for hotel booking. It provides users with the ability to book hotels, check hotel availability, manage check-in and checkout, view hotel details, write reviews, and process online payments using the Stripe API.

## Features

- **User Authentication** : Users can register, log in, and manage their accounts.
- **Book a New Hotel** : Users can search for hotels, select dates, and make bookings.
- **Check Hotel Availability** : Users can check the availability of hotels for specific dates.
- **Check-in and Checkout** : Users can manage their check-in and checkout dates.
- **Hotel Detail Description** : Users can view detailed information about hotels, including amenities, room types, and location.
- **Write Hotel Rating Reviews** : Users can write and submit reviews/ratings for hotels they have stayed in.
- **Online Booking with Stripe** : Integrated Stripe payment API for secure online payment processing.

## Screenshots  

**HomePage** 
![home-page](https://github.com/as4c/Motelo/assets/84590258/5a674010-2ca3-4aff-89a8-0671b6a271b3)

**Search result page**
![search-result](https://github.com/as4c/Motelo/assets/84590258/60badfd4-b72a-4cf2-88aa-e191238e26d0)

**Hotel Detail Page**
![hotel-detail](https://github.com/as4c/Motelo/assets/84590258/ea5937ff-4757-425f-abb0-2f0ea0ee332a)

**Hotel Services Page**
![services](https://github.com/as4c/Motelo/assets/84590258/bd404d36-8aa3-42cd-9b18-17acb913cf52)


**Hotel available page**
![available](https://github.com/as4c/Motelo/assets/84590258/78bd4a27-02ba-43b5-a6d7-3a11f73a9062)

**Booking Form**
![booking-form](https://github.com/as4c/Motelo/assets/84590258/fd295a4d-95d2-4743-a58e-5316adf2d126)

**Payment page**
![payment-page](https://github.com/as4c/Motelo/assets/84590258/efa9ee6e-5648-442d-948f-cf8c767e830f)

**Payment Successfull page**
![payment-successfull](https://github.com/as4c/Motelo/assets/84590258/0b2fa7c4-c48c-4c57-a48b-669c4d285d06)


## Installation

1. Clone the repository:
```
git clone https://github.com/as4c/Motelo.git
```


2. Change into the project directory:
3. Create a virtual environment:
```
python3 -m venv env
```


4. Activate the virtual environment:

- For Windows:
  ```
  .\env\Scripts\activate
  ```

- For Linux/Mac:
  ```
  source env\bin\activate
  ```

5. Install the required dependencies:
```
pip instatll -r requirements.txt
```


6. Set up the database:


7. Run the development server:
```
python manage.py migrate
```




8. Open your web browser and visit `http://localhost:8000` to access the application.

## Configuration

Before running the app, make sure to configure the following settings:

- Database Configuration: Update the database settings in the `settings.py` file.
- Stripe API Configuration: Set up your Stripe API keys in the `settings.py` file.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix:
```
git checkout -b feature/my-feature
```


3. Make your changes and commit them:
```
git commit -m "Add new feature"
```


4. Push the changes to your forked repository:
```
git push origin feature/my-feature
```

5. Open a pull request on the original repository.

## License

This project is licensed under the [MIT License](LICENSE).
