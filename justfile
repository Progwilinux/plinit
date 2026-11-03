build:
    mkdir -p dist
    crystal build src/main.cr --release --target "x86_64-pc-linux-gnu" -o dist/plinit
clean:
    rm -rf dist