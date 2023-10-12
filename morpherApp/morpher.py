from typing import Optional

import pymorphy2
from pytrovich.detector import PetrovichGenderDetector
from pytrovich.enums import Gender as PytrovichGender
from pytrovich.maker import PetrovichDeclinationMaker

from enums import CommonCase, PytrovichAliasCase, NamePartAlias

morph = pymorphy2.MorphAnalyzer()

pet = PetrovichDeclinationMaker()
detector = PetrovichGenderDetector()


def morph_post(post: str, case: CommonCase):
    words_list_in = post.split()
    words_list_out = []

    for word in words_list_in:
        p = morph.parse(word)[0]
        if p.tag.POS == "NOUN" and p.tag.case == CommonCase.nomn.value:
            cased_p = p.inflect({case.value})
            cased_word = cased_p.word
            if word.istitle():
                cased_word = cased_word.capitalize()
            words_list_out.append(cased_word)
        else:
            words_list_out.append(word)

    return " ".join(words_list_out)


def morph_fio(fio: str,
              case: CommonCase,
              content_order: str,
              gender: Optional[PytrovichGender] = None):
    if case == CommonCase.nomn:
        return fio

    orig_fio_list = fio.split()
    orig_fio_dict = {content_part: orig_fio_list[i]
                     for i, content_part in enumerate(content_order)}
    other_fio_part = orig_fio_list[len(orig_fio_dict.keys()):]
    pytrovich_case = PytrovichAliasCase[case.value].value

    if gender is None:
        gender = detector.detect(
            firstname=orig_fio_dict.get("i"),
            lastname=orig_fio_dict.get("f"),
            middlename=orig_fio_dict.get("o"),
        )

    return " ".join(
        [
            pet.make(
                NamePartAlias[content_part].value,
                gender,
                pytrovich_case,
                fio_part
            )
            for content_part, fio_part in orig_fio_dict.items()
        ] + other_fio_part
    )
