# Mail Generator

A simple, clean, and efficient email generator that creates **100 valid emails at a time**. Each run provides a new batch of 100 emails. This project is powered by Python and Flask.

## Features

- Generates **100 valid emails per run**
- Works on **both PC and mobile**
- Clean and responsive **web interface**
- Easy to extend and maintain

## How It Works?

This project uses a simple Flask web app that generates a batch of 100 valid emails each time the app is run. The emails are generated using a basic template and random data. **[Educational Purpose Only]**

## Credits

- **Developer:** Rexden
- **Language:** Python
- **Framework:** Flask
- **License:** MIT License

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/r3xden/Email-Generator
```

2. CD to repository:
```bash
cd Email-Generator
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app/init.py
```

5. Open your browser and go to:
```bash
http://localhost:5000
```

## Customization

You can customize the email template in the `utils/email_generator.py` file. You can also add more features like:

- Email validation
- Export to CSV or TXT
- Email sending (with `smtplib`)
- Template switching

## 📌 License

MIT License

Copyright (c) 2025 Rexden

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
