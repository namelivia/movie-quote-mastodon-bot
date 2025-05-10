# TODO: I've been unable to make this work with alpine because of problems with pybind11
FROM python:3.11 AS builder
WORKDIR /app
COPY . /app
RUN pip install poetry

FROM builder AS development
RUN poetry install
EXPOSE 4444

FROM builder AS production
RUN poetry install --without dev
CMD ["poetry", "run", "python", "main.py"]
