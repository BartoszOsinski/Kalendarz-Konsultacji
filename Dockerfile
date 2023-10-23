FROM python:3.11

WORKDIR /app
COPY . /app

# Use the shell script as the default command
CMD ["./startscript.sh"]