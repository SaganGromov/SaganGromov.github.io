[E]{.lettrine}m geral, a grande maioria dos cálculos de Geometria
Riemanniana se resumem a provar igualdades tensoriais. Isso geralmente é
realizado de uma das três maneiras a seguir:

-   *a maneira livre de coordenadas*: nesse caso, explicitamos a ação de
    cada tensor em campos arbitrários na variedade em questão,
    verificando que os resultados coincidem.

-   *usando coordenadas locais*: nesse caso, fixamos coordenadas locais
    apropriadas que facilitem os cálculos (por exemplo, coordenadas
    normais) e tomamos vantagem da multilinearidade dos tensores, que
    garante que a igualdade só precisa ser verificada numa base
    (conforme detalhado em **[@MeuTextoLivre]**).

-   *usando o método do referencial móvel*: nesse caso, fixamos um
    referencial ortonormal local (que induz um co-referencial ortonormal
    local) e calculamos as $1$-formas e $2$-formas de conexão e
    curvatura, respectivamente, que determinam a conexão e curvatura da
    variedade.

Dependendo da situação, um dos três métodos acima pode ser
significativamente mais fácil de ser aplicado do que os outros dois.
Nessa subseção, nos dedicaremos, com base na referência **[@TuRiem]**, a
explorar o suficiente às nossas aplicações do último método citado
acima.

Seja $(\mathcal{M}^n, g)$ uma variedade Riemanniana e fixe
$\{\mathbf{e}_1, \ldots, \mathbf{e}_n \}$ um referencial local
$g$-ortonormal definido num aberto $U \subset \mathcal{M}$, sendo
$\{\mathbf{e}^1, \ldots, \mathbf{e}^n\}$ o co-referencial associado
(determinado por $\mathbf{e}^i(\mathbf{e}_j) = \delta^i_j$). Como
qualquer campo $X \in \Gamma(T \mathcal{M})$ se escreve localmente como
$$\Gamma(TU) \ni  X|_{U} = \sum_{1 \leq j \leq n} X^j \, \mathbf{e}_j, \text{ onde } \{ X^j \}_{1 \leq j \leq n} \subset \mathscr{C}^{\infty}(\mathcal{M})$$
então dada $s \in \Gamma(TU)$ podemos determinar (usando a linearidade
de $\nabla$ na primeira entrada e a regra de Leibniz) $\nabla_X s$ pelo
conhecimento dos campos $\{\nabla_X \mathbf{e}_j \}_{1 \leq j \leq n}$.
Sendo um campo em $U$, $\nabla_X \mathbf{e}_j$ é uma combinação linear
dos $\mathbf{e}_i$'s com coeficientes $\omega^{i}_j$ dependendo de $X$,
*id est:*
$$\nabla_X \mathbf{e}_j = \sum_{1 \leq i \leq n} \omega^{i}_j(X) \, \mathbf{e}_i$$
A $\mathscr{C}^{\infty}(\mathcal{M})$-linearidade de
$\nabla_X \mathbf{e}_j$ em $X$ garante a
$\mathscr{C}^{\infty}(\mathcal{M})$-linearidade de $\omega^{i}_j$ em
$X$, de forma que $\omega^{i}_j \in \Gamma(T^{*} U)$ é uma $1$-forma em
$U$. As $1$-formas $\omega^{i}_j$ em $U$ são chamadas das ***formas de
conexão***, e a matriz $\omega = (\omega^{i}_j)_{1 \leq i, j \leq n}$ é
chamada da ***matriz de conexão***, da conexão $\nabla$ com respeito ao
referencial $\{\mathbf{e}_i \}_{1 \leq i \leq n} \subset \Gamma(T U)$.

Analogamente, dados $X, Y \in \Gamma(T U)$, o campo
$\mathrm{Rm}(X, Y)\mathbf{e}_j$ é uma combinação linear de
$\mathbf{e}_1, \ldots, \mathbf{e}_n$, *id est:*
$$\mathrm{Rm}(X, Y) \mathbf{e}_j = \sum_{1 \leq i \leq n} \Omega^{i}_j(X, Y) \, \mathbf{e}_i$$
Uma vez que
$$\mathrm{Rm}(X, Y) = \nabla_X \nabla_Y - \nabla_Y \nabla_X - \nabla_{[X, Y]}$$
é alternada e $\mathscr{C}^{\infty}(\mathcal{M})$-bilinear,
$\Omega^{i}_j$ também é alternada e
$\mathscr{C}^{\infty}(\mathcal{M})$-bilinear. Pelas propriedades de
$\mathrm{Rm}$, $\Omega^{i}_j$ é portanto uma $2$-forma em $U$. As
$2$-formas $\Omega^{i}_j$ são chamadas das ***formas de curvatura***, e
a matriz $\Omega = (\Omega^{i}_j)$ é chamada da matriz de curvatura, da
conexão $\nabla$ com respeito ao referencial
$\{\mathbf{e}_1, \ldots, \mathbf{e}_n \}$ em $U$.

Note que $\Omega^{i}_j$ é determinada por $\mathrm{Rm}$, pois
$$\begin{aligned}
\Omega^{i}_j &= \frac{1}{2} \, \sum_{1 \leq k, \ell \leq n}  \, \Omega^i_j(\mathbf{e}_k, \mathbf{e}_{\ell}) \, \mathbf{e}^k \wedge \mathbf{e}^{\ell} \\
&= -\frac{1}{2} \,  \sum_{1 \leq k, \ell \leq n} \mathrm{Rm}(\mathbf{e}_i, \mathbf{e}_j, \mathbf{e}_k, \mathbf{e}_{\ell})  \, \mathbf{e}^k \wedge \mathbf{e}^{\ell}
\end{aligned}$$ onde a última igualdade segue do fato de que
$$\begin{aligned}
\Omega^i_j(\mathbf{e}_k, \mathbf{e}_{\ell}) &= g\left( \sum_{1 \leq t \leq n} \Omega^{s}_j(\mathbf{e}_k, \mathbf{e}_{\ell}) \mathbf{e}_s, \mathbf{e}_i \right) \\
&= g\left( \mathrm{Rm}(\mathbf{e}_k, \mathbf{e}_{\ell}) \mathbf{e}_j, \mathbf{e}_i \right) \\
&= - \mathrm{Rm}(\mathbf{e}_i, \mathbf{e}_j, \mathbf{e}_k, \mathbf{e}_{\ell})
\end{aligned}$$

Cálculos diretos mostram os seguintes resultados:

[\[PrimeiraUnicaCartan\]]{#PrimeiraUnicaCartan
label="PrimeiraUnicaCartan"} Seja $(\mathcal{M}^n, g)$ uma variedade
Riemanniana e $U \subset \mathcal{M}$ um aberto em qual está definido um
referencial ortonormal $\mathbf{e}_1, \ldots, \mathbf{e}_n$, com
co-referencial associado $\mathbf{e}^1, \ldots, \mathbf{e}^n$. Então
existe uma matriz antissimétrica
$\left(\omega^{i}_j \right)_{1 \leq i, j \leq n}$ de $1$-formas tal que
$$\mathrm{d}\mathbf{e}^i + \sum_{1 \leq j \leq n} \omega^{i}_j \wedge \mathbf{e}^j = 0, \text{ seja qual for } 1 \leq i \leq n$$
Além disso, se $\left(\alpha^{i}_j \right)_{1 \leq i, j \leq n}$ é
qualquer outra matriz antissimétrica de $1$-formas satisfazendo
$$\mathrm{d}\mathbf{e}^i + \sum_{1 \leq j \leq n} \alpha^{i}_j \wedge \mathbf{e}^j = 0, \text{ seja qual for } 1 \leq i \leq n$$
então
$$\left(\alpha^{i}_j \right)_{1 \leq i, j \leq n} = \left(\omega^{i}_j \right)_{1 \leq i, j \leq n}$$

[\[SegEqEstrCartan\]]{#SegEqEstrCartan label="SegEqEstrCartan"} As
formas de curvatura $\Omega^{i}_j$ se relacionam às formas de conexão
$\omega^{i}_j$ pela seguinte equação, comumente chamada da **segunda
equação estrutural de Cartan**:
$$\Omega^{i}_j = \mathrm{d}\, \omega^{i}_j + \sum_{1 \leq k \leq n} \omega^{i}_k \wedge \omega^k_j, \text{ sejam quais forem } \{i, j\} \subset \{1, \ldots, n \}$$

Consulte **[@TuRiem]**.

$\rule{0.7em}{0.7em}$

Um dos conceitos mais importantes e frutíferos de geometria Riemanniana
é o *produto warped* de variedades Riemannianas, que generaliza o
produto Riemanniano comum. Tal conceito também tem grande relevância na
física, aparecendo na teoria da relatividade como modelo do próprio
Cosmos ou de buracos negros (veja, por exemplo, o modelo cosmológico de
Friedmann--Lemaître--Robertson--Walker).

Sejam $(\mathcal{B}, g_{B})$ e $(\mathcal{M}_i, g_{\mathcal{M}_i})$
variedades Riemannianas e $b_i: \mathcal{B}\to (0, \infty)$ funções
suaves para cada $i \in \{1, 2, \cdots, k \}$. O produto warped múltiplo
de tais variedades é a variedade produto
$\mathcal{N}= \mathcal{B}\times \mathcal{M}_1 \times \mathcal{M}_2 \times \cdots \times \mathcal{M}_k$
munida da métrica
$g = g_{\mathcal{B}} \oplus b_1^2 g_{\mathcal{M}_1} \oplus b_2^2 g_{\mathcal{M}_2} \oplus \cdots \oplus b_{k}^2 g_{\mathcal{M}_k}$
definida por
$$g = \sigma_0^{*} (g_{\mathcal{B}}) \oplus \left(b_1 \circ \pi \right)^2 \sigma_1^{*}\left(g_{\mathcal{M}_1} \right ) \oplus \cdots \oplus \left(b_k \circ \pi \right)^2 \sigma_{k}^{*} \left( g_{\mathcal{M}_k} \right)$$
onde $\sigma_0 : \mathcal{N}\to \mathcal{B}$ é a aplicação definida por
$$\begin{aligned}
\sigma_0: \mathcal{N}&\to \mathcal{B}\\
(p, q_1, \cdots, q_k) &\mapsto p \in \mathcal{B}\end{aligned}$$ e para
$i \geq 1$, $\sigma_i : \mathcal{N}\to \mathcal{M}_i$ é a aplicação
definida por $$\begin{aligned}
\sigma_i: \mathcal{N}&\to \mathcal{M}_i \\
(p, q_1, \cdots, q_i, \cdots, q_k) &\mapsto q_i \in \mathcal{M}_i\end{aligned}$$

-   É comum denotar a variedade Riemanniana
    $(\mathcal{N}=  \mathcal{B}\times \mathcal{M}_1 \times \mathcal{M}_2 \times \cdots \times \mathcal{M}_k, g = g_{\mathcal{B}} \oplus b_1^2 g_{\mathcal{M}_1} \oplus b_2^2 g_{\mathcal{M}_2} \oplus \cdots \oplus b_{k}^2 g_{\mathcal{M}_k})$
    simplesmente por
    $\mathcal{N}= \mathcal{B}\times_{h_1} \mathcal{M}_1^{d_1} \times \cdots \times_{h_k} \mathcal{M}_{k}^{d_k}$

-   Quando $k = 1$, temos o produto warped simples usual.

-   Se todos $b_i \equiv 1$, temos um produto Riemanniano trivial.

Se $\varphi: \mathcal{M}\to \mathcal{N}$ é uma aplicação suave, diremos
que dois campos $X \in \Gamma(T \mathcal{M})$ e
$Y \in \Gamma(T \mathcal{N})$ estão $\varphi$-relacionados (fato que
denotaremos por $X \overset{\varphi}{\sim} Y$) quando
$Y \circ \varphi = \mathrm{d}\varphi \circ X$.

O espaço tangente $T_p \mathcal{M}$ de um ponto
$p = (p_0, p_1, \cdots, p_k) \in \mathcal{M}= \mathcal{B}\times \mathcal{N}_1 \times \cdots \times \mathcal{N}_k$
é canonicamente isomorfo (no sentido de existir um isomorfismo que não
depende de escolhas de bases) ao produto
$T_{p_0} \mathcal{B}\times T_{p_1} \mathcal{N}_1 \times \cdots \times T_{p_k} \mathcal{N}_k$.

Considere as aplicações $$\begin{aligned}
\iota_0 : \mathcal{B}&\to \mathcal{M}\\
\mathcal{B}\ni q_0 &\mapsto \left( q_0, p_1, \ldots, p_k \right) \in \mathcal{M}\end{aligned}$$
e, para $\alpha \geq 1$, $$\begin{aligned}
\iota_{\alpha}: \mathcal{N}_{\alpha} &\to \mathcal{M}\\
\mathcal{N}_{\alpha} \ni q_{\alpha} &\mapsto \left(  p_0, p_1, \ldots, p_{\alpha - 1}, q_{\alpha}, p_{\alpha + 1}, \ldots, p_k \right)\end{aligned}$$
Afirmo que a aplicação $\psi$ definida por $$\begin{aligned}
\psi: T_{(p_0, p_1, \cdots, p_k)} \left( \mathcal{B}\times \mathcal{N}_1 \times \cdots \times \mathcal{N}_k \right)&\to T_{p_0} \mathcal{B}\times T_{p_1} \mathcal{N}_1 \times \cdots \times T_{p_k} \mathcal{N}_k  \\
v &\mapsto \left( \mathrm{d}\left( \sigma_0 \right)_{p}(v), \mathrm{d}\left( \sigma_1 \right)_{p}(v),  \mathrm{d}\left( \sigma_2 \right)_{p}(v), \cdots, \mathrm{d}\left( \sigma_k \right)_{p}(v) \right)\end{aligned}$$
é um isomorfismo, com inversa dada por $$\begin{aligned}
\varphi: T_{p_0} \mathcal{B}\times T_{p_1} \mathcal{N}_1 \times \cdots \times T_{p_k} \mathcal{N}_k &\to  T_{(p_0, p_1, \cdots, p_k)} \left( \mathcal{B}\times \mathcal{N}_1 \times \cdots \times \mathcal{N}_k  \right)\\
\left( v_0, v_1, \ldots, v_k \right) &\mapsto \sum_{0 \leq \ell \leq k}\mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}}\left( v_{\ell} \right)\end{aligned}$$
Inicialmente, note que $$\sigma_i \circ \iota_{\ell} = \begin{cases}
\text{a aplicação identidade } \mathrm{Id}_{\mathcal{N}_i} : \mathcal{N}_i \to \mathcal{N}_i, \text{ se $i = \ell$ } \\
\text{a aplicação constante } \mathcal{N}_{\ell} \ni q_{\ell} \mapsto p_i \in \mathcal{N}_i, \text{ se $i \neq \ell$}
\end{cases}$$ E portanto, segue da regra da cadeia que
$$\label{RegCadL116}
\begin{aligned}
\mathrm{d}\left( \sigma_i \circ \iota_{\ell}   \right)_{p_{\ell}} &= \mathrm{d}\left(  \sigma_i  \right)_p \circ \mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}} \\
&=\begin{cases}
\text{a aplicação identidade } \mathrm{Id}_{T_{p_{i}}\mathcal{N}_{i}} : T_{p_{i}}\mathcal{N}_i \to T_{p_{i}}\mathcal{N}_i, \text{ se $i = \ell$ } \\
\text{a aplicação identicamente nula } T_{p_{\ell}} \mathcal{N}_{\ell} \ni v_{\ell} \mapsto 0 \in  T_{p_{\ell}} \mathcal{N}_{\ell}, \text{ se $i \neq \ell$}
\end{cases}
\end{aligned}$$ Portanto, seja qual for
$\left( v_0, v_1, \ldots, v_k \right) \in T_{p_0} \mathcal{B}\times T_{p_1} \mathcal{N}_1 \times \cdots \times T_{p_k} \mathcal{N}_k$,
temos $$\begin{aligned}
\left( \psi \circ \varphi \right) \left( v_0, v_1, \ldots, v_k \right) &= \left(  \mathrm{d}\left( \sigma_0 \right)_p \left(   \sum_{0 \leq \ell \leq k}\mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}}\left( v_{\ell} \right) \right) , \ldots,\mathrm{d}\left( \sigma_k \right)_p \left(   \sum_{0 \leq \ell \leq k}\mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}}\left( v_{\ell} \right) \right)   \right) \\
&=\left( \sum_{0 \leq \ell \leq k} \mathrm{d}\left( \sigma_0 \right)_p \left(  \mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}}\left( v_{\ell} \right) \right), \ldots, \sum_{0 \leq \ell \leq k} \mathrm{d}\left( \sigma_k \right)_p \left(  \mathrm{d}\left( \iota_{\ell} \right)_{p_{\ell}}\left( v_{\ell} \right) \right)  \right) \\
&=\left( v_0, v_1, \ldots, v_k \right)\end{aligned}$$ onde na última
igualdade usamos [\[RegCadL116\]](#RegCadL116){reference-type="ref"
reference="RegCadL116"}. Segue que $\psi$ é sobrejetiva. Como
$T_{(p_0, p_1, \cdots, p_k)} \left( \mathcal{B}\times \mathcal{N}_1 \times \cdots \times \mathcal{N}_k \right)$
e
$T_{p_0} \mathcal{B}\times T_{p_1} \mathcal{N}_1 \times \cdots \times T_{p_k} \mathcal{N}_k$
têm a mesma dimensão, segue que $\psi$ é um isomorfismo. Como uma
aplicação bijetora possui um único inverso à direita, segue também que
$\varphi$ é o inverso de $\psi$.

$\rule{0.7em}{0.7em}$

Para cada $i \in \{0, 1, \cdots, k\}$, o conjunto dos campos em
$\mathcal{M}$ que surgem como levantamentos de campos em fatores do
produto será denotado por
$$\mathcal{L}(\mathcal{N}_i) = \{ X \in \Gamma(T \mathcal{M}) \ \vert \ \mathrm{d}\sigma_j (X) = 0, \text{ seja qual for $j\neq i$} \}$$
Dado $X_i \in \Gamma(T \mathcal{N}_i)$, é fácil ver que existe um único
campo $\text{Lev}(X_i) \in \mathcal{L}(\mathcal{N}_i)$ que satisfaz
$\left( \mathrm{d}\sigma_i \circ \text{Lev} \right)(X_i) = X_i$ (de
fato,
$\text{Lev}(X_i) = \psi^{-1}\left((0, \cdots, X_i, 0, \cdots, 0) \right)$).
O campo $\text{Lev}(X_i)$ é chamado do levantamento do campo $X_i$. O
abuso de notação de identificar um campo ou uma $1$-forma com seu
levantamento é portanto inofensivo, e o cometeremos várias vezes daqui
em diante. Note que $\text{Lev}(X_i)$ é o único campo
$\sigma_i$-relacionado com $X_i$ e $\sigma_j$-relacionado com
$0 \in \Gamma(T \mathcal{N}_j)$ para todo $j \neq i$.

Convém agora relembrarmos a equação de Gauss. Dizemos que uma aplicação
entre variedades Riemannianas
$f: \left( \mathcal{M}^n, g_{\mathcal{M}}  \right) \to \left( \widetilde{\mathcal{M}}^{n+p}, \widetilde{g}_{\widetilde{\mathcal{M}}^{n+p}} \right)$
é uma imersão isométrica quando vale
$$f^{*}\left(  \widetilde{g}_{\widetilde{\mathcal{M}}^{n+p}}  \right) =  g_{\mathcal{M}}$$
ou, equivalentemente,
$$g_{\mathcal{M}}(p) \left(  v, w  \right) = \widetilde{g}_{\widetilde{\mathcal{M}}^{n+p}}\left( f(p) \right) \left(  \mathrm{d}f_p(v), \mathrm{d}f_p(w)  \right)$$
sejam quais forem $p \in \mathcal{M}$ e $v, w \in T_{p} \mathcal{M}$.
Nesse caso, cometendo o abuso usual de identificar campos com suas
extensões, temos $$\label{EquacaoGauss}
\widetilde{\mathrm{Rm}}(X, Y, Z, W) = \mathrm{Rm}(X, Y, Z, W) - \widetilde{g}_{\widetilde{\mathcal{M}}^{n+p}} \left(  \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(X, W), \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(Y, Z)  \right) +  \widetilde{g}_{\widetilde{\mathcal{M}}^{n+p}} \left(  \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(X, Z), \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(Y, W)  \right)$$
sejam quais forem $X, Y, Z, W \in \Gamma(T \mathcal{M})$. Nesse sentido,
é importante ressaltar que, uma vez que fixarmos
$$p = (p_0, p_1, \ldots, p_k) \in \mathcal{M}= \mathcal{B}\times \mathcal{N}_1 \times \ldots \times \mathcal{N}_{k}$$
a inclusão $$\begin{aligned}
\iota_{\alpha}: \left(  \mathcal{N}_{\alpha}, g_{\mathcal{N}_{\alpha}}  \right) &\xhookrightarrow{}  \mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1 \times \ldots \times_{h_k} \mathcal{N}_{k} \\
q_{\alpha} &\mapsto  \left( p_0, \ldots, p_{\alpha - 1}, q_{\alpha}, p_{\alpha + 1}, \ldots, p_k  \right) 
\end{aligned}$$ *não* é uma imersão isométrica. De fato, fixando
arbitrariamente $q_{\alpha} \in \mathcal{N}_{\alpha}$ e denotando
$$P = \left( p_0, \ldots, p_{\alpha - 1}, q_{\alpha}, p_{\alpha + 1}, \ldots, p_k  \right)$$
temos $$\label{NaoIsometrica}
\begin{aligned}
\left[\left( \iota_{\alpha} \right)^{*}\left(  g_{\mathcal{M}} \right) \right](q_{\alpha})\left( v, w \right) &= g_{\mathcal{M}}(P)\left(  \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( v \right), \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( w \right)  \right) \\
&= h_{\alpha}^2 \left( p_0 \right) \, \left[\left( \sigma_{\alpha} \right)^{*} \left(  g_{\mathcal{N}_{\alpha}} \right) \right]_{P}\left(  \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( v \right), \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( w \right)  \right)  \\
&= h_{\alpha}^2 \left( p_0 \right) \, \left( g_{\mathcal{N}_{\alpha}} \right)_{q_{\alpha}} \left(  \mathrm{d}\left( \sigma_{\alpha} \right)_{P} \left( \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( v \right) \right),  \mathrm{d}\left( \sigma_{\alpha} \right)_{q_{\alpha}} \left( \mathrm{d}\left( \iota_{\alpha} \right)_{q_{\alpha}}\left( w \right) \right) \right) \\
&= h_{\alpha}^2 \left( p_0 \right) \left( q_{\alpha} \right) \, \left( g_{\mathcal{N}_{\alpha}} \right)_{q_{\alpha}}\left( v, w \right)
\end{aligned}$$ onde na última igualdade usamos a equação
[\[RegCadL116\]](#RegCadL116){reference-type="ref"
reference="RegCadL116"}. Porém, é claro dos cálculos feitos em
[\[NaoIsometrica\]](#NaoIsometrica){reference-type="ref"
reference="NaoIsometrica"} que com a métrica
$\left( h_{\alpha}\left( p_0 \right)  \right)^2 \, g_{\mathcal{N}_{\alpha}}$,
a inclusão $$\begin{aligned}
\iota_{\alpha}: \left(  \mathcal{N}_{\alpha}, \left( h_{\alpha}\left( p_0 \right)  \right)^2 \, g_{\mathcal{N}_{\alpha}}  \right) &\xhookrightarrow{}  \mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1 \times \ldots \times_{h_k} \mathcal{N}_{k} \\
q_{\alpha} &\mapsto  \left( p_0, \ldots, p_{\alpha - 1}, q_{\alpha}, p_{\alpha + 1}, \ldots, p_k  \right) 
\end{aligned}$$ *é* uma imersão isométrica, de forma nesse contexto
podemos usar a equação
[\[EquacaoGauss\]](#EquacaoGauss){reference-type="ref"
reference="EquacaoGauss"} (como faremos futuramente).

Embora usualmente a equação
[\[EquacaoGauss\]](#EquacaoGauss){reference-type="ref"
reference="EquacaoGauss"} seja utilizada para determinar a curvatura de
subvariedades, em algumas situações podemos usá-la no sentido contrário:
ou seja, via o conhecimento da curvatura de específicas subvariedades,
podemos determinar a curvatura da variedade total. Um exercício
interessante de Geometria Riemanniana (que comentaremos em mais detalhes
no exemplo
[\[FormaEspacialComoWarped\]](#FormaEspacialComoWarped){reference-type="ref"
reference="FormaEspacialComoWarped"}) que utiliza essa técnica envolve
calcular a curvatura do produto warped
$\mathcal{I} \times_{\varphi} \mathbb{Q}^n(\kappa)$, onde
$\mathcal{I} \subset \mathbb{R}$ é um intervalo,
$\varphi: \mathcal{I} \to (0, \infty)$ é uma função suave, e definimos
$$\mathbb{Q}^n(\kappa) \doteq \begin{cases}
\mathbb{R}^n, \text{ se } \kappa = 0 \\
\mathbb{S}^n, \text{ se } \kappa = 1 \\
\mathbb{H}^n, \text{ se } \kappa = -1 
\end{cases}$$

[\[PushBrack\]]{#PushBrack label="PushBrack"} Se
$\varphi: \mathcal{M}\to \mathcal{N}$ é uma aplicação suave, então
$$\mathrm{d}\varphi([X, Y]) = [\mathrm{d}\varphi(X), \mathrm{d}\varphi (Y)], \ \forall X, Y \in \Gamma(T \mathcal{M})$$

Segue da definição do colchete de Lie e da definição da diferencial de
uma aplicação. De fato, para qualquer $p \in \mathcal{M}$ e
$g \in \mathscr{C}^{\infty}(\mathcal{N})$ temos $$\begin{aligned}
\left( \mathrm{d}\varphi_p\left([X, Y](p) \right) \right)(g) &= [X, Y](p) (g \circ \varphi) \\
&= X_p\left( Y(g \circ \varphi) \right) -  Y_p\left( X(g \circ \varphi) \right) \\
&= X_p \left( \mathrm{d}\varphi(Y)(g) \circ \varphi \right) - Y_p \left( \mathrm{d}\varphi(X)(g) \circ \varphi \right) \\ 
&= \mathrm{d}\varphi_p(X_p)\left( \mathrm{d}\varphi(Y)(g) \right) -  \mathrm{d}\varphi_p(Y_p)\left( \mathrm{d}\varphi(X)(g) \right) \\
&= [\mathrm{d}\varphi (X), \mathrm{d}\varphi(Y)]_p(g)\end{aligned}$$

$\rule{0.7em}{0.7em}$

[\[RelBrack\]]{#RelBrack label="RelBrack"} Se
$\varphi: \mathcal{M}\to \mathcal{N}$ é uma aplicação suave e
$X_1, X_2 \in \Gamma(T \mathcal{M}), Y_1, Y_2 \in \Gamma(T \mathcal{N})$
são campos satisfazendo $X_i \stackrel{\varphi}{\sim} Y_i$ para cada
$1 \leq i \leq 2$, então
$[X_1, X_2] \stackrel{\varphi}{\sim} [Y_1, Y_2]$.

Consequência imediata do lema anterior. De fato, dado qualquer
$p \in \mathcal{M}$ temos $$\begin{aligned}
\mathrm{d}\varphi_p \left( [X_1, X_2](p) \right) &= \left[ \mathrm{d}\varphi_p \left( X_1(p) \right),  \mathrm{d}\varphi_p \left( X_2(p) \right) \right] \\
&= [Y_1, Y_2](\varphi(p))\end{aligned}$$

$\rule{0.7em}{0.7em}$

Naturalmente, o conhecimento das conexões e curvaturas dos fatores de
tal produto determina a conexão e curvatura do próprio produto. Para
determinar estes, usaremos o método do referencial móvel. Antes,
estabeleceremos algumas notações importantes para as demonstrações dos
lemas a seguir (enunciados também em **[@dascontaswarped]** - com um
erro de sinal no item (8) da Proposição 2.4, corrigido no
[\[sinalerrado\]](#sinalerrado){reference-type="ref"
reference="sinalerrado"} do lema
[\[RmDoWarped\]](#RmDoWarped){reference-type="ref"
reference="RmDoWarped"}).

Seja
$\mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$$
e conexão $\nabla^g = \nabla$. Denotaremos
$\mathcal{N}^r_0 \doteq \mathcal{B}$ e $d_i \doteq \dim(\mathcal{N}_i)$
para cada $0 \leq i \leq k$. Para cada $0 \leq i \leq n$, fixaremos
referenciais locais $g_{\mathcal{N}_i}$-ortonormais, que denotaremos por
$\{ \mathbf{e}_{(i, j)} \}_{1 \leq j \leq d_i}$. Seus co-referenciais
associados serão denotados por
$\{\Theta^{(i, j)} \}_{1 \leq i, j \leq d_i}$ (e estão determinados por
$\Theta^{(i, j)}( \mathbf{e}_{(i, s)}) = \delta^j_s$). As $1$-formas de
conexão e $2$-formas de curvatura associadas a tais referenciais serão
denotadas por $\{ \omega^{(i, j)}_{q} \}_{1 \leq j, q \leq d_i}$ e
$\{ \Omega^{(i, j)}_{q} \}_{1 \leq j, q \leq d_i}$, respectivamente.
Sendo assim, note que
$$\left\{\mathbf{e}_{(0, 1)}, \ldots, \mathbf{e}_{(0, r)}, \frac{1}{h_1} \, \mathbf{e}_{(1, 1)}, \ldots,  \frac{1}{h_1} \, \mathbf{e}_{(1, d_1)}, \ldots, \frac{1}{h_k} \, \mathbf{e}_{(k, 1)}, \ldots,  \frac{1}{h_k} \, \mathbf{e}_{(k, d_k)} \right\}$$
é um referencial local $g$-ortonormal. Usaremos a notação
$$\widetilde{\mathbf{e}}_{(i, j)} = \begin{cases}
\mathbf{e}_{(0, j)}, \text{ se } i = 0 \\
\frac{1}{h_i} \, \mathbf{e}_{(i, j)}, \text{ se } i \neq 0
\end{cases}$$ de forma que
$$\{ \widetilde{\mathbf{e}}_{(i, j)}\}_{0 \leq i \leq k, 1 \leq j \leq d_i}$$
é um referencial local $g$-ortonormal, sendo seu co-referencial local
associado dado por
$$\{\widetilde{\Theta}^{(i, j))} \}_{0 \leq i \leq k, 1 \leq j \leq d_i}$$
onde $$\widetilde{\Theta}^{(i, j)} = \begin{cases}
\Theta^{(0, j)}, \text{ se } i = 0 \\
h_i \Theta^{(i, j)} \, \text{, se } i \neq 0
\end{cases}$$ de forma que num aberto $U \subset \mathcal{M}$, todo
campo $s \in \Gamma(T U)$ se escreve como
$$\left.s\right|_{U} = \sum_{\substack{0 \leq i \leq k\\
1 \leq j \leq d_i 
}} \widetilde{s}^{(i, j)} \, \widetilde{\mathbf{e}}_{(i, j)} =  \sum_{\substack{0 \leq i \leq k\\
1 \leq j \leq d_i 
}} \widetilde{\Theta}^{(i, j)}(s) \, \widetilde{\mathbf{e}}_{(i, j)}$$
Finalmente, as $1$-formas de conexão e $2$-formas de curvatura de
$(\mathcal{M}, g)$ com respeito a esse referencial serão denotadas por
$\{ \widetilde{\omega}^{(i, j)}_{(p, m)} \}_{\substack{0 \, \leq i, p \, \leq k\\
1 \, \leq j, m \, \leq d_i 
}}$ e
$\{ \widetilde{\Omega}^{(i, j)}_{(p, m)} \}_{\substack{0 \, \leq i, p \, \leq k\\
1 \, \leq j, m \, \leq d_i 
}}$, de forma que
$$\nabla_s \left( \widetilde{\mathbf{e}}_{(p, m)} \right) = \sum_{\substack{0 \, \leq i \, \leq k\\
1 \, \leq j \, \leq d_i  
}} \widetilde{\omega}^{(i, j)}_{(p, m)}(s) \, \widetilde{\mathbf{e}}_{(i, j)}$$
e
$$\mathrm{Rm}(s_1, s_2) \widetilde{\mathbf{e}}_{(p, m)}= \sum_{\substack{0 \, \leq i \, \leq k\\
1 \, \leq j \, \leq d_i  
}} \widetilde{\Omega}^{(i, j)}_{(p, m)}(s_1, s_2) \, \widetilde{\mathbf{e}}_{(i, j)}$$

[\[MovelWarped\]]{#MovelWarped label="MovelWarped"} Seguindo a notação
acima, seja
$\mathcal{M}= \mathcal{B}^r \times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$
e conexão $\nabla^g = \nabla$. As $1$-formas de conexão
$\{ \widetilde{\omega}^{(i, j)}_{(p, m)} \}_{\substack{0 \, \leq i, p \, \leq k\\
1 \, \leq j, m \, \leq d_i 
}}$ são dadas por

1.  [\[letraA118\]]{#letraA118 label="letraA118"}
    $$\widetilde{\omega}^{(0, j)}_{(0, \ell)} = \omega^{(0, j)}_{\ell}, \text{ sejam quais forem $1 \leq j, \ell \leq r$}$$

2.  [\[letraB118\]]{#letraB118 label="letraB118"}
    $$\widetilde{\omega}^{(0, j)}_{(\beta, \ell)} = - \frac{\mathbf{e}_{(0, j)}(h_{\beta})}{h_{\beta}} \, \widetilde{\Theta}^{(\beta, \ell)}, \text{ para quaisquer $1 \leq j \leq r$ e $\beta, \ell \geq 1$}$$

3.  [\[letraC118\]]{#letraC118 label="letraC118"}
    $$\widetilde{\omega}^{(\gamma, j)}_{(0, a)} = \frac{ \mathbf{e}_{(0, a)}(h_{\gamma})}{h_{\gamma}} \, \widetilde{\Theta}^{(\gamma, j)}, \text{ se $1 \leq \gamma \leq k$ e $1 \leq a, j \leq r$}$$

4.  [\[letraD118\]]{#letraD118 label="letraD118"}
    $$\widetilde{\omega}^{(\gamma, q)}_{(\beta, p)} = \delta_{\gamma \beta} \, \omega^{(\gamma, q)}_p, \text{ se $1 \leq \gamma, \beta \leq k$ e $1 \leq p, q \leq d_{\gamma}$ }$$

A ideia da demonstração é clássica: motivados pelo teorema
[\[PrimeiraUnicaCartan\]](#PrimeiraUnicaCartan){reference-type="ref"
reference="PrimeiraUnicaCartan"}, iremos definir uma matriz
antissimétrica
$\left(\alpha^{(i, j)}_{(p, m)} \right)_{\substack{0 \leq i, p \leq k\\
1 \leq j, m \leq d_{i} \\
}}$ que satisfaz $$\label{AlphaUnica}
\begin{cases}
\mathrm{d}\widetilde{\Theta}^{(0, j)} + \sum_{1 \leq \ell \leq r} \alpha^{(0, j)}_{(0, \ell)} \wedge \widetilde{\Theta}^{(0, \ell)} + \sum_{\substack{1\leq \gamma  \leq k\\
1 \leq \beta \leq d_{\gamma}\\
}} \alpha^{(0, j)}_{(\gamma, \beta)} \wedge \widetilde{\Theta}^{(\gamma, \beta)}= 0 \\
\mathrm{d}\widetilde{\Theta}^{(\beta, \gamma)} + \sum_{1 \leq \ell \leq r} \alpha^{(\beta, \gamma)}_{(0, \ell)} \wedge \widetilde{\Theta}^{(0, \ell)} + \sum_{\substack{1\leq \xi  \leq k\\
1 \leq \eta \leq d_{\xi}\\
}} \alpha^{(\beta, \gamma)}_{(\xi, \eta)} \wedge \widetilde{\Theta}^{(\xi, \eta)}= 0
\end{cases}$$ sejam quais forem $1 \leq j \leq r$,
$1 \leq \beta \leq k$, $1 \leq \gamma \leq d_{\beta}$. Da unicidade
enunciada no teorema
[\[PrimeiraUnicaCartan\]](#PrimeiraUnicaCartan){reference-type="ref"
reference="PrimeiraUnicaCartan"}, seguirá que
$\left(\alpha^{(i, j)}_{(p, m)} \right)_{\substack{0 \leq i, p \leq k\\
1 \leq j, m \leq d_{i} \\
}}$ é a matriz de $1$-formas da conexão de Levi-Civita de $\mathcal{M}$.
Uma vez que $$\label{AlphaUnica1}\begin{aligned}
\mathrm{d}\widetilde{\Theta}^{(0, j)} &= \mathrm{d}\Theta^{(0,j)} \\
&= - \sum_{1 \leq \ell \leq r} \omega^{(0, j)}_{\ell} \wedge \widetilde{\Theta}^{(0, \ell)}
\end{aligned}$$ E também $$\label{AlphaUnica2}
\begin{aligned}
\mathrm{d}\widetilde{\Theta}^{(\gamma, j)} &= \mathrm{d}\left(h_{\gamma} \Theta^{(\gamma, j)} \right) \\
&= \mathrm{d}h_{\gamma} \wedge \Theta^{(\gamma,j)} + h_{\gamma} \, \mathrm{d}\Theta^{(\gamma, j)} \\
&= \left( \sum_{1 \leq a \leq r} \mathbf{e}_{(0, a)}\left( h_{\gamma} \right) \, \Theta^{(0, a)} \right) \wedge \Theta^{(\gamma, j)} - h_{\gamma} \sum_{1 \leq \ell \leq d_{\gamma}} \omega^{(\gamma, j)}_{\ell} \wedge \Theta^{(\gamma, \ell)} \\
&= -\sum_{1 \leq a \leq r}  \left( \mathbf{e}_{(0, a)}\left( h_{\gamma} \right) \, \Theta^{(\gamma, j)}  \right) \wedge  \widetilde{\Theta}^{(0, a)} - \sum_{1 \leq \ell \leq d_{\gamma}} \omega^{(\gamma, j)}_{\ell} \wedge \widetilde{\Theta}^{(\gamma, \ell)}  
\end{aligned}$$ Definiremos $$\begin{aligned}
&\alpha^{(0, j)}_{(0, \ell)} = \omega^{(0, j)}_{\ell} \\
&\alpha^{(0, j)}_{(\gamma, \beta)} = -\frac{ \mathbf{e}_{(0, j)}(h_{\gamma})}{h_{\gamma}} \, \widetilde{\Theta}^{(\gamma, \beta)} \\
&\alpha^{(\beta, \gamma)}_{(0, \ell)} = \frac{\mathbf{e}_{(0, \ell)} (h_{\beta})}{h_{\beta}} \, \widetilde{\Theta}^{(\beta, \gamma)} \\
&\alpha^{(\beta, \gamma)}_{(\xi, \eta)} = 0, \text{ para qualquer $\xi \geq 1$ com $\xi \neq \beta$}\end{aligned}$$
É fácil ver que a matriz $\alpha$ assim definida é antissimétrica. Além
disso, segue das equações
[\[AlphaUnica1\]](#AlphaUnica1){reference-type="ref"
reference="AlphaUnica1"} e
[\[AlphaUnica2\]](#AlphaUnica2){reference-type="ref"
reference="AlphaUnica2"} que $\alpha$ assim definida satifaz
[\[AlphaUnica\]](#AlphaUnica){reference-type="ref"
reference="AlphaUnica"}, donde segue o resultado desejado.

$\rule{0.7em}{0.7em}$

[\[ConexaoDoWarped\]]{#ConexaoDoWarped label="ConexaoDoWarped"} Seja
$\mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$
e conexão $\nabla^g = \nabla$. Suponha que
$X, Y \in \mathcal{L}(\mathcal{B})$,
$V \in \mathcal{L}(\mathcal{N}_{\alpha})$ e
$W \in \mathcal{L}(\mathcal{N}_{\eta})$. Então:

1.  [\[nablaXYWarp\]]{#nablaXYWarp label="nablaXYWarp"}
    $\nabla_X Y = \nabla^{\mathcal{B}}_X Y$

2.  [\[NablaWarp\]]{#NablaWarp label="NablaWarp"}
    $\nabla_X V = \nabla_V X = \frac{X(h_{\alpha})}{h_{\alpha}} V$

3.  [\[NablaVWdoWarp\]]{#NablaVWdoWarp label="NablaVWdoWarp"}
    $\nabla_V W = \begin{cases} 0, \text{ se } \alpha \neq \eta \\ \nabla^{\mathcal{N}_{\eta}}_V W - \frac{g(V, W)}{h_{\eta}} \text{grad}_{\mathcal{B}} h_{\eta}, \text{ se } \alpha = \eta \end{cases}$

Temos $$\begin{aligned}
\nabla_X Y &= \nabla_X\left(\sum_{1 \leq a \leq  r} \widetilde{Y}^{(0, a)} \,  \widetilde{\mathbf{e}}_{(0, a)} \right) \\
&= \sum_{1 \leq a \leq r} \left\{  X\left(\widetilde{Y}^{(0, a)} \right)  \widetilde{\mathbf{e}}_{(0, a)} + \widetilde{Y}^{(0, a)} \,  \nabla_X \left( \widetilde{\mathbf{e}}_{(0, a)} \right) \right\} \\
&= \sum_{1 \leq a \leq r} \left\{  X\left(Y^{(0, a)} \right)  \mathbf{e}_{(0, a)} + Y^{(0, a)} \,  \nabla_X \left( \widetilde{\mathbf{e}}_{(0, a)} \right) \right\}\end{aligned}$$
Agora, note que $$\begin{aligned}
 \nabla_X \left( \widetilde{\mathbf{e}}_{(0, a)} \right) &=  \sum_{\substack{0 \leq i \leq k\\
1 \leq j \leq d_i 
}}  \widetilde{\omega}^{(i, j)}_{(0, a)}(X) \, \widetilde{\mathbf{e}}_{(i, j)} \\
&= \sum_{1 \leq j \leq r} \widetilde{\omega}^{(0, j)}_{(0, a)}(X) \, \widetilde{\mathbf{e}}_{(0, j)} + \sum_{\substack{1 \leq \gamma \leq k\\
1 \leq j \leq d_{\gamma}
}}  \widetilde{\omega}^{(\gamma, j)}_{(0, a)}(X) \, \widetilde{\mathbf{e}}_{(\gamma, j)} \\
&= \sum_{1 \leq j \leq r} \omega^{(0, j)}_a(X) \, \mathbf{e}_{(0, j)} + \sum_{\substack{1 \leq \gamma \leq k\\
1 \leq j \leq d_{\gamma}
}} \mathbf{e}_{(0, a)} \left(h_{\gamma} \right) \, \begingroup \color{violet} \underbrace{\color{black} \Theta^{(\gamma, j)}(X) }_{\color{violet} =0, \text{ pois } X \in \mathcal{L}(\mathcal{B}) } \endgroup \, \widetilde{\mathbf{e}}_{(\gamma, j)}  \\
&= \nabla^{\mathcal{B}}_{X} \left( \mathbf{e}_{(0, a)} \right)\end{aligned}$$
Portanto $$\begin{aligned}
\nabla_X Y &= \sum_{1 \leq a \leq r} \left\{ X\left(Y^{(0, a)} \right)  \mathbf{e}_{(0, a)} + Y^{(0, a)} \,  \nabla_X \left( \mathbf{e}_{(0, a)} \right) \right\} \\
&=\nabla^{\mathcal{B}}_X \left( \sum_{1 \leq a \leq r}  Y^{(0, a)} \, \mathbf{e}_{(0, a)} \right) \\
&= \nabla^{\mathcal{B}}_X Y\end{aligned}$$ onde na terceira igualdade
usamos os itens [\[letraA118\]](#letraA118){reference-type="ref"
reference="letraA118"} e
[\[letraC118\]](#letraC118){reference-type="ref" reference="letraC118"}
do lema [\[MovelWarped\]](#MovelWarped){reference-type="ref"
reference="MovelWarped"}. Uma vez que
$X\left( V^{(\alpha, \beta)} \right) = 0$, temos também

$$\begin{aligned}
\nabla_X{V} &= \nabla_X \left( \sum_{1 \leq \beta \leq d_{\alpha}} \widetilde{V}^{(\alpha, \beta)} \, \widetilde{\mathbf{e}}_{(\alpha, \beta)}\right) \\
&= \sum_{1 \leq \beta \leq d_{\alpha}} \left\{  X \left(\widetilde{V}^{(\alpha, \beta)} \right)  \widetilde{\mathbf{e}}_{(\alpha, \beta)} + \widetilde{V}^{(\alpha, \beta)} \, \nabla_X\left( \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \right \} \\
&= \sum_{1 \leq \beta \leq d_{\alpha}} \left\{  \frac{X(h_{\alpha})}{h_{\alpha}} \, V^{(\alpha, \beta)} \, \mathbf{e}_{(\alpha, \beta)} + \widetilde{V}^{(\alpha, \beta)} \, \left( \sum_{1 \leq \ell \leq r}  \begingroup \color{violet} \underbrace{\color{black} \widetilde{\omega}^{(0, \ell)}_{(\alpha, \beta)} (X) }_{\color{violet} =0, \text{ por \ref{letraB118} de \cref{MovelWarped}} } \endgroup \, \widetilde{\mathbf{e}}_{(0, \ell)} + \sum_{\substack{1 \leq \gamma \leq k\\
1 \leq s \leq d_{\gamma}
}}\,  \widetilde{\omega}^{(\gamma, s)}_{(\alpha, \beta)} (X) \, \widetilde{\mathbf{e}}_{(\gamma, s)} \right) \right\} \\
&= \frac{X(h_{\alpha})}{h_{\alpha}} \, V + \sum_{\substack{1 \leq s, \beta \leq d_{\alpha}
}} \begingroup \color{violet} \underbrace{\color{black} \omega^{(\alpha, s)}_{\beta}(X) }_{\color{violet} =0, \text{pois } X \in \mathcal{L}(\mathcal{B}) } \endgroup \, \widetilde{\mathbf{e}}_{(\alpha, s)} \\
&= \frac{X(h_{\alpha})}{h_{\alpha}} \, V \end{aligned}$$ onde na
penúltima igualdade usamos o item
[\[letraD118\]](#letraD118){reference-type="ref" reference="letraD118"}
do lema [\[MovelWarped\]](#MovelWarped){reference-type="ref"
reference="MovelWarped"}.

Finalmente, usando novamente o lema
[\[MovelWarped\]](#MovelWarped){reference-type="ref"
reference="MovelWarped"}, temos $$\begin{aligned}
\nabla_V W &= \nabla_V \left(  \sum_{1 \leq \beta \leq d_{\eta}} \widetilde{W}^{(\eta, \beta)} \, \widetilde{\mathbf{e}}_{(\eta, \beta)}  \right) \\
&= \sum_{1 \leq \beta \leq d_{\eta}}  V\left( \widetilde{W}^{(\eta, \beta)}  \right) \, \widetilde{\mathbf{e}}_{(\eta, \beta)} + \sum_{1 \leq \beta \leq d_{\eta}} \widetilde{W}^{(\eta, \beta)} \, \nabla_V \left(   \widetilde{\mathbf{e}}_{(\eta, \beta)}  \right) \\
&=   \sum_{1 \leq \beta \leq d_{\eta}}  V\left( \widetilde{W}^{(\eta, \beta)}  \right) \, \widetilde{\mathbf{e}}_{(\eta, \beta)} + \sum_{1 \leq \beta \leq d_{\eta}} \widetilde{W}^{(\eta, \beta)} \left\{ \sum_{1 \leq a \leq r}\widetilde{\omega}^{(0, a)}_{(\eta, \beta)} (V) \,  \widetilde{\mathbf{e}}_{(0, a)}  + \sum_{ \substack{1 \leq \xi \leq k \\
1 \leq \gamma \leq d_{\xi} }}  \widetilde{\omega}^{(\xi, \gamma)}_{(\eta, \beta)} (V) \,  \widetilde{\mathbf{e}}_{(\xi, \gamma)}    \right\} \\
&=  \sum_{1 \leq \beta \leq d_{\eta}}  V\left( \widetilde{W}^{(\eta, \beta)}  \right) \, \widetilde{\mathbf{e}}_{(\eta, \beta)} + \sum_{1 \leq \beta \leq d_{\eta}} \widetilde{W}^{(\eta, \beta)} \left\{-\sum_{1 \leq a \leq r} \frac{\mathbf{e}_{(0, a)}\left( h_{\eta} \right)}{h_{\eta}} \, \widetilde{V}^{(\eta, \beta)} \,  \widetilde{\mathbf{e}}_{(0, a)} + \sum_{1 \leq \gamma \leq d_{\eta}}\omega^{(\eta, \gamma)}_{\beta}(V) \, \widetilde{\mathbf{e}}_{(\eta, \gamma)} \right\} \\
&= \sum_{1 \leq \beta \leq d_{\eta}}  \left\{  V\left( \widetilde{W}^{(\eta, \beta)}  \right) \, \widetilde{\mathbf{e}}_{(\eta, \beta)} + \widetilde{W}^{(\eta, \beta)} \, \nabla_V \left( \widetilde{\mathbf{e}}_{(\eta, \beta)} \right) \right\}\, - \sum_{1 \leq a \leq r} \frac{\mathbf{e}_{(0, a)}\left( h_{\eta} \right)}{h_{\eta}} \, g(V, W) \, \mathbf{e}_{(0, a)} \\
&= \nabla^{\mathcal{N}_{\eta}}_{ \mathrm{d}\sigma_{\eta}(V)} W - \delta_{\alpha \eta } \, \frac{g(V, W)}{h_{\eta}} \text{grad}_{\mathcal{B}} h_{\eta} \\
&=\delta_{\alpha \eta} \left( \nabla^{\mathcal{N}_{\eta}}_V W - \frac{g(V, W)}{h_{\eta}} \text{grad}_{\mathcal{B}} h_{\eta} \right)\end{aligned}$$

$\rule{0.7em}{0.7em}$

A progressão "natural" após termos calculado as $1$-formas de conexão no
lema [\[MovelWarped\]](#MovelWarped){reference-type="ref"
reference="MovelWarped"} seria usarmos o teorema
[\[SegEqEstrCartan\]](#SegEqEstrCartan){reference-type="ref"
reference="SegEqEstrCartan"} para calcularmos as $2$-formas de
curvatura. Não faremos isso pois para determinarmos $\mathrm{Rm}$, esse
caminho é bem mais complicado em comparação a simplesmente usarmos a
definição de $\mathrm{Rm}$ nos cálculos, amparados do lema
[\[MovelWarped\]](#MovelWarped){reference-type="ref"
reference="MovelWarped"}. Faremos isso na demonstração do lema
[\[RmDoWarped\]](#RmDoWarped){reference-type="ref"
reference="RmDoWarped"}.

[\[ConexWarped\]]{#ConexWarped label="ConexWarped"} Seja
$\mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$.
Denotemos $\text{grad}^{\mathcal{M}}= \text{grad}$ e
$\Delta^{\mathcal{M}} = \Delta$. Se
$\phi \in \mathscr{C}^{\infty}(\mathcal{B})$ e
$\psi \in \mathscr{C}^{\infty}(\mathcal{N}_i)$, então

1.  [\[GradPrimeiro\]]{#GradPrimeiro label="GradPrimeiro"}
    $\text{grad}(\phi \circ \pi) = \text{grad}_{\mathcal{B}} \phi$

2.  $\text{grad}(\psi \circ \sigma_i) = \frac{\text{grad}_{\mathcal{N}_i} \psi}{h_i^2}$

3.  $\Delta(\phi \circ \pi) = \Delta_{\mathcal{B}} \phi + \sum_{1 \leq i \leq k} d_i \frac{g_{\mathcal{B}}\left(\text{grad}_{\mathcal{B}} \phi, \text{grad}_{\mathcal{B}} h_i \right)}{h_i}$

4.  $\Delta(\psi \circ \sigma_i) = \frac{\Delta_{\mathcal{N}_i} \psi}{h_i^2}$

Fixe $p = \left( p_0, q_1, \ldots, q_k  \right) \in \mathcal{M}$. Uma
vez que $\phi \circ \pi$ é constante em
$\{p_0 \} \times \mathcal{N}_1 \times \ldots \times \mathcal{N}_k$ seja
qual for $p_0 \in \mathcal{B}$, temos $$\begin{aligned}
\text{grad}\left( \phi \circ \pi \right)(p) &= \sum_{1 \leq i \leq r} \mathbf{e}_{(0, i)}(p) \left( \phi \circ \pi \right) \, \mathbf{e}_{(0, i)}(p) \\
&= \sum_{1 \leq i \leq r} \mathrm{d}\left( \phi \circ \pi \right)_p \left( \mathbf{e}_{(0, i)}(p) \right) \, \mathbf{e}_{(0, i)}(p) \\
&=  \sum_{1 \leq i \leq r} \mathrm{d}\phi_{p_0}\left( \mathbf{e}_{(0, i)}(p_0) \right)  \, \mathbf{e}_{(0, i)}(p) \\ 
&=  \sum_{1 \leq i \leq r}  \mathbf{e}_{(0, i)}(p_0) \left( \phi \right) \, \mathbf{e}_{(0, i)}(p) \\
&= \left( \text{grad}_{\mathcal{B}} \phi \right) (p)\end{aligned}$$
Analogamente, $$\begin{aligned}
\text{grad}\left( \psi \circ \sigma_i \right)(p) &= \sum_{1 \leq j \leq d_i} \widetilde{\mathbf{e}}_{(i, j)}(p)(\psi) \, \widetilde{\mathbf{e}}_{(i, j)}(p) \\
&= h_{i}^{-2} \, \left( \text{grad}_{\mathcal{N}_i} \psi \right)(p)\end{aligned}$$
Da definição do Laplaciano, do item
[\[NablaWarp\]](#NablaWarp){reference-type="ref" reference="NablaWarp"}
do lema [\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"} e do item
[\[GradPrimeiro\]](#GradPrimeiro){reference-type="ref"
reference="GradPrimeiro"} do lema atual, segue também que
$$\begin{aligned}
\Delta\left( \phi \circ \pi \right) &= \sum_{1 \leq i \leq r} g\left(  \nabla_{\mathbf{e}_{(0, i)}} \nabla^{\mathcal{B}} \phi, \mathbf{e}_{(0, i)}  \right) + \sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} g\left(  \nabla_{\widetilde{\mathbf{e}}_{(\alpha, \beta)}} \nabla^{\mathcal{B}} \phi, \widetilde{\mathbf{e}}_{(\alpha, \beta)}  \right) \\
&= \Delta_{\mathcal{B}} \phi + \sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} g\left(  \frac{\left( \nabla^{\mathcal{B}} \phi \right)\left( h_{\alpha} \right)}{h_{\alpha}} \, \widetilde{\mathbf{e}}_{(\alpha, \beta)} , \widetilde{\mathbf{e}}_{(\alpha, \beta)}  \right) \\
&= \Delta_{\mathcal{B}} \phi + \sum_{1 \leq \alpha \leq k} d_{\alpha} \frac{\left( \nabla^{\mathcal{B}} \phi \right)\left( h_{\alpha} \right)}{h_{\alpha}} \\
&=\Delta_{\mathcal{B}} \phi + \sum_{1 \leq \alpha \leq k} d_{\alpha} \frac{g_{\mathcal{B}} \left( \nabla^{\mathcal{B}} \phi, \nabla^{\mathcal{B}} h_{\alpha} \right)}{h_{\alpha}}\end{aligned}$$
Finalmente, $$\begin{aligned}
\Delta\left(  \psi \circ \sigma_i \right) &= \sum_{1 \leq j \leq r} g\left(  \nabla_{\mathbf{e}_{(0, j)}} \nabla\psi, \mathbf{e}_{(0, j)}  \right) + \sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} g\left(  \nabla_{\widetilde{\mathbf{e}}_{(\alpha, \beta)}} \nabla \psi, \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \\
&= \sum_{1 \leq j \leq r} g\left(  \nabla_{\mathbf{e}_{(0, j)}} \left(  \frac{\nabla^{\mathcal{N}_i} \psi}{h_i^2} \right), \mathbf{e}_{(0, j)}   \right) + \sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} g\left( \nabla_{\widetilde{\mathbf{e}}_{(\alpha, \beta)}} \left( \frac{\nabla^{\mathcal{N}_i} \psi}{h_i^2}  \right) , \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \\
&= \sum_{1 \leq j \leq r} g\left(  -\frac{2 \, \mathbf{e}_{(0, j)}(h_i)}{h_i^3} \, \nabla^{\mathcal{N}_i} \psi + \frac{1}{h_i^2} \, \nabla_{\mathbf{e}_{(0, j)}} \nabla^{\mathcal{N}_i} \psi, \mathbf{e}_{(0, j)}  \right) \\
&+\sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} h_i^{-4} \, g\left( \nabla_{\mathbf{e}_{(\alpha, \beta)}} \nabla^{\mathcal{N}_i} \psi, \mathbf{e}_{(\alpha, \beta)}  \right) \\
&= \sum_{\substack{1 \leq \alpha \leq k \\
1 \leq \beta \leq d_{\alpha}}} h_i^{-2} \, g^{\mathcal{N}_i}\left( \nabla_{\mathbf{e}_{(\alpha, \beta)}} \nabla^{\mathcal{N}_i} \psi, \mathbf{e}_{(\alpha, \beta)}  \right) \\
&= h_i^{-2} \, \Delta_{\mathcal{N}_i} \psi\end{aligned}$$

$\rule{0.7em}{0.7em}$

[\[RmDoWarped\]]{#RmDoWarped label="RmDoWarped"} Seja
$\mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$.
Denotemos $\mathrm{Rm}^{\mathcal{M}} = \mathrm{Rm}$ e tomemos
$X, Y, Z \in \mathcal{L}(\mathcal{B})$,
$V \in \mathcal{L}(\mathcal{N}_{\alpha}), W \in \mathcal{L}(\mathcal{N}_{\eta})$
e $U \in \mathcal{L}(\mathcal{N}_{\beta})$. Então

1.  [\[1RmWarp\]]{#1RmWarp label="1RmWarp"}
    $\mathrm{Rm}(X, Y)Z = \mathrm{Rm}_B(X, Y)Z$.

2.  [\[2RmWarp\]]{#2RmWarp label="2RmWarp"}
    $\mathrm{Rm}(V, X)Y = -\frac{\left(\nabla^2_{\mathcal{B}} h_{\alpha} \right)(X, Y)}{h_{\alpha}} V$.

3.  [\[3RmWarp\]]{#3RmWarp label="3RmWarp"}
    $\mathrm{Rm}(X, V) W = \mathrm{Rm}(V, W)X = \mathrm{Rm}(V, X)W = 0$
    sempre que $\alpha \notin \{ \eta \}$.

4.  [\[4RmWarp\]]{#4RmWarp label="4RmWarp"} $\mathrm{Rm}(X, Y)V = 0$.

5.  [\[5RmWarp\]]{#5RmWarp label="5RmWarp"} $\mathrm{Rm}(V, W)X = 0$
    sempre que $\alpha = \eta$.

6.  [\[6RmWarp\]]{#6RmWarp label="6RmWarp"} $\mathrm{Rm}(V, W)U = 0$
    sempre que $\alpha \in \{\eta \} \neq \{\beta \}$.

7.  [\[7RmWarp\]]{#7RmWarp label="7RmWarp"}
    $\mathrm{Rm}(U, V) W = -g(V, W) \, \frac{g_{\mathcal{B}}(\text{grad}_{\mathcal{B}} h_{\alpha}, \text{grad}_{\mathcal{B}} h_{\beta})}{h_{\alpha} h_{\beta}} \, U$
    sempre que $\alpha \in \{ \eta \} \neq \{ \beta \}$.

8.  [\[sinalerrado\]]{#sinalerrado label="sinalerrado"}
    $\mathrm{Rm}(X, V)W = -\frac{g(V, W)}{h_{\alpha}} \nabla^{\mathcal{B}}_X(\text{grad}_{\mathcal{B}} h_{\alpha})$
    sempre que $\alpha \in \{ \eta \}$.

9.  [\[9doRmWarped\]]{#9doRmWarped label="9doRmWarped"}
    $\mathrm{Rm}(V, W)U = \mathrm{Rm}_{\mathcal{N}_{\alpha}}(V, W)U + \frac{\| \text{grad}_{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha}^2 \right)} \cdot \left(g(V, U)W - g(W, U)V \right)$
    sempre que $\{\alpha, \eta \}= \{\beta \}$.

O item [\[1RmWarp\]](#1RmWarp){reference-type="ref" reference="1RmWarp"}
é uma consequência direta do item
[\[nablaXYWarp\]](#nablaXYWarp){reference-type="ref"
reference="nablaXYWarp"} do lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"}. Para provar o item
[\[2RmWarp\]](#2RmWarp){reference-type="ref" reference="2RmWarp"}, note
inicialmente que $[X, V] = 0$ como consequência imediata do lema
[\[RelBrack\]](#RelBrack){reference-type="ref" reference="RelBrack"}, de
forma que $$\begin{aligned}
\mathrm{Rm}(V, X)Y &= \nabla_V \nabla_X Y - \nabla_X \nabla_V Y \\
&= \nabla_V \nabla^{\mathcal{B}}_X Y - \nabla_X \left( \frac{Y(h_{\alpha})}{h_{\alpha}} V  \right) \\
&= \frac{\left( \nabla^{\mathcal{B}}_X Y \right)(h_{\alpha}) }{h_{\alpha}} \, V - X \left( \frac{Y\left( h_{\alpha} \right) }{h_{\alpha}}  \right) V - \frac{Y\left( h_{\alpha} \right) }{h_{\alpha}} \, \frac{X\left( h_{\alpha} \right) }{h_{\alpha}} \, V \\
&= \frac{\nabla_{\nabla^{\mathcal{B}}_X Y} \left( h_{\alpha} \right)}{h_{\alpha}} \, V - \frac{X \left( Y\left( h_{\alpha} \right) \right)}{h_{\alpha}} \, V + \frac{X \left( h_{\alpha} \right)}{h_{\alpha}^2} \, Y\left( h_{\alpha} \right) \, V - \frac{X\left( h_{\alpha} \right) \, Y\left(  h_{\alpha} \right)}{h_{\alpha}^2} \, V \\
&=- \frac{\left( \text{Hess}_g \left( h_{\alpha} \right) \right)(X, Y) }{h_{\alpha}} \, V\end{aligned}$$
O item [\[3RmWarp\]](#3RmWarp){reference-type="ref" reference="3RmWarp"}
segue como consequência direta do item
[\[NablaVWdoWarp\]](#NablaVWdoWarp){reference-type="ref"
reference="NablaVWdoWarp"} do lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"}. Agora, segue do item
[\[NablaWarp\]](#NablaWarp){reference-type="ref" reference="NablaWarp"}
do lema [\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"} que $$\begin{aligned}
\nabla_X \nabla_Y V - \nabla_Y \nabla_X V &= \nabla_X \left(  \frac{Y \left( h_{\alpha}  \right)}{h_{\alpha}}  \, V \right) - \nabla_Y \left(  \frac{X \left( h_{\alpha}  \right)}{h_{\alpha}} \, V \right) \\
&= X \left( \frac{Y \left( h_{\alpha}  \right)}{h_{\alpha}}  \right) \, V + \frac{Y \left( h_{\alpha}  \right)}{h_{\alpha}}  \, \nabla_X V - Y \left( \frac{X \left( h_{\alpha}  \right)}{h_{\alpha}}  \right) \, V  - \frac{X \left( h_{\alpha}  \right)}{h_{\alpha}} \, \nabla_Y V \\
&= \frac{ X\left( Y\left( h_{\alpha} \right)  \right) }{h_{\alpha}}  \, V - \frac{X\left( h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, Y\left( h_{\alpha} \right) \, V + \frac{Y\left( h_{\alpha} \right) }{h_{\alpha}} \, \frac{X\left( h_{\alpha} \right) }{h_{\alpha}} \, V \\
&-\frac{ Y\left( X\left( h_{\alpha} \right)  \right) }{h_{\alpha}}  \, V + \frac{X\left( h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, Y\left( h_{\alpha} \right) \, V  - \frac{X\left( h_{\alpha} \right) }{h_{\alpha}} \, \frac{Y\left( h_{\alpha} \right) }{h_{\alpha}} \, V  \\
&= \frac{[X, Y] \left( h_{\alpha} \right)}{h_{\alpha}} \, V \\
&= \nabla_{[X, Y]} V\end{aligned}$$ e portanto $\mathrm{Rm}(X, Y)V =0$,
como afirmado no item [\[4RmWarp\]](#4RmWarp){reference-type="ref"
reference="4RmWarp"}. O item
[\[5RmWarp\]](#5RmWarp){reference-type="ref" reference="5RmWarp"} é uma
consequência simples do item
[\[NablaWarp\]](#NablaWarp){reference-type="ref" reference="NablaWarp"}
do lema [\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"}. De fato, $$\begin{aligned}
\mathrm{Rm}(V, W)X &= \nabla_V \nabla_W X - \nabla_W \nabla_V X - \nabla_{[V,W]}X \\
&= \nabla_V \left(  \frac{X\left( h_{\alpha} \right)}{h_\alpha} \, W \right) - \nabla_W \left(  \frac{X\left( h_{\alpha} \right)}{h_\alpha} \, V \right) - \frac{X\left( h_{\alpha} \right)}{h_\alpha} \, [V, W] \\
&= \frac{X\left( h_{\alpha} \right)}{h_\alpha} \, \left(  \nabla_V W - \nabla_W V - [V, W]  \right) \\
&=0\end{aligned}$$ O item [\[6RmWarp\]](#6RmWarp){reference-type="ref"
reference="6RmWarp"} é uma consequência direta dos itens
[\[NablaVWdoWarp\]](#NablaVWdoWarp){reference-type="ref"
reference="NablaVWdoWarp"} e
[\[nablaXYWarp\]](#nablaXYWarp){reference-type="ref"
reference="nablaXYWarp"} do lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"}. Para provar o item
[\[7RmWarp\]](#7RmWarp){reference-type="ref" reference="7RmWarp"}, note
que novamente como consequência do lema
[\[RelBrack\]](#RelBrack){reference-type="ref" reference="RelBrack"},
temos $[U, V] = 0$, de forma que usando o lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"}, obtemos: $$\begin{aligned}
\mathrm{Rm}(U, V)W &= \nabla_U \nabla_V W - \nabla_V \begingroup \color{violet} \underbrace{\color{black} \nabla_U W }_{\color{violet} =0 } \endgroup \\
&=\nabla_U \left( \nabla^{\mathcal{N}_{\alpha}}_V W - \frac{g(V, W)}{h_{\alpha}} \, \nabla^{\mathcal{B}} h_{\alpha} \right) \\
&= -\frac{g(V, W)}{h_{\alpha}} \, \nabla_U \nabla^{\mathcal{B}} h_{\alpha} \\
&= -\frac{g(V, W)}{h_{\alpha}} \, \frac{\left(  \nabla^{\mathcal{B}} h_{\alpha}  \right) \left( h_{\beta} \right)}{h_{\beta}} \, U \\
&= -g(V, W) \, \frac{g_{\mathcal{B}}(\text{grad}_{\mathcal{B}} h_{\alpha}, \text{grad}_{\mathcal{B}} h_{\beta})}{h_{\alpha} h_{\beta}} \, U\end{aligned}$$
Iremos agora provar o item
[\[sinalerrado\]](#sinalerrado){reference-type="ref"
reference="sinalerrado"}. Primeiramente, temos $$\begin{aligned}
\nabla_X \nabla_V W &= \nabla_X \left( \nabla^{\mathcal{N}_{\alpha}}_{V} W - \frac{g(V, W)}{h_{{\alpha}} } \,  \nabla^{\mathcal{B}} h_{\alpha}  \right) \\
&= \frac{X\left(  h_{\alpha} \right)}{h_{\alpha}} \, \nabla^{\mathcal{N}_{\alpha}}_{V} W - X \left(  \frac{g(V, W)}{h_{\alpha}}  \right) \, \nabla^{\mathcal{B}} h_{\alpha} -  \frac{g(V, W)}{h_{\alpha}} \, \nabla_X \nabla^{\mathcal{B}} h_{\alpha} \\
&= \frac{X\left(  h_{\alpha} \right)}{h_{\alpha}} \, \nabla^{\mathcal{N}_{\alpha}}_{V} W - \frac{\left(   g\left( \nabla_X V, W    \right) +  g\left( V, \nabla_X W    \right)     \right)}{h_{\alpha}} \, \nabla^{\mathcal{B}} h_{\alpha} + \frac{X \left( h_{\alpha} \right)   }{\left( h_{\alpha} \right)^2} \, g(V, W) \, \nabla^{\mathcal{B}} h_{\alpha} \\
&- \frac{g(V, W)}{h_{\alpha}} \nabla^{\mathcal{B}}_X \nabla^{\mathcal{B}} h_{\alpha} \\
&=  \frac{X\left(  h_{\alpha} \right)}{h_{\alpha}} \, \nabla^{\mathcal{N}_{\alpha}}_{V} W - 2 \, \frac{X\left(  h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, g(V, W) \, \nabla^{\mathcal{B}} h_{\alpha} + \frac{X\left(  h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, g(V, W) \, \nabla^{\mathcal{B}} h_{\alpha} - \frac{g(V, W)}{h_{\alpha}} \nabla^{\mathcal{B}}_X \nabla^{\mathcal{B}} h_{\alpha} \\
&=  \frac{X\left(  h_{\alpha} \right)}{h_{\alpha}} \, \nabla^{\mathcal{N}_{\alpha}}_{V} W -  \, \frac{X\left(  h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, g(V, W) \, \nabla^{\mathcal{B}} h_{\alpha} - \frac{g(V, W)}{h_{\alpha}} \nabla^{\mathcal{B}}_X \nabla^{\mathcal{B}} h_{\alpha}\end{aligned}$$
E também: $$\begin{aligned}
\nabla_V \nabla_X W &= \nabla_V \left( \frac{X \left( h_{\alpha} \right) }{h_{\alpha}} W  \right) \\
&=\frac{X \left( h_{\alpha} \right) }{h_{\alpha}} \left(  \nabla^{\mathcal{N}_{\alpha}}_V W - \frac{g(V, W)}{h_{\alpha}} \, \nabla^{\mathcal{B}} h_{\alpha}   \right) \\
&= \frac{X \left( h_{\alpha} \right) }{h_{\alpha}}  \, \nabla^{\mathcal{N}_{\alpha}}_V W  - \frac{X\left(  h_{\alpha} \right)}{\left( h_{\alpha} \right)^2} \, g(V, W) \, \nabla^{\mathcal{B}} h_{\alpha}\end{aligned}$$
Como $[X, V] = 0$, segue então que
$$\mathrm{Rm}(X, V)W = -\frac{g(V, W)}{h_{\alpha}} \, \nabla^{\mathcal{B}}_X(\text{grad}_{\mathcal{B}} h_{\alpha})$$
Finalmente, para provar
[\[9doRmWarped\]](#9doRmWarped){reference-type="ref"
reference="9doRmWarped"}, note primeiramente que
$\mathrm{Rm}(V, W)U \in \mathcal{L}(\mathcal{N}_{\alpha})$, já que dados
$X \in \mathcal{L}(\mathcal{B})$ e
$L \in \mathcal{L}(\mathcal{N}_{\xi})$ com $\xi \neq \alpha$, temos
$$\begin{aligned}
&g\left( \mathrm{Rm}(V, W)U, X  \right) = -g\left( \mathrm{Rm}(V, W)X, U  \right) = 0 , \text{ pelo item \ref{5RmWarp}}\\
&g\left( \mathrm{Rm}(V, W)U, L  \right) = -g\left( \mathrm{Rm}(V, W)L, U  \right) = 0, \text{  pelo item \ref{6RmWarp}}\end{aligned}$$
Segue então da equação de Gauss e do item
[\[NablaVWdoWarp\]](#NablaVWdoWarp){reference-type="ref"
reference="NablaVWdoWarp"} do lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"} que dado qualquer
$C \in \mathcal{L}(\mathcal{N}_{\alpha})$, temos $$\begin{aligned}
g\left( \mathrm{Rm}(V, W)U, C  \right) &= \left( h_{\alpha} \right)^2 \, \mathrm{Rm}^{\mathcal{N}_{\alpha}}(V, W, U, C) - g\left(  \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(V, C), \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(W, U)  \right) + g\left(  \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(V, U), \mathbf{\mathrm{\textbf{\uppercase{\romannumeral 2\relax}}}}(W, C)  \right) \\
&= \left( h_{\alpha} \right)^2 \, \mathrm{Rm}^{\mathcal{N}_{\alpha}}(V, W, U, C) - \frac{g(V, C) \, g(W, U)}{\left( h_{\alpha} \right)^2} \, \| \nabla^{\mathcal{B}} h_{\alpha} \|^2 + \frac{g(V, U) \, g(W, C)}{\left( h_{\alpha} \right)^2} \, \| \nabla^{\mathcal{B}} h_{\alpha} \|^2  \end{aligned}$$
Equivalentemente, como
$\mathrm{Rm}(V, W)U \in \mathcal{L}(\mathcal{N}_{\alpha})$,
$$\flat^{g} \left( \mathrm{Rm}(V, W)U  \right) = \flat^{g} \left(  \mathrm{Rm}^{\mathcal{N}_{\alpha}}(V, W) U + \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \cdot \left\{ g(V, U) \, W - g(W, U) \, V \right\}  \right)$$
Como $\flat^{g}$ é um isomorfismo em cada fibra de $T \mathcal{M}$,
segue, como queríamos mostrar, que
$$\mathrm{Rm}(V, W)U = \mathrm{Rm}^{\mathcal{N}_{\alpha}}(V, W) U + \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \cdot \left\{ g(V, U) \, W - g(W, U) \, V \right\}$$

$\rule{0.7em}{0.7em}$

[\[TensorRicciDoWarped\]]{#TensorRicciDoWarped
label="TensorRicciDoWarped"} Seja
$\mathcal{M}= \mathcal{B}\times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{\mathcal{B}} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$.
Suponha que $X, Y, Z \in \mathcal{L}(\mathcal{B})$,
$V \in \mathcal{L}(\mathcal{N}_{\alpha})$ e
$W \in \mathcal{L}(\mathcal{N}_{\eta})$. Então:

1.  [\[RicXY\]]{#RicXY label="RicXY"}
    $\mathrm{Ric}(X, Y) = \mathrm{Ric}_{\mathcal{B}}(X, Y) - \sum_{1 \leq \mu \leq k} \frac{d_{\mu}}{h_{\mu}} \nabla^2_{\mathcal{B}}(h_{\mu})(X, Y)$.

2.  [\[RicXV\]]{#RicXV label="RicXV"} $\mathrm{Ric}(X, V) = 0$.

3.  [\[RicVWd\]]{#RicVWd label="RicVWd"} $\mathrm{Ric}(V, W) = 0$ se
    $\alpha \neq \eta$.

4.  [\[RicVWi\]]{#RicVWi label="RicVWi"}
    $$\mathrm{Ric}(V, W) = \mathrm{Ric}^{\mathcal{N}_{\alpha}}\left(  V, W  \right) -
    \begin{split}\hspace{-7.9cm}
        \left(
        \begin{aligned}
              &\frac{\Delta_{\mathcal{B}} h_{\alpha}}{h_{\alpha}} + \left( d_{\alpha} - 1 \right) \, \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \\[0.5cm]
             &+ \sum_{\substack{1 \leq \gamma \leq k \\
    \gamma \neq \alpha}} d_{\gamma} \, \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}  \right)}{h_{\gamma} \, h_{\alpha}}
        \end{aligned}
        \right) g\left(  V, W  \right), \text{ se } \alpha = \eta.
    \end{split}$$

Primeiramente, temos $$\begin{aligned}
\mathrm{Ric}(X, Y) &= \sum_{1 \leq i \leq r} \mathrm{Rm}\left( \mathbf{e}_{(0, i)}, X, Y, \mathbf{e}_{(0, i)} \right) + \sum_{\substack{1 \leq \mu \leq k \\ 
1 \leq \beta \leq d_{\mu}}} \mathrm{Rm}\left(  \widetilde{\mathbf{e}}_{(\mu, \beta)}, X, Y, \widetilde{\mathbf{e}}_{(\mu, \beta)}  \right) \\
&= \mathrm{Ric}^{\mathcal{B}}(X, Y)  + \sum_{\substack{1 \leq \mu \leq k \\ 
1 \leq \beta \leq d_{\mu}}} g\left(  -\frac{ \left( \nabla^2_{\mathcal{B}} h_{\mu}  \right)(X, Y)}{h_{\mu}} \, \widetilde{\mathbf{e}}_{(\mu, \beta)}, \widetilde{\mathbf{e}}_{(\mu, \beta)}  \right) \\
&= \mathrm{Ric}^{\mathcal{B}}(X, Y)  - \sum_{1 \leq \mu \leq k }  \frac{d_{\mu}}{h_{\mu}} \, \left(  \nabla^{2}_{\mathcal{B}} h_{\mu}  \right)(X, Y)\end{aligned}$$
Pela $\mathscr{C}^{\infty}(\mathcal{M})$-bilinearidade de
$\mathrm{Ric}$, para provar os itens restantes podemos supor sem perda
de generalidade que $V = \widetilde{\mathbf{e}}_{(\alpha, \beta)}$ e
$W = \widetilde{\mathbf{e}}_{(\eta, \xi)}$. Temos $$\begin{aligned}
\mathrm{Ric}(X, V) &= \sum_{1 \leq i \leq r} g \left(  \mathrm{Rm}\left(  \mathbf{e}_{(0, i)}, X  \right)V, \mathbf{e}_{(0, i)}  \right) + \sum_{ \substack{1 \leq \gamma \leq k \\ 
1 \leq \ell \leq d_{\gamma}}} g \left(  \mathrm{Rm}\left(  \mathbf{e}_{(\gamma, \ell)}, X \right)V, \mathbf{e}_{(\gamma, \ell)} \right) \\
&= - \sum_{1 \leq i \leq r}  \begingroup \color{violet} \underbrace{\color{black} g \left(  \mathrm{Rm}\left(  \mathbf{e}_{(0, i)}, X  \right)\mathbf{e}_{(0, i)} , V \right) }_{\color{violet} =0, \text{ por \ref{1RmWarp} de \cref{RmDoWarped}} } \endgroup - \sum_{ \substack{1 \leq \gamma \leq k \\ 
1 \leq \ell \leq d_{\gamma}}}  \begingroup \color{violet} \underbrace{\color{black} g \left(   \mathrm{Rm}\left(  X,  \mathbf{e}_{(\gamma, \ell)}  \right) \mathbf{e}_{(\alpha, \beta)} , \mathbf{e}_{(\gamma, \ell)}  \right) }_{\color{violet} =0, \text{ por \ref{3RmWarp} e \ref{sinalerrado} de \cref{RmDoWarped}} } \endgroup \\
&= 0\end{aligned}$$ Se $\alpha \neq \eta$, temos: $$\begin{aligned}
\mathrm{Ric}\left( \widetilde{\mathbf{e}}_{(\alpha, \beta)}, \widetilde{\mathbf{e}}_{(\eta, \xi)}  \right) &= \sum_{1 \leq i \leq r} \begingroup \color{violet} \underbrace{\color{black} g\left(  \mathrm{Rm}\left( \mathbf{e}_{(0, i)}, \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \widetilde{\mathbf{e}}_{(\eta, \xi)}, \mathbf{e}_{(0, i)} \right) }_{\color{violet} =0, \text{ por \ref{3RmWarp} de \cref{RmDoWarped}} } \endgroup + \sum_{\substack{1 \leq \gamma \leq k \\
1 \leq p \leq d_{\gamma}} } g \left(  \mathrm{Rm}\left( \widetilde{\mathbf{e}}_{(\gamma, p)},\widetilde{\mathbf{e}}_{(\alpha, \beta)} \right)\widetilde{\mathbf{e}}_{(\eta, \xi)}, \widetilde{\mathbf{e}}_{(\gamma, p)} \right)\end{aligned}$$
É óbvio que os termos do último somatório do lado direito acima todos se
anulam. De fato, se $\gamma = \alpha$ isso é absolutamente trivial, e
quando $\gamma, \alpha$ e $\eta$ são todos distintos, o item
[\[NablaVWdoWarp\]](#NablaVWdoWarp){reference-type="ref"
reference="NablaVWdoWarp"} do lema
[\[ConexaoDoWarped\]](#ConexaoDoWarped){reference-type="ref"
reference="ConexaoDoWarped"} garante que
$$\mathrm{Rm}\left(  \widetilde{\mathbf{e}}_{(\gamma, p)}, \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \widetilde{\mathbf{e}}_{(\eta, \xi)} = 0$$
Agora, quando $\alpha = \eta$, temos $$\begin{aligned}
\mathrm{Ric}\left( \widetilde{\mathbf{e}}_{(\alpha, \beta)}, \widetilde{\mathbf{e}}_{(\alpha, \xi)}  \right) &= \sum_{1 \leq i \leq r} g\left(  \mathrm{Rm}\left( \mathbf{e}_{(0, i)}, \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \widetilde{\mathbf{e}}_{(\alpha, \xi)}, \mathbf{e}_{(0, i)} \right) + \sum_{\substack{1 \leq \gamma \leq k \\
1 \leq p \leq d_{\gamma}} } g \left(  \mathrm{Rm}\left( \widetilde{\mathbf{e}}_{(\gamma, p)},\widetilde{\mathbf{e}}_{(\alpha, \beta)} \right)\widetilde{\mathbf{e}}_{(\alpha, \xi)}, \widetilde{\mathbf{e}}_{(\gamma, p)} \right) \\
&= \sum_{1 \leq i \leq r} g\left(  \frac{-\delta_{\beta \xi}}{h_{\alpha}} \, \nabla^{\mathcal{B}}_{\mathbf{e}_{(0, i)}} \nabla^{\mathcal{B}} h_{\alpha}, \mathbf{e}_{(0, i)} \right) + \sum_{1 \leq p \leq d_{\alpha}} g \left(  \mathrm{Rm}\left( \widetilde{\mathbf{e}}_{(\alpha, p)},\widetilde{\mathbf{e}}_{(\alpha, \beta)} \right)\widetilde{\mathbf{e}}_{(\alpha, \xi)}, \widetilde{\mathbf{e}}_{(\alpha, p)} \right) \\
&+ \sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha \\
1 \leq p \leq d_{\gamma}} } g \left(  \mathrm{Rm}\left( \widetilde{\mathbf{e}}_{(\gamma, p)},\widetilde{\mathbf{e}}_{(\alpha, \beta)} \right)\widetilde{\mathbf{e}}_{(\alpha, \xi)}, \widetilde{\mathbf{e}}_{(\gamma, p)} \right) \\
&=-\frac{\delta_{\beta \xi}}{h_{\alpha}} \, \Delta_{\mathcal{B}} h_{\alpha} \\
&+ \sum_{1 \leq p \leq d_{\alpha}} g \left(  \mathrm{Rm}^{\mathcal{N}_{\alpha}}\left(  \widetilde{\mathbf{e}}_{(\alpha, p)}, \widetilde{\mathbf{e}}_{(\alpha, \beta)} \right) \widetilde{\mathbf{e}}_{(\alpha, \xi)} + \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \, \left\{ \delta_{p \xi} \, \widetilde{\mathbf{e}}_{(\alpha, \beta)} - \delta_{\beta \xi} \, \widetilde{\mathbf{e}}_{(\alpha, p)} \right\} , \widetilde{\mathbf{e}}_{(\alpha, p)}   \right) \\
&-\sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha \\
1 \leq p \leq d_{\gamma}} } g \left(  \delta_{\beta \xi} \, \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}   \right)}{h_{\gamma} \, h_{\alpha}} \widetilde{\mathbf{e}}_{(\gamma, p)},  \widetilde{\mathbf{e}}_{(\gamma, p)} \right) \\
&=-\frac{\delta_{\beta \xi}}{h_{\alpha}} \, \Delta_{\mathcal{B}} h_{\alpha} + \mathrm{Ric}^{\mathcal{N}_{\alpha}}\left(  \widetilde{\mathbf{e}}_{(\alpha, \beta)}, \widetilde{\mathbf{e}}_{(\alpha, \xi)}  \right) + \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \, \delta_{\beta \xi} - \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \, \delta_{\beta \xi} \, d_{\alpha} \\
&- \delta_{\beta \xi} \sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha}} d_{\gamma} \, \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}  \right) }{h_{\gamma} \, h_{\alpha}} \\[1cm]
&=  \mathrm{Ric}^{\mathcal{N}_{\alpha}}\left(  \widetilde{\mathbf{e}}_{(\alpha, \beta)}, \widetilde{\mathbf{e}}_{(\alpha, \xi)}  \right) -
\begin{split}\hspace{-10cm}
    \left(
    \begin{aligned}
          \frac{\Delta_{\mathcal{B}} h_{\alpha}}{h_{\alpha}} &+ \left( d_{\alpha} - 1 \right) \, \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \\[0.5cm]
         &+ \sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha}} d_{\gamma} \, \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}  \right)}{h_{\gamma} \, h_{\alpha}}
    \end{aligned}
    \right) g\left(  \widetilde{\mathbf{e}}_{(\alpha, \beta)}, \widetilde{\mathbf{e}}_{(\alpha, \xi)}  \right) 
\end{split}\end{aligned}$$

$\rule{0.7em}{0.7em}$

[\[warped\]]{#warped label="warped"} Seja
$\mathcal{M}= B \times_{h_1} \mathcal{N}_1^{d_1} \times \cdots \times_{h_k} \mathcal{N}_{k}^{d_k}$
um produto warped múltiplo com métrica
$g = g_{B} \oplus h_1^2 g_{\mathcal{N}_1} \oplus \cdots \oplus h_{k}^2 g_{\mathcal{N}_k}$.
Então a curvatura escalar de $\mathcal{M}$ é dada por
$$\label{ScalWarped}
\begin{aligned}
R = R_{B} &- 2 \sum_{1 \leq i \leq k} d_i \frac{\Delta_B h_i}{h_i} + \sum_{1 \leq i \leq k} \frac{R_{\mathcal{N}_i}}{h_i^2} - \sum_{1 \leq i \leq k} d_i(d_i - 1) \frac{\| \text{grad}_B h_i \|_B^2}{h_i^2} \\
&- \sum_{1 \leq i \leq k} \sum_{\substack{1 \leq \ell \leq k \\
\ell \neq i  \\
}} d_i d_{\ell} \frac{g_B(\text{grad}_B h_i, \text{grad}_B h_{\ell})}{h_i h_{\ell}}
\end{aligned}$$

Temos $$\begin{aligned}
R &= \sum_{1 \leq i \leq r} \mathrm{Ric}\left( \mathbf{e}_{(0, i)}, \mathbf{e}_{(0, i)}  \right) + \sum_{ \substack{1 \leq \alpha \leq k \\
1 \leq \varphi \leq d_{\alpha}}} \mathrm{Ric}\left(  \widetilde{\mathbf{e}}_{(\alpha, \varphi)}, \widetilde{\mathbf{e}}_{(\alpha, \varphi)}  \right) \\
&= R_{\mathcal{B}} - \sum_{\substack{1 \leq \mu \leq k \\
1 \leq i \leq r}} \frac{d_{\mu}}{h_{\mu}} \, \left( \nabla^2_{\mathcal{B}} h_{\mu} \right)\left( \mathbf{e}_{(0, i)}, \mathbf{e}_{(0, i)} \right) \\
&+\sum_{ \substack{1 \leq \alpha \leq k \\
1 \leq \varphi \leq d_{\alpha}}} \mathrm{Ric}^{\mathcal{N}_{\alpha}}\left(  \widetilde{\mathbf{e}}_{(\alpha, \varphi)}, \widetilde{\mathbf{e}}_{(\alpha, \varphi)}  \right) - \begin{split}\hspace{-7.1cm}
    \sum_{\substack{1 \leq \alpha \leq k \\
    1 \leq \varphi \leq d_{\alpha}}}\left(
    \begin{aligned}
          \frac{\Delta_{\mathcal{B}} h_{\alpha}}{h_{\alpha}} &+ \left( d_{\alpha} - 1 \right) \, \frac{\| \nabla^{\mathcal{B}} h_{\alpha} \|^2}{\left( h_{\alpha} \right)^2} \\[0.5cm]
         &+ \sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha}} d_{\gamma} \, \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}  \right)}{h_{\gamma} \, h_{\alpha}}
    \end{aligned}
    \right) g\left(  \widetilde{\mathbf{e}}_{(\alpha, \varphi)}, \widetilde{\mathbf{e}}_{(\alpha, \varphi)}  \right) 
\end{split} \\
&= R_{\mathcal{B}} - 2 \, \sum_{1 \leq \mu \leq k} d_{\mu} \frac{\Delta_{\mathcal{B}} h_{\mu}}{h_{\mu}} \, + \sum_{1 \leq \mu \leq k} \frac{R_{\mathcal{N}_{\mu}}}{\left( h_{\mu} \right)^2} - \sum_{1 \leq \mu \leq k} d_{\mu} \, \left(  d_{\mu} - 1 \right) \frac{\|\text{grad}_{\mathcal{B}} h_{\mu} \|^2}{\left( h_{\mu} \right)^2} \\
&- \sum_{1 \leq \alpha \leq k} \sum_{\substack{1 \leq \gamma \leq k \\
\gamma \neq \alpha}} d_{\alpha} \, d_{\gamma} \,  \frac{g_{\mathcal{B}} \left(  \nabla^{\mathcal{B}} h_{\gamma}, \nabla^{\mathcal{B}} h_{\alpha}  \right)}{h_{\gamma} \, h_{\alpha}}\end{aligned}$$

$\rule{0.7em}{0.7em}$

[\[FormaEspacialComoWarped\]]{#FormaEspacialComoWarped
label="FormaEspacialComoWarped"} Para este exemplo, lembramos
primeiramente que uma variedade Riemanniana
$\left( \mathcal{M}, g  \right)$ tem curvatura seccional constante igual
a $S \in \mathbb{R}$ se, e somente se, seu tensor de curvatura é dado
por
$$\mathrm{Rm}= S \, \left( g \mathbin{\bigcirc\mspace{-15mu}\wedge\mspace{4mu}}g \right)$$
(onde $\mathbin{\bigcirc\mspace{-15mu}\wedge\mspace{4mu}}$ denota o
produto de Kulkarni-Nomizu), ou, equivalentemente, se e só se,
$$\mathrm{Rm}(X, Y, Z, W)=  S \, \left(  g(X, W) \, g(Y, Z)  - g(X, Z) \, g(Y, W)  \right)$$
sejam quais forem $X, Y, Z, W \in \Gamma\left( T \mathcal{M} \right)$.
Agora, denotando $$\mathbb{Q}^n(\kappa) \doteq \begin{cases}
\mathbb{R}^n, \text{ se } \kappa = 0 \\
\mathbb{S}^n, \text{ se } \kappa = 1 \\
\mathbb{H}^n, \text{ se } \kappa = -1 
\end{cases}$$ Temos (conforme demonstrado em **[@Ortega]**) que o tensor
Riemanniano de $\mathcal{I} \times_{h} \mathbb{Q}^n(\kappa)$ (onde
$\mathcal{I} \subset \mathbb{R}$ é um intervalo aberto e $h$ é uma
função real suave e positiva definida em $\mathcal{I}$) é dado por
$$\begin{aligned}
\mathrm{Rm}(X, Y, Z, W) &= \left(  \frac{\left( h' \right)^2 - \kappa}{h^2} \circ \pi_{\mathcal{I}} \right) \, \left(  g(X, Z) \, g(Y, W) - g(X, W) \, g(Y, Z) \right) \\
&+ \left( \frac{h \, h'' - \left( h' \right)^2 + \kappa}{h^2}  \circ \pi_{\mathcal{I}} \right) \, \begin{split}\hspace{0cm}
    \left(
    \begin{aligned}
          &g(X, Z) \, g\left( Y, \partial_t \right) \, g\left( W, \partial_t \right) - g(Y, Z) \, g\left( X, \partial_t \right) \,  g\left( W, \partial_t \right) \\[0.5cm]
         &-g(X, W) \, g\left( Y, \partial_t \right) \, g\left( Z, \partial_t \right) + g(Y, W) \, g\left( X, \partial_t \right) \, g\left( Z, \partial_t \right)
    \end{aligned}
    \right) 
\end{split}
\end{aligned}$$ Em particular,
$\mathcal{I} \times_{h} \mathbb{Q}^n(\kappa)$ tem curvatura seccional
constante igual a $C \in \mathbb{R}$ se, e somente se,
$$-C = \frac{\left( h' \right)^2 - \kappa}{h^2}  \text{ é constante e } \frac{h''}{h} = \frac{\left( h' \right)^2 - \kappa}{h^2}$$
Consequentemente, $$\begin{aligned}
&\text{$\mathbb{S}^n$ é localmente isométrico a $\mathcal{I} \times_{\operatorname{sen(t)}} \mathbb{S}^{n-1}$} \\
&\text{$\mathbb{H}^n$ é localmente isométrico a $\mathcal{I} \times_{e^{t}} \mathbb{R}^{n-1}$ e a  $\mathcal{I} \times_{\operatorname{senh}(t)} \mathbb{S}^{n-1}$} \\
&\text{$\mathbb{R}^n$ é localmente isométrico a $\mathcal{I} \times_{t} \mathbb{S}^{n-1}$}\end{aligned}$$

Pelo lema a seguir, a variedade Riemanniana do exemplo
[\[BryantSoliton\]](#BryantSoliton){reference-type="ref"
reference="BryantSoliton"} é localmente conformemente plana.

[\[LemaGarciaRio\]]{#LemaGarciaRio label="LemaGarciaRio"} Seja
$\mathcal{M}= \mathcal{I} \times_{h} \mathcal{N}$ um produto warped.
Então
$$\mathcal{M}\text{ é localmente conformemente plana} \iff \left(  \mathcal{N}, g_{\mathcal{N}}  \right) \text{ tem curvatura seccional constante}$$

Consulte **[@GarciaRio]**.

$\rule{0.7em}{0.7em}$

[\[BryantSoliton\]]{#BryantSoliton label="BryantSoliton"} Seja
$g_{\mathbb{S}^{n-1}}$ a métrica usual na esfera redonda unitária
$(n-1)$-dimensional. Procuraremos sólitons de Ricci steady que surgem
como produtos warped em $(0, \infty) \times \mathbb{S}^{n-1}$.
Consideremos então métricas da forma
$$g = \mathrm{d}r^2 + (\phi(r))^2 g_{\mathbb{S}^{n-1}}$$ Tomando um
referencial ortonormal local em $\mathbb{S}^{n-1}$, digamos
$$\left\{\frac{\partial}{\partial \theta^i} \right\}_{1 \leq i \leq n-1}$$
vemos que
$\left\{\frac{\partial}{\partial r}, \frac{1}{\phi} \frac{\partial}{\partial \theta^i} \right\}_{1 \leq i \leq n -1}$
é um referencial ortonormal local em
$(0, \infty) \times_{\phi} \mathbb{S}^{n-1}$. Pelo
[\[sinalerrado\]](#sinalerrado){reference-type="ref"
reference="sinalerrado"} do lema
[\[RmDoWarped\]](#RmDoWarped){reference-type="ref"
reference="RmDoWarped"}, vemos que a curvatura radial de um plano
passando pelo vetor radial $\frac{\partial}{\partial r}$ é dada por
$$\begin{aligned}
K_{{\rm rad}} = K\left(\frac{\partial}{\partial r}, \frac{1}{\phi} \frac{\partial}{\partial \theta^i}\right) &= g\left(\mathrm{Rm}\left( \frac{\partial}{\partial r}, \frac{1}{\phi} \frac{\partial}{\partial \theta^i}\right)\frac{1}{\phi} \frac{\partial}{\partial \theta^i} , \frac{\partial}{\partial r}\right) \\
&= \frac{1}{\phi^2} \cdot g(\mathrm{Rm}(\partial_r, \partial_{\theta^i}) \partial_{\theta^i}, \partial_r) \\
&= -\frac{1}{\phi^2} \cdot \frac{\phi^2}{\phi} \cdot \phi'' \\
&= -\frac{\phi''}{\phi}
\end{aligned}$$ Analogamente, usando o item
[\[9doRmWarped\]](#9doRmWarped){reference-type="ref"
reference="9doRmWarped"} do lema do lema
[\[RmDoWarped\]](#RmDoWarped){reference-type="ref"
reference="RmDoWarped"}, vemos que a curvatura seccional de um plano
$P_{{\rm sph}}$ perpendicular a $\frac{\partial}{\partial r}$ é dada por
$$\begin{aligned}
K_{{\rm sph}} = K\left(\frac{1}{\phi} \partial_{\theta^i}, \frac{1}{\phi} \partial_{\theta^j} \right) &= \frac{1}{\phi^4} \cdot g\left( \mathrm{Rm}(\partial_{\theta^i}, \partial_{\theta^j}) \partial_{\theta^j}, \partial_{\theta^i} \right) \\
&= \frac{1}{\phi^4} \cdot \phi^2 \cdot g_{\mathbb{S}^{n-1}} \left( [\pi_{\mathbb{S}^{n-1}}^{*} \mathrm{Rm}]\left(\partial_{\theta^i}, \partial_{\theta^j}) \partial_{\theta^j} \right) , \partial_{\theta^i}\right) \\
&= \frac{1}{\phi^2} \cdot \left(1 - \frac{(\phi')^2}{\phi^2} \cdot \phi^2 \right) \\
&= \frac{1-(\phi')^2}{\phi^2}
\end{aligned}$$ Portanto
$$\mathrm{Ric}\left(\frac{\partial}{\partial r}, \frac{\partial}{\partial r} \right) = \sum_{1 \leq i \leq n -1} K_{{\rm rad}} = -(n-1) \frac{\phi''}{\phi}$$
e $$\begin{aligned}
\mathrm{Ric}\left(\frac{\partial}{\partial \theta^i}, \frac{\partial}{\partial \theta^j} \right) &= \phi^2 \cdot \mathrm{Ric}\left(\frac{1}{\phi} \cdot \frac{\partial}{\partial \theta^i}, \frac{1}{\phi} \cdot \frac{\partial}{\partial \theta^j} \right) \\
&= \phi^2 \cdot \left(\left[\sum_{\substack{1 \leq i \leq n-2 \\
i \leq j}} K_{{\rm sph}} \right] + K_{{\rm rad}}\right) \\
&= (n-2) \left( 1 - (\phi')^2 \right) - \phi \phi''
\end{aligned}$$ Concluímos então que
$$\mathrm{Ric}(g) = -(n-1) \frac{\phi''}{\phi} \cdot \mathrm{d}r^2 + \left(  (n-2) \left( 1 - (\phi')^2 \right) - \phi \phi'' \right) g_{\mathbb{S}^{n-1}}$$
Agora, como consequência direta do lema
[\[ConexWarped\]](#ConexWarped){reference-type="ref"
reference="ConexWarped"}, temos também
$$\nabla^2 f = f''(r) \cdot \mathrm{d}r^2 + \phi \phi' f' \cdot  g_{\mathbb{S}^{n-1}}$$
Vemos que a equação para os sólitons de Ricci steady
$\mathrm{Ric}(g) + \nabla^2 f = 0$ nesse caso é equivalente ao seguinte
sistema de EDOs de segunda ordem: $$\begin{cases}
f^{\prime \prime}=(n-1) \frac{\phi^{\prime \prime}}{\phi} \\
\phi \phi^{\prime} f^{\prime}=-(n-2)\left(1-\left(\phi^{\prime}\right)^{2}\right)+\phi \phi^{\prime \prime}
\end{cases}$$ Estudando detalhadamente esse sistema, pode-se provar a
existência de um sóliton de Ricci gradiente steady rotacionalmente
simétrico e completo, que é único a menos de homotetias.

9

[[ **Horácio, M.A.R.M.** *One chart to rule them all!* Texto encontrado
em página pessoal. Disponível em:
[**https://sagangromov.github.io/assets/pdf/OneChart.pdf**](https://sagangromov.github.io/assets/pdf/OneChart.pdf).
Acessado em 15 de fevereiro de 2023. ]{style="color: black"}]{.nodecor}

[[ **Tu, Loring W.** Differential geometry. Connections, curvature, and
characteristic classes. Graduate Texts in Mathematics, 275. *Springer,
Cham,* 2017. xvi+346 pp. ISBN: 978-3-319-55082-4; 978-3-319-55084-8.
]{style="color: black"}]{.nodecor}

[[**Dobarro, Fernando; Ünal, Bülent.** Curvature of multiply warped
products. *J. Geom. Phys.* **55** (2005), no. 1, 75--106.
[**MR2157416.**](https://mathscinet.ams.org/mathscinet-getitem?mr=2157416)]{style="color: black"}]{.nodecor}

[[ **Marie-Amélie Lawn, Miguel Ortega,** A fundamental theorem for
hypersurfaces in semi-Riemannian warped products, Journal of Geometry
and Physics, Volume **90**, 2015, Pages 55-70, ISSN 0393-0440,
[**https://doi.org/10.1016/j.geomphys.2015.01.002.**](https://www.sciencedirect.com/science/article/pii/S0393044015000030)
]{style="color: black"}]{.nodecor}

[[ **Brozos-Vázquez, M.; García-Río, E.; Vázquez-Lorenzo, R.** Warped
product metrics and locally conformally flat structures. *Mat. Contemp.*
28 (2005), 91--110.
[**MR2195191.**](http://www.ams.org/mathscinet-getitem?mr=2195191)
]{style="color: black"}]{.nodecor}
