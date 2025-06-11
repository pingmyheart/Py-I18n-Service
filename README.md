# PY-I18N-SERVICE

*Python based internationalization service*

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/Py-I18n-Service)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/Py-I18n-Service)
![Issues](https://img.shields.io/github/issues/pingmyheart/Py-I18n-Service)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/Py-I18n-Service)
![License](https://img.shields.io/github/license/pingmyheart/Py-I18n-Service)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/Py-I18n-Service)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/Py-I18n-Service)

## Why Py-I18n-Service?

This project provides a simple and efficient way to manage internationalization (i18n). The core features include:

- 🌐 **Multi-language Support**: Easily manage translations for multiple languages.
- 📦 **Lightweight**: Built with Python, ensuring a minimal footprint.
- 🤝 **Open Source Collaboration**: Built under the MIT License, promoting innovation and community contributions.
- 🚀 **Productivity Boost**: Streamlines the i18n process, allowing developers to focus on building features rather than
  managing translations.

# Getting started

## Files Structure

Translation file are simply key value pairs stored through properties files. The file naming convention is
`translation-<language_code>.properties`, where `<language_code>` is the ISO 639-1 code for the language (e.g.,
`translation-en.properties` for English, `translation-it.properties` for Italian).

## Native Installation

1. **Clone the repository**:

```bash
git clone https://github.com/pingmyheart/Py-I18n-Service.git
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:

```bash
export TRANSLATION_FOLDER=/home/user/translation
```

4. **Run the service**:

```bash
python main.py
```

## Docker Installation

1. **Pull the Docker image**:

```bash
docker pull ghcr.io/pingmyheart/py-i18n-service:${VERSION}
```

2. **Run the Docker container**:

```yaml
services:
  i18n:
    image: ghcr.io/pingmyheart/py-i18n-service:${VERSION}
    environment:
      - TRANSLATION_FOLDER=/opt/i18n/translation
    volumes:
      - ./translation:/opt/i18n/translation
    ports:
      - "8080:8080"
```

# Usage

```bash
curl --location 'localhost:8080/py-i18n-service/translation?key=placeholder.insertion.dateTime&language=en'
```