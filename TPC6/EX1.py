import ply.lex as lex
import re

# List of token names. This is always required
tokens = (
'COMENT1',
'COMENT2',
'VAR',
'FUNC',
'PROG',
'LPAR',
'RPAR',
'PARL',
'PARD',
'MENOR',
'MAIOR',
'COMA',
'SEMICOLON',
'EQUAL',
'NUM',
'WHILE',
'FOR',
'IN',
'PRINT',
'SUB',
'MULT',
'WORD',
'SPACE',
'LIST'
)

reserved = {
   'for' : 'FOR',
   'print' : 'PRINT',
   'in' : 'IN',
   'while' : 'WHILE',
   'function' : 'FUNC',
   'program' : 'PROG'
}

# Regular expression rules for simple tokens
t_COMENT1 = r'(\/)(\*)(.|\n)*(\*)(\/)'
t_COMENT2 = r'\/\/.*'
t_VAR = r'int \w*'
t_LPAR = r'\{'
t_RPAR = r'\}'
t_PARL = r'\('
t_PARD = r'\)'
t_MENOR = r'(\<|\<\=)'
t_MAIOR = r'(\>|\>\=)'
t_COMA = r'\,'
t_SEMICOLON = r'\;'
t_EQUAL = r'\='
t_FOR = r'for'
t_IN = r' in '
t_WHILE =r'while \w*'
t_PRINT = r'print\(.*\)'
t_SUB = r'\-'
t_MULT = r'\*'
t_WORD = r'\w+'
t_SPACE = r'\s'
t_FUNC = r'function \w*\(.*\)'
t_PROG = r'program \w*'
t_LIST = r'\[.*\]'


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

# Give the lexer some input
lexer.input(data)
for tok in lexer:
    print(tok)
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)