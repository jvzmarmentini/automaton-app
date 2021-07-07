<br />
<p align="center">

  <h3 align="center">Final Formal Languages and Automata Work</h3>

  <p align="center">
    An application that converts a finite non-deterministic automaton into a finite deterministic automaton and process a given word
  </p>
</p>

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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### 1. Objectives

Create a program that, given an finite deterministic automaton M, defined in a text file, execute the following operations:

- Convert a non-deterministic automaton into an equivalent finite deterministic  automaton;
- Allow the user to give a word to be recognized by the deterministic automaton;
- The program should determinate if the word received is accepted by the automaton;

### 2. Description

- The program from item 1 should be implemented using any programming language;
- The entry file format containing the non-deterministic automaton definition must follow the following pattern (including spaces between words):

\<M>=({\<q0>,...,\<qn>},{\<s1>,...,\<sn>},\<ini>,{ \<f0>,...,\<fn>})

Prog

(\<q0>,\<s1>)=\<q1>
...
(\<qn>,\<sn>)=\<q0>

Where:
\<M> is the automaton name;
\<qi> represents one state of the automaton for 0 ≤ i ≤ n, com n ∈ N e n ≥ 0;
\<si> represents one symbol of the alphabet of the language recognized by the automaton for 1 ≤ i ≤ n, com n ∈ N e n ≥1;
\<ini> indicates the initial state of the automaton, where ini is a state of the automaton;
\<fi> represents one final state of the automaton where ini is a state of the automaton and 0 ≤ i ≤ n, com n ∈ N e n ≥ 0;
(\<qi>,\<si>)=\<qj> describes the function applied to a state \<qi> and a \<si> entry symbol that leads to the computation to a state \<qj>.

Example:
AUTÔMATO=({q0,q1,q3,q4,q5,q7,q8},{L,S,I,P,C,E},q0,{q7})

Prog

(q0,S)=q4
(q0,L)=q1
(q0,L)=q3
(q1,I)=q7
(q3,P)=q5
(q4,E)=q7
(q8,I)=q7
(q5,I)=q7
(q3,C)=q8

![alt text](https://github.com/jvzmarmentini/automaton-app/blob/main/aut.png?raw=true)

### Built With

- [Python](https://www.python.org/)
- [NetworkX](https://networkx.org/)
- [PyGraphviz](https://pygraphviz.github.io/)

## Getting Started

Install python 3 and download the project files.

### Prerequisites

The initial requisites is to have Python installed in your machine. Here's where you can get it:

- [Download Python](https://www.python.org/downloads/)

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

- 3.1. Linux (ubuntu or debian)

   ```sh
   sudo apt install graphviz graphviz-dev
   pip install pygraphviz
   ```

- 3.2. macOs - Homebrew

   ```sh
   brew install graphviz
   pip install pygraphviz
   ```

- 3.3. Windows
   <https://pygraphviz.github.io/documentation/stable/install.html#windows>

## Usage

Before executing the application, be sure that the automato.txt file has a state machine and it is formated.

To run, use:

```sh
python3 main.py automaton-file word
```

Then, the generated state machine will be drawn in a png file and the result (if the word is accepted) will be printed.

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
