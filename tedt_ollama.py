import ollama

problema="""
    'Si tuvieran que justificarse ciertos hechos por su enorme tradición entonces,
    si estos hechos son inofensivos y respetan a todo ser viviente y al medio ambiente,
    no habría ningún problema. Pero si los hechos son bárbaros o no respetuosos con los seres
    vivientes o el medio ambiente, entonces habría que dejar de justificarlos o no podríamos
    considerarnos dignos de nuestro tiempo.'

    📌 **Expresiones:**  
    p = 'justificar hechos por su tradición'  
    q = 'ser inofensivo'  
    r = 'ser respetuoso con los seres vivos'  
    s = 'ser respetuoso con el medio ambiente'  
    t = 'tener problemas'  
    ¬q = 'ser bárbaro' (= no ser inofensivo)  
    u = 'ser digno de nuestro tiempo'  

    ✅ **Resultado**

"""

prompt ="""
Teniendo en cuenta los siguientes ejemplos, retornar el UNICAMENTE el resultado del ejercicio problema

Ejemplo 1:

    'Si un animal fabuloso se enfada, te quedas paralizado del susto; y si te quedas paralizado del susto, 
    entonces no puedes sino apelar a su bondad y así no ser engullido. Por lo tanto, si un animal fabuloso se enfada, 
    tendrás que apelar a su bondad o serás engullido.'

    📌 **Expresiones:** 

    p = 'se enfada un animal fabuloso'  
    q = 'quedarse paralizado del susto'  
    r = 'apelar a su bondad'  
    s = 'ser engullido'  

    ✅ **Resultado**
    
    {( p → q ) ˄ [ q → (r ˄ ¬ s )]} → [ p → (r ˅ s )]

    
Ejemplo 2: 

    'Si un triángulo tiene tres ángulos, un cuadrado tiene cuatro ángulos rectos.  
    Un triángulo tiene tres ángulos y su suma vale dos ángulos rectos.  
    Si los rombos tienen cuatro ángulos rectos, los cuadrados no tienen cuatro ángulos rectos.  
    Por tanto, los rombos no tienen cuatro ángulos rectos.'

    📌 **Expresiones:**  

    p = 'un triángulo tiene tres ángulos'  
    q = 'un cuadrado tiene cuatro ángulos rectos'  
    r = 'su suma vale dos ángulos rectos'  
    s = 'los rombos tienen cuatro ángulos rectos'  

    ✅ **Resultado**
    [ ( p → q ) ∧ ( p ∧ r ) ∧ ( s → ¬q ) ] → ¬s


Ejemplo 3:

    'Si no es cierto que se puede ser rico y dichoso a la vez, entonces la vida está llena 
    de frustraciones y no es un camino de rosas. Si se es feliz, no se puede tener todo.  
    Por consiguiente, la vida está llena de frustraciones.'

    📌 **Expresiones:**  

    p = 'se puede ser rico'  
    q = 'se puede ser dichoso'  
    r = 'la vida está llena de frustraciones'  
    s = 'es un camino de rosas'  

    ✅ **Resultado** 
    { [ ¬( p ∧ q ) → ( r ∧ ¬s ) ] ∧ ( q → ¬p ) } → r

Ejemplo 4:

    'La vida no tiene cosas así de fuertes o yo te puedo contar cómo es una llama por dentro.  
    Si yo te puedo contar cómo es una llama por dentro, entonces pienso entregarte mi tiempo y  
    pienso entregarte mi fe. No es cierto que piense entregarte mi tiempo y piense entregarte mi fe.  
    Por lo tanto, la vida no tiene cosas así de fuertes.'

    📌 **Expresiones:**  

    p = 'tener la vida cosas así de fuertes'  
    q = 'contar cómo es una llama por dentro'  
    r = 'entregarte mi tiempo'  
    s = 'entregarte mi fe'  

    ✅ **Resultado**
    { ( ¬p ∨ q ) ∧ [ q → ( r ∧ s ) ] ∧ ¬( r ∧ s ) } → ¬p 

    
Ejemplo 5:

    'Aprobaré lógica, si Dios quiere. Aprobaré lógica si y sólo si estudio y hago todos 
    los ejercicios. Sin embargo, no he hecho los ejercicios, así que Dios no quiere que apruebe lógica.'

    📌 **Expresiones:**  

    p = 'aprobaré lógica'  
    q = 'Dios quiere que apruebe lógica'  
    r = 'estudio'  
    s = 'hago todos los ejercicios'  

    ✅ **Resultado**
    [(q → p) ∧ [p ↔ (r ∧ s)] ∧ ¬s] → ¬q  


Ejemplo 6:

    'Si el euro está fuerte, el petróleo está barato pero las exportaciones resultan caras. 
    Si Europa se endeuda o la economía no crece, el petróleo no estará barato. 
    La economía crece si y sólo si ni las exportaciones resultan caras ni la inflación aumenta. 
    Por tanto, si la inflación aumenta, el euro no está fuerte.'
     
    📌 **Expresiones:** 
    
    p = 'euro está fuerte'
    q = 'petróleo está barato'
    r = 'exportaciones caras'
    s = 'E se endeuda'
    t = 'economía crece'
    u = 'inflación aumenta'
    
    ✅ **Resultado**
    ([p → (q ∧ r)] ∧ [(s ∨ ¬t) → ¬q] ∧ [t ↔ (¬q ∧ ¬u)]) → (u → ¬p)
    

Ejemplo 7:
    
    'Todo número entero o es primo o es compuesto.  
    Si es compuesto, es un producto de factores primos, y si es un producto de factores primos,  
    entonces es divisible por ellos.  
    Pero si un número entero es primo, no es compuesto, aunque es divisible por sí mismo y por  
    la unidad, y consiguientemente, también divisible por números primos.  
    Por tanto, todo número entero es divisible por números primos.'

    📌 **Expresiones:**  

    p = 'ser primo'  
    q = 'ser compuesto'  
    r = 'producto de factores primos'  
    s = 'ser divisible por factores primos'  
    t = 'ser divisible por sí mismo'  
    u = 'ser divisible por la unidad'  

    ✅ **Resultado**
    ( p ˅ q ) ∧ ( ( q → r ) ∧ ( r → s ) ) ∧ [ ( ( p → ¬q ) ∧ ( t ∧ u ) ) → r ] ⊢ ( p ˅ q ) → s
    

Ejemplo 8:

    'Habrá inflación, a menos que se moderen los precios y los salarios. Siempre que  
    se moderan los salarios pero no los precios, si el Gobierno no interviene ocurre  
    que el consumo interno disminuye y la economía se ralentiza. Por tanto, cuando  
    no se moderan los precios, es necesario que el Gobierno intervenga para que la  
    economía no se ralentice.'

    📌 **Expresiones:**  

    p = 'hay inflación'  
    q = 'moderan precios'  
    r = 'moderan salarios'  
    s = 'gobierno interviene'  
    t = 'consumo disminuye'  
    u = 'economía ralentiza'  

    ✅ **Resultado**
    ([p ∨ (q ∧ r)] ∧ [(r ∧ ¬q) → (¬s → (t ∧ u))]) → [¬q → (¬s → u)]


Ejercicio problema:

"""+problema;

chat_sesion = [
    {"role": "system", "content": "Eres un experto en lógica proposicional. Teniendo en cuenta los ejemplos, formaliza la proposición del ejercicio problema, usando SOLO los conectores estándar (→, ˄, ˅, ¬, ↔) y retorna UNICAMENTE, sin texto extra, la expresión lógica."},
    {"role": "user", "content": prompt}
]

# Llamar al modelo con el historial completo
respuesta = ollama.chat(model="deepseek-coder:6.7b", messages=chat_sesion)

# Mostrar el resultado
print(respuesta['message']['content'])