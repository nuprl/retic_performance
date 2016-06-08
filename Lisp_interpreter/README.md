This project implements an evaluator for a small subset of Racket, called 
Beginning Student Language (BSL). 

The context-free grammar of BSL is defined as follows: 

**A BSLProgram is a sequence of BSLdefinitions followed by a BSLexpression.**

**A BSLDefiition is one of:** 
- (define (Variable Variable ...) BSLexpression)
- (define-struct Variable (Variable ...))
- (define Variable BSLexpression)

**A BSLexpression is one of:**
- PythonNumber  | Num(PythonNumber)
- true          | Boolean(true)
- false         | Boolean(false)
- Variable      | Var(String)
- (FunctionName BSLExpression ...)
- (PrimitiveName BSLExpression ...)
- (lambda (Strings ...) BSLExpression)
- ((lambda (strings ...) BSLExpression ...))
- (if BSLExpression BSLexpression BSLexpression)
- (and BSLExpression BSLExpression BSLExpression ...)

**A Variable:** is a Token (that is not a Literal token or a PythonNumber)<br/>
**A FunctionaName:** is a Token (that is not a Literal token or a PythonNumber)<br/>
**A PrimitiveName is one of:** <br/>
- +
- - 
- * 
- /
- >
- <
- = 

**The LiteralTokens are:**
- define
- define-struct

**A Token:** is a sequence of characters not including '(', ')' and whitespace (' ')
*All whitespace between tokens and ( and ) is ignored.*
  
  ----------------------------------------

R E A D E R: -> P-expression
*reads one S-expression from STDIN* 

**An S-expression has the following textual representation:**
- Token
- OpenParen 

**An OpenParen is:** 
 '(' followed by Seq

**A Seq is one of:**
- ')'
- S-expression followed by Seq



**An P-expression is one of:**
- Atom
- [Listof P-expression]

**An Atom is:**
- Any sequence of characters 

| S-expression |    P-expression     |
|--------------|---------------------|
| Token        | Atom                |
| OpenParen    | Listof P-expression |

_____________________________________________

P A R S E R: P-expression -> AST 

**An AST is one of:**
- BSLDef
- Binding
- IsClsDef
- BSLExpr
- ComparisonDef([Num ... -> bool or float or complex or int],
                [bool of float or complex or int -> Value]
                Value)  %% but not Structure 

**A BSLDef is one of:**
- StructDef 
- ConstructorDef
- SelectorDef
- PredicateDef

**A Binding is one of: **
- FuncDef

**An IsClsDef is one of:**
- IsBooleanDef

**A BSLExpr is one of:**
- And([BSLExpr])
- Boolean(bool)
- FunctionApplication(String, [BSLExpr])
- If([BSLExpr])
- Num((int or complex or float))
- LambdaExpr([Strings], [BSLExpr])
- Variable(String)


Notes:<br />
*The parser will create an AST for P-expression whose original S-expression satisfies the context-free grammar of BSL.*<br />
   * EX: A parser will not catch the following error: ['define', ['add', 'x', 'x', 'z'], ['+', 1, 3]]
       because the repetition of 'x' is not context free. <br />
   * EX: It will catch the following error: ['define', ['f', 'x', 1, 'y'], 42]
       because 1 is not a variable <br />
   * EX: It will catch the following error: ['define', ['f', 'x', '+', 'y'], 42]
       because '+' is not a variable <br />
       

| S-expression |        AST        |
|--------------|-------------------|
| PythonNumber | Num(PythonNumber) |
| true         | Boolean(true)     |
| false        | Boolean(false)    |
| Variable     | Var(String)       |

_____________________________________________

I N T E R P R E T E R: AST -> Value

**A Value is one of:**
- Boolean(bool)
- Num(PythonNumber)
- Closure(LambdaExpr, Scope)
- Structure(String, [Listof (String, Value)])

For StructDef and FuncDef, eval_internal does not exist. 
For AST that come from BSLexpr, the following table explains eval_internal: 

| Expression ASTs      |  Value  |  
|----------------------|---------|
| And                  | Boolean |  
| Boolean              | Boolean |  
| Num                  | Num     |  
| FunctionApplication  | Value   |  
| If                   | Value   |
| Variable             | Value   |

Values produced from calling the apply method on some Definition

|    Definition    |    Value    |
|------------------|-------------|
| ComparisonDef    | Num/Boolean |
| IsClsDef         | Boolean     |
| PredicateDef     | Boolean     |
| SelectorDef      | Value       |
| ConstructorDef   | Structure   |
| FuncDef          | Closure     |


