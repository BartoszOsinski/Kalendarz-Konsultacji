from routes import *

# Watch for file changes and execute the update script
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Run the Flask application with debug mode enabled for development
