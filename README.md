<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Final Formal Languages and Automata Work</h3>

  <p align="center">
    An application that converts a Nondeterministic Finite state machine into a Deterministic Finite state machine and give a response for a given word
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

1. Criar um programa que, dado um autômato finito não determinístico M, 
definido em um arquivo texto, execute as seguintes operações:
a. Converta M em um autômato finito determinístico MD equivalente;
b. Após a conversão, permita ao usuário fornecer uma palavra w para 
reconhecimento por MD;
c. O Programa deve determinar se w pertence à ACEITA(MD) ou 
REJEITA(MD);

2 - INSTRUÇÕES
* O programa do item 1 deve ser implementado usando a qualquer 
linguagem de programação;
* O formato do arquivo de entrada contendo a definição do AFND deve 
seguir o seguinte padrão:
<M>=({<q0>,...,<qn>},{<s1>,...,<sn>},<ini>,{ <f0>,...,<fn>})
Prog
(<q0>,<s1>)=<q1>
...
(<qn>,<sn>)=<q0>TRABALHO FINAL - LINGUAGENS FORMAIS E AUTÔMATOS
onde:
< M >: nome dado ao autômato;
< qi >: para 0 ≤ i ≤ n, com n ∈ N e n ≥ 0, representa um estado do 
autômato;
< si >: para 1 ≤ i ≤ n, com n ∈ N e n ≥1, representa um símbolo do 
alfabeto da linguagem reconhecida pelo autômato;
< ini >: indica o estado inicial do autômato, sendo que ini é um estado do 
autômato;
< fi >: para 0 ≤ i ≤ n, com n ∈ N e n ≥ 0, representa um estado final do 
autômato, sendo que fi é um estado do autômato;
(< qi >,< si >) =< qj > : descreve a função programa aplicada a um 
estado qi e um símbolo de entrada si que leva a computação a um estado 
qj.
Exemplo:
AUTÔMATO=({q0,q1,q2,q3},{a,b},q0,{q1,q3})
Prog
(q0,a)=q1
(q0,b)=q2
(q1,b)=q2
(q2,a)=q3
(q2,a)=q2
(q3,a)=q3
(q3,b)=q2
* As conversões de AFND para AFD deve seguir o algoritmo apresentado 
em aula.
* No teste de reconhecimento de uma palavra w pelo autômato MD, a 
mesma deve ser fornecida pelo usuário e o resultado deve ser:
** ACEITA se w ∈ ACEITA(MD) ou
** REJEITA se w ∈ REJEITA(MD)

### Built With

* [Python](https://www.python.org/)
* [NetworkX](https://networkx.org/)
* [PyGraphviz](https://pygraphviz.github.io/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

The only requisite is to have Python installed in your machine. Here's where you can get it
* [Download Python](https://www.python.org/downloads/)

### Installation

We strongly recommend using linux or macOs.

1. Clone the repo
   ```sh
   git clone https://github.com/jvzmarmentini/automaton-app.git
   ```
2. Install NetworkX package
   ```sh
   pip install networkx
   ```
3. Install PyGraphviz package
* 3.1. Linux (ubuntu or debian)
   ```sh
   sudo apt-get install graphviz graphviz-dev
   pip install pygraphviz
   ```
* 3.2. macOs - Homebrew
   ```sh
   brew install graphviz
   pip install pygraphviz
   ```
* 3.3. Windows
   https://pygraphviz.github.io/documentation/stable/install.html#windows


<!-- USAGE EXAMPLES -->
## Usage

Before executing the application, be sure that the automato.txt file has a state machine and it is formated.

To run, use:
```sh
python3 main.py
```

Then, the generated state machine will be drawn in file.png




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com) -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->