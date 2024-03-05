# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Tesseract OCR
# Install any needed packages specified in requirements.txt
# Download NLTK resources
RUN apt-get update && apt-get install -y tesseract-ocr \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m nltk.downloader stopwords \
    && python -m nltk.downloader wordnet

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "source/main.py"]
