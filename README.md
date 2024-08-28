# Телеграм user-бот с которым можно общаться
Для запуска нужно установить [ollama](https://ollama.com/) и установить модель llama3.1 при помощи команды 
```
ollama run llama3.1
```
так же нужно установить python библиотеки
```
pip install pyrogram python-decouple
```
ещё нужно сделать файлы с названием `.env` который содержит
```
API_ID=https://my.telegram.org/apps

API_HASH=https://my.telegram.org/apps

PHONE=phone number

LOGIN=telegram login

URL_OLLAMA=localhost
```
если вы будете сервер на котором установлена ollama то настройте его по [этому гайду](https://github.com/ollama/ollama/blob/main/docs/faq.md) и вставьте ip адрес сервера ollama'ы в `URL_OLLAMA`
