/* 7 kyu "Complementary DNA" by JustFY 
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

"ATTGC" --> "TAACG"
"GTAT" --> "CATA" */

function dnaStrand(dna){
    result = ''
    for (let i = 0; i < dna.length; i++) {
        switch (dna[i]) {
            case 'A':
                result += 'T'
                break;
            case 'T':
                result += 'A'
                break;
            case 'G':
                result += 'C'
                break;
            case 'C':
                result += 'G'
                break;
        }
    }
    return result
  }
  