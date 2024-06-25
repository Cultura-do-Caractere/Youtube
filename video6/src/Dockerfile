FROM golang:latest

# pre-copy/cache go.mod for pre-downloading dependencies and only redownloading them in subsequent builds if they change
COPY ./src/ /opt/

WORKDIR /opt/

RUN go mod download && go mod verify

EXPOSE 1323

CMD ["go","run","/opt/main.go"]