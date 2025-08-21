# 🔐 Password Generator Project

Welcome to the Password Generator Project! This is a simple yet powerful tool built using **Python** and **Streamlit** that allows users to generate different types of secure passwords.


## 🧩 Features

This project supports four types of password generators:

1. **Pin Password**: A simple numeric PIN with a user-defined length.
2. **Words Password**: A string of random English words. Can be selected randomly from English vocabulary or you you can get the words yourself.
3. **Random Password**: A mix of letters, digits, and special characters. Fully customizable.
4. **Memorable Password**: A combination of human-readable words, letters, digits, and special characters to make your password more secure. Can be customized however you want.


## 📁 Project Structure

```
Password_Generator/
│
├── src/
│   ├── app.py
│   ├── main.py
│
├── README.md
└── requirements.txt
```

## 🚀 How To Run

1. Install dependencies:

```Bash
pip install -r requirements.txt
```

2. Run the app

To run the app, you have to be in the project's file:
```Bash
streamlit run src/app.py
```

## 🧠 How It Works

The main.py file contains all the password generation logic:

pin_password_generator(length)

words_password_generator(length, capitalization, all_capitalized, separator, vocabulary)

random_password_generator(length, include_letters, include_numbers, include_characters)

memorable_password_generator(num)

These functions are imported into app.py, which provides a friendly interface via Streamlit for users to customize and generate their desired passwords.

## 📝 Notes

The project uses the nltk library's English word corpus. The first run will download the corpus automatically.

Ensure you are connected to the internet the first time you run the app to allow NLTK to download required data.

## 📃 License

This project is open-source and available under the MIT License.

## 💬 Contributing

Pull requests and suggestions are welcome! Feel free to open an issue to discuss improvements or report bugs.
