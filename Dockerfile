FROM julia:latest

RUN julia -e 'import Pkg; Pkg.update()' && \
    julia -e 'using Pkg; pkg"add JSON3"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add BSON"; pkg"precompile"' 

ENV PATH="/opt/program:${PATH}"
WORKDIR /opt/program
COPY . /opt/program

ENTRYPOINT [ "julia", "./algo/train" ]

