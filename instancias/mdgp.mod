# -- DOMINIOS --
# Grupos 
set M;

# Indivíduos
set N;

# -- PARAMETROS --

# minimo de individuos de g
param a{g in M} >= 0;

# maximo de individuos de g
param b{g in M} >= 0;

# valor da diversidade entre i e j (para cada par de individuos)
param d{i in N,j in N};

# -- VARIAVEIS --

# Relação: individuo i pertence ao grupo g
#     1, se i individuo i pertence ao grupo g
#     0, c.c.
var x{i in N,g in M} binary;

# Relação: individuos i e j estao no mesmo grupo g
#     1, se i e j pertencem ao mesmo grupo g
#     0, c.c.
var y{i in N, j in N, g in M} binary;

# -- FUNCAO OBJETIVO --

maximize obj: sum {g in M, i in N, j in N:i != j} d[min(i,j), max(i,j)] * y[i,j,g];

# -- RESTRIÇOES --

# 4 - todo individuo i pertencente a algum g
s.t. pertenceGrupo{i in N}: sum {g in M} x[i,g] == 1;

# 5 - minimo de individuos em uma equipe g
s.t. minimoIndividuosGrupo{g in M}: sum {i in N} x[i,g] >= a[g];

# 6 - maximo de individuos em uma equipe g
s.t. maximoIndividuosGrupo{g in M}: sum {i in N} x[i,g] <= b[g];

# 7 - exige que se caso dois individuos i e j estao na mesma equipe y[i,j,g] == 1
s.t. individuosMesmoGrupo{g in M,i in N, j in N: i != j}: x[i,g] + x[j,g] - 1 <= y[i,j,g]; #VERIFICARRRRRR POIS EH RELATIVO AS ARESTAS ENAO AOS VERTICES 

# 8 - garante que cada individuo estara se relacionando em uma equipe g com no minimo a[g] individuos
s.t. relIndividuoGrupoMin{j in N,g in M}: sum {i in N: i != j} y[i,j,g] >= (a[g] - 1) * x[j,g];

# 9 - garante que cada individuo estara se relacionando em uma equipe g com no maximo b[g] individuos
s.t. relIndividuoGrupoMax{j in N,g in M}: sum {i in N: i != j} y[i,j,g] <= (b[g] - 1) * x[j,g];



end;