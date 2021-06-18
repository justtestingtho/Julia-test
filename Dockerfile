FROM julia:latest

RUN julia -e 'import Pkg; Pkg.update()' && \
    julia -e 'using Pkg; pkg"add NeuralPDE"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add Flux"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add ModelingToolkit"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add GalacticOptim"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add Optim"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add DiffEqFlux"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add JSON3"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add StructTypes"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add Plots"; pkg"precompile"' && \
    julia -e 'using Pkg; pkg"add BSON"; pkg"precompile"'
ENV PATH="/opt/program:${PATH}"
WORKDIR /opt/program
COPY . /opt/program

ENTRYPOINT [ "julia", "./algo/train" ]

