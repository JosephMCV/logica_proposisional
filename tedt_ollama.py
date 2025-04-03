import ollama

# Definir la sesión de chat con ejemplos previos
chat_sesion = [
    {"role": "system", "content": "Eres un experto en lógica proposicional. Convierte texto en lógica usando solo →, ˄, ˅, ¬."},
    
    # ✅ Ejemplo 1
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'Si un animal fabuloso se enfada, te quedas paralizado del susto; y si te quedas paralizado del susto, "
     "entonces no puedes sino apelar a su bondad y así no ser engullido. Por lo tanto, si un animal fabuloso se enfada, "
     "tendrás que apelar a su bondad o serás engullido.'\n"
     "Expresiones: p = 'se enfada un animal fabuloso', q = 'quedarse paralizado del susto', r = 'apelar a su bondad', s = 'ser engullido'"},
    {"role": "assistant", "content": "{( p → q ) ˄ [ q → (r ˄ ¬ s )]} → [ p → (r ˅ s )]"},
    
    # ✅ Ejemplo 2
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'Si un triángulo tiene tres ángulos, un cuadrado tiene cuatro ángulos rectos. "
     "Un triángulo tiene tres ángulos y su suma vale dos ángulos rectos. "
     "Si los rombos tienen cuatro ángulos rectos, los cuadrados no tienen cuatro ángulos rectos. "
     "Por tanto los rombos no tienen cuatro ángulos rectos.'\n"
     "Expresiones: p = 'un triángulo tiene tres ángulos', q = 'un cuadrado tiene cuatro ángulos rectos', "
     "r = 'su suma vale dos ángulos rectos', s = 'los rombos tienen cuatro ángulos rectos'"},
    {"role": "assistant", "content": "[ ( p → q ) ∧ ( p ∧ r ) ∧ ( s → ¬q ) ] → ¬s"},

    # ✅ Ejemplo 3
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'Si no es cierto que se puede ser rico y dichoso a la vez, entonces la vida está llena "
     "de frustraciones y no es un camino de rosas. Si se es feliz, no se puede tener todo. "
     "Por consiguiente, la vida está llena de frustraciones.'\n"
     "Expresiones: p = 'se puede ser rico', q = 'se puede ser dichoso', r = 'la vida está llena de frustraciones', "
     "s = 'es un camino de rosas'"},
    {"role": "assistant", "content": "{ [ ¬( p ∧ q ) → ( r ∧ ¬s ) ] ∧ ( q → ¬p ) } → r"},

    # ✅ Ejemplo 4
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'La vida no tiene cosas así de fuertes o yo te puedo contar cómo es una llama por "
     "dentro. Si yo te puedo contar cómo es una llama por dentro, entonces pienso entregarte mi tiempo y "
     "pienso entregarte mi fe. No es cierto que piense entregarte mi tiempo y piense entregarte mi fe. "
     "Por lo tanto, la vida no tiene cosas así de fuertes.'\n"
     "Expresiones: p = 'tener la vida cosas así de fuertes.', q = 'contar cómo es una llama por dentro', "
     "r = 'entregarte mi tiempo', s = 'entregarte mi fe'"},
    {"role": "assistant", "content": "{ ( ¬p ∨ q ) ∧ [ q → ( r ∧ s ) ] ∧ ¬( r ∧ s ) } → ¬p"},

    # ✅ Ejemplo 5
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'Aprobaré lógica, si Dios quiere. Aprobaré lógica si y sólo si estudio y hago todos "
     "los ejercicios. Sin embargo, no he hecho los ejercicios, así que Dios no quiere que apruebe lógica.'\n"
     "Expresiones: p = 'aprobaré lógica', q = 'D quiere que apruebe lógica', r = 'estudio', s = 'hago todos los ejercicios'"},
    {"role": "assistant", "content": "[(q → p) ∧ [p ↔ (r ∧ s)] ∧ ¬s] → ¬q"},

    # ✅ Ejemplo 6
    {"role": "user", "content": "Convierte el siguiente texto en lógica proposicional:\n"
     "'Si el euro está fuerte, el petróleo está barato pero las exportaciones resultan caras. "
     "Si Europa se endeuda o la economía no crece, el petróleo no estará barato. "
     "La economía crece si y sólo si ni las exportaciones resultan caras ni la inflación aumenta. "
     "Por tanto, si la inflación aumenta, el euro no está fuerte.'\n"
     "Expresiones: p = 'euro está fuerte', q = 'petróleo está barato', r = 'exportaciones caras', "
     "s = 'E se endeuda', t = 'economía crece', u = 'inflación aumenta'"},
    {"role": "assistant", "content": "([p → (q ∧ r)] ∧ [(s ∨ ¬t) → ¬q] ∧ [t ↔ (¬q ∧ ¬u)]) → (u → ¬p)"},
]

# Ahora enviamos el problema real
nuevo_problema = {
    "role": "user",
    "content": """Convierte el siguiente texto en lógica proposicional, usando SOLO los conectores estándar (→, ˄, ˅, ¬).

Texto:  
'Si tuvieran que justificarse ciertos hechos por su enorme tradición entonces, si estos hechos son inofensivos y respetan a todo ser viviente y al medio ambiente, no habría ningún problema. Pero si los hechos son bárbaros o no respetuosos con los seres vivientes o el medio ambiente, entonces habría que dejar de justificarlos o no podríamos considerarnos dignos de nuestro tiempo.'  

📌 **Expresiones:**  
p = 'justificar hechos por su tradición'  
q = 'ser inofensivo'  
r = 'ser respetuoso con los seres vivos'  
s = 'ser respetuoso con el medio ambiente'  
t = 'tener problemas'  
¬q = 'ser bárbaro' (= no ser inofensivo)  
u = 'ser digno de nuestro tiempo'  

✅ **Devuelve SOLO la expresión lógica esperada**
"""
}

# Agregar la nueva consulta al historial
chat_sesion.append(nuevo_problema)

# Llamar al modelo con el historial completo
respuesta = ollama.chat(model="deepseek-coder:6.7b", messages=chat_sesion)

# Mostrar el resultado
print(respuesta['message']['content'])
