ARG GCC_VERSION=11

FROM gcc:${GCC_VERSION} AS builder

ARG REDIS_VERSION=stable

# from https://redis.io/topics/quickstart
RUN wget https://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz && \
    tar xvzf redis-${REDIS_VERSION}.tar.gz && \
    cd redis-${REDIS_VERSION} && \
    make CFLAGS="-static" EXEEXT="-static" LDFLAGS="-static"

RUN mkdir -p /output/bin

WORKDIR /output/bin
RUN cp /redis-${REDIS_VERSION}/src/redis-server .
# Choose whatever binary that suits you, and change accordingly the ENTRYPOINT
#RUN cp /redis-${REDIS_VERSION}/src/redis-sentinel .
#RUN cp /redis-${REDIS_VERSION}/src/redis-cli .
#RUN cp /redis-${REDIS_VERSION}/src/redis-benchmark .
#RUN cp /redis-${REDIS_VERSION}/src/redis-check-aof .
#RUN cp /redis-${REDIS_VERSION}/src/redis-check-rdb .

RUN mkdir -p /output/conf
WORKDIR /output/conf
RUN cp /redis-${REDIS_VERSION}/redis.conf .

FROM scratch

COPY --from=builder /output/conf/redis.conf /etc/redis/redis.conf
COPY --from=builder /output/bin/*           /bin/

ENTRYPOINT ["/bin/redis-server", "/etc/redis/redis.conf"]