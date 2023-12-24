# Stage 1: Build Redis
ARG GCC_VERSION=11
FROM gcc:${GCC_VERSION} AS builder

ARG REDIS_VERSION=stable

# from https://redis.io/topics/quickstart
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz && \
    tar xvzf redis-${REDIS_VERSION}.tar.gz && \
    cd redis-${REDIS_VERSION} && \
    make CFLAGS="-static" EXEEXT="-static" LDFLAGS="-static"

RUN mkdir -p /output/bin

WORKDIR /output/bin
RUN cp /redis-${REDIS_VERSION}/src/redis-server .

RUN mkdir -p /output/conf
WORKDIR /output/conf
RUN cp /redis-${REDIS_VERSION}/redis.conf .

# Stage 2: Use a minimal base image with shell
FROM debian:buster-slim

# Copy binaries and configuration from the builder stage
COPY --from=builder /output/conf/redis.conf /etc/redis/redis.conf
COPY --from=builder /output/bin/* /bin/

# Set up directories and permissions for PID file
RUN mkdir -p /var/run/redis && \
    chown -R nobody:nogroup /var/run/redis

# Set sysctl values to enable memory overcommit
RUN echo "vm.overcommit_memory = 1" > /etc/sysctl.conf

# Entry point
ENTRYPOINT ["/bin/redis-server", "/etc/redis/redis.conf"]
