import re


def remove_tags(text: str):
    pattern = re.compile("<.*?>")
    cleantext = re.sub(pattern, "", text)
    return cleantext


question_sample = '<p>Com base em seus conhecimentos sobre o compositor John Cage, analise as seguintes afirmativas.</p><blockquote><p style="box-sizing:inherit;margin:0px 0px 1rem;padding:0px;font-size:inherit;line-height:1.6;text-rendering:optimizelegibility;color:rgb(138, 138, 138)"><b style="box-sizing:inherit;font-weight:700;line-height:inherit">I.</b> Sua composição intitulada <em style="box-sizing:inherit;font-style:italic;line-height:inherit">4’33</em>’ faz o público refletir sobre o que é música, silêncio e paisagem sonora.</p><p style="box-sizing:inherit;margin:0px 0px 1rem;padding:0px;font-size:inherit;line-height:1.6;text-rendering:optimizelegibility;color:rgb(138, 138, 138)"><b style="box-sizing:inherit;font-weight:700;line-height:inherit">II.</b> Os músicos que tocam essa composição são orientados a não executar uma nota sequer durante quatro minutos e trinta e três segundos.</p><p style="box-sizing:inherit;margin:0px;padding:0px;font-size:inherit;line-height:1.6;text-rendering:optimizelegibility;color:rgb(138, 138, 138)"><b style="box-sizing:inherit;font-weight:700;line-height:inherit">III.</b> Para John Cage, o silêncio absoluto não existe porque tudo se move.</p></blockquote><p>Marque a alternativa correta:</p>'

print(remove_tags(question_sample))
