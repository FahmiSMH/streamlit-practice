whoa
additional Requirement

installed tesseract
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe

to build the Dockerfile
docker build -t paperclip . 

to run the build
docker run -p 8080:8501 paperclip