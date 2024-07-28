# Build Container
FROM golang:alpine as builder

WORKDIR /app

COPY video7/go-app/go.* ./
RUN go mod download

COPY video7/go-app/* ./
RUN go build -mod=readonly -v -o server

# Application Container
FROM debian:12.5-slim

RUN mkdir /app
RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/server /app/server
CMD ["/app/server"]