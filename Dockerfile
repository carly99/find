#parent image
FROM python

#cartella di lavoro nell'immagine -> container
WORKDIR home/find

#Copio il file locale dist/find-0.0.1-py3-none-any.whl
COPY dist/find-0.0.1-py3-none-any.whl .

RUN ["python","-m","pip","install","find-0.0.1-py3-none-any.whl"]

ENTRYPOINT ["find"]
